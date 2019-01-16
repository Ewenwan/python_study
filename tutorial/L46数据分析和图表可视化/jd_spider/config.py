from os import path
import logging

# app
DEBUG = True
LOGGER_LEVEL = logging.DEBUG

# database
DB = {
    'database': 'jd_spider',
    'user': 'jd_spider',
    'password': '56tyghbn',
    'host': '127.0.0.1',
    'port': 5432
}

# 请求
COMMENT_REQUEST = {
    'url_product_detail': 'https://sclub.jd.com/comment/productPageComments.action',
    'headers': {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'Accept':'*/*',
        # 'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Connection': 'close',
        'Referer': 'https://www.jd.com/',
    },
    'cookie_detail': 'pinId=uGywawhW5xQ; pin=zzdxyz; unick=%E7%BB%86%E8%BD%AF%E8%B7%91; _tp=EtAWqzuy%2FaNSh0LFcTfGgQ%3D%3D; _pst=zzdxyz; ipLocation=%u6cb3%u5357; ipLoc-djd=7-412-3546-51752.138717862; __jdu=1116854873; PCSYCityID=412; storeuuid=34e44c080257acef7d5c7a381322c200; __jdv=122270672|direct|-|none|-|1525602531948; user-key=8b3bd651-237d-40b3-8ff2-ae6f55287036; shshshfpa=47ce8031-3d21-6ec4-a199-4b04761f98d6-1525623427; shshshfpb=132de6f4db5b547f8b7579cd030acc2a5424c1fe33fdd7f245aef2a83f; ceshi3.com=000; __jdc=122270672; wlfstk_smdl=1napqxlem5xovw3ge5hpb9d8w8oul8en; _jrda=4; TrackID=1jx-DjE00e6ZPABZqOOLcGWISd3rqFve7QjcnG7y_Ij2Q6zfPugsRi3DKuB_WoEMIUB_Vbbw8tCAMoMaF57ACtKiaSQfVXzC0q24tmf5Po-WUETBh7OzsZ00Bjb_Oqur3; 3AB9D23F7A4B3C9B=P3R4PR62ZZYXLL66CERAFTQSQSAKT7ITZPAJADRRZETZZX62AERZVN622DZ5N36LFOTG2FT5H5AAR23E72LJ77L6ZI; areaId=7; cn=3; __jda=122270672.1116854873.1501152429.1525917806.1525946141.120; shshshfp=87378f16b794028ca9f07259710d20e2; __jdb=122270672.10.1116854873|120.1525946141',
    'cookie_home': 'pinId=uGywawhW5xQ; pin=zzdxyz; unick=%E7%BB%86%E8%BD%AF%E8%B7%91; _tp=EtAWqzuy%2FaNSh0LFcTfGgQ%3D%3D; _pst=zzdxyz; userInfo2016=1; ipLocation=%u6cb3%u5357; ipLoc-djd=7-412-3546-51752.138717862; __jdu=1116854873; PCSYCityID=412; storeuuid=34e44c080257acef7d5c7a381322c200; __jdv=122270672|direct|-|none|-|1525602531948; user-key=8b3bd651-237d-40b3-8ff2-ae6f55287036; shshshfpa=47ce8031-3d21-6ec4-a199-4b04761f98d6-1525623427; shshshfpb=132de6f4db5b547f8b7579cd030acc2a5424c1fe33fdd7f245aef2a83f; ceshi3.com=000; __jdc=122270672; wlfstk_smdl=1napqxlem5xovw3ge5hpb9d8w8oul8en; _jrda=4; TrackID=1jx-DjE00e6ZPABZqOOLcGWISd3rqFve7QjcnG7y_Ij2Q6zfPugsRi3DKuB_WoEMIUB_Vbbw8tCAMoMaF57ACtKiaSQfVXzC0q24tmf5Po-WUETBh7OzsZ00Bjb_Oqur3; 3AB9D23F7A4B3C9B=P3R4PR62ZZYXLL66CERAFTQSQSAKT7ITZPAJADRRZETZZX62AERZVN622DZ5N36LFOTG2FT5H5AAR23E72LJ77L6ZI; areaId=7; cn=3; shshshfp=87378f16b794028ca9f07259710d20e2; __jda=122270672.1116854873.1501152429.1525946141.1526011500.121; __jdb=122270672.1.1116854873|121.1526011500; o2Control=webp|lastvisit=11; shshshsID=bd67d5e772b2918eda4d3261202acc1a_1_1526011501286',
    'time_sleep': 5,
}



PRODUCT_IMAGE_PREFIX = 'https://img10.360buyimg.com/n1/s80x80_'



COMMON_REQUEST = {

}

# 路径
PATH_ROOT = path.dirname(__file__)
PATH_FONT = path.join(PATH_ROOT, 'static/font/Arial Unicode.ttf')
# 图片
WORD_CLOUD_IMG = PATH_ROOT + '/static/word_cloud_images/word_cloud.png'
CHART_WORD_FREQUENCY_IMG = PATH_ROOT + '/static/pygal_chart_images/word_frequency.svg'
CHART_WORD_POSITIVE_IMG = PATH_ROOT + '/static/pygal_chart_images/word_positive.svg'
CHART_PRODUCT_PROPORTION_IMG = PATH_ROOT + '/static/pygal_chart_images/product_proportion.svg'
CHART_COMMENT_TREND_IMG = PATH_ROOT + '/static/pygal_chart_images/comment_trend.svg'
# CHART_WORD_FREQUENCY_IMG = PATH_ROOT + '/static/pygal_chart_images/word_frequency.svg'

# 字典
STOPWORD_ZH_DICT = path.join(PATH_ROOT, 'dict/stop_words_zh.txt')
EMOTION_POSITIVE_ZH_DICT = path.join(PATH_ROOT, 'dict/emotion_dict/pos_all_dict.txt')
EMOTION_NEGATIVE_ZH_DICT = path.join(PATH_ROOT, 'dict/emotion_dict/neg_all_dict.txt')


user_agent_list = [
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)',
    'DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)',
    'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
    'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)',
    'ia_archiver (+http://www.alexa.com/site/help/webmasters; crawler@alexa.com)',
]


CATEGORY = [
    {'name':'手机', 'category':(737,794,798)},
]