import pygame,sys,random
from pygame.locals import *
def print_text(font,x,y,text,color):
    imgText=font.render(text, True, color)
    screen.blit(imgText,(x,y))
    
def line():
    print("———————————————————分割线—————————————————————")

def use(prop_name,prop_number,ATT):         #创建使用模块，用来执行吃饭/喝水选项的操作
    if prop_number==0:                      #如果没有对应的道具
        print("你没有"+prop_name+"!")       #返回提示
    elif prop_number>=1:                    #如果有对应的道具
        prop_number-=1                      #道具-1
        ATT+=int(random.randint(15, 20))    #执行使用操作，恢复15%-20%的对应属性
        print("你使用了一个"+prop_name+"。")
        line()
    return prop_number,ATT
    
def draw(VIT,WIL):                                     #创建采集模块，用来执行采集选项的操作
    ran=0
    number=0
    answer=''                                    #初始化变量，ran为随机数,answer为结果
    ran=int(random.randint(1,100000))               #调用函数，令ran=十万个数字里的随机一个
    if ran>0 and ran<=13125:                        #接下来的函数都是伪随机模拟抽卡
        answer='草药1'                              #五种拉胯草药各占比13.125%
        number=1
        WIL-=int(random.randint(5,8))
    elif ran>13125 and ran<=26250:                  #所需草药占比1%
         answer='草药2'                              #食物，水，体力药的草药各占11.125%
         number=2
         WIL-=int(random.randint(5,8))
    elif ran>26250 and ran<=39375:                  #加起来概率共100%
        answer='草药3'                              #通过扩大100倍，达到随机数选取方法
        number=3
        WIL-=int(random.randint(5,8))
    elif ran>39375 and ran<=52500:
        answer='草药4'
        number=4
        WIL-=int(random.randint(5,8))
    elif ran>52500 and ran<=65625:
        answer='草药5'
        number=5
        WIL-=int(random.randint(5,8))
    elif ran>65625 and ran<=66625:
        answer='关键草药'
        number=6
        WIL+=int(random.randint(22,25))
    elif ran>66625 and ran<=77750:
        answer='可食用草药'
        number=7
    elif ran>77750 and ran<=88875:
        answer='水分高草药'
        number=8
    elif ran>88875 and ran<=100000:
        answer='镇静草药'                          #截止至此代码
        number=9
    print("你采集到了"+answer)
    print("体力值剩余",VIT,"点！")
    line()
    return number,WIL

def next_day(day,HUN,THI,WIL,VIT):            #创建下一天模块，用来执行下一天选项的操作
    ran=0
    #先扣除相应资源
    global game_over
    HUN-=int(random.randint(25, 30))         #饥饿值随机减10%-15%，注意饥饿值单位为%，即初始是100
    THI-=int(random.randint(25, 30))         #口渴值同理，与饥饿值相同
    #然后检测死亡条件，判断玩家是否死亡
    if HUN<0:                           #饥饿值不够扣，达成饿死结局
        game_over=True                       #死亡标记点亮
                                             #播放死亡动画
        print("你饿极了，长时间没进食使你头昏眼花，尽管拯救亲人的意志让你撑到现在，但你明白，可能无法继续撑下去了。")
        input("终于，在某一个太阳升起的时刻，你的眼前，陷入黑暗")
        input("结局1：饥寒交迫")
        pygame.quit()
    elif THI<0:                         #口渴值不够扣，达成渴死结局
        game_over=True                       #死亡标记点亮
                                             #播放死亡动画
        print("你渴极了，你感觉嗓子火烧一样，尽管拯救亲人的意志让你撑到现在，但你明白，可能无法继续撑下去了。")
        input("终于，在某一个太阳升起的时刻，你的眼前，陷入黑暗")
        input("结局2：水分不足")
        pygame.quit()
    elif WIL<10:                        #精神濒临崩溃，进行判定
        ran=int(random.randint(1, 100)) #进行百分比检测，25%会死
        if ran>75:                      #如果触发了25%
            game_over=True                       #死亡标记点亮
                                                 #播放死亡动画
        print("长时间找不到有用的草药，你开始思考自己出来的意义。")
        input("在见识到无止境的草药后，你觉得一切，都无所谓了")
        input("结局3：精神失常")
        pygame.quit()
    if game_over==False:
        #若任何死亡条件都没触发，则进行下一天操作
        day+=1                                      #天数+1
        WIL+=int(random.randint(15, 20))         #精神力相同，不过它是每天恢复加值
        VIT=100                                  #体力值无论多少，均恢复成100
                                                     #此行空置，用来插入过场图片
        aa=int(random.randint(1, 3))
        if aa==1:
            print("夜深人静的时候，你开始为明天的食物发愁")
        elif aa==2:
            print("夜深人静的时候，你开始为明天的水发愁。")
        elif aa==3:
            print("夜深人静的时候，你思考起人生的意义")
        print("思考无果，你只知道你又度过了一天")
        line()
        return day,HUN,THI,WIL,VIT
        
