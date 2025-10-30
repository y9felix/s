import urllib.request, concurrent.futures, json, os, re, requests

def main():
    url_map = {
        '0': "your set of links",
        '1': "https://sub.amiralter.com/config https://itsyebekhe.github.io/PSG/ https://f0rc3run.github.io/F0rc3Run-panel/ https://raw.githubusercontent.com/mermeroo/QX/main/Nodes https://raw.githubusercontent.com/Ashkan-m/v2ray/main/VIP.txt https://raw.githubusercontent.com/nscl5/5/main/configs/all.txt https://apps.apple.com/us/app/proton-vpn-fast-secure/id1437005085 https://raw.githubusercontent.com/mermeroo/Loon/main/all.nodes.txt https://raw.githubusercontent.com/Kolandone/v2raycollector/main/ss.txt https://raw.githubusercontent.com/MhdiTaheri/V2rayCollector/main/sub/ss https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/python/ss https://raw.githubusercontent.com/MhdiTaheri/V2rayCollector/main/sub/mix https://raw.githubusercontent.com/T3stAcc/V2Ray/main/All_Configs_Sub.txt https://raw.githubusercontent.com/liketolivefree/kobabi/main/sub_all.txt https://raw.githubusercontent.com/Kolandone/v2raycollector/main/vless.txt https://raw.githubusercontent.com/LalatinaHub/Mineral/master/result/nodes https://raw.githubusercontent.com/misersun/config003/main/config_all.yaml https://raw.githubusercontent.com/penhandev/AutoAiVPN/main/allConfigs.txt https://raw.githubusercontent.com/Kolandone/v2raycollector/main/config.txt https://raw.githubusercontent.com/MhdiTaheri/V2rayCollector/main/sub/vless https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/configtg.txt https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/python/vless https://raw.githubusercontent.com/lagzian/SS-Collector/main/SS/TrinityBase https://raw.githubusercontent.com/terik21/HiddifySubs-VlessKeys/main/6Satu https://raw.githubusercontent.com/terik21/HiddifySubs-VlessKeys/main/7Sand https://raw.githubusercontent.com/wiki/gfpcom/free-proxy-list/lists/ss.txt https://raw.githubusercontent.com/Danialsamadi/v2go/main/All_Configs_Sub.txt https://raw.githubusercontent.com/sevcator/5ubscrpt10n/main/protocols/vl.txt https://raw.githubusercontent.com/aqayerez/MatnOfficial-VPN/main/MatnOfficial https://raw.githubusercontent.com/wiki/gfpcom/free-proxy-list/lists/vless.txt https://raw.githubusercontent.com/youfoundamin/V2rayCollector/main/ss_iran.txt https://raw.githubusercontent.com/Argh94/V2RayAutoConfig/main/configs/Vless.txt https://raw.githubusercontent.com/RaitonRed/ConfigsHub/main/All_Configs_Sub.txt https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/main/all_configs.txt https://raw.githubusercontent.com/skywrt/v2ray-configs/main/All_Configs_Sub.txt https://raw.githubusercontent.com/SamanGho/v2ray_collector/main/v2tel_links2.txt https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/main/Protocols/ss.txt https://raw.githubusercontent.com/Argh94/V2RayAutoConfig/main/configs/Germany.txt https://raw.githubusercontent.com/barry-far/V2ray-Config/main/All_Configs_Sub.txt https://raw.githubusercontent.com/coldwater-10/V2rayCollector/main/vmess_iran.txt https://raw.githubusercontent.com/youfoundamin/V2rayCollector/main/vless_iran.txt https://github.com/Epodonios/v2ray-configs/raw/main/Splitted-By-Protocol/vmess.txt https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/main/Protocols/vless.txt https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/main/Protocols/vmess.txt https://raw.githubusercontent.com/HosseinKoofi/GO_V2rayCollector/main/vless_iran.txt https://raw.githubusercontent.com/hamedcode/port-based-v2ray-configs/main/sub/ss.txt https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge.txt https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/main/githubmirror/14.txt https://raw.githubusercontent.com/10ium/ScrapeAndCategorize/main/output_configs/USA.txt https://raw.githubusercontent.com/Danialsamadi/v2go/main/Splitted-By-Protocol/vmess.txt https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/main/splitted-by-protocol/vless.txt https://raw.githubusercontent.com/RaitonRed/ConfigsHub/main/Splitted-By-Protocol/ss.txt https://raw.githubusercontent.com/ebrasha/free-v2ray-public-list/main/vmess_configs.txt https://raw.githubusercontent.com/hamedcode/port-based-v2ray-configs/main/sub/vless.txt https://raw.githubusercontent.com/hamedcode/port-based-v2ray-configs/main/sub/vmess.txt https://raw.githubusercontent.com/mshojaei77/v2rayAuto/main/telegram/popular_channels_1 https://raw.githubusercontent.com/mshojaei77/v2rayAuto/main/telegram/popular_channels_2 https://raw.githubusercontent.com/10ium/ScrapeAndCategorize/main/output_configs/Vless.txt https://raw.githubusercontent.com/barry-far/V2ray-Config/main/Splitted-By-Protocol/ss.txt https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/ss.txt https://raw.githubusercontent.com/kismetpro/NodeSuber/main/Splitted-By-Protocol/vless.txt https://raw.githubusercontent.com/nyeinkokoaung404/V2ray-Configs/main/All_Configs_Sub.txt https://raw.githubusercontent.com/itsyebekhe/PSG/main/config.txt https://github.com/4n0nymou3/multi-proxy-config-fetcher/raw/main/configs/proxy_configs.txt https://raw.githubusercontent.com/10ium/ScrapeAndCategorize/main/output_configs/France.txt https://raw.githubusercontent.com/RaitonRed/ConfigsHub/main/Splitted-By-Protocol/vless.txt https://raw.githubusercontent.com/RaitonRed/ConfigsHub/main/Splitted-By-Protocol/vmess.txt https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/sub/sub_merge.txt https://raw.githubusercontent.com/barry-far/V2ray-Config/main/Splitted-By-Protocol/vless.txt https://raw.githubusercontent.com/barry-far/V2ray-Config/main/Splitted-By-Protocol/vmess.txt https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vmess.txt https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/Splitted-By-Protocol/vmess.txt https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/main/splitted-by-protocol/shadowsocks.txt https://raw.githubusercontent.com/10ium/ScrapeAndCategorize/main/output_configs/Montenegro.txt https://raw.githubusercontent.com/10ium/ScrapeAndCategorize/main/output_configs/ShadowSocks.txt https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/all_sub.txt https://raw.githubusercontent.com/Firmfox/Proxify/main/v2ray_configs/seperated_by_protocol/shadowsocks.txt https://raw.githubusercontent.com/ebrasha/free-v2ray-public-list/main/V2Ray-Config-By-EbraSha-All-Type.txt",
        '2': "https://raw.githubusercontent.com/NiREvil/vless/main/sub/SSTime https://raw.githubusercontent.com/nscl5/5/main/configs/vmess.txt https://raw.githubusercontent.com/HakurouKen/free-node/main/public https://raw.githubusercontent.com/Mosifree/-FREE2CONFIG/main/Vless https://raw.githubusercontent.com/awesome-vpn/awesome-vpn/master/ss https://raw.githubusercontent.com/mfuu/v2ray/master/merge/merge.txt https://raw.githubusercontent.com/Mosifree/-FREE2CONFIG/main/Reality https://raw.githubusercontent.com/awesome-vpn/awesome-vpn/master/all https://raw.githubusercontent.com/VpnNetwork01/vpn-net/main/README.md https://raw.githubusercontent.com/Kolandone/v2raycollector/main/ssr.txt https://raw.githubusercontent.com/xiaoji235/airport-free/main/v2ray.txt https://raw.githubusercontent.com/penhandev/AutoAiVPN/main/AtuoAiVPN.txt https://raw.githubusercontent.com/Kolandone/v2raycollector/main/vmess.txt https://raw.githubusercontent.com/Syavar/V2ray-Configs/main/OK_vk.com.txt https://raw.githubusercontent.com/peasoft/NoMoreWalls/master/list_raw.txt https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/server.txt https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/ndnode.txt https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/wenode.txt https://raw.githubusercontent.com/MhdiTaheri/V2rayCollector/main/sub/vmess https://raw.githubusercontent.com/SonzaiEkkusu/V2RayDumper/main/config.txt https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/python/vmess https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/tg-parser.py https://raw.githubusercontent.com/iboxz/free-v2ray-collector/main/main/mix https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/yudou66.txt https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/nodefree.txt https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/main-parser.py https://raw.githubusercontent.com/Syavar/V2ray-Configs/main/OK_viber.com.txt https://raw.githubusercontent.com/iboxz/free-v2ray-collector/main/main/vless https://raw.githubusercontent.com/iboxz/free-v2ray-collector/main/main/vmess https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/clashmeta.txt https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/nodev2ray.txt https://raw.githubusercontent.com/Syavar/V2ray-Configs/main/OK_TLS_vk.com.txt https://raw.githubusercontent.com/Syavar/V2ray-Configs/main/OK_google.com.txt https://raw.githubusercontent.com/rango-cfs/NewCollector/main/v2ray_links.txt https://raw.githubusercontent.com/roosterkid/openproxylist/main/V2RAY_RAW.txt https://raw.githubusercontent.com/Barabama/FreeNodes/main/nodes/v2rayshare.txt https://raw.githubusercontent.com/arshiacomplus/v2rayExtractor/main/vless.html https://raw.githubusercontent.com/miladtahanian/V2RayCFGDumper/main/config.txt https://raw.githubusercontent.com/Created-By/Telegram-Eag1e_YT/main/%40Eag1e_YT https://raw.githubusercontent.com/Kolandone/v2raycollector/main/config_lite.txt https://raw.githubusercontent.com/Syavar/V2ray-Configs/main/OK_telegram.org.txt https://raw.githubusercontent.com/Syavar/V2ray-Configs/main/OK_whatsapp.com.txt https://raw.githubusercontent.com/skywrt/v2ray-configs/main/Config%20list15.txt https://raw.githubusercontent.com/skywrt/v2ray-configs/main/Config%20list49.txt https://raw.githubusercontent.com/MahsaNetConfigTopic/config/main/xray_final.txt https://raw.githubusercontent.com/SamanGho/v2ray_collector/main/v2tel_links1.txt https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/main/Countries/Tr.txt https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/main/Countries/Us.txt https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/python/splitter.py https://raw.githubusercontent.com/Syavar/V2ray-Configs/main/OK_TLS_viber.com.txt https://raw.githubusercontent.com/arshiacomplus/v2rayExtractor/main/mix/sub.html https://raw.githubusercontent.com/ermaozi/get_subscribe/main/subscribe/v2ray.txt https://raw.githubusercontent.com/Mahdi0024/ProxyCollector/master/sub/proxies.txt https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/backups/tg-parser_1 https://raw.githubusercontent.com/Syavar/V2ray-Configs/main/OK_TLS_google.com.txt https://raw.githubusercontent.com/Syavar/V2ray-Configs/main/OK_activision.com.txt https://raw.githubusercontent.com/Syavar/V2ray-Configs/main/OK_css.rbxcdn.com.txt https://raw.githubusercontent.com/youfoundamin/V2rayCollector/main/mixed_iran.txt https://raw.githubusercontent.com/Epodonios/v2ray-configs/main/All_Configs_Sub.txt https://raw.githubusercontent.com/iboxz/free-v2ray-collector/main/main/shadowsocks https://raw.githubusercontent.com/Argh94/V2RayAutoConfig/main/configs/Hysteria2.txt https://raw.githubusercontent.com/Farid-Karimi/Config-Collector/main/mixed_iran.txt https://raw.githubusercontent.com/MhdiTaheri/V2rayCollector_Py/main/sub/Mix/mix.txt https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/backups/main-parser_1 https://raw.githubusercontent.com/Syavar/V2ray-Configs/main/OK_TLS_telegram.org.txt https://raw.githubusercontent.com/Syavar/V2ray-Configs/main/OK_TLS_whatsapp.com.txt https://raw.githubusercontent.com/Syavar/V2ray-Configs/main/OK_TLS_activision.com.txt https://raw.githubusercontent.com/Syavar/V2ray-Configs/main/OK_TLS_css.rbxcdn.com.txt https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity.txt https://raw.githubusercontent.com/Syavar/V2ray-Configs/main/OK_speedtest.tinkoff.ru.txt https://raw.githubusercontent.com/Kwinshadow/TelegramV2rayCollector/main/sublinks/ss.txt  https://raw.githubusercontent.com/Kwinshadow/TelegramV2rayCollector/main/sublinks/mix.txt https://raw.githubusercontent.com/skywrt/v2ray-configs/main/Splitted-By-Protocol/vmess.txt https://raw.githubusercontent.com/Kwinshadow/TelegramV2rayCollector/main/sublinks/vless.txt https://raw.githubusercontent.com/Kwinshadow/TelegramV2rayCollector/main/sublinks/vmess.txt https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/main/Countries/Liechtenstein.txt https://raw.githubusercontent.com/Syavar/V2ray-Configs/main/OK_TLS_speedtest.tinkoff.ru.txt https://raw.githubusercontent.com/Firmfox/Proxify/main/v2ray_configs/mixed/subscription-2.txt https://raw.githubusercontent.com/SoliSpirit/v2ray-configs/main/Countries/North_Macedonia.txt https://raw.githubusercontent.com/10ium/ScrapeAndCategorize/main/output_configs/Turkmenistan.txt https://raw.githubusercontent.com/MrAbolfazlNorouzi/iran-configs/main/configs/working-configs.txt https://raw.githubusercontent.com/ebrasha/free-v2ray-public-list/main/V2Ray-Config-By-EbraSha.txt https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/v2ray/subs/sub1.txt https://raw.githubusercontent.com/mohamadfg-dev/telegram-v2ray-configs-collector/main/category/xhttp.txt https://raw.githubusercontent.com/mohamadfg-dev/telegram-v2ray-configs-collector/main/category/httpupgrade.txt https://raw.githubusercontent.com/MrMohebi/xray-proxy-grabber-telegram/master/collected-proxies/row-url/all.txt https://raw.githubusercontent.com/MrMohebi/xray-proxy-grabber-telegram/master/collected-proxies/row-url/actives.txt",
    }

    urls = []
    old_lines = set()
    new_lines = set()
    existing_lines = set()

    user_input = input("Enter numbers: ")
    things = input("Enter thing(s): ").split()
    use_old = input("Use old.json? (y/n): ") == 'y'
    update_old = input("Update old.json dump? (y/n): ") == 'y'

    if os.path.exists('all.txt'):
        with open('all.txt') as f:
            for line in f:
                cleaned = line.split('#')[0].strip()
                if cleaned:
                    existing_lines.add(cleaned)

    if use_old and os.path.exists('old.json'):
        with open('old.json') as f:
            old_lines = set(json.load(f))

    for num in user_input:
        urls.extend(url_map.get(num, '').split())

    def fetch(url):
        try:
            with urllib.request.urlopen(url, timeout=3) as r:
                return r.read().decode().splitlines()
        except Exception:
            return []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        for result in executor.map(fetch, urls):
            for line in result:
                cleaned = line.split('#')[0].strip()
                if cleaned and any(word in line.lower() for word in things) and cleaned not in old_lines:
                    new_lines.add(cleaned)

    before = len(existing_lines)
    existing_lines.update(new_lines)
    added = len(existing_lines) - before

    def sort_key(line):
        parts = line.split('?', 1) if '?' in line else line.split('@', 1)
        return (len(line), parts[1] if len(parts) > 1 else line)

    sorted_lines = sorted(existing_lines, key=sort_key)
    total_lines = len(sorted_lines)
    digits_needed = len(str(total_lines))

    processed = []
    if total_lines < 1500:
        print(f"Adding flags automatically for {total_lines} lines...")

        def get_flag(code):
            return ''.join(chr(ord(c) + 127397) for c in code) if code else ''

        def get_country_batch(ip_list):
            url = "http://ip-api.com/batch?fields=countryCode,query"
            try:
                data = json.dumps(ip_list)
                headers = {'Content-Type': 'application/json'}
                response = requests.post(url, data=data, headers=headers, timeout=5)
                if response.status_code == 200:
                    results = response.json()
                    return {item['query']: item.get('countryCode', '') for item in results}
            except Exception:
                pass
            return {}

        ips_to_resolve = []
        for line in sorted_lines:
            match = re.search(r'@([^:]+):', line)
            ip = match.group(1) if match else ''
            if ip:
                ips_to_resolve.append(ip)

        ip_country = {}
        batch_size = 100
        for i in range(0, len(ips_to_resolve), batch_size):
            batch_ips = ips_to_resolve[i:i + batch_size]
            print(f"Processing batch {i // batch_size + 1}/{(len(ips_to_resolve)-1)//batch_size + 1}")
            batch_results = get_country_batch(batch_ips)
            ip_country.update(batch_results)

        for i, line in enumerate(sorted_lines, 1):
            match = re.search(r'@([^:]+):', line)
            ip = match.group(1) if match else ''
            flag = get_flag(ip_country.get(ip, ''))
            processed.append(f"{line}#{i:0{digits_needed}d}{flag}")

    else:
            processed = [f"{line}" for line in sorted_lines]

    with open('all.txt', 'w') as f:
        f.write('\n'.join(processed))

    print(f"Added {added} new lines. Total: {len(sorted_lines)}")

    if update_old:
        existing_data = set()
        if os.path.exists('old.json'):
            with open('old.json', 'r') as f:
                existing_data = set(json.load(f))
        combined_data = existing_data.union(sorted_lines)
        with open('old.json', 'w') as f:
            json.dump(list(combined_data), f, indent=2)
        print(f"Updated old.json with {len(combined_data)} total lines")

if __name__ == "__main__":
    main()
