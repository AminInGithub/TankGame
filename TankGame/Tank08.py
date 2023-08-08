"""
坦克大战v1.08
    新增功能：
        1.死亡之后按ESC键重生
"""
# 引用pygame游戏引擎、时间、及随机包
import pygame, time, random

# 定义游戏版本号
version = "1.08"

# 定义游戏主控制类
class MainGame():
    # 游戏主窗口
    window = None
    SCREENWIDTH = 800
    SCREENHEIGHT = 500
    COLOR_BLACK = pygame.Color(0, 0, 0)
    COLOR_RED = pygame.Color(255, 0, 0)
    TANK_P1 = None
    EnemyTank_list = []
    EnemyTank_count = 5
    Bullet_list = []
    Enemybullet_list = []
    Explode_list = []
    TANK_P1_SPEED = 1

    # text="敌方坦克还剩余8个"

    def __init__(self):
        pass

    # 游戏开始
    def starGame(self):
        pygame.display.init()
        # MainGame.TANK_P1 = Tank(420, 370)
        self.createMyTank()
        self.creatEnemyTank()
        # 创建窗口加载窗口（借鉴官方文件）
        MainGame.window = pygame.display.set_mode([MainGame.SCREENWIDTH, MainGame.SCREENHEIGHT])
        pygame.display.set_caption("坦克大战" + version)
        while (True):
            # 窗口的颜色设置
            MainGame.window.fill(MainGame.COLOR_BLACK)
            self.getEvent()

            # 将绘制文字得到的画布粘贴到窗口中
            MainGame.window.blit(self.getTextSurface("剩余地方坦克%d辆" % len(MainGame.EnemyTank_list)), [10, 10])

            # 将我方坦克加载到窗口中
            if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                MainGame.TANK_P1.displayTank()
            self.blitEnemyTank()
            if MainGame.TANK_P1 and not MainGame.TANK_P1.stop:
                MainGame.TANK_P1.move()
            self.blitBullet()
            self.blitEnemyBullet()

            # 调用展示爆炸效果的方法
            self.displayExplode()
            # 窗口的刷新
            time.sleep(0.01)
            pygame.display.update()

    def createMyTank(self):
        MainGame.TANK_P1 = Tank(420, 370)

    def creatEnemyTank(self):
        top = 100
        for i in range(MainGame.EnemyTank_count):
            speed = random.randint(3, 6)
            left = random.randint(1, 7)
            eTank = EnemyTank(top, left * 100)
            MainGame.EnemyTank_list.append(eTank)

    def blitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            if eTank.live:
                eTank.displayTank()
                eTank.randMove()
                eBullet = eTank.shot()
                if eBullet:
                    MainGame.Enemybullet_list.append(eBullet)
            else:
                MainGame.EnemyTank_list.remove(eTank)


    def blitBullet(self):
        for bullet in MainGame.Bullet_list:
            if bullet.live:
                bullet.displayBullet()
                bullet.bulletMove()
                bullet.hitEnemyTank()
            else:
                MainGame.Bullet_list.remove(bullet)

    # 定义渲染敌方子弹的方法
    def blitEnemyBullet(self):
        for ebullet in MainGame.Enemybullet_list:
            if ebullet.live:
                ebullet.displayBullet()
                ebullet.bulletMove()
                ebullet.hitMyTank()
            else:
                MainGame.Enemybullet_list.remove(ebullet)

    # 新增方法，展示爆炸效果
    def displayExplode(self):
        for explode in MainGame.Explode_list:
            if explode.live:
                explode.displayExplode()
            else:
                MainGame.Explode_list.remove(explode)

    def getEvent(self):
        # 1.获取所有事件
        # 2.对事件进行处理（1.点击关闭按钮。2.按下键盘上某个按键。）
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                self.endGame()
            # 判断是否是按键按下，如果是，继续判断是哪个按键
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and not MainGame.TANK_P1.live:
                    self.createMyTank()
                if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                    if event.key == pygame.K_LEFT:
                        MainGame.TANK_P1.direction = "L"
                        MainGame.TANK_P1.move()
                        MainGame.TANK_P1.stop = False
                        print("坦克向左掉头，移动")
                    elif event.key == pygame.K_RIGHT:
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
                        if len(MainGame.Bullet_list) < 3:
                            m = Bullet(MainGame.TANK_P1)
                            MainGame.Bullet_list.append(m)
                        else:
                            print("子弹数量不足")
                        print("当前屏幕中的子弹数量为：%d" % len(MainGame.Bullet_list))
            if event.type == pygame.KEYUP:
                if MainGame.TANK_P1 and MainGame.TANK_P1.live:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT \
                            or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        MainGame.TANK_P1.stop = True

    # 左上角提示内容
    def getTextSurface(self, text):
        # 初始化字体模块
        pygame.font.init()
        # 选中一个字体
        # fontlist=pygame.font.get_fonts()
        # print(fontlist)
        font = pygame.font.SysFont("kaiti", 18)
        textSurface = font.render(text, True, MainGame.COLOR_RED)
        return textSurface
        # 绘制自己设计的内容

    # 游戏结束
    def endGame(self):
        print("谢谢使用")
        # 结束Python解释器
        exit()


class BaseItem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__()

