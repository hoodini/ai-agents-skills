# Pixel setup: from zero to a verified funnel

Read this before any conversion campaign. A Sales campaign without a working pixel pays Meta to optimize toward nothing. Most "my ads don't convert" problems are a pixel problem, not an ads problem.

Walk the user through it one step at a time, verify each step yourself, and only then move on.

## Step 0. Map the funnel before touching code

Ask (or find out by fetching the pages) where each step of the purchase happens. The usual shape for a course, a product or a service:

```
ad -> landing page (your site) -> checkout page (often a third-party platform) -> payment -> thank-you page
```

Write down, for each step: the URL, who controls the code (the user, or a platform like a course host, Shopify, a payment page), and how the user can add code there (edit HTML, a "tracking codes" field, a native "Facebook pixel" integration).

**The step that matters most is the one the user does NOT control.** If the purchase happens on a third-party platform, the Purchase event has to come from that platform. A pixel only on the landing page will never see a sale.

## Step 1. Pick the right ad account FIRST, then create the pixel there

This is the most expensive mistake to undo, so settle it before anything else:

- **The pixel must be usable by the ad account that will pay for the ads.** A pixel created inside one ad account cannot simply be "moved" later.
- **Business-owned beats ad-account-owned.** Create the pixel (Events Manager calls it a dataset) inside a Business Portfolio and connect it to the ad account. A pixel owned directly by a personal ad account (no Business) has two problems: it cannot be shared with another ad account, and the **Instagram app's Boost flow does not list it** (the boost pixel picker only shows Business-owned pixels).
- Before creating anything, check the ad account: active status, a valid payment method, and whether it belongs to a Business (`GET /act_<id>?fields=account_status,funding_source_details,business`). See troubleshooting.md for the status codes that bite here (9 grace period, 100 pending closure).
- If the user wants to boost from the Instagram app later, make sure that account + a Business-owned pixel are what the app will use. If not, steer them to Ads Manager campaigns instead (more control, multiple creatives, real optimization).

Do not let the user flip-flop between accounts and pixels. Every switch means re-installing the pixel on every page, re-testing, and losing the learning collected so far. One account, one pixel, decided once.

## Step 2. Pixel only, or Pixel + Conversions API?

Events Manager recommends "Conversions API and Meta Pixel". That needs a server you control. Decide by the stack:

| Stack | Choose |
|---|---|
| Static site (Netlify, Vercel static, GitHub Pages), checkout on a third-party platform | **Meta Pixel only.** Add CAPI later through a serverless function or the platform's own integration if needed. |
| Your own server/backend handles checkout | Pixel + CAPI, with `event_id` deduplication |
| Shopify / WooCommerce / big platforms | Use their native Meta integration; it usually does both |

CAPI can be added to the same pixel later without starting over. Don't block a launch on it.

## Step 3. Install the base code on every page of the funnel

The base code (`fbq('init', '<PIXEL_ID>'); fbq('track', 'PageView');`) goes in the `<head>` of each page, plus the `<noscript>` image right after `<body>`.

**The paste mistake to check for:** users often paste the **ad account ID** (also 15-16 digits) where the pixel ID belongs. Nothing errors; the page just sends nothing. Always verify the ID that is actually live (Step 6).

## Step 4. One event name per funnel step, no collisions

Standard events, in funnel order:

| Step | Event | Where it fires |
|---|---|---|
| Visit | `PageView` | every page (base code) |
| Saw the offer | `ViewContent` (with `value`, `currency`) | landing page load |
| Clicked toward checkout | `AddToCart` (with `value`, `currency`) | click on the buy/CTA button of the landing page |
| Started paying | `InitiateCheckout` | the checkout/pay button |
| Paid | `Purchase` (with `value`, `currency`) | thank-you page / payment success, **once** |

