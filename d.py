import urllib.request
import concurrent.futures

file_path = "/home/felix/Documents/all.txt"
url_map = {
    '0': "your set of links",
    '1': "https://raw.githubusercontent.com/barry-far/V2ray-Config/refs/heads/main/All_Configs_Sub.txt https://raw.githubusercontent.com/Argh94/V2RayAutoConfig/refs/heads/main/configs/Vless.txt https://raw.githubusercontent.com/T3stAcc/V2Ray/refs/heads/main/All_Configs_Sub.txt https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/All_Configs_Sub.txt https://raw.githubusercontent.com/AvenCores/goida-vpn-configs/refs/heads/main/githubmirror/14.txt https://raw.githubusercontent.com/Surfboardv2ray/TGParse/refs/heads/main/configtg.txt https://raw.githubusercontent.com/gfpcom/free-proxy-list/main/list/vless.txt https://raw.githubusercontent.com/darknessm427/V2ray-Sub-Collector/refs/heads/main/All_Darkness_Sub.txt https://github.com/Epodonios/v2ray-configs/raw/main/Splitted-By-Protocol/ss.txt https://github.com/Epodonios/v2ray-configs/raw/main/Splitted-By-Protocol/vmess.txt https://github.com/Epodonios/v2ray-configs/raw/main/Splitted-By-Protocol/trojan.txt https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/xray/normal/mix https://raw.githubusercontent.com/itsyebekhe/PSG/main/lite/subscriptions/xray/normal/hy2 https://raw.githubusercontent.com/itsyebekhe/PSG/main/subscriptions/xray/normal/vmess https://yalda.nscl.ir https://raw.githubusercontent.com/NiREvil/vless/refs/heads/main/sub/SSTime https://dev1.irdevs.sbs https://raw.githubusercontent.com/darkvpnapp/CloudflarePlus/refs/heads/main/index.html https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/ss.txt https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vmess.txt https://raw.githubusercontent.com/barry-far/V2ray-config/main/Splitted-By-Protocol/vless.txt https://v2.alicivil.workers.dev https://v2.alicivil.workers.dev/?list=us&count=300&shuffle=true&unique=false https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/Eternity https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/EternityAir https://raw.githubusercontent.com/mahdibland/ShadowsocksAggregator/master/sub/splitted/trojan.txt https://raw.githubusercontent.com/nscl5/5/refs/heads/main/configs/all.txt https://raw.githubusercontent.com/nscl5/5/refs/heads/main/configs/vmess.txt https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/mixed https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/python/hysteria2 https://shadowmere.xyz/api/b64sub https://raw.githubusercontent.com/NiREvil/vless/refs/heads/main/sub/fragment https://raw.githubusercontent.com/Mahdi0024/ProxyCollector/master/sub/proxies.txt https://raw.githubusercontent.com/arshiacomplus/v2rayExtractor/refs/heads/main/mix/sub.html https://raw.githubusercontent.com/arshiacomplus/v2rayExtractor/refs/heads/main/vless.html https://raw.githubusercontent.com/10ium/free-config/refs/heads/main/HighSpeed.txt https://raw.githubusercontent.com/DarknessShade/Sub/main/V2mix https://raw.githubusercontent.com/DarknessShade/Sub/main/Ss https://raw.githubusercontent.com/NiREvil/vless/refs/heads/main/sub/freedom https://raw.githubusercontent.com/lagzian/IranConfigCollector/main/Base64.txt https://raw.githubusercontent.com/lagzian/SS-Collector/refs/heads/main/SS/TrinityBase https://raw.githubusercontent.com/MahsaNetConfigTopic/config/refs/heads/main/xray_final.txt https://raw.githubusercontent.com/hamedcode/port-based-v2ray-configs/main/sub/vless.txt https://raw.githubusercontent.com/hamedcode/port-based-v2ray-configs/main/sub/vmess.txt https://raw.githubusercontent.com/hamedcode/port-based-v2ray-configs/main/sub/ss.txt https://raw.githubusercontent.com/Pawdroid/Free-servers/refs/heads/main/sub https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/ss https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/trojan https://raw.githubusercontent.com/Surfboardv2ray/TGParse/main/splitted/vless https://raw.githubusercontent.com/roosterkid/openproxylist/main/V2RAY_BASE64.txt https://raw.githubusercontent.com/HosseinKoofi/GO_V2rayCollector/main/mixed_iran.txt https://raw.githubusercontent.com/HosseinKoofi/GO_V2rayCollector/main/vless_iran.txt https://raw.githubusercontent.com/HosseinKoofi/GO_V2rayCollector/main/ss_iran.txt https://raw.githubusercontent.com/ebrasha/free-v2ray-public-list/refs/heads/main/V2Ray-Config-By-EbraSha.txt https://raw.githubusercontent.com/ebrasha/free-v2ray-public-list/refs/heads/main/vmess_configs.txt https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/main/splitted-by-protocol/ss/ss.txt https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/main/splitted-by-protocol/trojan/trojan_part1.txt https://raw.githubusercontent.com/F0rc3Run/F0rc3Run/main/splitted-by-protocol/vless/vless_part1.txt https://raw.githubusercontent.com/youfoundamin/V2rayCollector/main/mixed_iran.txt https://raw.githubusercontent.com/youfoundamin/V2rayCollector/main/vless_iran.txt https://raw.githubusercontent.com/youfoundamin/V2rayCollector/main/trojan_iran.txt https://raw.githubusercontent.com/youfoundamin/V2rayCollector/main/ss_iran.txt https://raw.githubusercontent.com/youfoundamin/V2rayCollector/main/vmess_iran.txt https://raw.githubusercontent.com/Stinsonysm/GO_V2rayCollector/refs/heads/main/trojan_iran.txt https://raw.githubusercontent.com/MhdiTaheri/V2rayCollector_Py/refs/heads/main/sub/Mix/mix.txt https://raw.githubusercontent.com/MhdiTaheri/V2rayCollector_Py/refs/heads/main/sub/United%20States/config.txt https://raw.githubusercontent.com/liketolivefree/kobabi/main/sub.txt https://raw.githubusercontent.com/liketolivefree/kobabi/main/sub_all.txt https://raw.githubusercontent.com/10ium/ScrapeAndCategorize/refs/heads/main/output_configs/Hysteria2.txt https://raw.githubusercontent.com/10ium/V2ray-Config/main/Splitted-By-Protocol/hysteria2.txt https://raw.githubusercontent.com/10ium/V2Hub3/main/merged_base64 https://raw.githubusercontent.com/10ium/base64-encoder/main/encoded/10ium_mixed_iran.txt https://raw.githubusercontent.com/10ium/ScrapeAndCategorize/refs/heads/main/output_configs/Vless.txt https://raw.githubusercontent.com/10ium/ScrapeAndCategorize/refs/heads/main/output_configs/ShadowSocks.txt https://raw.githubusercontent.com/10ium/ScrapeAndCategorize/refs/heads/main/output_configs/Trojan.txt https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Sub1.txt https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Sub2.txt https://raw.githubusercontent.com/Epodonios/v2ray-configs/refs/heads/main/Sub3.txt https://github.com/Epodonios/v2ray-configs/raw/main/All_Configs_base64_Sub.txt https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub1.txt https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub2.txt https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub3.txt https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub4.txt https://raw.githubusercontent.com/V2RAYCONFIGSPOOL/V2RAY_SUB/refs/heads/main/v2ray_configs.txt https://raw.githubusercontent.com/bamdad23/JavidnamanIran/refs/heads/main/WS%2BHysteria2 https://raw.githubusercontent.com/mshojaei77/v2rayAuto/refs/heads/main/telegram/popular_channels_1 https://raw.githubusercontent.com/mshojaei77/v2rayAuto/refs/heads/main/telegram/popular_channels_2 https://raw.githubusercontent.com/mshojaei77/v2rayAuto/refs/heads/main/subs/hysteria https://raw.githubusercontent.com/mshojaei77/v2rayAuto/refs/heads/main/subs/hy2 https://raw.githubusercontent.com/ndsphonemy/proxy-sub/refs/heads/main/speed.txt https://raw.githubusercontent.com/ndsphonemy/proxy-sub/refs/heads/main/hys-tuic.txt https://trojanvmess.pages.dev/cmcm?b64 https://raw.githubusercontent.com/Mosifree/-FREE2CONFIG/refs/heads/main/Reality https://raw.githubusercontent.com/Mosifree/-FREE2CONFIG/refs/heads/main/Vless https://raw.githubusercontent.com/AzadNetCH/Clash/refs/heads/main/AzadNet_iOS.txt https://raw.githubusercontent.com/Proxydaemitelegram/Proxydaemi44/refs/heads/main/Proxydaemi44 https://raw.githubusercontent.com/MrMohebi/xray-proxy-grabber-telegram/refs/heads/master/collected-proxies/xray-json-full/actives_all.json https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub6.txt https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub7.txt https://raw.githubusercontent.com/barry-far/V2ray-config/main/Sub8.txt https://raw.githubusercontent.com/barry-far/V2ray-Configs/main/Sub9.txt https://azadnet05.pages.dev/sub/4d794980-54c0-4fcb-8def-c2beaecadbad https://raw.githubusercontent.com/amirparsaxs/Vip-s/refs/heads/main/Sub.vip https://raw.githubusercontent.com/rango-cfs/NewCollector/refs/heads/main/v2ray_links.txt",
}

