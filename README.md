# news-image-20261122

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/muskabc/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/muskabc/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

One 1024×1024 image summing up the world's news of Sunday, 22 November 2026, drawn as a newspaper front page: "THE WORLD IN ONE DAY". A wide lead story on top and four more stories in a grid below, each with its own hand-drawn illustration, headline and short summary.

## The five stories

1. **Australia / Defence** — Defence Minister Richard Marles said in Sydney on Sunday that a US Congressional Budget Office report was wrong to claim selling Virginia-class submarines to Australia would shrink the US attack-submarine fleet. Source: https://krro.com/2026/11/21/australia-criticises-us-congressional-budget-office-over-aukus-comments/
2. **Germany / Labour** — IG Metall announced on Sunday a 24-hour strike by 23,000 workers at 19 firms in northern Germany on Monday, in a pay dispute. Source: https://www.europesays.com/germany/134040/
3. **Hong Kong / Election** — Voting opened at 9am on Sunday in the Election Committee subsector elections, with 856 candidates standing for 723 seats. Source: https://www.chinadailyasia.com/hk/article/642994
4. **Israel / Politics** — Gadi Eisenkot, tasked with forming Israel's next government, invited Benjamin Netanyahu's Likud party to talks starting on Sunday, aiming for a broad unity government. Source: https://www.thedailyjagran.com/world/news/israel-government-formation-arab-parties-snubbed-as-gadi-eisenkot-reaches-out-to-benjamin-netanyahus-likud-in-shocking-coalition-move-10337188
5. **Italy / Sport** — Alexander Zverev meets Carlos Alcaraz in the ATP Finals singles final in Turin on Sunday evening, not before 18:00 local time. Source: https://tennistourcalendar.com/atp-finals-final-preview/ (see also http://www.atptour.com/en/news/nitto-atp-finals-2026-final-schedule)

All five stories were first reported on 22 November 2026. The tennis final had not yet been played when this image was made, so no result is shown; the Israeli talks are shown as starting on Sunday, not as concluded.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. The image itself is drawn by `build_image.py` (Python, Pillow) — every illustration is drawn with plain shapes, no photos.

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=a4mjt6w8&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>