Rules:
- **Find out what the checkout platform already sends before adding your own events.** Platforms often fire `InitiateCheckout` and `Purchase` themselves once the pixel ID is entered. If you also fire `InitiateCheckout` on the landing page's CTA, two different steps get the same name and the funnel becomes unreadable. Give the landing-page CTA its own event (`AddToCart`).
- **How to find out:** platform docs are often vague or wrong about names. Fetch the checkout page, find the platform's JS bundle, and grep it for `fbq(`. The real calls are there (e.g. an internal `view_cart` mapped to `fbq('track','InitiateCheckout')`, `purchase` mapped to `fbq('track','Purchase',{currency,value})`). Event names are case-sensitive: `Purchase` is standard, `purchase` is a custom event Meta cannot optimize for.
- **Purchase must fire only after a real payment.** Never put `Purchase` in a code box that loads on every page view. If the platform can't place code only on the success page, ask its support, or redirect buyers to a thank-you page you control (accepting that a static page can't verify payment).
- **Take the value from config, not a hard-coded number,** so a price change never leaves the pixel reporting the old price.
- **Attach the CTA listener to a selector (`[data-cta]`, `a[href*="checkout-domain"]`), not to one button,** so buttons added later are tracked too.
- Hard-coded `value` on a platform-wide code box is wrong if several products share it: each product needs its own value or the platform's native event.

Minimal landing-page pattern:

```html
<script>
  /* base code here: fbq('init', 'PIXEL_ID'); fbq('track', 'PageView'); */
  fbq('track', 'ViewContent', {content_name: 'Product', value: PRICE, currency: 'ILS'});
  document.addEventListener('click', function (e) {
    if (e.target.closest('[data-cta]')) fbq('track', 'AddToCart', {value: PRICE, currency: 'ILS'});
  });
</script>
```

## Step 4b. Instrument the gaps between stages

Two stages that no event separates can't get different ads. Close the usual gaps:
- **Engaged vs bounced on the landing page:** add an `EngagedVisit` custom event (30 seconds or 60% scroll) and a `PageVideoPlay` event for the page's video. Snippet in full-funnel-system.md section 4.
- **Registered vs not on a third-party checkout:** platforms rarely fire a pixel event on registration. Find the route the platform moves people to after registering (read its JS bundle for route strings, e.g. a cart route) and build a URL-contains audience on it. Confirm in Events Manager that PageViews with that URL arrive (single-page apps report route changes as PageViews only if the pixel's history tracking catches them).
- **Identified stages:** the mailing tool's "signed up" and "paid" lists cover registered people by email from the first person, and can be uploaded as customer lists for ads.

## Step 5. Check what could block it

- A `Content-Security-Policy` header without `connect.facebook.net` and `www.facebook.com` silently blocks the pixel. Check the host's header config (`netlify.toml`, `vercel.json`, `_headers`, server config).
- Consent banners that never load the pixel until consent: expected in the EU; make sure the user knows numbers will be lower.
- Update the privacy policy to disclose Meta tracking (and check local privacy law).

## Step 6. Verify, in three layers

1. **Installed:** `python scripts/check_pixel.py --pixel-id <PIXEL> --ad-account-id <act_...> <landing-url> <checkout-url>`. Flags missing pixels, extra/old pixels, and the ad-account-ID paste mistake.
2. **Calls are made:** in a headless browser, wrap `window.fbq` before the page loads and record the calls (init, PageView, ViewContent, the CTA event with value). Note: Meta suppresses network events from headless browsers, so absence of `facebook.com/tr` requests there proves nothing; record the `fbq` calls instead. A fetch of `connect.facebook.net/signals/config/<PIXEL_ID>` confirms Meta knows the ID.
3. **Meta receives them:** Events Manager -> the pixel -> **Test events**, enter the landing URL, and walk the funnel on a real phone/browser: landing, click to checkout, click pay. Each event should appear within a minute.
4. **Purchase, for real:** create a one-time coupon for ~99% off (not 100%: zero-value orders may skip the payment flow and the Purchase event), buy, confirm `Purchase` arrives **with `value` and `currency`**, then delete the coupon.

## Step 7. Domain verification

Business Settings -> Brand safety -> Domains -> add the root domain (one verification covers all subdomains) -> DNS TXT record. Check first: `dig +short TXT example.com` may already show a `facebook-domain-verification` record from an earlier attempt. Multiple TXT records can coexist; never delete existing ones.

## Step 8. Write it down

Record in the project (not in chat only): pixel ID, which ad account and Business own it, which page sends which event, and the date it was verified. The next person (or the next session) should not have to rediscover the funnel.
