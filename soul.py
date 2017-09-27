import random


class Soul:
    """
    Soul class
    """
    def __init__(self, name):
        self.name = name
        pool = random.randint(3, 10)

        self.ar_boost = random.randint(1, pool-2)
        pool -= self.ar_boost
        self.df_boost = random.randint(1, pool-1)
        pool -= self.df_boost
        self.spd_boost = random.randint(1, pool)
