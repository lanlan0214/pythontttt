import time

# 遊戲介紹函數
def intro():
    print("歡迎來到冒險之地！")  
    time.sleep(1)  
    print("你身處在一個神秘的森林中。")  
    time.sleep(1)  
    print("你必須做出選擇以探索這片神秘的地方。")  
    time.sleep(1)

# 讓玩家做出選擇的函數
def make_choice(options):
    print("選擇你的下一步:")
    for i, option in enumerate(options, 1):  
        print(f"{i}. {option}")  
    
    while True:
        try:
            choice = int(input("輸入選項的編號: "))  
            if 1 <= choice <= len(options):  
                return choice
            else:
                print("請輸入有效的選項編號。")  
        except ValueError:
            print("請輸入一個數字。")  

# 森林場景函數
def forest_scene():
    print("\n你來到了森林深處。")
    time.sleep(1)
    print("你看到一條小徑通向左邊，一個古老的橋通向右邊。")
    time.sleep(1)
    
    options = ["探索小徑", "穿越古老的橋", "超級通道"]
    choice = make_choice(options)
    
    if choice == 1:
        print("\n你選擇探索小徑。")
        time.sleep(1)
        print("小徑帶領你發現了一個神秘的洞穴。")
        cave_scene()  
    elif choice == 3:
        print("\n你選擇通往神的道路")
        time.sleep(1)
        print("神的通道，無路可走。")
        god_scene()  
    else:
        print("\n你選擇穿越古老的橋。")
        time.sleep(1)
        print("橋下有一條河流，你成功渡過。")
        river_scene()  

# 洞穴場景函數
def cave_scene():
    print("\n你進入了神秘的洞穴。")
    time.sleep(1)
    print("洞穴裡充滿了閃閃發光的寶石。")
    time.sleep(1)
    
    options = ["拿取寶石", "返回森林"]
    choice = make_choice(options)
    
    if choice == 1:
        print("\n你選擇拿取寶石。")
        time.sleep(1)
        print("突然，洞穴開始顫抖，你趕緊返回森林。")
        forest_scene()  
    else:
        print("\n你選擇返回森林。")
        time.sleep(1)
        forest_scene()  

# 河流場景函數
def river_scene():
    print("\n你成功渡過河流。")
    time.sleep(1)
    print("河對岸有一座神祕的城堡。")
    time.sleep(1)
    
    options = ["進入城堡", "返回森林"]
    choice = make_choice(options)
    
    if choice == 1:
        print("\n你選擇進入城堡。")
        time.sleep(1)
        print("城堡裡有一位仙女，她給了你一個神奇的禮物。")
        print("恭喜，你完成了冒險！")
    else:
        print("\n你選擇返回森林。")
        time.sleep(1)
        forest_scene()  

# 神的道路
def god_scene():
    print("\n凡人，你居然能找到這。")
    time.sleep(1)
    print("我就給你一位美女讓你爽！")
    time.sleep(1)
    print("爽到升天了！")

# 主程式，遊戲開始
while True:  # 迴圈讓玩家能夠多次玩遊戲
    intro()  
    forest_scene()  

    play_again = input("你想再玩一次嗎？(輸入 'yes' 或 'no'): ")
    if play_again.lower() != 'yes':
        print("感謝您的遊玩！再見！")
        break  # 如果玩家不想再玩一次，結束遊戲
