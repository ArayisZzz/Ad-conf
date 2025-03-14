import re
import requests
import time

rules_url = [
            # 'filters.txt',
             #Ads
            # 'badware.min.txt',
             #Badware risks
            # 'privacy.txt',
             #Privacy
            # 'quick-fixes.txt',
             #Quick fixes
            # 'unbreak.txt',
             #Unbreak
            # 'easylist.txt',
             #EasyList
            # '2_without_easylist.txt',
            # '11.txt',
            # 'urlhaus-filter-ag-online.txt',
            # '224.txt',
             #Anti-AD
             'anti-ad-adguard.txt'
             ]
f2 = open("ad.conf",'a')
t = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime())
f2.write("# This config is generated on " +t+"\n")
f2.write("[General]\nprefer-ipv6 = true\nipv6 = true\nbypass-system = true\nskip-proxy = 192.168.0.0/16, 10.0.0.0/8, 172.16.0.0/12, fe80::/10, fc00::/7, localhost, *.local, *.lan, *.internal, e.crashlytics.com, captive.apple.com, sequoia.apple.com, seed-sequoia.siri.apple.com, *.ls.apple.com\nbypass-tun = 10.0.0.0/8,100.64.0.0/10,127.0.0.0/8,169.254.0.0/16,172.16.0.0/12,192.0.0.0/24,192.0.2.0/24,192.88.99.0/24,192.168.0.0/16,198.18.0.0/15,198.51.100.0/24,203.0.113.0/24,233.252.0.0/24,224.0.0.0/4,255.255.255.255/32,::1/128,::ffff:0:0/96,::ffff:0:0:0/96,64:ff9b::/96,64:ff9b:1::/48,100::/64,2001::/32,2001:20::/28,2001:db8::/32,2002::/16,3fff::/20,5f00::/16,fc00::/7,fe80::/10,ff00::/8\ndns-server = https://dns.adguard-dns.com/dns-query, https://security.cloudflare-dns.com/dns-query, https://doh.pub/dns-query\n")
f2.write("update-url = https://raw.githubusercontent.com/ArayisZzz/Ad-conf/refs/heads/main/ad.conf\n")
f2.write("[Rule]\n")

for url in rules_url:
    f1 = open(url,'r',encoding='utf-8')
    for str in f1:
        flag = 0
        it = re.finditer('^\|\|[0-9.]+\^$',str)
        for match in it:
            if flag != 0:
                flag = 1
            f2.write("IP-CIDR,"+match.string[2:len(match.string)-2]+",REJECT\n")
        if flag:
            break
        it = re.finditer('^\|\|[\w.-]+\^$',str)
        for match in it:
            f2.write("DOMAIN-SUFFIX,"+match.string[2:len(match.string)-2]+",REJECT\n")
        #time.sleep(1)
    f1.close
#f1 = open("11.txt","r",encoding='utf-8')

f2.write("GEOIP,PRIVATE,DIRECT\nGEOIP,FACEBOOK,PROXY\nGEOIP,CN,DIRECT\nFINAL,PROXY\n")
f2.write("[Host]\nlocalhost = 127.0.0.1\n[URL Rewrite]\n^https?://(www.)?(g|google)\.cn https://www.google.com 302\n")
f2.write("[MITM]\nhostname = *.google.cn,*.googlevideo.com")
f2.close
#f1.close