def display_text():                                                  #文字统一显示
    print_text(font1,0,0,"饱食度："+str(HUN),red)                    #↓第一行，表示属性状态↓
    print_text(font1,0,50,"水分："+str(THI),red)
    print_text(font1,0,100,"精神力："+str(WIL),red)                  #第一行
    print_text(font1,300,0,"体力："+str(VIT),red)
    print_text(font1,300,75,"天数："+str(day),red)                   #↑第一行，表示属性状态↑

    print_text(font3,10,155,"剧情背景：",red)    
    print_text(font3,10,165,"我的爷爷被下达了病危通知书",red)
    print_text(font3,10,180,"无药可医，且最多只能撑一年",red)
    print_text(font3,10,200,"我不相信，我不相信人会这么轻易死去",red)
    print_text(font3,10,220,"100株‘关键草药’，可活死人，药白骨",red)
    print_text(font3,10,240,"地窖里找到的偏方，是我最后的希望",red)
    print_text(font3,10,260,"我识得这种草药，这么想着的我，背起了行囊",red)
    print_text(font3,10,280,"等着我，爷爷，我会救你的！",red)
    
    print_text(font3,305,155,"游戏提示：",red)
    print_text(font3,310,165,"在一年内寻找到100株关键草药吧",red)
    print_text(font3,310,180,"每天开始时，会回满所有体力",red)
    print_text(font3,310,200,"饱食度与水分每天开始时会减少，而精神力会增加",red)
    print_text(font3,310,220,"如果饱食度，水分降为0，游戏就会失败",red)
    print_text(font3,310,240,"精神低于一定程度，某个早上起来游戏可能就会失败",red)
    print_text(font3,310,260,"委托目前可以快速体验结局",red)
    print_text(font3,310,280,"为了救下爷爷，向着胜利条件迈进吧",red)

    print_text(font1,0,300,"仓库",red)                    #↓第三行，用来表示仓库，道具数量↓    
    print_text(font2,120,330,"草药1："+str(plant_1_number),black)                    #↓第四行，用来表示交互按钮↓
    print_text(font2,120,345,"草药3："+str(plant_3_number),black)
    print_text(font2,120,360,"草药5："+str(plant_5_number),black)                    #第四行
    print_text(font2,360,330,"草药2："+str(plant_2_number),black)    
    print_text(font2,360,345,"草药4："+str(plant_4_number),black)
    print_text(font2,360,360,"关键草药："+str(key_plant_number),red)                    #↑第四行，用来表示交互按钮↑
    print_text(font1,0,405,"可食用草药："+str(Edible_plant_number),red)                    #↓第四行，用来表示交互按钮↓
    print_text(font1,200,405,"水分高草药："+str(Drinkable_plant_number),red)
    print_text(font1,400,405,"镇静草药："+str(Clam_plant_number),red)                    #第四行 
    
    print_text(font1,100,470,"进食",red)                    #↓第四行，用来表示交互按钮↓
    print_text(font3,50,500,"（消耗可食用草药，回复饱食度）",red)
    print_text(font1,300,470,"喝水",red)
    print_text(font3,250,500,"（消耗水分高草药，回复水分）",red)
    print_text(font1,500,470,"镇静",red)                    #第四行
    print_text(font3,450,500,"（消耗镇静草药，回复精神力）",red)
    print_text(font1,100,550,"采集",red)
    print_text(font3,75,580,"（消耗体力，采集药草）",red)    
    print_text(font1,300,550,"下一天",red)
    print_text(font3,275,580,"（开始下一天）",red)  
    print_text(font1,500,550,"委托",red)                    #↑第四行，用来表示交互按钮↑
    print_text(font3,475,540,"（未完成，正在加紧制作）",red)
    print_text(font3,450,580,"（按下此按钮可体验采集满结局）",red)
    print_text(font3,400,530,"（按下此",red)  
    print_text(font3,410,545,"按钮可",red)
    print_text(font3,410,562,"体验",red)  
    print_text(font3,410,575,"天数满",red)
    print_text(font3,410,585,"结局)",red)
pygame.init()                                               #初始化
screen=pygame.display.set_mode((600,600))                   #初始化窗口
pygame.display.set_caption("采药人生")                          #初始化标题


#属性状态初始化
HUN=100
THI=100
WIL=100
VIT=100
day=1

#仓库道具初始化
plant_1_number=plant_2_number=plant_3_number=plant_4_number=plant_5_number=0        #五个草药初始为0
key_plant_number=Edible_plant_number=Drinkable_plant_number=Clam_plant_number=1     #四个关键道具初始为1
    
#游戏走向初始化
game_win=False                                          #游戏胜利标记未启用
game_over=False                                         #游戏失败标记未启用

red=255,0,0                                                 #初始化颜色
black=0,0,0
white=255,255,255

font1=pygame.font.SysFont('华文中宋', 24)                    #初始化字体
font2=pygame.font.SysFont('华文中宋', 20)
font3=pygame.font.SysFont('华文中宋', 10)
pygame.display.flip()                                       #刷新

