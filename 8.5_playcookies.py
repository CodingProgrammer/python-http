import requests
import json

def show():
    res = session.get(url_original)
    print(json.dumps(res.json(), indent=4))

commanddesp='''请输入cookies指令：
add key=value ，用于增加cookies
del key       ，用于删除cookies
show          ，用于显示当前的cookies
quit          , 退出
'''
commands = input(commanddesp).split()
url_original = 'http://httpbin.org/cookies'
session = requests.session()
while commands[0] != 'quit':
    if commands[0] == 'add':
        url = url_original + '/set?' + commands[1]
        res = session.get(url)
        show()

    elif commands[0] == 'del':
        url = url_original + '/delete?' + commands[1]
        res = session.get(url)
        show()

    elif commands[0] == 'show':
        show()
    
    commands = input().split()

print('Bye!') 