# 定义坦克父类
class Tank(BaseItem):
    def __init__(self, top, left):
        self.images = {
            "U": pygame.image.load("images/P1Tank_U.png"),
            "D": pygame.image.load("images/P1Tank_D.png"),
            "L": pygame.image.load("images/P1Tank_L.png"),
            "R": pygame.image.load("images/P1Tank_R.png"),
        }
        self.direction = "U"
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = 1
        self.stop = True
        self.live = True

    # 坦克移动
    def move(self):
        if self.direction == "L":
            if self.rect.left >= 0:
                self.rect.left -= self.speed
        elif self.direction == "R":
            if self.rect.left + self.rect.width < MainGame.SCREENWIDTH:
                self.rect.left += self.speed
        elif self.direction == "U":
            if self.rect.top >= 0:
                self.rect.top -= self.speed
        elif self.direction == "D":
            if self.rect.top + self.rect.height < MainGame.SCREENHEIGHT:
                self.rect.top += self.speed

    # 坦克射击
    def shot(self):
        return Bullet(self)

    def displayTank(self):
        self.image = self.images[self.direction]
        MainGame.window.blit(self.image, self.rect)


class MyTank(Tank):
    def __init__(self):
        pass


# 定义敌方坦克类，继承坦克父类
class EnemyTank(Tank):
    def __init__(self, top, left):
        super(EnemyTank, self).__init__(top,left)
        self.images = {
            "U": pygame.image.load("images/EnemyTank1_U.png"),
            "D": pygame.image.load("images/EnemyTank1_D.png"),
            "L": pygame.image.load("images/EnemyTank1_L.png"),
            "R": pygame.image.load("images/EnemyTank1_R.png"),
        }
        self.direction = "U"
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = 1
        self.stop = True
        self.step = 50

    def randDirection(self):
        num = random.randint(1, 4)
        if num == 1:
            return "U"
        elif num == 2:
            return "D"
        elif num == 3:
            return "L"
        elif num == 4:
            return "R"

    def randMove(self):
        if self.step <= 0:
            self.direction = self.randDirection()
            self.step = 50
        else:
            self.move()
            self.step -= 1

    def shot(self):
        num = random.randint(1, 1000)
        if num <= 5:
            return Bullet(self)

    def displayEnemyTank(self):
        super().displayTank()


# 定义子弹类
class Bullet(BaseItem):
    def __init__(self, tank):
        self.image = pygame.image.load("images/bullet/bullet_up.png")
        self.diredction = tank.direction
        self.rect = self.image.get_rect()
        if self.diredction == "U":
            self.image = pygame.image.load("images/bullet/bullet_up.png")
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.diredction == "D":
            self.image = pygame.image.load("images/bullet/bullet_Down.png")
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.diredction == "L":
            self.image = pygame.image.load("images/bullet/bullet_Left.png")
            self.rect.left = tank.rect.left - self.rect.width
            self.rect.top = tank.rect.top + tank.rect.height / 2 - self.rect.width / 2
        elif self.diredction == "R":
            self.image = pygame.image.load("images/bullet/bullet_Right.png")
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.height / 2 - self.rect.width / 2
        self.speed = 3
        self.live = True


    # 子弹的移动
    def bulletMove(self):
        if self.diredction == "U":
            if self.rect.top > 0:
                self.rect.top -= self.speed
            else:
                self.live = False
        elif self.diredction == "D":
            if self.rect.top + self.rect.height < MainGame.SCREENHEIGHT:
                self.rect.top += self.speed
            else:
                self.live = False
        elif self.diredction == "L":
            if self.rect.left > 0:
                self.rect.left -= self.speed
            else:
                self.live = False
        elif self.diredction == "R":
            if self.rect.left + self.rect.width < MainGame.SCREENWIDTH:
                self.rect.left += self.speed
            else:
                self.live = False

    # 子弹的显示
    def displayBullet(self):
        MainGame.window.blit(self.image, self.rect)

    # 新增我方子弹碰撞敌方坦克的方法
    def hitEnemyTank(self):
        for eTank in MainGame.EnemyTank_list:
            if pygame.sprite.collide_rect(eTank, self):
                # 产生爆炸效果
                # 将效果加入到爆炸效果列表中
                explode = Explode(eTank)
                MainGame.Explode_list.append(explode)
                self.live = False
                eTank.live = False

    # 新增敌方子弹和我方坦克的碰撞
    def hitMyTank(self):
        if pygame.sprite.collide_rect(self,MainGame.TANK_P1):
            # 产生爆炸效果，并加入到爆炸效果列表中
            explode = Explode(MainGame.TANK_P1)
            MainGame.Explode_list.append(explode)
            # 修改子弹状态
            self.live = False
            # 修改我方坦克状态
            MainGame.TANK_P1.live = False

class Explode():
    def __init__(self,tank):
        self.rect = tank.rect
        self.step = 0
        self.images = [
            pygame.image.load("images/effct/blast01.png"),
            pygame.image.load("images/effct/blast02.png"),
            pygame.image.load("images/effct/blast03.png"),
            pygame.image.load("images/effct/blast04.png"),
            pygame.image.load("images/effct/blast05.png"),

        ]
        self.image = self.images[self.step]
        self.live = True

    # 展示爆炸效果的方法
    def displayExplode(self):
        if self.step<len(self.images):
            MainGame.window.blit(self.image,self.rect)
            self.image = self.images[self.step]
            self.step += 1
        else:
            self.live = False
            self.step = 0



class Wall():
    def __init__(self, left, top):
        # self.image = pygame.image.load("images/scene/brick.png")
        # self.rect = self.image.get_rect()
        # self.rect.left = left
        # self.rect.top = top
        # # 用来判断墙壁是否应该在窗口中展示
        # self.live = True
        # # 用来记录墙壁的生命值
        # self.hp = 3
        pass
    # 障碍物墙壁展示
    def displayWall(self):
        # MainGame.window.blit(self.image,self.rect)
        pass

class Music():
    def __init__(self):
        pass

    # 开始播放音乐
    def displayMusic(self):
        pass


MainGame().starGame()