while True:                                                     #利用条件代码创建循环，因为条件为恒真，所以会无限执行，直至执行退出操作
    screen.fill((255,255,255))
    for event in pygame.event.get():                     #pygame.event.get会创建待处理事件列表，利用for循环遍历该列表，做到顺序执行操作
        if event.type ==pygame.QUIT:                            #执行关闭窗口操作
            pygame.quit()                                       #当按下右上角的×时，程序退出
        elif event.type==pygame.MOUSEBUTTONDOWN:
            x,y=event.pos
            if y>450 and y<525:                                              #此时代表鼠标在第一行交互按钮中
                if x>0 and x<200:                                               #此位置表示鼠标处在进食区域
                    Edible_plant_number,HUN=use('可食用草药',Edible_plant_number,HUN)                   #进行吃饭操作
                elif x>200 and x<400:                                           #此位置表示鼠标处在喝水区域
                    Drinkable_plant_number,THI=use('水分高草药',Drinkable_plant_number,THI)             #进行喝水操作
                elif x>400 and x<600:                                           #此位置表示鼠标处在镇静区域
                    Clam_plant_number,WIL=use('镇静草药',Clam_plant_number,WIL)                       #进行镇静操作
            elif y>525 and y<600:                                            #此位置表示鼠标在第二行交互按钮中
                if x>0 and x<200:                                               #此位置表示鼠标处在采集区域
                    if VIT<10:                                      #如果体力值不够采药
                        print("你的体力值不够！")                   #返回提示
                    elif VIT>=10:                                   #如果体力值够采药                                                    #执行采集操作
                        VIT-=10                                     #花费10体力值，进行采药操作'''
                        kkk,WIL=draw(VIT,WIL)                                               #返回采集数据，并根据返回值增加道具数量
                        if kkk==1:
                            plant_1_number+=1
                        elif kkk==2:
                            plant_2_number+=1
                        elif kkk==3:
                            plant_3_number+=1
                        elif kkk==4:
                            plant_4_number+=1
                        elif kkk==5:
                            plant_5_number+=1
                        elif kkk==6:
                            key_plant_number+=1
                        elif kkk==7:
                            Edible_plant_number+=1
                        elif kkk==8:
                            Drinkable_plant_number+=1
                        elif kkk==9:
                            Clam_plant_number+=1
                elif x>200 and x<400:                                           #此位置表示鼠标处在下一天区域
                    day,HUN,THI,WIL,VIT=next_day(day,HUN,THI,WIL,VIT)           #执行下一天操作，并返回对应变量值
                elif x>400 and x<450:                                           #此位置表示鼠标处在委托左边的区域
                    day=365                                                     #内测中，按下此键可体验天数耗尽结局
                elif x>450 and x<600:                                           #此位置表示鼠标处在委托区域
                    key_plant_number = 100                                      #内测中，按下此键可体验通关结局
        keys=pygame.key.get_pressed()                               #该代码用来轮询键盘接口，利用键位与标志一一对应来交互按下按键时的反应
        if keys[K_ESCAPE]:                                          #好处是可以同时检测多个按键
            pygame.quit()                                           #这个代码作用是当按下esc键时进行退出程序操作

        if HUN>100:                                                 #这是限制的代码，用来限制数量，使其不超过上限与下限
            HUN=100
        elif THI>100:
            THI=100
        elif VIT>100:
            VIT=100
        elif WIL>100:
            WIL=100
        elif WIL<0:
            WIL=0
        elif game_over:
            pygame.quit()
        elif key_plant_number >=100:
            game_win = True
            key_plant=0
        if game_win:
            line()
            input("经过长途跋涉，少年终于采下最后一株草药。")
            input("他满心欢喜的熬成汤喂给爷爷。")
            input("但偏方很显然只是偏方，不能起死回生。")
            input("少年一瞬间觉得自己这么长时间做的努力，全部变成了泡沫。")
            input("然而，爷爷并不会因此醒来，永远不会。")
            input("真*结局5：值得吗？\n按下enter键退出游戏")
            if keys[K_ENTER]:
                pygame.quit()
        if day==365:
            line()
            print("不知不觉间，已经过了一年了")
            input("我仍然没有采到足够草药")
            print("不忍去看爷爷最后一面，我逃也似的离开了这座村庄")
            input("不再复还。")
            input("结局4：寿终正寝")
            pygame.quit()

    #画线时间
    color=255,255,0
    width=8
    display_text()
    pygame.draw.line(screen,color,(0,150),(600,150),width)
    pygame.draw.line(screen,color,(0,300),(600,300),width)
    pygame.draw.line(screen,color,(0,450),(600,450),width)
    pygame.draw.line(screen,color,(0,525),(600,525),width)
    pygame.draw.line(screen,color,(300,150),(300,300),width)
    pygame.draw.line(screen,color,(200,450),(200,600),width)
    pygame.draw.line(screen,color,(450,525),(450,600),width)
    pygame.draw.line(screen,color,(400,450),(400,600),width)
    pygame.display.update()