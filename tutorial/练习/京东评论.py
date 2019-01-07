# coding:utf-8
__author__ = 'ym'
import requests
from CrawlerUtility import ChromeHeaders2Dict
import json
import time


class Jdcomment(object):

    def __init__(self):
        self.header = """
:authority: sclub.jd.com
:method: GET
:path: /comment/productPageComments.action?callback=fetchJSON_comment98vv15260&productId=100000287113&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=a2cc2478caba42fc&fold=1
:scheme: https
accept: */*
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
cache-control: no-cache
cookie: __jdc=122270672; __jdu=1241630742; PCSYCityID=412; shshshfpa=55b0af51-02c3-1e40-a310-1c57890f85e9-1545875426; TrackID=1CBs1NgwoA4kdyJ_DHv_k4eV1rM83Ka0EnopIXoJARMAhbARg7uNGSxvBqh4wcVwOxlpYwH4NqrIv9eA6Xryy2Z62BJKkdAxeFsA3UQGaoo4; user-key=8abc6212-d9b5-44ff-bc2c-ddd9e8be0554; ipLoc-djd=1-72-2799-0; unpl=V2_ZzNtbRdRFkJ8WBJSLxxUBmICRVpLVEIWJwwVAyseDgFuAEFUclRCFXwURldnGlUUZwIZXkVcRxVFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2VHgcXAJlAhRYQWdzEkU4dlN9HVoNZTMTbUNnAUEpDERccx5USGcAF11FVUITcAt2VUsa; __jda=122270672.1241630742.1543824136.1545880963.1545964078.3; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_d7df8ae7e49240f68202c5bfa6c582b8|1545964077739; pinId=7i7kN8FksT-lGMqtUbaimQ; pin=49817795-598178; ceshi3.com=000; _tp=5PStYdOEJwZICWIaFuxuUQ%3D%3D; _pst=49817795-598178; cn=5; _gcl_au=1.1.730340221.1545964394; thor=868BA4D0E4372F9130214B99DAB50625903B38F62B09C4BFFE47A360066B6295AF2286835649C9BC0EEEA10E4D3BDE45417D3EC64FAEEB7A30A4D918DA20ECF70EB138078B097F1CDE60DFA73DE9283BAFE14E351C3A104B97A5938B40D73BF923C68F6A8F7E1D3AF3A6D470BB2C9FCB883981D5C5191432D91806B45D7E6AD1B342418803092685C52BD439BDD8F14E6723ACCE0916C39EEE017B7A9171BDCF; 3AB9D23F7A4B3C9B=5LFBQ2OIQGNALF4257ZN4K2W63PZ3AYMFTJ5TD5LNKU3G3QYXGREWS7J4XBXPOFPFGUOUTIBKPOC2FY4D465O7NOAA; shshshfp=26620f2aeddc936158d73d66697b4aff; shshshsID=ef24363d4037bc94ef352ce87cc44eaa_3_1545964456703; __jdb=122270672.6.1241630742|3.1545964078; shshshfpb=ow5Ddp1hdUuLFIWx0fLMELw%3D%3D; JSESSIONID=0372305F9FCCC2C53B077FD07DBD5F98.s1
pragma: no-cache
referer: https://item.jd.com/100000287113.html
user-agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
"""
        self.headers = ChromeHeaders2Dict(self.header)
        self.url = "https://sclub.jd.com/comment/productPageComments.action?"

    def get_json(self, num):
        comment_list = []
        for i in range(num):
            params = {
                'productId': 100000287113,
                'score': 0,
                'sortType': 5,
                'page': i,
                'pageSize': 10
            }
            time.sleep(1)
            json_data = requests.get(self.url, params=params, headers=self.headers).text
            comment = json.loads(json_data)
            comment_list.append(comment)
        return comment_list

    def save_data(self, num):
        import pymysql
        conn = pymysql.connect(user='root', password='trc', host='127.0.0.1', db='jddd')
        cursor = conn.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS jdcomment(id INTEGER PRIMARY KEY,comment VARCHAR (500),username VARCHAR (50),create_time DATE )')
        comment_list = self.get_json(num)
        xx = 1
        y = 1
        for comment in comment_list:
            print(f'正在保存第{y}页')
            for i in comment['comments']:
                cursor.execute('INSERT INTO jdcomment(id,comment,username,create_time) VALUES (%s,%s,%s,%s)', [xx, i['content'], i['nickname'], i['creationTime']])
                xx += 1
                y += 1
        conn.commit()
        conn.close()


if __name__ == '__main__':
    x = Jdcomment()
    x.save_data(7)

