# 导入标准库模块
import sys
from time import sleep, time
from random import choice, randint
# 导入第三方库模块
import pygame.image
# 导入自定义模块
from bullet import *
from alien import *
from settings import Settings
from game_stats import Gamestats
from button import *
from scoreboard import *
from energy_r import Energyr

class AlienInvasion: 
    """管理游戏资源和行为的类"""

    def __init__(self):                                                              # 初始化游戏并创建游戏资源
        pygame.init()                                                                # 初始化游戏并创建游戏资源
        self.settings = Settings()                                                   # 游戏设置
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.title_font = pygame.font.SysFont('Times New Roman', 40)                 # 创建字体对象
        self.title_text = self.title_font.render('Alien  Invention', True, (0, 0, 0))  # 创建文本图像
        pygame.display.set_caption("外星人入侵")                                      # 设置窗口标题
        self.stats = Gamestats(self)                                                 # 创建一个用于存储游戏统计信息的实例
        self.ship = Ship(self, 'images/ship.png')                                    # 创建飞船
        self.bullets = pygame.sprite.Group()                                         # 存储子弹的编组
        self.jineng1 = pygame.sprite.Group()                                         # 存储技能1子弹的编组
        self.aliens = pygame.sprite.Group()                                          # 存储外星人的编组
        self.boss = pygame.sprite.Group()                                            # 存储boss的编组
        self.energy = pygame.sprite.Group()                                          # 存储能量球的编组
        self.jineng2_1duan = pygame.sprite.Group()                                   # 存储技能2-1段子弹的编组
        self.jineng2_2duan = pygame.sprite.Group()                                   # 存储技能2-2段子弹的编组
        self.enemy_bulletgroup = pygame.sprite.Group()                               # 存储敌方子弹的编组
        self._create_fleet()                                                         # 创建外星人群
        self._create_energyqun()                                                     # 创建能量球群
        self.play_button = Button(self, 'click to play ↑', 0, 0, 0)                  # 游戏开始按钮
        self.replay_button = Button(self, 'replay', 255, 255, 255)                   # 游戏重新开始按钮
        self.music_button = Music_flag(self, 'playing', 255, 255, 255)               # 游戏音乐按钮
        self.youxishuoming = Youxishuoming(self, 'Specification ↓', 0, 0, 0)         # 游戏说明按钮
        self.Made_By = Made_By(self, ' ', 0, 0, 0)                                   # 制作说明按钮
        self.score_board = Scoreboard(self)                                          # 记分牌
        self.history = History(self)                                                 # 游戏历史记录
        self.energy_note = Energyr(self)                                             # 能量提示
        self.clock = pygame.time.Clock()                                             # 游戏时钟
        self.current_time = pygame.time.get_ticks()                                  # 获取当前时间

    def Run_Game(self):                                                              # 开始游戏的主循环
        while True:
            self._check_events()                                                     # 监听事件
            self.music_update()                                                      # 更新音乐
            if self.stats.game_active == True:                                       # 游戏开始
                if self.settings.jiluboss_time_flag:                                 # 记录boss出现时间
                    self.settings.create_boss_time = time()                          # 记录当前时间
                    self.settings.jiluboss_time_flag = False                         # 关闭记录boss出现时间的开关

                self.ship.update()                      # 更新飞船
                self.update_bullets()                   # 更新子弹
                self.update_jineng1()                   # 更新技能1
                self.update_jineng2_1duan()             # 更新技能2-1段
                self.update_jineng2_2duan()             # 更新技能2-2段
                self.update_aliens()                    # 更新外星人
                self.update_boss()                      # 更新boss
                self.update_enemybullet()               # 更新敌方子弹
                self.update_energy()                    # 更新能量球
            self._update_screen()                       # 更新屏幕

    def _check_events(self):                                                        # 响应按键和鼠标事件
        for event in pygame.event.get():                                            # 监听事件
            if event.type == pygame.QUIT:                                           # 退出游戏
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:                              # 鼠标点击事件
                mouse_pos = pygame.mouse.get_pos()
                if self.stats.ships_left == self.settings.ship_limit:               # 游戏未开始
                    self._check_play_button(mouse_pos)
                    self._check_youxishuoming_button(mouse_pos)
                elif self.stats.ships_left == 0:                                    # 游戏结束
                    self._check_replay_button(mouse_pos)

            elif event.type == pygame.KEYDOWN:                                      # 键盘按下事件
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:                                        # 键盘松开事件
                self._check_keyup_events(event)

    def music1_start(self):                                                         # 开始播放背景音乐1
        pygame.mixer.init()                                                         # 初始化
        pygame.mixer.music.load('musics/bgmusic1.mp3')                              # 加载音乐文件
        pygame.mixer.music.play(-1)                                                 # 播放音乐

    def music_update(self):                                                         # 更新音乐
        if self.stats.game_active == False:                                         # 游戏未开始
            if self.settings.music2_active == False:                                # 如果音乐2未播放
                self.music2_start()
                self.settings.music2_active = True
        else:                                                                       # 游戏开始
            if self.settings.music1_active == False:
                self.music1_start()
                self.settings.music1_active = True

    def music2_start(self):                                                         # 开始播放背景音乐2
        pygame.mixer.init()                                                         # 初始化
        pygame.mixer.music.load('musics/bgmusic2.mp3')                              # 加载音乐文件
        pygame.mixer.music.play(-1)

    def _update_screen(self):  # 更新屏幕上的图像，并切换到新屏幕
        if self.stats.play_click == False: # 游戏未开始                                      
            self.screen.blit(self.settings.background1, (0, 0))
            self.screen.blit(self.title_text, (469, 300))  # 在屏幕上绘制标题  
            if self.settings.show_youxishuoming_flag:
                self.screen.blit(self.settings.youxiguize_image, (0, 0))
        if self.stats.play_click == True: # 游戏开始
            # self.screen.fill(self.settings.bg_color)
            self.screen.blit(self.settings.background2, (0, 0))
            self.ship_show()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            # for enemybullet in self.new_bulletgroup.copy():
            for bullet in self.enemy_bulletgroup.sprites():
                bullet.draw_bullet()
            self.jineng1.draw(self.screen)   # 画散射子弹
            self.jineng2_1duan.draw(self.screen) # 画火焰弹
            self.jineng2_2duan.draw(self.screen) # 画爆炸弹
            self.aliens.draw(self.screen) # 画外星人
            self.boss.draw(self.screen) # 画boss
            self.energy.draw(self.screen) # 画能量球
            self.score_board.show_score() # 显示得分
            self.shuaxin_history() # 刷新历史记录
            self.history.show_history() # 显示历史记录
            self.energy_note.show_energy_note() # 显示能量提示
            self.energy_note.show_amount() # 显示能量值
            self.music_button.draw_button() # 显示音乐按钮
            self.music_button.draw_note_image() # 显示音乐按钮提示

        if not self.stats.game_active: # 游戏结束
            if self.stats.ships_left == self.settings.ship_limit and self.stats.play_click == False: 
                # 游戏未开始
                if self.settings.show_youxishuoming_flag == False: # 如果游戏说明未显示
                    self.play_button.draw_button() # 显示开始按钮
                    self.play_button.draw_note_image() # 显示开始按钮提示
                self.youxishuoming.draw_button() # 显示游戏说明按钮
                self.youxishuoming.draw_youxishuoming_image() # 显示游戏说明按钮提示
                self.Made_By.draw_button()                                        
            elif self.stats.ships_left <= self.settings.ship_limit and self.stats.ships_left > 0:    
                self.play_button.draw_button() # 显示继续按钮
                self.play_button.draw_note_pause_image() # 显示继续按钮提示
            elif self.stats.ships_left == 0: # 游戏结束
                self.replay_button.draw_button() # 显示重新开始按钮
                self.replay_button.draw_note_image() # 显示重新开始按钮提示
                self.ship.center_ship() # 飞船居中

        pygame.display.flip() # 让最近绘制的屏幕可见

    def _check_keydown_events(self, event):                                             # 按键按下事件
        if event.key == pygame.K_j:                                                     # 按下j键
            self._fire_bullet(self.settings.bullet_allowed)
        if self.stats.zifa_limit_flag == False:                                         # 如果飞船未被撞击
            if event.key == pygame.K_u:                                                 # 按下u键
                if self.stats.amount >= 5:                                              # 如果能量值大于5
                    if len(self.jineng1) < self.settings.jineng1_bullet_allowed:
                        self._fire_jineng1()
                        self.stats.amount -= 5
                        self.energy_note.prep_energy_amount()
            if event.key == pygame.K_i:                                                 # 按下i键
                if self.stats.amount >= 10:
                    self._fire_jineng2_1duan()
                    self.stats.amount -= 10
                    self.energy_note.prep_energy_amount()
            if event.key == pygame.K_o:                                                 # 按下o键
                if self.stats.amount >= 20:
                    self.jineng3_xiangyin()
        if event.key == pygame.K_TAB:                                                   # 按下tab键
            if self.stats.ships_left <= 3 and self.stats.ships_left > 0:
                self.stats.game_active = False
                pygame.mouse.set_visible(True)
        if event.key == pygame.K_CAPSLOCK:                                              # 按下大写锁定键
            if self.stats.ships_left <= 3 and self.stats.ships_left > 0:
                self.stats.game_active = True
        if event.key == pygame.K_RIGHT:                                                 # 按下右键
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:                                                  # 按下左键
            self.ship.moving_left = True
        if event.key == pygame.K_UP:                                                    # 按下上键
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:                                                  # 按下下键
            self.ship.moving_down = True

        if event.key == pygame.K_d:                                                     # 按下d键
            self.ship.moving_right = True
        if event.key == pygame.K_a:                                                     # 按下a键
            self.ship.moving_left = True
        if event.key == pygame.K_w:                                                     # 按下w键
            self.ship.moving_up = True
        if event.key == pygame.K_s:                                                     # 按下s键
            self.ship.moving_down = True
        if event.key == pygame.K_p:
            self.settings.music_switch *= -1
            if self.settings.music_switch == -1:
                self.music_button.msg = 'pause'
                pygame.mixer.music.pause()
            else:
                self.music_button.msg = 'playing'
                pygame.mixer.music.unpause()
            self.music_button._prep_msg()

        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):                                               # 按键松开事件
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False

        if event.key == pygame.K_d:
            self.ship.moving_right = False
        if event.key == pygame.K_a:
            self.ship.moving_left = False
        if event.key == pygame.K_w:
            self.ship.moving_up = False
        if event.key == pygame.K_s:
            self.ship.moving_down = False


    """子弹"""

    def _fire_bullet(self, bullet_allowed): # 发射普通或超级子弹"
        if len(self.bullets) < bullet_allowed: # 如果子弹数量小于允许的最大数量
            if self.ship.image_prep == 'images/ship.png':
                new_bullet = Bullet(self, 'images/ordinary_bullet.png') #普通子弹
                self.bullets.add(new_bullet)
            elif self.ship.image_prep == 'images/superform22.png':
                new_bullet = Bullet(self, 'images/super_bullet.png') #超级子弹
                self.bullets.add(new_bullet)

    def _fire_jineng1(self):                                                             # 发射技能1
        i = 0
        while i < 9:
            new_bullet = Jineng1(self, 'images/ordinary_bullet.png')                     #散射子弹
            self.jineng1.add(new_bullet)
            i += 1

    def _fire_jineng2_1duan(self):                                                       # 发射技能2-1段
        if len(self.jineng2_1duan.sprites()) < 1:
            new_bullet = Jineng2_1duan(self, 'images/fire_bullet.png')                   #火焰弹
            self.jineng2_1duan.add(new_bullet)

    def update_jineng1(self):                                                            # 更新技能1散射子弹位置
        pianyi_x = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
        i = 0
        for bullet in self.jineng1.sprites():
            bullet.update(pianyi_x[i])
            i += 1
            if i == 8:
                i = 0
        for bullet in self.jineng1.copy():
            if bullet.rect.bottom <= 0 or bullet.rect.right <= 0 or bullet.rect.left >= self.screen.get_rect().right:
                self.jineng1.remove(bullet)
        self._check_jineng1_alien_collisions()

    def update_jineng2_1duan(self):                                                       # 更新火焰弹位置
        self.jineng2_1duan.update()
        for bullet in self.jineng2_1duan.copy():                                          # 删除已经消失的火焰弹
            if bullet.rect.bottom <= 0:
                self.jineng2_1duan.remove(bullet)
        self._check_jineng1_1duan_alien_collisions()

    def _check_jineng1_1duan_alien_collisions(self):                                      # 检查火焰弹与外星人的碰撞
        for alien in self.aliens.sprites():
            for bullet in self.jineng2_1duan.sprites():
                if bullet.rect.colliderect(alien):
                    self.stats.score += self.settings.alien_point
                    self.score_board.prep_score()
                    self.aliens.remove(alien)
                    self.jineng2_1duan.remove(bullet)
                    self._fire_jineng2_2duan(alien)
                    break

    def _fire_jineng2_2duan(self, alien):                                                   # 发射技能2-2段子弹
        i = 0
        while i < 16:
            new_bullet = Jineng2_2duan(self, 'images/explosive_bullet.png', alien)
            self.jineng2_2duan.add(new_bullet)
            i += 1

    def update_jineng2_2duan(self):
        """更新技能2-2段子弹位置"""
        pianyi_x = [0, 0.5, 1, 2, 1, 2, 1, 0.5, 0, -0.5, -1, -2, -1, -2, -1, -0.5] # 技能2-2段子弹的x轴偏移量
        pianyi_y = [1, 1, 1, 1, 0, -1, -1, -1, -1, -1, -1, -1, 0, 1, 1, 1] # 技能2-2段子弹的y轴偏移量
        i = 0
        for bullet in self.jineng2_2duan.sprites(): # 更新技能2-2段子弹位置
            bullet.update(pianyi_x[i], pianyi_y[i])
            i += 1
            if i == 15:
                i = 0

        for bullet in self.jineng2_2duan.copy():
            if bullet.rect.bottom <= 0 or bullet.rect.right <= 0 or bullet.rect.left >= self.screen.get_rect().right \
                    or bullet.rect.top >= self.screen.get_rect().bottom:
                self.jineng2_2duan.remove(bullet)
        self._check_jineng1_2duan__alien_collisions()

    def _check_jineng1_2duan__alien_collisions(self): 
        """检查技能2-2段子弹与外星人的碰撞"""
        collisions = pygame.sprite.groupcollide(self.jineng2_2duan, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_point * len(aliens)
                self.score_board.prep_score()

    def update_bullets(self):
        """更新子弹位置"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    
    def _create_fleet(self):
        """创建外星人群"""
        images = ['images/alien1.png', 'images/alien2.png']
        choose_image = choice(images)
        alien = Alien(self, choose_image)
        number_alien_x = 4
        number_rows = 2
        # 创建群体
        i = 1
        j = randint(0, 5)
        while (i <= j):
            row_number = randint(0, number_rows)
            alien_number = randint(0, number_alien_x - 1)
            self._create_alien(alien_number, row_number)
            i += 1

    def _create_alien(self, alien_number, row_number): 
        """创建单个外星人"""
        images = ['images/alien1.png', 'images/alien2.png']
        choose_image = choice(images)
        alien = Alien(self, choose_image)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = float(alien.x)
        alien.rect.y = float(alien.rect.height + 1.5 * alien.rect.height * row_number)
        self.aliens.add(alien)

    def update_aliens(self): 
        """更新外星人位置"""
        # 记录当前时间
        h_time2 = time()
        # 获取之前创建子弹的时间
        h_time1 = self.settings.create_bullet

        # 如果距离上一次创建子弹的时间超过了1秒
        if h_time2 - h_time1 >= 1:
            # 调用方法创建新的子弹
            self.create_enemy_bullets()

        # 检查外星人群是否到达屏幕边缘
        self._check_fleet_edges()

        # 更新外星人的位置
        self.aliens.update()


        # 检测飞船与目标的碰撞
        for alien in self.aliens.copy():
            if alien.rect.colliderect(self.ship):
                if self.settings.wudi_flag == True:
                    self.aliens.remove(alien)
                else:
                    if alien.image_prep == 'images/alien2.png':
                        self.zifa_xiangyin()
                        self.aliens.remove(alien)
                    if alien.image_prep == 'images/alien1.png':
                        self._ship_hit()
        # 检测目标到达屏幕底端
        self._check_alien_bottom()

    def create_enemy_bullets(self):
        """创建敌方子弹"""
        self.settings.create_bullet = time()
        for alien in self.aliens.sprites():
            if alien.image_prep == 'images/alien1.png':
                new_bullet = Enemy_bullet(self, 'images/alien_bullet.png', alien)
                self.enemy_bulletgroup.add(new_bullet)

    def update_enemybullet(self): # 更新敌方子弹位置
        """更新敌方子弹位置"""
        self.enemy_bulletgroup.update()
        self._check_enemybullet_bottom()
        self._check_enemybullet_ship_collision()

    def _check_enemybullet_bottom(self): 
        """检查敌方子弹是否到达底部"""
        for bullet in self.enemy_bulletgroup.copy():
            if bullet.rect.top > self.screen.get_rect().bottom:
                self.enemy_bulletgroup.remove(bullet)

    def _check_enemybullet_ship_collision(self): 
        """检查敌方子弹与飞船的碰撞"""
        for enemybullet in self.enemy_bulletgroup.sprites():
            if enemybullet.rect.colliderect(self.ship):
                if self.settings.wudi_flag == True:
                    self.enemy_bulletgroup.remove(enemybullet)
                else:
                    self._ship_hit()

    def _check_fleet_edges(self): 
        """检查外星人是否到达屏幕边缘"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self): 
        """改变外星人群移动方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def change_energyqun_direction(self): 
        """改变能量群移动方向"""
        for energy in self.energy.sprites():
            energy.rect.y += self.settings.energyqun_drop_speed
        self.settings.energyqun_direction *= -1

    def _check_bullet_alien_collisions(self): 
        """检查子弹与外星人的碰撞"""
        # 检查是否击中
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_point * len(aliens)
                self.score_board.prep_score()
        # 全部击中后清空子弹并再次生成目标
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

            self.settings.increase_speed()  # 加速

    def _check_jineng1_alien_collisions(self): 
        """检查散射子弹与外星人的碰撞"""
        collision = pygame.sprite.groupcollide(self.jineng1, self.aliens, True, True)
        if collision:
            for aliens in collision.values():
                self.stats.score += self.settings.alien_point * len(aliens)
                self.score_board.prep_score()
    """飞船被撞击处理"""
    def _ship_hit(self): 
        '''飞船被撞击处理'''
        self.stats.ships_left -= 1
        if self.stats.ships_left > 0:
            self.score_board.prep_ships_sign()
            print(f"剩余:{self.stats.ships_left}")
            # 碰撞
            self.ship.image = pygame.image.load('images/collision.png')
            self._update_screen()
            # 暂停
            sleep(1.0)
            self.ship.image = pygame.image.load('images/ship.png')
            self._empty_all()
            self.enemy_bulletgroup.empty()
            # 重绘
            self._create_fleet()
            self.ship.center_ship()
        else:
            self.stats.game_active = False
            self.score_board.prep_ships_sign()
            pygame.mouse.set_visible(True)

            print(f"剩余:{self.stats.ships_left}\nGame over!")

    
    def _check_alien_bottom(self): 
        """检查外星人到达屏幕底端"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.screen.get_rect().bottom:
                self._ship_hit()  # 像ship被撞到一样处理
                break


    def _create_boss(self):  
        """创建Boss"""
        self.settings.create_boss_time = time()
        boss = Boss1(self, 'images/boss.png')
        self.boss.add(boss)

    def update_boss(self):
        """更新Boss位置"""
        boss_time2 = time()
        boss_time1 = self.settings.create_boss_time
        # print(boss_time2-boss_time1)
        if (boss_time2 - boss_time1) >= 30:
            self._create_boss()

        self.boss.update()
        self._check_boss_bottom()
        self._check_boss_gezhong_bullets_collision()

    def _check_boss_bottom(self):  
        """检查Boss到达屏幕底端"""
        for boss in self.boss.copy():
            if boss.rect.top > self.screen.get_rect().bottom:
                self._ship_hit()
                self.boss.remove(boss)

    def _check_boss_ship_collision(self):  
        """检查Boss与飞船的碰撞"""
        if self.settings.wudi_flag == False:
            for boss in self.boss.sprites():
                if boss.rect.colliderect(self.ship):
                    self._ship_hit()
                    boss.hp -= 15

    def _check_boss_gezhong_bullets_collision(self):  
        """检查Boss各种子弹与飞船的碰撞"""
        for boss in self.boss.sprites():
            for bullet in self.bullets.sprites():
                if boss.rect.colliderect(bullet):
                    if bullet.image_prep == 'images/ordinary_bullet.png':
                        boss.hp -= 1
                        print(boss)
                    elif bullet.image_prep == 'images/explosive_bullet.png':
                        boss.hp -= 4
                    self.bullets.remove(bullet)
                    if boss.hp == 0:
                        self.hp_0(boss, 5)
            for bullet1 in self.jineng1.sprites():
                if boss.rect.colliderect(bullet1):
                    self.jineng1.remove(bullet1)
                    boss.hp -= 1
                    print(boss)
                    if boss.hp == 0:
                        self.hp_0(boss, 5)
            for bullet2 in self.jineng2_1duan.sprites():
                if boss.rect.colliderect(bullet2):
                    self.jineng2_1duan.remove(bullet2)
                    self._fire_jineng2_2duan(boss)
                    boss.hp -= 1
                    print(boss)
                    if boss.hp == 0:
                        self.hp_0(boss, 5)
            for bullet3 in self.jineng2_2duan.sprites():
                if boss.rect.colliderect(bullet3):
                    self.jineng2_2duan.remove(bullet3)
                    boss.hp -= 1
                    print(boss)
                    if boss.hp == 0:
                        self.hp_0(boss, 5)

    def hp_0(self, boss, beishu):  
        """Boss血量为0时的处理"""
        self.boss.remove(boss)
        self.stats.score += self.settings.alien_point * beishu
        self.score_board.prep_score()

    def _create_energyqun(self): 
        """创建能量球群"""
        self.energy.create_time = time()
        images = ['images/energy.png', 'images/transformation.png']
        choose_image = choice(images)
        energy = Energys(self, choose_image)
        energy_width, energy_height = energy.rect.size
        available_space_x = self.settings.screen_width - (2 * energy_width)
        number_energy_x = available_space_x // (2 * energy_width)
        # print(number_alien_x)
        available_space_y = (self.settings.screen_height - 3 * energy_height)
        number_rows = available_space_y // (2 * energy_height)
        # print(number_rows)

        # 创建群体
        i = 1
        while (i <= 2):
            row_number = randint(0, number_rows)
            energy_number = randint(0, number_energy_x - 1)
            self._create_energy(energy_number, row_number)
            i += 1

    def _create_energy(self, energy_number, row_number): # 创建单个能量球
        images = ['images/energy.png', 'images/transformation.png']
        choose_image = choice(images)
        energy = Energys(self, choose_image)
        energy_width, energy_height = energy.rect.size
        energy.x = energy_width + 2 * energy_width * energy_number
        energy.rect.x = energy.x
        energy.rect.y = energy.rect.height + 1.5 * energy.rect.height * row_number
        self.energy.add(energy)

    def update_energy(self): # 更新能量球位置
        # self._check_energyqun_edges()
        self.energy.update()
        # 检测飞船与能量球的碰撞
        for energy in self.energy.copy():
            if energy.rect.colliderect(self.ship):
                if energy.image_prep == 'images/energy.png':
                    self.stats.amount += 100
                    self.energy_note.prep_energy_amount()
                    self.energy.remove(energy)
                    self.stats.score += 10 * self.settings.energy_point
                    self.score_board.prep_score()
                elif energy.image_prep == 'images/transformation.png':
                    self.ship.image_prep = 'images/superform11.png'
                    self.ship.image = pygame.image.load(self.ship.image_prep)
                    self.settings.incvinsible_time = time()
                    self.energy.remove(energy)

        if not self.energy:
            m_time1 = self.energy.create_time
            m_time2 = time()
            # print(m_time2 - m_time1)
            if m_time2 - m_time1 > 15:
                self._create_energyqun()
        # 检测能量球到达底部
        self._check_energy_bottom()

    def _check_energy_bottom(self): # 检查能量球到达底部
        for energy in self.energy.copy():
            if energy.rect.top >= self.screen.get_rect().bottom:
                self.energy.remove(energy)
        if not self.energy:
            m_time1 = self.energy.create_time
            m_time2 = time()
            # print(m_time2-m_time1)
            if m_time2 - m_time1 > 15:
                self._create_energyqun()

    """..."""

    def _check_youxishuoming_button(self, mouse_pos): # 检查游戏说明按钮
        button_clicked = self.youxishuoming.youxishuoming_image_rect.collidepoint(mouse_pos)
        if button_clicked:
            if self.settings.show_youxishuoming_flag == False:
                self.settings.show_youxishuoming_flag = True
            else:
                self.settings.show_youxishuoming_flag = False

    def _check_play_button(self, mouse_pos): # 检查游戏开始按钮
        button_clicked = self.replay_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.prep()
            self.stats.play_click = True

    def _check_replay_button(self, mouse_pos): # 检查游戏重新开始按钮
        button_clicked = self.replay_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            self._empty_all()
            self.stats.reset_stats()
            self.stats.amount = 0
            self.prep()
            self._update_screen()

    def prep(self):     # 游戏开始前的准备
        print("Game start!")
        self.stats.game_active = True
        self.score_board.prep_score()
        self.shuaxin_history()
        self.score_board.prep_ships_sign()
        self.energy_note.prep_energy_amount()
        pygame.mouse.set_visible(False)

    def shuaxin_history(self): # 刷新历史记录
        if self.stats.score >= self.stats.history:
            self.stats.history = self.stats.score
            self.history.prep_history()

    def zifa_xiangyin(self): # 飞船被撞击后的处理
        self.ship.image_prep = 'images/unable_attack.png'
        self.ship.image = pygame.image.load(self.ship.image_prep)
        self.ship.bianshen_time = time()
        self.stats.zifa_limit_flag = True

    def jineng3_xiangyin(self): # 技能3的处理
        self.ship.image_prep = 'images/mini_ship.png'
        self.ship.image = pygame.image.load(self.ship.image_prep)
        self.ship.suoxiao_time = time()

    def ship_show(self): # 飞船的显示
        if self.ship.image_prep == 'images/ship.png':
            self.ship.blitme()


        elif self.ship.image_prep == 'images/superform11.png' or self.ship.image_prep == 'images/superform22.png':
            xiamu_last_time2 = time()
            xiamu_last_time1 = self.settings.incvinsible_time
            self.settings.wudi_flag = True
            if (xiamu_last_time2 - xiamu_last_time1) < 3:
                incvinsible_time1 = self.settings.incvinsible_time
                incvinsible_time2 = time()
                if (incvinsible_time2 - incvinsible_time1) < 0.2:
                    self.ship.blitme()
                else:
                    self.ship.image_prep = 'images/superform22.png'
                    self.ship.image = pygame.image.load(self.ship.image_prep)
                    self.ship.blitme()
            else:
                self.settings.wudi_flag = False
                self.ship.image_prep = 'images/ship.png'
                self.ship.image = pygame.image.load(self.ship.image_prep)
                self.ship.blitme()

        elif self.ship.image_prep == 'images/unable_attack.png':
            end = time()
            start = self.ship.bianshen_time
            # print(end-start)
            if end - start < 2:
                self.ship.blitme()
            else:
                self.ship.image_prep = 'images/ship.png'
                self.ship.image = pygame.image.load(self.ship.image_prep)
                self.ship.blitme()
                self.stats.zifa_limit_flag = False

        elif self.ship.image_prep == 'images/mini_ship.png':
            end = time()
            start = self.ship.suoxiao_time
            # print(end-start)
            if end - start < 2:
                self.ship.blitme()
            else:
                self.ship.image_prep = 'images/ship.png'
                self.ship.image = pygame.image.load(self.ship.image_prep)
                self.ship.blitme()

    def _empty_all(self): # 清空所有编组
        self.enemy_bulletgroup.empty()
        self.aliens.empty()
        self.bullets.empty()
        self.jineng1.empty()
        self.jineng2_1duan.empty()
        self.jineng2_2duan.empty()
        self.energy.empty()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.Run_Game()
