import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # Alien 类的初始化方法
    def __init__(self, ai_game, image):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image_prep = image
        self.image = pygame.image.load(self.image_prep)
        self.rect = self.image.get_rect()

        # 每个外星人最初在屏幕左上角附近
        self.rect.x = self.rect.width - 100  # 这里将 x 坐标设置为外星人宽度减去 100
        self.rect.y = self.rect.height - 100  # 这里将 y 坐标设置为外星人高度减去 100
        # 存储外星人的精确水平位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def update(self): # 更新外星人的位置
        """移动"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True


class Energys(Alien): # 能量球类
    def __init__(self, ai_game, image):
        super().__init__(ai_game, image)
        self.create_time = 0
        # 每个能量球最初在屏幕左上角附近
        self.rect.x = self.rect.width - 150
        self.rect.y = self.rect.height - 150
        # 存储能量球的精确水平位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self): # 更新能量球的位置
        """移动"""
        self.y += self.settings.energy_speed
        self.rect.y = self.y


class Boss1(Alien): # Boss1 类
    def __init__(self, ai_game, image):
        super().__init__(ai_game, image)
        self.hp = 50
        self.rect.midtop = self.screen.get_rect().midtop
        self.rect.y = -100
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self): # 更新 Boss1 的位置
        """移动"""
        self.y += self.settings.boss_speed
        self.rect.y = self.y

    def __repr__(self): # 返回 Boss1 的血量
        return 'hp:%r' % (self.hp)
