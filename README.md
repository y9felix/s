## VPN subscriptions for daily usage
Tested to work in Russia, RTK ISP. 
Configurations are collected from other similar github repositories, you can find the best collection of them in [NiREvils](https://github.com/NiREvil/vless?tab=readme-ov-file#xray) repository. 
80% are guaranteed to work on the first day after an update.

Config checking algorhythm:
- run a.py
- check with [nekoray](https://github.com/MatsuriDayo/nekoray) for validity
- use the ones that work

a - all valid cfg from github

b - manually chosen VLESS with Reality/XTLS configurations [Recommended]

c - subscription for testing

g - all valid cfg from sites [Recommended]

a.py - searches for the lines that have **thing** in links and adds them to **path**. Also does some cleaning, sorting and numbering for better experience.

b.py - adds country flags to configs by checking their IP's through a free API.

c.py - config scraper from a site I found

More about VLESS VPN (in Russian) - [Article](https://habr.com/ru/articles/727868/)||[Video](https://www.youtube.com/watch?v=Ajy1lS9qJbs)

