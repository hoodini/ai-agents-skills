"""Fetch Rubik 700+900 woff2 subsets covering the FULL Hebrew alphabet + latin + digits."""
import re, urllib.request, urllib.parse, os
os.makedirs("fonts", exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"}
TEXT = ("אבגדהוזחטיכךלמםנןסעפףצץקרשת"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        "?!,.·:;-–—'\"()%+=×@ ")
def fetch(w, out):
    url = "https://fonts.googleapis.com/css2?family=Rubik:wght@%d&text=%s" % (w, urllib.parse.quote(TEXT))
    css = urllib.request.urlopen(urllib.request.Request(url, headers=UA)).read().decode()
    m = re.search(r"url\((https://[^)]+)\)", css)
    open(out, "wb").write(urllib.request.urlopen(urllib.request.Request(m.group(1), headers=UA)).read())
    print(out, os.path.getsize(out), "bytes")
fetch(900, "fonts/Rubik-900.woff2")
fetch(700, "fonts/Rubik-700.woff2")
