## VPN subscriptions for daily usage
Tested to work in Russia, RTK ISP. 
Configurations are collected from other similar github repositories, you can find the best collection of them in [NiREvils](https://github.com/NiREvil/vless?tab=readme-ov-file#xray) repository. 
80% are guaranteed to work on the first day after an update.

Config checking algorhythm:
- run d.py
- check with [nekoray](https://github.com/MatsuriDayo/nekoray) for validity
- use the ones that work

a - all valid configurations found by me

b - manually chosen VLESS with Reality/XTLS configurations [Recommended]

c - subscription for testing

d.py - searches for the lines that have **thing** in links and adds them to **path**. Also does some cleaning, sorting and numbering for better experience.

e.py - adds country flags to configs by checking their IP's through a free API.

