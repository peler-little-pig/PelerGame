"""导入游戏引擎, 头文件, 模块"""
import pygame
from pygame.locals import *


#个人FS logo设置
class FSLogo():

    def __init__(self, imagePath, indexAdder=1, size=(640, 642), maxAlpha=254,
                 beInCenter=True):
        self.screen = pygame.display.get_surface()
        self.surface = self.screen.get_rect()

        self.indexAdder = indexAdder
        self.timer = Timer(2)   #计时控制器
        self.size = size
        self.alphaIndex = 0
        self.LOGOImage = pygame.image.load(imagePath).convert_alpha()
        self.LOGOImage.set_alpha(self.alphaIndex)
        self.rect = self.LOGOImage.get_rect()
        self.maxAlpha = maxAlpha
        self.beInCenter = beInCenter

        if self.beInCenter:
            self.rect.center = self.surface.center

    #正常一次闪烁
    def update(self):
        if self.alphaIndex >= self.maxAlpha:
            self.indexAdder = -self.indexAdder

        if self.timer.update():
            self.alphaIndex += self.indexAdder * 3

        self.LOGOImage.set_alpha(self.alphaIndex)
        self.timer.update()

    #获取LOGO刷新回调函数
    def getRestarter(self):
        if self.alphaIndex <= -1:
            return True

    #渲染绘制
    def pack(self):
        self.screen.blit(self.LOGOImage, self.rect)

"""CR计时器, 正常计时"""
class Timer():

    """形参maxTime是最大计时时间, 到则指针清零, 返回True"""

    def __init__(self, maxTime):
        self.maxTime = maxTime  #最大时间
        self.timeIndex = 0      #指针

    #清零指针函数
    def timeIndexReset(self, reseter=0):
        self.timeIndex = reseter

    #添加指针数函数
    def timeIndexAdd(self, adder=1):
        self.timeIndex += adder

    #返回函数, 刷新, 返回, 刷新调用两次
    def update(self):

        #函数主体
        if self.timeIndex >= self.maxTime:

            self.timeIndexReset()   #指针清零
            return True
        else:
            self.timeIndexAdd()     #增加指针