# News Image — 25 November 2026

[![make.fun](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/weichanghong24-lgtm/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/weichanghong24-lgtm/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

Entry for the make.fun bounty **"Sum up 25 November's world news in one image"**:
https://make.fun/bounty/news-image-20261125

- **Prize:** $100 USDC, top 50 entries
- **Deadline:** 27 November 2026 00:00 UTC
- **Entry:** free

## What the image shows

A bold magazine-cover style image (1024×1024 PNG) summing up Wednesday
25 November 2026 world news:

- **Lead — Strait of Hormuz:** two oil tankers struck naval mines, exploded
  and caught fire; Iran's Revolutionary Guard said they were on an
  unauthorised route. Illustrated with a vector-drawn tanker at sea, flames
  and smoke (Pillow shapes only, no photos).
- **Houthis / Riyadh:** attack on Saudi Arabia's Ras Tanura oil refinery;
  Riyadh's tallest skyscraper hit again, second time in under a week,
  11 injured.
- **Gaza:** Israel killed Hamas security chief Mohammad Abuelouf in a strike,
  with his wife and two children.
- **Ukraine:** Russian strike on Odesa killed 2 and injured 3 including a
  child; Kyiv apartment block hit, 2 injured; leaked Russian figures analysed
  by the BBC put Russian soldiers killed at 490,334.
- **Sudan:** RSF drone strikes killed 19 civilians and wounded 20 in two cities.
- **Also today:** COP31 ended with no agreement (Pope Leo XIV voiced
  concern); Solomon Islands and Australia signed a treaty barring any foreign
  military base; Huawei found guilty in a US court of trade-secret theft and
  bank fraud; China carried Pakistan's first astronaut into orbit; an
  unclassified CIA system was breached; Trump awarded Rudy Giuliani the Medal
  of Freedom; police freed hostages in a Colombia supermarket; Denmark banned
  headscarves for prosecutors.

## How it was made

`build_image.py` renders `entry.png` from scratch with Python 3 + Pillow
only — no network, no randomness, no timestamps, so the output is
byte-for-byte deterministic. `main.py` (stdlib only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png`.

```sh
python3 build_image.py        # renders entry.png (1024x1024, < 1 MiB)
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

See `BUILD_LOG.md` for the build record. License: MIT.
