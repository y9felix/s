## VPN subscriptions for daily usage
Tested in Russia, RTC ISP.  
Free forever, no possibility of data leaks or linking them to a person.  
Configurations are collected from other similar GitHub repositories; the best collection can be found in [NiREvil](https://github.com/NiREvil/vless?tab=readme-ov-file#xray)'s repository.  
80% are guaranteed to work on the first day after an update.

Configuration checking algorithm:
- Start `a.py`
- Check validity via [Throne](https://github.com/throneproj/Throne)

Subscriptions
- `a` — All valid configs from GitHub. Updated weekly.
- `b` — Manually selected VLESS configurations with Reality/XTLS. [Recommended]
- `c` — Most stable (1+ month) configs. Updated monthly.
- `r` — Russian servers. Updated weekly.

Scripts
- `a.py` — Searches for the lines that have thing in links and adds them to path. Has an option for caching old invalid configs. Also does some cleaning, sorting and numbering with optional flagging for better experience.
- `b.py` — Adds country flags to configs by checking their IP via a free API. [Slow]
- `chart.py` — Checks all commits of one file for the most long-working and stable configs.
- `flagsort.py` — Separates by flag when you need configs only from one country.
- `ispfinder.py` — Sorts configs by their ISP.
- `siteparse.py` — One website always changes it's domain, and when I locate it, I scrape all configs from it with this script.

[VLESS](https://github.com/v2fly/v2ray-core) is a FOSS privacy and anti-censority oriented proxy protocol. It is capable of going through China's GFW and other countries internet censorship, and is evidently untraceable by any modern system. The configurations here are also completely private if used with HTTPS. If I ever stop support, you are free to get the scripts that I use in the [scripts](https://github.com/y9felix/s/tree/main/scripts) folder.

More about VLESS and other protocols (In Russian) — [Article](https://habr.com/ru/articles/727868/) || [Video](https://www.youtube.com/watch?v=Ajy1lS9qJbs)
