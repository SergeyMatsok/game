class Stats():
    """отслеживание статистики"""

    def __init__(self):
        self.reset_stats()
        self.run_game = True
        with open('high_score.txt', 'r') as re:
            self.high_score = (int(re.readline()))

    def reset_stats(self):
        """статистика изменяющаяся во время игры"""
        self.guns_left = 2
        self.score = 0
