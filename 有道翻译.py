import json

import requests
import hashlib
import time
from Crypto.Cipher import AES
import base64

from Crypto.Util.Padding import unpad


def generate_signature(t):
    # 构建字符串并进行哈希运算生成签名
    data = f'client=fanyideskweb&mysticTime={t}&product=webfanyi&key=fsdsogkndfokasodnaso'
    signature = hashlib.md5(data.encode()).hexdigest()
    return signature


word=input('请输入一个单词')
# word = 'dog'
t = str(int(time.time() * 1000))
sign = generate_signature(t)
url = "https://dict.youdao.com/webtranslate"
data = {
    'i': word,
    'from': 'auto',
    'to': '',
    'domain': '0',
    'dictResult': 'true',
    'keyid': 'webfanyi',
    'sign': sign,
    'client': 'fanyideskweb',
    'product': 'webfanyi',
    'appVersion': '1.0.0',
    'vendor': 'web',
    'pointParam': 'client,mysticTime,product',
    'mysticTime': t,
    'keyfrom': 'fanyi.web'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=-1719929258@10.110.96.154; OUTFOX_SEARCH_USER_ID_NCOO=1968911892.8356373',
    'Referer': 'https://fanyi.youdao.com/'
}
session = requests.session()
resp = session.post(url, data=data, headers=headers)
print(resp.text)

def encrypt_data(data):
    md5_hash = hashlib.md5()
    md5_hash.update(data.encode('utf-8'))
    encrypted_data = md5_hash.digest()
    return encrypted_data

def decode_data(data, key, iv):
    cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
    # if len(data) % 4 != 0:
    #     data += '=' * (4 - len(data) % 4)
    decrypted_data = cipher.decrypt(base64.b64decode(data))
    return unpad(decrypted_data,16)
