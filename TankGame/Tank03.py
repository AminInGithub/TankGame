'''
坦克大战v1.03
    游戏基础功能实现
    新增功能：
        实现左上角问题提示内容
'''
import pygame
version="1.02"
class MainGame():
    #游戏主窗口
    window=None
    SCREENWIDTH=800
    SCREENHEIGHT=500
    COLOR_BLACK=pygame.Color(0,0,0)
    COLOR_RED=pygame.Color(255,0,0)
    # text="敌方坦克还剩余8个"

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
            #将绘制文字得到的画布粘贴到窗口中
            MainGame.window.blit(self.getTextSurface("剩余地方坦克%d辆"%5),[10,10])
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