existing_lines = set()
try:
    with open(file_path) as f:
        for line in f:
            cleaned = line.split('#')[0].strip()
            if cleaned: existing_lines.add(cleaned)
except FileNotFoundError:
    pass

user_input = input("Enter numbers: ").split()
thing = input("Enter thing: ")
urls = []
for num in user_input:
    urls.extend(url_map.get(num, '').split())

new_lines = set()
def fetch(url):
    try:
        with urllib.request.urlopen(url, timeout=3) as r:
            return r.read().decode().splitlines()
    except Exception:
        return []
with concurrent.futures.ThreadPoolExecutor() as executor:
    for result in executor.map(fetch, urls):
        for line in result:
            if thing in line.lower():
                cleaned = line.split('#')[0].strip()
                if cleaned: new_lines.add(cleaned)

before = len(existing_lines)
existing_lines.update(new_lines)
added = len(existing_lines) - before

def sort_key(line):
    parts = line.split('?', 1) if '?' in line else line.split('@', 1)
    return (len(line), parts[1] if len(parts) > 1 else line)

sorted_lines = sorted(existing_lines, key=sort_key)
with open(file_path, 'w') as f:
    for i, line in enumerate(sorted_lines, 1):
        f.write(f"{line}#{i:05d}\n")

print(f"Added {added} new lines. Total: {len(sorted_lines)}")