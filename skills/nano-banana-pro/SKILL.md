---
name: nano-banana-pro
description: Generate images with Google's Nano Banana Pro (Gemini 3 Pro Image). Use when generating AI images via Gemini API, creating professional visuals, or building image generation features. Triggers on Nano Banana Pro, Gemini 3 Pro Image, gemini-3-pro-image-preview, Google image generation.
---

# Nano Banana Pro (Gemini 3 Pro Image)

Generate high-quality images with Google's Gemini 3 Pro Image API.

## Overview

**Nano Banana Pro** is the marketing name for **Gemini 3 Pro Image** (`gemini-3-pro-image-preview`), Google's state-of-the-art image generation and editing model built on Gemini 3 Pro.

## Quick Start

### Get API Key
1. Go to [Google AI Studio](https://aistudio.google.com)
2. Click "Get API Key"
3. Store securely as environment variable

### Basic Image Generation (Python)
```python
from google import genai
from google.genai import types

client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="A serene Japanese garden with cherry blossoms and a koi pond",
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE']
    )
)

# Process response
for part in response.candidates[0].content.parts:
    if hasattr(part, 'text'):
        print(f"Description: {part.text}")
    elif hasattr(part, 'inline_data'):
        # Save image
        image_data = part.inline_data.data  # Base64 encoded
        mime_type = part.inline_data.mime_type  # image/png
        
        import base64
        with open("output.png", "wb") as f:
            f.write(base64.b64decode(image_data))
```

### REST API (cURL)
```bash
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [{"text": "Create a vibrant infographic about photosynthesis"}]
    }],
    "generationConfig": {
      "responseModalities": ["TEXT", "IMAGE"]
    }
  }'
```

### TypeScript/JavaScript
```typescript
const GEMINI_API_KEY = process.env.GEMINI_API_KEY;

async function generateImage(prompt: string) {
  const response = await fetch(
    'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent',
    {
      method: 'POST',
      headers: {
        'x-goog-api-key': GEMINI_API_KEY!,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        contents: [{ 
          role: 'user', 
          parts: [{ text: prompt }] 
        }],
        generationConfig: {
          responseModalities: ['TEXT', 'IMAGE'],
        },
      }),
    }
  );

  const data = await response.json();
  return data;
}
```

## Configuration Options

### Image Configuration
```python
response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Professional product photo of a coffee mug",
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
        image_config=types.ImageConfig(
            aspect_ratio="16:9",  # Options: 1:1, 3:2, 16:9, 9:16, 21:9
            image_size="2K"       # Options: 1K, 2K, 4K
        )
    )
)
```

### With Google Search Grounding
```python
response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="Create an infographic showing today's stock market trends",
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
        tools=[{"google_search": {}}]  # Enable search grounding
    )
)
```

## Alternative Access: Atlas Cloud

The same model is served by [Atlas Cloud](https://www.atlascloud.ai/?utm_source=github&utm_medium=link&utm_campaign=ai-agents-skills) as `google/nano-banana-pro/text-to-image`, which is useful when a Google AI Studio key is not available. It is a different API shape — a POST queues a job and the result is polled — not a drop-in for the calls above.

```bash
# 1. Submit
curl -s -X POST https://api.atlascloud.ai/api/v1/model/generateImage \
  -H "Authorization: Bearer $ATLASCLOUD_API_KEY" \
  -H "Content-Type: application/json" \
  -H "User-Agent: my-app/1" \
  -d '{
    "model": "google/nano-banana-pro/text-to-image",
    "prompt": "Professional product photo of a coffee mug",
    "aspect_ratio": "16:9"
  }'
# -> {"code":200,"data":{"id":"<prediction-id>","status":"processing"}}

# 2. Poll every 5-6s until completed, then download data.outputs[0]
curl -s https://api.atlascloud.ai/api/v1/model/prediction/<prediction-id> \
  -H "Authorization: Bearer $ATLASCLOUD_API_KEY" \
  -H "User-Agent: my-app/1"
```

What carries over from the section above and what does not (measured against this endpoint, not copied from a vendor page):

| Control documented above | On this path |
|---|---|
| `aspect_ratio` | Works. `1:1` → 1024×1024, `16:9` → 1376×768, `9:16` → 768×1376 |
| `image_size` (`1K`/`2K`/`4K`) | Not exposed — the model's default resolution comes back |
| Output container | JPEG, not PNG |
| Multi-turn editing, Google Search grounding | Not available — those are Gemini API features |

Two more things worth knowing:

- A `size` field is **ignored** by this model (a `1024*1024` request still returned 1408×768); use `aspect_ratio` instead. Other Atlas image models behave the opposite way, so check per model.
- `api.atlascloud.ai` rejects the default `User-Agent` of some HTTP clients with `403 error code 1010` — send an explicit one, as above. The result URL is short-lived, so download it right away.

Stay on the Gemini API when you need 2K/4K output, PNG, grounding, or the iterative editing flow below.

## Multi-Turn Conversations (Iterative Editing)

```python
# Create a chat session
chat = client.chats.create(
    model="gemini-3-pro-image-preview",
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE'],
        tools=[{"google_search": {}}]
    )
)

# Initial generation
response1 = chat.send_message(
    "Create a vibrant infographic explaining photosynthesis"
)

# Edit the image
response2 = chat.send_message(
    "Update this infographic to be in Spanish. Keep all other elements the same."
)
```

## Key Capabilities

### 1. Superior Text Rendering
```python
response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="""Create a professional poster with:
    - Title: "Annual Tech Summit 2025"
    - Date: March 15-17, 2025
    - Location: San Francisco Convention Center
    """,
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE']
    )
)
```

### 2. Character Consistency (Up to 5 Subjects)
```python
import base64

def load_image(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

character_ref = load_image("character.png")

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents=[
        {"text": "Generate an image of this person at a tech conference"},
        {"inline_data": {"mime_type": "image/png", "data": character_ref}}
    ],
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE']
    )
)
```

## Next.js API Route

```typescript
// app/api/generate-image/route.ts
import { NextRequest, NextResponse } from 'next/server';

export async function POST(request: NextRequest) {
  const { prompt, aspectRatio = '1:1', imageSize = '2K' } = await request.json();

  try {
    const response = await fetch(
      'https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent',
      {
        method: 'POST',
        headers: {
          'x-goog-api-key': process.env.GEMINI_API_KEY!,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          contents: [{ role: 'user', parts: [{ text: prompt }] }],
          generationConfig: {
            responseModalities: ['TEXT', 'IMAGE'],
            imageConfig: { aspectRatio, imageSize },
          },
        }),
      }
    );

    const data = await response.json();
    const parts = data.candidates?.[0]?.content?.parts || [];
    const imagePart = parts.find((p: any) => p.inline_data);

    return NextResponse.json({
      image: imagePart ? {
        data: imagePart.inline_data.data,
        mimeType: imagePart.inline_data.mime_type,
        url: `data:${imagePart.inline_data.mime_type};base64,${imagePart.inline_data.data}`,
      } : null,
    });
  } catch (error) {
    return NextResponse.json({ error: 'Generation failed' }, { status: 500 });
  }
}
```

## Model Comparison

| Feature | Nano Banana (2.5 Flash) | Nano Banana Pro (3 Pro Image) |
|---------|-------------------------|-------------------------------|
| Model ID | gemini-2.5-flash-image | gemini-3-pro-image-preview |
| Quality | Good | Best |
| Speed | Faster | Slower |
| Cost | Lower | Higher |
| Best For | Previews, high-volume | Production, professional |

## Resources

- **Documentation**: https://ai.google.dev/gemini-api/docs/image-generation
- **Google AI Studio**: https://aistudio.google.com
- **Prompt Guide**: https://ai.google.dev/gemini-api/docs/prompting-intro
