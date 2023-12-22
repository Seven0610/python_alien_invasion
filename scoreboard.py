import pygame.font
from ship import Ship


class Scoreboard(): # 得分板类
    def __init__(self, ai_game):
        self.ai_game = ai_game # 用于初始化飞船
        self.screen = ai_game.screen # 用于显示得分
        self.screen_rect = ai_game.screen.get_rect() # 用于显示得分
        self.settings = ai_game.settings # 用于显示得分
        self.stats = ai_game.stats # 用于显示得分
        # 显示得分信息的字体设置
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 48)
        # 准备得分图像
        self.prep_score()
        self.ships_sign = pygame.sprite.Group()

    def prep_score(self):
        """将得分转换为一幅渲染的图像"""
        score_str = f"score: {str(self.stats.score)}" # 将得分转换为字符串
        # 将得分渲染为图像
        self.score_image = self.font.render(score_str, True, self.text_color) 
        # 右上角显示得分
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_ships_sign(self): # 显示剩余生命值
        self.ships_sign = pygame.sprite.Group() # 创建一个空编组
        for ship_number in range(self.stats.ships_left): # 创建飞船实例
            ship_sign = Ship(self.ai_game, 'images/hp.png') # 加载生命值图标
            ship_sign.rect.x = 10 + ship_number * (ship_sign.rect.width + 3) 
            # 设置飞船位置
            ship_sign.rect.y = 10 # 设置飞船位置
            self.ships_sign.add(ship_sign) # 将飞船加入编组

    def show_score(self): # 显示得分
        self.screen.blit(self.score_image, self.score_rect)
        self.ships_sign.draw(self.screen)


class History(): # 历史最高分类
    def __init__(self, ai_game): # 初始化历史最高分
        self.ai_game = ai_game # 用于初始化飞船
        self.screen = ai_game.screen # 用于显示得分
        self.screen_rect = ai_game.screen.get_rect() # 用于显示得分
        self.settings = ai_game.settings # 用于显示得分
        self.stats = ai_game.stats # 用于显示得分
        self.text_color = (255, 255, 255) # 设置字体颜色
        self.font = pygame.font.SysFont(None, 48) # 设置字体

    def prep_history(self): # 准备历史最高分图像
        history_str = f"History: {str(self.stats.history)}"
        self.history_image = self.font.render(history_str, True, self.text_color)
        self.history_rect = self.history_image.get_rect()
        self.history_rect.midtop = self.screen_rect.midtop

    def show_history(self): # 显示历史最高分
        self.screen.blit(self.history_image, self.history_rect)
