# 警告：以下代码仅为示例，可以运行，请随意尝试！

from classmates import LC
from random import randint
from datetime import datetime
from time import sleep
from os import system

def happy_birthday(person, num):
    sentenses = ['祝你生日快乐！', '天天开心！', '时运加满！', '你可爱死我了', '成绩突飞猛进！', '一定要快乐幸福啊！', '保持阳光！', '', '']
    sentense = person + '，' + sentenses[(randint(0, 8)  + num) % 9]
    return sentense

date = datetime.now().strftime('%m-%d')
#if date == LC.birthday:
if True:
    system('clear')
    for i in range(36):
        i += 1
        t = 2 / i
        for a in range(i):
            print(happy_birthday(LC.name), a)
            if i <= 15:
                sleep(t / 8)
        sleep(t)
        system('clear')
    sleep(0.25)
    system('sl | lolcat -')
    system('clear')
    sleep(2)
    system('figlet HappyBirthday,LC! | lolcat -')
    # 奈何这个特效显示不了中文……
    sleep(5)
    system('figlet IloveU. | lolcat -')
    system('figlet Forever. | lolcat -')
    sleep(10)

