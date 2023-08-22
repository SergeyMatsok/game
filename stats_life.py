class Stats():
    """отслеживание статистики"""

    def __init__(self):
        self.reset_stats()

    def reset_stats(self):
        """статистика изменяющаяся во время игры"""
        self.guns_left = 2
