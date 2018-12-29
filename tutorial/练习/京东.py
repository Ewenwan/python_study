# coding:utf-8
import requests
from  CrawlerUtility import ChromeHeaders2Dict
from lxml import etree

jingdong_url= 'https://search.jd.com/Search?keyword=%E6%88%B4%E5%B0%94%E7%AC%94%E8%AE%B0%E6%9C%AC&enc=utf-8&suggest=1.def.0.V11&wq=%E6%88%B4%E5%B0%94&pvid=fd26f1f5e26b40c997ec97fdd073ba0d'

header="""
content-encoding: gzip
content-type: text/html
date: Thu, 27 Dec 2018 02:05:31 GMT
server: nginx
set-cookie: xtest=2137.cf6b6759; expires=Sat, 26-Jan-2019 02:05:31 GMT; Max-Age=2592000; domain=search.jd.com
status: 200
strict-transport-security: max-age=86400
vary: Accept-Encoding
:authority: search.jd.com
:method: GET
:path: /Search?keyword=%E6%88%B4%E5%B0%94%E7%AC%94%E8%AE%B0%E6%9C%AC&enc=utf-8&suggest=1.def.0.V11&wq=%E6%88%B4%E5%B0%94&pvid=fd26f1f5e26b40c997ec97fdd073ba0d
:scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: no-cache
cookie: __jdu=1748840955; user-key=8fe4e1e6-7754-4192-b361-4d8c97207bad; cn=0; shshshfpa=b22ac211-878b-bb3f-5c50-5cf700de874e-1544060619; shshshfpb=181be432c665246ee9f610250677e1453c350996dc04811155c087ec9d; xtest=2137.cf6b6759; ipLoc-djd=1-72-2799-0; qrsc=3; ipLocation=%u5317%u4EAC; unpl=V2_ZzNtbUJeFBx9DEFRLxxaUmJQFVxLABdAdVtBAXhMVA1nVhNVclRCFXwURldnGloUZgsZWUtcQxxFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2VH0cVQxiAhpZRmdzEkU4dl14GVsBZDMTbUNnAUEpDkNXcxFZSGcFF1RLUkIdcQx2VUsa; __jda=122270672.1748840955.1544060591.1544666536.1545875901.3; __jdc=122270672; shshshfp=134a0b70fbe4bec59179a83a16db94ea; PCSYCityID=7; TrackID=1rQkqIHa4PmQ4lhw0f1mV2-lcJ9MSm9_AvXoF05PolM6au-_ntvag6eCARCAgjsB8JcjqsZtYbnblhTsPi--VLj7vX4j0K9wUuzCNUNV0xLs; thor=236971B4223F4E974A9554AFBCB4403886F6F0431B6C660AFDA33C4E9AFD8552AE81F405F2983D359FD66B6A6DCD6730EE49AECBB079F293BD24E2E0B2053CAB09DA5E22DFC2EFA6E8880FF8ADBC890B2C2BF1137B9CC9542907B18BBF4FBB4E261C596A0EF23F03EC85AA0B56057C53130D166FA3EFEC1D05303DF140ED6CC057428F330CC45E7E62680D70022BF25B689FE125058BAD8A4C89528DFEDC59FD; pinId=s5LaW4nqpNhLBzXzCl_wnrV9-x-f3wj7; pin=jd_6207f7184529a; unick=trc1999; ceshi3.com=201; _tp=JNzKxe7DcCfngCwIpeljGPHF2xkonm%2BVgi2OnGhA3jU%3D; _pst=jd_6207f7184529a; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_18f89564e47f4b608fed1b6d2d991d09|1545876211200; __jdb=122270672.6.1748840955|3.1545875901; shshshsID=c20ce3f443ba93dd572d10c9697fec09_4_1545876267813; rkv=V0600; 3AB9D23F7A4B3C9B=63GCTH622YUFDF7LLLKS4SFGGAQNAOCG7344QFFU4MPE2EQSTKICUSWSUVO6K5WJBWOIOA2E25WLZZVJ4SMBFYYLEY
pragma: no-cache
referer: https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_18f89564e47f4b608fed1b6d2d991d09
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36
"""
headers = ChromeHeaders2Dict(header)
title = requests.get(jingdong_url,headers=headers).content
tree = etree.HTML(title)
pattern ='//*[@id="J_goodsList"]/ul/li/div/div/a/em/text()'
pattern1 ='/html/body/div[5]/a/text()'
price = '//*[@id="J_goodsList"]/ul/li/div/div/strong/i/text()'
configure ='//*[@id="J_goodsList"]/ul/li/div/div/a/i/text()'

notebook_name =tree.xpath(pattern)
notebook_style=tree.xpath(pattern1)
note_price =tree.xpath(price)
configure1 =tree.xpath(configure)
for i in range(len(note_price)):
    print(f'戴尔笔记本：{i}')
    print(f'笔记本的名字:{notebook_name[i]}，笔记本的价格:{note_price[i]},笔记本的配置：{configure1[i]}')

