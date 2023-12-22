import pygame


class Energyr(): # 能量球类
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.sb = ai_game.score_board
        self.stats = ai_game.stats
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/energy_note.png')
        self.rect = self.image.get_rect()
        # 显示能量球信息的字体设置
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        # 准备能量球数图像
        self.prep_energy_amount()
        # 位置
        self.rect.top = self.sb.score_rect.bottom + 14
        self.rect.x = self.screen_rect.right - 40

    def show_energy_note(self): # 显示能量球
        self.screen.blit(self.image, self.rect)

    def prep_energy_amount(self): # 准备能量球数图像
        amount_str = f"{str(self.stats.amount)} x "
        self.energy_amount_image = self.font.render(amount_str, True, self.text_color)
        self.energy_amount_rect = self.energy_amount_image.get_rect()
        self.energy_amount_rect.right = self.rect.right - 40
        self.energy_amount_rect.top = self.rect.bottom - 30

    def show_amount(self): # 显示能量球数
        self.screen.blit(self.energy_amount_image, self.energy_amount_rect)
