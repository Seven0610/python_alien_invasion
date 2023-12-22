class Gamestats(): 
    """跟踪游戏的统计信息"""
    def __init__(self, ai_game):
        """初始化统计信息"""
        self.game_active = False # 游戏刚启动时处于非活动状态
        self.settings = ai_game.settings # 游戏设置
        self.reset_stats() # 在任何情况下都不应重置最高得分
        self.score = 0 # 得分，初始值为零
        self.amount = 0 # 用于记录敌人数量
        self.history = 0 # 用于记录历史最高分
        self.zifa_limit_flag = False # 用于记录是否使用了技能1
        self.create_m_limit = False # 用于记录是否创建了boss
        self.play_click = False # 用于记录是否点击了开始游戏按钮

    def reset_stats(self): 
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit 
        # 飞船数
        self.score = 0 
        # 得分，初始值为零
