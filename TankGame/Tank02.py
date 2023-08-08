'''
坦克大战v1.02
    游戏基础功能实现
    新增功能：
        点击关闭按钮，退出程序的事件
        子弹射击事件，与键盘交互
'''
import pygame
version="1.02"
class MainGame():
    #游戏主窗口
    window=None
    SCREENWIDTH=800
    SCREENHEIGHT=500
    COLOR_BLACK=pygame.Color(0,0,0)
    def __init__(self):
        pass
    #游戏开始
    def starGame(self):
        pygame.display.init()
        #创建窗口加载窗口（借鉴官方文件）
        MainGame.window=pygame.display.set_mode([MainGame.SCREENWIDTH,MainGame.SCREENHEIGHT])
        pygame.display.set_caption("坦克大战"+version)
        while(True):
            #窗口的颜色设置
            MainGame.window.fill(MainGame.COLOR_BLACK)
            self.getEvent()
            #窗口的刷新
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
                    print("坦克向左掉头，移动")
                elif event.key==pygame.K_RIGHT:
                    print("坦克向右掉头，移动")
                elif event.key == pygame.K_UP:
                    print("坦克向上掉头，移动")
                elif event.key == pygame.K_DOWN:
                    print("坦克向下掉头，移动")
                elif event.key == pygame.K_SPACE:
                    print("发射子弹")

    #游戏结束
    def endGame(self):
        print("谢谢使用")
        #结束Python解释器
        exit()

class Tank():
    def __init__(self):
        pass
    #坦克移动
    def move(self):
        pass
    #坦克射击
    def shot(self):
        pass
    def displayTank(self):
        pass

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