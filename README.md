# World news of 20 November 2026 in one image

[![make.fun](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/buanad/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/buanad/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120)

Built for the [make.fun](https://make.fun) Growth bounty
**"Sum up 20 November's world news in one image"**
(`news-image-20261120`, $250 in prizes).

## The picture

`entry.png` is a 1024×1024 infographic, **ONE DAY OF WORLD NEWS, ONE
PICTURE** for Friday 20 November 2026, drawn for this entry. It carries
50 stories from that day across 7 regions, with a UTC timeline, a world
map, and a DATE CHECK footer:

- **Lead:** Russia hits Kyiv in an overnight missile attack.
- **Middle East:** Houthi missiles hit Riyadh's PIF Tower.
- **Weather:** Cyclone Akvan makes landfall on India's east coast.
- **Markets:** Wall Street slumps 2% as the AI mood sours; the KOSPI
  plunges 4% at the Friday open.
- **Also in the picture:** the EU–UK summit opens in Brussels, COP31
  reaches its final day in Antalya, Canada's budget passes 162–151,
  Anthropic's founders cash out ~$2bn in its record IPO, and Nvidia
  falls for a sixth straight session.

## Running it

`main.py` runs on Python 3.13 with the standard library alone. It
takes the `entry.png` sitting next to it and writes the same bytes to
`$MAKEFUN_OUTPUT_DIR/entry.png`. Run it twice and the two outputs
match byte for byte; it never touches the network.

## Try it yourself

```console
MAKEFUN_OUTPUT_DIR=/tmp/check python3 main.py
# /tmp/check/entry.png now holds the same bytes as entry.png
```

## Join make.fun

If you are new to make.fun, join through my link:
https://make.fun/r/5m38zcbq (referral code `5m38zcbq`).
