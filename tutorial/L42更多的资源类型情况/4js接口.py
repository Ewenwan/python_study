# 4. js异步请求
# 一些后端语言框架django是把变量渲染到html模板最终再requests返回，用户交互时需要刷新页面才能看到修改后的效果。为了更好地网页体验和前后端程序员工作分离。前端js工作中也有类似后端requests包的前端操作包。导致有些数据第一次html中并看不到，浏览器会在加载html后执行js，但requests包不会，无法直接获取到信息。
# 解决思路：js中发送http请求，浏览器开发者工具会截取到，分析http请求结构，用requests包构造请求获取信息。

"""
<html>
    <body>
        <hl>待爬取内容</hl>
            <script>
                document.onloads(
                function foo():{
                //请求商品列表
                // (伪代码)
                function request(page_no=1){
                    resp = request('http://www.js.com/itemlist')
                    dom.create('div').text = resp.text
                }
                //操作dom节点把商品嘻嘻渲染到页面中。
                })

                $.('button').ajax({
                    ur：xxx,
                    params: page_no=1
                })
            </script>

    </body>
</html>

js中情况一  类似后端的requests包，发送http请求。开发者工具中看到响应是否是json数据。
js中情况二   ajax 相当于上面的封装。xml结构沟通。开发者工具XHR(XMLHttpRequest)

小技巧：网页请求非常多，1.排除jpg，css这些请求 2. 看XHR里有没有  3. 看post类型  4. 猜请求接口关键字comment list。ctrl+F开发者工具中搜索。查看疑似请求的响应是不是json评论数据。
"""


# 需求：爬取一个商品的评论
"""
分析：商品评论原始url https://item.jd.com/100000287113.html#comment
当点击评论里的第二页的时候，url路由并没有变化没有参数。
如果django来做分页路由形式如下
https://item.jd.com/100000287113.html/comment?page_no=2。
其实评论信息的请求在js中，由浏览器后台执行。
所以我们需要在谷歌开发者工具中 找出js中的评论信息请求，requests包构造请求，模拟浏览器的执行过程。
"""
"""
分析后得到的请求地址
https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv15261&productId=100000287113&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1
然后用requests包构造这个请求。
分析参数：发现有的参数不知含义或动态生成或保存默认即可。考虑删减具有默认值或无用的参数。
"""
from urllib.request import urlretrieve
import json
import requests
from lxml import etree
from CrawlerUtility import ChromeHeaders2Dict

comment_url = 'https://sclub.jd.com/comment/productPageComments.action'

params = {
    'productId':'100000287113', #商品id。先写死 苹果手机。
    'score': 0,
    'sortType': 5,
    'page': 0,
    'pageSize': 10,
    # 'isShadowSky': 0,
    # 'fold': 1
    #  'callback':'fetchJSON_comment98xx15261',
}
header="""
cookie: __jdu=1748840955; user-key=8fe4e1e6-7754-4192-b361-4d8c97207bad; cn=0; shshshfpa=b22ac211-878b-bb3f-5c50-5cf700de874e-1544060619; shshshfpb=181be432c665246ee9f610250677e1453c350996dc04811155c087ec9d; ipLoc-djd=1-72-2799-0; ipLocation=%u5317%u4EAC; PCSYCityID=7; TrackID=1rQkqIHa4PmQ4lhw0f1mV2-lcJ9MSm9_AvXoF05PolM6au-_ntvag6eCARCAgjsB8JcjqsZtYbnblhTsPi--VLj7vX4j0K9wUuzCNUNV0xLs; pinId=s5LaW4nqpNhLBzXzCl_wnrV9-x-f3wj7; pin=jd_6207f7184529a; unick=trc1999; _tp=JNzKxe7DcCfngCwIpeljGPHF2xkonm%2BVgi2OnGhA3jU%3D; _pst=jd_6207f7184529a; unpl=V2_ZzNtbRUCRUdwDRIBK05VAmJWE1QSUkpAdVgSB3IdXlFjBEdZclRCFXwURldnGlUUZwIZX0NcQxRFCHZXfBpaAmEBFl5yBBNNIEwEACtaDlwJAxNaS1ZFF3ILQlR5KWwGZzMSXHJXRRB8AUNVcx1YNVcEIm1yXkASfABAZHopXTUlV05YQ1VEHXZFRlJ%2bEFUAZgsWWXJWcxY%3d; __jda=122270672.1748840955.1544060591.1545875901.1545964214.4; __jdc=122270672; __jdv=122270672|baidu-search|t_262767352_baidusearch|cpc|106807362513_0_fd7c44edaf864d08a48d1aeb853e56d5|1545964213728; shshshfp=708292ddd9506c94fecb7b1d907dab98; _gcl_au=1.1.931372864.1545964371; 3AB9D23F7A4B3C9B=63GCTH622YUFDF7LLLKS4SFGGAQNAOCG7344QFFU4MPE2EQSTKICUSWSUVO6K5WJBWOIOA2E25WLZZVJ4SMBFYYLEY; JSESSIONID=70280F71C2B650E20154FFF4FEB9EAB1.s1; shshshsID=6416ba643b6e926b396e642966b5ecee_6_1545967003649; __jdb=122270672.8.1748840955|4.1545964214
referer: https://item.jd.com/100000177764.html
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36 """
headers = ChromeHeaders2Dict(header)
comment_resp=requests.get(url=comment_url,params=params,headers=headers)
print(comment_resp.status_code)
comment_str = comment_resp.text
print(comment_str)
comment_dict = json.loads(comment_str)
# comment_dict = json.load('4js接口-京东评论-评论数据.json')
comments = comment_dict['comments']
for comment in comments:
    print(comment['id'])
    print(comment['content'])
    print(comment['creationTime'])
    print(comment['score'])
    print(comment['nickname'])
    images = comment['images']
    tupian=images['imgUrl']
    tupian1 ='https:' + tupian
    print(tupian1)
    for i in range(100):
     urlretrieve(tupian1,filename=f'D:/李大米一号/{i}.jpg')

