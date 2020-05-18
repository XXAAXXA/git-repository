'''
扇贝网：https://www.shanbay.com/已经有一个测单词量的功能，
我们要做的就是把这个功能复制下来，并且做点改良，搞一个网页版没有的功能 ———— 自动生成错词本。
'''

import requests
import openpyxl

# 伪装
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

# 发起请求
res = requests.get('https://www.shanbay.com/api/v1/vocabtest/category/', headers=headers)
json = res.json()
list = json['data']

catgs_code = {}  # 选择序号与参数对应字典
i = 1
print('可以选择的出题范围：')
for catg in list:
    print('%d. %s' % (i, catg[1]), end='; ')
    catgs_code[i] = catg[0]
    i += 1

choice = int(input('\n请输入序号：'))

# 根据选择序号发起请求
params = {'category': catgs_code[choice]}
res = requests.get('https://www.shanbay.com/api/v1/vocabtest/vocabularies/', headers=headers, params=params)
json = res.json()
vocab_list = json['data']

vocab_excel = [['单词', '是否认识', '是否掌握']]  # 最后录入excel的表格
i = 1
print('\n接下来会一次出现40到50个不等的词汇，输入“1”表示认识此单词并选择正确的注释，不认识的话请直接回车跳过')
for vocab in vocab_list:
    print('\n第{}题:'.format(i) + vocab['content'])
    know = input()

    if know == str(1):
        know_record = '是'

        definition_choices = vocab['definition_choices']
        for choices in range(4):
            print(str(choices + 1) + definition_choices[choices]['definition'])
        choice = int(input('请输入序号：'))
        if definition_choices[choice-1]['pk'] == vocab['pk'] and definition_choices[choice-1]['rank'] == vocab['rank']:
            answer = '正确'
        else:
            answer = '错误'

        vocab_excel.append([vocab['content'], know_record, answer])

    else:
        know_record = '否'
        answer = ''

        vocab_excel.append([vocab['content'], know_record, answer])

    i += 1

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '词汇量记录'

for row in vocab_excel:
    sheet.append(row)

wb.save('扇贝网词汇量记录表格.xlsx')