# s='Z21kD9ZK1ke6ugku2ccWu-MeDWh3z252xRTQv-wZ6jddVo3tJLe7gIXz4PyxGl73nSfLAADyElSjjvrYdCvEP4pfohVVEX1DxoI0yhm36ytQNvu-WLU94qULZQ72aml654CUIMt5aM5VBWpoEJTgiLod0BBe7lk_tfiXDEgASfdNXR3NUQeIo60MZ2BxZ3ELv5q99fS6Ib0VntsB2zY4MCigMWGpVQ0GoQue6KWZ_5ALar3Nftw5dXe3vt5riRBcDTFVfFj5HMc_U4Hhi7MMaxbotGC9hmBuP-mVQFeDbhrmGUmFLwGbx6k7zk2vlLY9wspgXWq5NGUUSywQamjF6CTx_rOBfeGHVEXA2omJMrRKa5XMjns96RUO1HQBAop8205BrWUh1ZG-0 OnKPCA_NzyNRyaeaSWKieXAZ5jmCL_x_zCrQ-Cjq-UJmO8IL7R_CuqUXxpCVWqu6MWRT1z5diVwOpi3gP1vSN0yvFw76qWN4JGwvYIZIbF5Uqo1sZJP-NpwKU9Pl_YJDeGll9AnNjOsOTKx_vilWKskx2nhZvqAN2aGF4ktsdJpsSJJFrfDhCaYzG7ZdclOkI2PjUJ7NIVmCFwQHL-rGQPuDM5qf_CWgPhcEy0_459JP7_j0aaZ-EjamlPtJ230O3H2N7DSiQBNoOb25YTQYxSeeKgUA4vjjcwSvl_yo8_GZ_5_8EcBD3PdZ5ocR5YI4SJgPHHGYshwJ34volHktImsbDua6Bk8EdrFCRmEN2NynFwodMAm1Qqx1Md0R9lkNiFiUuMJG8cmhHK-HlqQpfaxVMkY4KVg4fTNOkfmncuOdKJZYRySgxUtNux9Ff2YYAmdrk-ihsoRc-jIYMwp3UCE_C2El8PaY-mE5mhQNET-RPWlorhWAVF4ZqIJaMtEl6lEjV9XSjYcDW2gppb5C97GWx_zA2cUEUaL_s8nCJyTliwRczT3NZOJMZ3Y4rQ0MncAnoDUpuZ-RV1GilG4lPwfk9lqPk9vfh65hvTTKj7cKrsWUOFUYlKhd0QRryekkthLMm-M6be3SqHV4jtGUwH4HKr5PZQLHyDDh2LZNygiRzGIdcXQjzWXi6bFUFzHQLBjs8C9VrcZXfKvPGdosYAobal6kCmZnEdTw60CmZ0Cgsp1bBVO4Za4F9dzczEloCUOYPrVmv_pLbp4WRjW78q9oxakZNi-4 VLo4EM3XtcebhHHx-DYIG_RaEojm5z7unrEKdvCXS7S3kGZ8goZ5ivSel5lZxHwu40JFU5AsvTjCx2xjM2mfjiWfh-GpXJhyelp7YtC6KYEF8g4lUOXVY5MxtNh6iIst3tsprAft3_l48ocrv9uv_eju-1 eqvCZdnq3NkbkR3XVU_4PbR_IR8_6xKjnIuQ-qYx8PlB46Z_uHmCXo1hUx0oG5xV-SxgVIdQahIn7zI5HItGON5o21voX7t01pbznKmEJi2UTLP26Hkj3sxptz-Zev79hxQXLX8WNSxjM9beyZPwRRcQRFPoQHp9JET7H553_-MR06eBIOsoGndBwczn7-5 oqYnZWsANwasCvcF8uK1kIxdwlq83ZwKdrqWv2OOW4qDwW3SiWVRp2YgwZhWnekx7r5och19caRkOQqhSKY_LR4CEceYqRSAVZQ2_pIzzHRnulPcIS9y39iW38xajx83EeH6nIAQAlEEt4vIFcF6ElXiXUu2R-XqbgRydstTWw5Bfo2i2k2puZ0ZnxuS5X8Uri9rz7wKQXvLPj3ejxP5IpVVVvkPuFh-802 CxcBe6cJ9IqeJwobQqqh9Ga6ATCIuoaq5nIbglAMQ-HnFe85zeDA63xhUhzgcsjWBkL9VJQp8r86cXr8HPUY02sPqj1k5TRaDEcPTvaJuhIsSBHolwdIbuxN3rj-nlrR8ld_Qb5f77aUYE9_npMaCtSjioQ-h7yQRjAUDqQDJsgy3veHLOQQXD-6 QOiyTpYcmFebICrIZRBP5lxY3lTLMGVNfvB3y03AKe_b0P9mlNtpiuvPG7dMF7duWHjC8ULL9ct-9 Wqqf7cQiUEaGyyw6UVgGt-69 gE_GG6ro8WB8jXBZNm6xmAMtuEZ2ZHlM76cvHt_D_C1o9xk-aPBmUEXK-J_N3VXKBQhTIKX1uZbnozfm8vJfRifyOwoJ6hjMU42ByXx2slIhkhBf_sxpTyRQGY4tpP9450dsQ8r0LWibvm-YPmS2M5dF7bzTD5r_isOhv5MyryYJnNMS_w_PjFYOOaDPv3a5AO4btIq3xhZ3eYFRxh7fUKk2tEFj_mqKd-wfAiX7hIZlH9AuBQ96v65jri'
# print(len(s))
# data = resp.text
s=resp.text
key = 'ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl'
iv = 'ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4'

encrypted_iv = encrypt_data(iv)
encrypted_key = encrypt_data(key)
s=s.replace("_","/").replace("-","+")
decrypted_data = decode_data(s,encrypted_key, encrypted_iv)
real_data=decrypted_data.decode('utf-8')
print(json.loads(real_data)['dictResult']['ec']['word']['trs'][0]['tran'])





