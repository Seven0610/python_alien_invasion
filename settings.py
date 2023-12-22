import pygame


class Settings:
    """存储游戏中所有的设置的类"""

    def __init__(self):
        """初试化游戏的设置"""
        self.title_font = pygame.font.Font(None, 50)  # 创建字体对象
        self.title_text = self.title_font.render('外星人入侵', True, (255, 255, 255))  # 创建文本图像
        
        # 屏幕设置
        self.screen_width = 1200 
        self.screen_height = 780
        self.bg_color = (106, 90, 205)
        self.background1 = pygame.image.load('images/Opening background.png')
        self.background2 = pygame.image.load('images/Combat background.jpg')
        # 飞船设置
        self.ship_limit = 3
        self.ship_speed = 1.4
        self.incvinsible_time = 0 # 无敌时间
        self.wudi_flag = False # 无敌标志
        # 子弹设置
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_speed = 4.5
        self.bullet_allowed = 20
        self.jineng1_bullet_allowed = 10
        # enemy目标设置
        self.alien_speed = 0.8
        self.fleet_drop_speed = 15
        self.fleet_direction = 1  # right
        self.alien_point = 10
        self.enemy_bullet_speed = 4
        self.create_bullet = 0
        # boss设置
        self.boss_speed = 0.1
        self.create_boss_time = 0.1
        self.c_b_limit = False
        self.jiluboss_time_flag = True
        # 蓝色能量球目标设置
        self.energy_speed = 1.2
        self.energyqun_drop_speed = 10
        self.energyqun_direction = -1  # left
        self.energy_point = 1
        # 加快节奏
        self.speedup_scale = 1.1
        self.score_scale = 1.3
        self.initialize_dynamic_settings()
        # 背景音乐
        self.music1 = pygame.mixer.music.load('musics/bgmusic1.mp3')
        self.music2 = pygame.mixer.music.load('musics/bgmusic2.mp3')
        self.music1_active = False
        self.music2_active = False
        self.music_switch = 1
        # 游戏说明
        self.youxiguize_image = pygame.image.load('images/specification.png')
        self.youxiguize_image_rect = self.youxiguize_image.get_rect()
        self.youxiguize_image_rect.x = 300
        self.youxiguize_image_rect.y = 200
        self.show_youxishuoming_flag = False

    def initialize_dynamic_settings(self):
        """初始化设置"""
        self.ship_speed = 4
        self.bullet_speed = 5
        self.alien_speed = 1.7
        self.alien_point = 10
        self.fleet_direction = 1  # right

    def increase_speed(self): # 加快节奏
        if self.ship_speed <= 5:
            self.ship_speed *= self.speedup_scale
        if self.alien_speed <= 4.5:
            self.alien_speed *= self.speedup_scale
            self.alien_point = int(self.alien_point * self.score_scale)
        if self.bullet_speed <= 5.5:
            self.bullet_speed *= self.speedup_scale
        if self.alien_speed > 4.5 and self.fleet_drop_speed < 30:
            self.fleet_drop_speed *= self.speedup_scale

        # print(f"s:{float(self.ship_speed)} a:{float(self.alien_speed)}\nb:{float(self.bullet_speed)} p:{self.alien_point}")
