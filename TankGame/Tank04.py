'''
坦克大战v1.04
    游戏基础功能实现
    新增功能：
        实现加载我方坦克
'''
import pygame,time
version="1.02"
class MainGame():
    #游戏主窗口
    window=None
    SCREENWIDTH=800
    SCREENHEIGHT=500
    COLOR_BLACK=pygame.Color(0,0,0)
    COLOR_RED=pygame.Color(255,0,0)
    TANK_P1 = None
    TANK_P1_SPEED=5
    # text="敌方坦克还剩余8个"

    def __init__(self):
        pass
    #游戏开始
    def starGame(self):
        pygame.display.init()
        MainGame.TANK_P1=Tank(420,370)
        #创建窗口加载窗口（借鉴官方文件）
        MainGame.window=pygame.display.set_mode([MainGame.SCREENWIDTH,MainGame.SCREENHEIGHT])
        pygame.display.set_caption("坦克大战"+version)
        while(True):
            #窗口的颜色设置
            MainGame.window.fill(MainGame.COLOR_BLACK)
            self.getEvent()
            #将绘制文字得到的画布粘贴到窗口中
            MainGame.window.blit(self.getTextSurface("剩余地方坦克%d辆"%5),[10,10])
            #将我方坦克加载到窗口中
            MainGame.TANK_P1.displayTank()
            if MainGame.TANK_P1 and not MainGame.TANK_P1.stop :
                MainGame.TANK_P1.move()
            #窗口的刷新
            time.sleep(0.002)
            pygame.display.update()
    def getEvent(self):
        #1.获取所有事件
        #2.对事件进行处理（1.点击关闭按钮。2.按下键盘上某个按键。）
        eventList=pygame.event.get()
        for event in eventList:
            if event.type==pygame.QUIT:
                self.endGame()
            #判断是否是按键按下，如果是，继续判断是哪个按键
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    MainGame.TANK_P1.direction = "L"
                    MainGame.TANK_P1.move()
                    MainGame.TANK_P1.stop = False
                    print("坦克向左掉头，移动")
                elif event.key==pygame.K_RIGHT:
                    MainGame.TANK_P1.direction = "R"
                    MainGame.TANK_P1.move()
                    MainGame.TANK_P1.stop = False
                    print("坦克向右掉头，移动")
                elif event.key == pygame.K_UP:
                    MainGame.TANK_P1.direction = "U"
                    MainGame.TANK_P1.move()
                    MainGame.TANK_P1.stop = False
                    print("坦克向上掉头，移动")
                elif event.key == pygame.K_DOWN:
                    MainGame.TANK_P1.direction = "D"
                    MainGame.TANK_P1.move()
                    MainGame.TANK_P1.stop = False
                    print("坦克向下掉头，移动")
                elif event.key == pygame.K_SPACE:
                    print("发射子弹")
            if event.type==pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT \
                    or event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                        MainGame.TANK_P1.stop = True

    #左上角提示内容
    def getTextSurface(self,text):
        #初始化字体模块
        pygame.font.init()
        #选中一个字体
        # fontlist=pygame.font.get_fonts()
        # print(fontlist)
        font=pygame.font.SysFont("kaiti",18)
        textSurface=font.render(text,True,MainGame.COLOR_RED)
        return textSurface
        #绘制自己设计的内容
    #游戏结束
    def endGame(self):
        print("谢谢使用")
        #结束Python解释器
        exit()

class Tank():
    def __init__(self,top,left):
        self.images = {
            "U": pygame.image.load("images/P1Tank_U.png"),
            "D": pygame.image.load("images/P1Tank_D.png"),
            "L": pygame.image.load("images/P1Tank_L.png"),
            "R": pygame.image.load("images/P1Tank_R.png"),
        }
        self.direction = "U"
        self.image=self.images[self.direction]
        self.rect=self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = 1
        self.stop = True
    #坦克移动
    def move(self):
        if self.direction == "L" :
            if self.rect.left >= 0:
                self.rect.left -= self.speed
        elif self.direction == "R" :
            if self.rect.left +self.rect.width < MainGame.SCREENWIDTH :
                self.rect.left += self.speed
        elif self.direction == "U" :
            if self.rect.top >= 0:
                self.rect.top -= self.speed
        elif self.direction == "D" :
            if self.rect.top + self.rect.height < MainGame.SCREENHEIGHT:
                self.rect.top += self.speed
    #坦克射击
    def shot(self):
        pass
    def displayTank(self):
        self.image=self.images[self.direction]
        MainGame.window.blit(self.image,self.rect)


class MyTank(Tank):
    def __init__(self):
        pass

class EnemyTank(Tank):
    def __init__(self):
        pass

class Bullet():
    def __init__(self):
        pass
    #子弹的移动
    def move(self):
        pass
    #子弹的显示
    def displayBuller(self):
        pass

class Explode():
    def __init__(self):
        pass
    #展示爆炸效果的方法
    def displayExplode(self):
        pass

class Wall():
    def __init__(self):
        pass
    #障碍物墙壁展示
    def displayWall(self):
        pass

class Music():
    def __init__(self):
        pass
    #开始播放音乐
    def displayMusic(self):
        pass

MainGame().starGame()