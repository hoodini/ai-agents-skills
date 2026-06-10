# yuv-reel-covers
Unified Instagram Reel covers for YUV.AI — giant Hebrew text BEHIND + IN FRONT of the subject,
Neon Phoenix brand, series-colored chips, one command per cover. See SKILL.md for the formula,
rules and full usage. Example output: assets/example-cover.png

Quick start:
  npx --yes hyperframes@latest remove-background photo.png -o assets/cutout.png
  py gen_cover.py behind --img assets/cutout.png --back "..." --front "..." --accent-back 1 --color pink --tag "AI" --out cover1
