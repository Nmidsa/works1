#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：
日期：
"""
print("欢迎使用RPSLS游戏")

import random
answer=random.randint(0,5)# 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(player_chioce):# 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
    """
    将游戏对象对应到不同的整数
    """

    # 使用if/elif/else语句将各游戏对象对应到不同的整数
    # 不要忘记返回结果
    if player_chioce=="石头":
        name1=0
    elif player_chioce=="史波克":
        name1=1
    elif player_chioce=="纸":
        name1=2
    elif player_chioce=="蜥蜴":
        name1=3
    else :#剪刀
        name1=4
    return name1
player_chioce=input("请输入您的选择：")# 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
player_chioce_number=name_to_number(player_chioce)
print("----------------")# 输出"-------- "进行分割
print("您的选择为："+player_chioce)







def number_to_name(answer):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """

 # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
 # 不要忘记返回结果
    if  answer==0 :
        name2="石头"
    elif answer==1 :
        name2="史波克"
    elif answer==2 :
        name2="纸"
    elif answer==3 :
        name2="蜥蜴"
    else :
        name2="剪刀"
    return name2
comp_number=answer
name2=number_to_name(comp_number)# 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

print("计算机的选择为："+(name2))# 在屏幕上显示计算机选择的随机对象










def rpsls(player_choice):# 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
if player_chioce_number==0 and comp_number==3 or comp_number==4:
    print("您赢了")
elif player_chioce_number==1 and comp_number==0 or comp_number==4:
    print("您赢了")
elif player_chioce_number==2 and comp_number==0 or comp_number==1:
    print("您赢了")
elif player_chioce_number==3 and comp_number==1 or comp_number==2:
    print("您赢了")
elif player_chioce_number==4 and comp_number==2 or comp_number==3:
    print("您赢了")
elif player_chioce_number==comp_number:
    print("您和计算机出得一样呢")
else :
    print("计算机赢了")
result=rpsls(player_chioce)# 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”























