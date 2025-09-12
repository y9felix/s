## VPN subscriptions for daily usage

Tested in Russia, RTK ISP.  
Free forever, no possibility of data leaks or linking them to a person.  
Configurations are collected from other similar GitHub repositories; the best collection can be found in the [NiREvil](https://github.com/NiREvil/vless?tab=readme-ov-file#xray) repository.  
80% are guaranteed to work on the first day after an update.

Configuration checking algorithm:
- Start `a.py`
- Check validity via [nekoray](https://github.com/MatsuriDayo/nekoray)

Subscriptions
- a — All valid configs from GitHub. Updated once a week.
- b — Manually selected VLESS configurations with Reality/XTLS. Updated every 2–3 days. [Recommended]
- c — For testing
- d — configs that are active longer than a month

Scripts
- `a.py` — Searches for the lines that have thing in links and adds them to path. Also does some cleaning, sorting and numbering for better experience.
- `b.py` — Adds country flags to configs by checking their IP via a free API. [Slow]

More about VLESS and other protocols (In Russian) — [Article](https://habr.com/ru/articles/727868/) || [Video](https://www.youtube.com/watch?v=Ajy1lS9qJbs)
