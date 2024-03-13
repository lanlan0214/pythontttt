import time

# 遊戲介紹
def intro():
    print("歡迎來到冒險之地！")  
    time.sleep(1)  
    print("你來到了一個神秘的森林。")  
    time.sleep(1)  
    print("你必須做出選擇以探索這片神秘的地方。")  
    time.sleep(1)

# 森林場景
def forest_scene():
    print("\n你來到了森林深處。")
    time.sleep(1)
    print("你看到一條小徑通向左邊，一個古老的橋通向右邊。")
    time.sleep(1)
    
    while True:
        print("\n你想要走哪條路呢？")
        print("1. 探索小徑")
        print("2. 穿越古老的橋")
        
        choice = input("請輸入選項的編號: ")
        
        if choice == "1":
            print("\n你選擇探索小徑。")
            time.sleep(1)
            print("小徑帶領你發現了一個神秘的洞穴。")
            time.sleep(1)
            print("你發現了一顆閃閃發光的寶石！")
            time.sleep(1)
            break
        elif choice == "2":
            print("\n你選擇穿越古老的橋。")
            time.sleep(1)
            print("橋下有一條河流，你成功渡過。")
            time.sleep(1)
            break
        else:
            print("\n請輸入有效的選項（1 或 2）！")
            time.sleep(1)

# 主程式，遊戲開始
while True:  
    intro()
    forest_scene()  

    play_again = input("你想再玩一次嗎？(輸入 'yes' 或 'no'): ")
    if play_again.lower() != 'yes':
        print("感謝您的遊玩！再見！")
        break
