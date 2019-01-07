from urllib.request import urlretrieve
import json
import requests
from lxml import etree
from CrawlerUtility import ChromeHeaders2Dict
def get_comment(page=None):
    """
    取评论
    :return: [id,username,score] 或[‘id’,'123']
    """
    comment_url = 'https://sclub.jd.com/comment/productPageComments.action'
    params = {
        'productId': 100000287113, #商品id。先写死
        'score': 0,
        'sortType': 5,
        'page': page,
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
    comment_dict = json.loads(comment_str)
    comments = comment_dict['comments']
    result_list=[]
    for comment in comments:
        print(comment['id'])
        print(comment['content'])
        print(comment['creationTime'])
        print(comment['score'])
        print(comment['nickname'])
        print(comment['productColor'])
        print(comment['productSize'])
        result_list.append({
            'id':comment['id'],
            'content':comment['content'],
            'creationTime': comment['creationTime'],
            'score': comment['score'],
            'nickname': comment['nickname'],
            'productColor': comment['productColor'],
            'productSize': comment['productSize'],
        })
    return result_list

def save_db(comments):
    """
    :param comments:
    :return:
    """
    import pymysql
    connect = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='trc', db='jddd')
    cursor = connect.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS jdjd(
        id bigint,
        content varchar(500),
        create_time datetime,
        score int,
        username VARCHAR(20),
        productColor varchar(20),
        productSize varchar(20)
        )""")
    y = 1
    for i in comments:
        print(f'正在保存第{y}页')
        cursor.execute("""INSERT INTO jdjd(id,content,create_time,score,username,productColor,productSize) VALUES (%s,%s,%s,%s,%s,%s,%s)""",
                           [i['id'], i['content'],i['creationTime'], i['score'],i['nickname'],i['productColor'],i['productSize']])
        y += 1
    connect.commit()
    connect.close()


if __name__ == '__main__':
    page =10
    for i in range(0,page):
        comments=get_comment(page)
        a = save_db(comments)
        print(a)