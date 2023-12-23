## python-alien-invasion（外星人入侵β）
基于pygame的小游戏外星人入侵β，初学python时做的小游戏，其中很多代码可以优化，仅供参考，日后有时间会考虑优化。

注意事项：

         1.图片路径要配置好，根据本地文件路径来配置

优化建议：

         1.属性、方法、类名规范化，驼峰命名；

         2.抽取共用代码，善用继承多态，提高代码复用性；
         
         3.alien、boss这些alien或debuff可以采用多线程，增加游戏可玩性；
         
         4.可以加一些动画效果，增加视觉体验；

陆续更新中...
#### 版本更迭的开发日志信息
         2023-11-08 14:27:57-[UPDATE]-version_源版本-完成外星人入侵游戏主体功能的编写，对游戏帧数进行了提升
         2023-11-10 21:18:06-[UPDATE]-version_源版本-增加了一些玩家技能与能量设置，提高了游戏的可玩性。
         2023-11-15 12:31:35-[UPDATE]-version_-新增了难度系数与消灭敌方目标的不同奖励得分机制
         2023-11-17 10:58:20-[FIX]-version_α优化了游戏内资源贴图及飞船与敌方目标的碰撞体积问题
         2023-11-20 0:05:51-[FIX]-version_α优化了游戏内的声音资源，并优化了指针移动至按钮上，按钮会改变形态或颜色的功能以实现人机交互的功能
         2023-11-21 21:19:15-[UPDATE]-version_α新增了爆炸特效、优化了血量设定
         2023-11-26 0:50:52-[FIX]-version_α修复了报错和死循环的问题，修复了一些已知问题与bug
         2023-11-27 20:19:44-[UPDATE]-version_α新增了玩家技能中的火焰弹分裂成小型火焰弹以7个为编组的弹射操作
         2023-11-30 23:10:26-[FIX]-version_α修复了一些文字显示问题、按钮无法显示完全的问题
         2023-12-05 23:45:23-[UPDATE]-version_α新增了退出游戏按钮、优化了美术效果
         2023-12-05 23:59:07-[FIX]-version_α修复了一些已知问题与bug
         2023-12-09 01:31:14-[UPDATE]-version_β新增了超级形态增益包、多行外星人刷新机制
         2023-12-09 19:37:03-[FIX]-version_β调整了增益包刷新的概率，并设置了生命值上限为3
         2023-12-09 21:36:12-[UPDATE]-version_β新增了外星Boss
         2023-12-09 22:58:23-[FIX]-version_β修复了一些内侧玩家反馈的问题与bug
         2023-12-15 23:41:31-[UPDATE]-version_β新增了外星Boss能够发射自动跟踪子弹的功能
         2022-12-15 0:29:08-[FIX]-version_β优化了外星Boss发射的子弹的自动跟踪算法
         2022-12-21 23:34:54-[FIX]-version_β优化了外星Boss及子弹的贴图及碰撞体积问题
         2023-12-21 23:34:54-[ARCHIVE]-version__fixed-Archive the Alien Gaming β

#### 心得体会
在过去的几周里，我们小组共同努力，成功地完成了一项令人兴奋的游戏项目——基于Pygame的外星人入侵游戏。这个过程不仅让我们学到了许多关于游戏设计和团队协作的知识，而且也锻炼了我们解决问题的能力。以下是我们小组在这个项目中的一些心得体会。
1. 团队合作与沟通:
合作是整个项目成功的关键。我们小组明确了每个成员的角色和任务分工，确保每个人都能充分发挥自己的优势。通过定期的团队会议，我们讨论了项目的进展、遇到的问题以及下一步的计划。良好的沟通帮助我们更好地理解彼此的想法，提高了项目整体的效率。
2. 学习与挑战:
在项目中，我们遇到了许多新的技术和概念，特别是在Pygame框架下进行游戏设计的方面。虽然有时候我们会遇到困难，但通过学习文档、在线教程和相互讨论，我们成功地克服了这些挑战。这使我们对游戏设计的理解更加深入，并提高了我们解决问题的能力。
3. 代码管理与版本控制:
为了更好地协同工作，我们采用了版本控制工具（如Git）来管理我们的代码。这使得我们能够追踪代码的修改、合并不同成员的工作，并在需要时回滚到先前的版本。这种良好的代码管理实践有助于避免潜在的冲突，并使整个项目更加可维护。
4. 用户体验与游戏设计:
在设计游戏时，我们注重用户体验，确保玩家能够轻松上手并享受游戏过程。我们进行了反复的游戏测试，收集了玩家的反馈，并对游戏进行了不断的优化。这使我们认识到用户体验在游戏设计中的重要性，并学到了如何平衡游戏的难度以提供更好的游戏体验。
5. 持续改进与反思:
项目结束并不意味着一切结束，我们小组会继续通过反馈和自我评估寻找改进的空间。我们会保留项目文档，记录我们的经验和教训，以便将来的项目中能够更好地应对类似的挑战。
通过这个项目，我们不仅成功地完成了一个有趣的游戏，还建立了团队协作的技能，学到了新的知识，并且在实践中提高了解决问题的能力。这次合作经历将成为我们团队发展的宝贵财富，为未来的项目奠定了坚实的基础。
