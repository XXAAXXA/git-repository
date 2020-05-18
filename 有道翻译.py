'''
实现功能：用户输入英文或中文，程序即可打印出来对应的译文。
'''


import requests
# import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

def translate():
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    data = {'i': input('请输入需要翻译的内容：'),
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTIME',
            'typoResult': 'false'}

    res = requests.post(url, headers=headers, data=data)
    json = res.json()
    result = json['translateResult'][0][0]['tgt']
    print(result)

def main():
    translate()

main()