# https://www.codewars.com/kata/51fda2d95d6efda45e00004e
class User():
    ranks = [-i for i in range(8, 0, -1)] + [i for i in range(1, 9)]

    def __init__(self):
        self.rank_index = 0
        self.progress = 0

    @property
    def rank(self):
        return self.ranks[self.rank_index]

    def inc_progress(self, kata_rank):
        if kata_rank == 0 or abs(kata_rank) > 8:
            raise Error
        
        if self.rank == 8:
            return
    
        diff = kata_rank - self.rank - int(self.rank * kata_rank < 0) * (1 if kata_rank > self.rank else -1)
        if diff == 0:
            self.progress += 3
        elif diff == -1:
            self.progress += 1
        elif diff >= 1:
            self.progress += 10 * diff * diff
                    
        div, self.progress = divmod(self.progress, 100)
        print(div, self.progress)
        self.rank_index += div
        
        if self.rank >= 8:
            self.progress = 0
            self.rank_index = len(self.ranks) - 1
        