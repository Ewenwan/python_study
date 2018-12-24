import re
import requests
import lxml.html
from bs4 import BeautifulSoup
from lxml import etree

url='http://example.python-scraping.com/places/default/view/United-States-234?tdsourcetag=s_pcqq_aiomsg'
headers={
    'UserAgent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
}
html = requests.get(url,headers=headers).text
print(html)
neighbours= re.compile(r'<a href="/places/default/iso/.*?>(.*?)</a>')
country=re.compile(r'</label></td><td class="w2p_fw">US</td><td class="w2p_fc"></td></tr><tr id="places_country_or_district__row"><td class="w2p_fl"><label class="readonly" for="places_country_or_district" id="places_country_or_district__label">(.*?)</label></td><td class="w2p_fw">(.*?)</td><td class="w2p_fc"></td></tr><tr id="places_capital__row"><td class="w2p_fl"><label class="readonly" for="places_capital"')
a= re.findall(neighbours,html)
b= re.findall(country,html)
print(f'国家是{b}，邻国是{a}')




tree =etree.HTML(html)
print(tree)
# <div><a href="/places/default/iso/CA">CA </a><a
country1= tree.xpath('//tr[@id="places_country_or_district__row"]/td[@class="w2p_fw"]/text()')
#neighbours1 = tree.xpath('//tr[@id="places_neighbours__row"]/td[@id="places_neighbours__row"]/text()')
print(f'国家是{country1}')


bs = BeautifulSoup(html, 'lxml')
# print(bs.prettify()) 格式化输出
tag_tr =bs.find(id="places_country_or_district__row")
print(tag_tr)
tag_td =tag_tr.find('td', class_="w2p_fw")
print(tag_tr)
print(tag_td.string)
