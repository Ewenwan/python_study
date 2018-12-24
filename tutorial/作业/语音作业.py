from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '14863227'
API_KEY = '4DB0zpEf791L65HRGi41Iq9A'
SECRET_KEY = 'zrV6YOd6dVHjGHo3jINuheYH6DHuuGdp'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

result = client.synthesis('田润超是一只大傻逼啊大傻逼，哈哈哈哈哈哈哈哈', 'zh', 1, {
    'vol': 5, 'per': 4
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(result)

