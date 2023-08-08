'''
坦克大战v1.01
游戏基础框架搭建
'''
import pygame

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
        pygame.display.set_caption("坦克大战1.03")
        while(True):
            #窗口的颜色设置
            MainGame.window.fill(MainGame.COLOR_BLACK)
            #窗口的刷新
            pygame.display.update()
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