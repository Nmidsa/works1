#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�
���ڣ�
"""
print("��ӭʹ��RPSLS��Ϸ")

import random
answer=random.randint(0,5)# ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(player_chioce):# ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number
    """
    ����Ϸ�����Ӧ����ͬ������
    """

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��
    if player_chioce=="ʯͷ":
        name1=0
    elif player_chioce=="ʷ����":
        name1=1
    elif player_chioce=="ֽ":
        name1=2
    elif player_chioce=="����":
        name1=3
    else :#����
        name1=4
    return name1
player_chioce=input("����������ѡ��")# ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice
player_chioce_number=name_to_number(player_chioce)
print("----------------")# ���"-------- "���зָ�
print("����ѡ��Ϊ��"+player_chioce)







def number_to_name(answer):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """

 # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
 # ��Ҫ���Ƿ��ؽ��
    if  answer==0 :
        name2="ʯͷ"
    elif answer==1 :
        name2="ʷ����"
    elif answer==2 :
        name2="ֽ"
    elif answer==3 :
        name2="����"
    else :
        name2="����"
    return name2
comp_number=answer
name2=number_to_name(comp_number)# ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

print("�������ѡ��Ϊ��"+(name2))# ����Ļ����ʾ�����ѡ����������










def rpsls(player_choice):# ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
if player_chioce_number==0 and comp_number==3 or comp_number==4:
    print("��Ӯ��")
elif player_chioce_number==1 and comp_number==0 or comp_number==4:
    print("��Ӯ��")
elif player_chioce_number==2 and comp_number==0 or comp_number==1:
    print("��Ӯ��")
elif player_chioce_number==3 and comp_number==1 or comp_number==2:
    print("��Ӯ��")
elif player_chioce_number==4 and comp_number==2 or comp_number==3:
    print("��Ӯ��")
elif player_chioce_number==comp_number:
    print("���ͼ��������һ����")
else :
    print("�����Ӯ��")
result=rpsls(player_chioce)# ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�























