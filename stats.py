

class Stats:
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.lives_left = self.settings.mario_lives
        self.last_mario_left = self.lives_left
        self.score = 0
        self.level = 0
        self.highscore = self.load_high_score()

    def __del__(self): self.save_high_score()    

    @staticmethod
    def load_high_score():
        try:
            with open("highscore.txt", "r") as f:
                return int(f.read())    
        except:
            return 0
        
    def save_high_score(self):
        try:
            with open("highscore.txt", "w+") as f:
                f.write(str(round(self.highscore, -1)))  # 314.15 --> 310,  (0) --> 314
        except:
            print("highscore.txt not found...")

    def get_score(self): return self.score
    def get_highscore(self): return self.highscore
    def get_level(self): return self.level
    def get_lives_left(self): return self.lives_left

    def reset_stats(self):
        self.lives_left = self.settings.mario_lives

    def goomba_hit(self, goomba):
        self.score += self.settings.goomba_points
        goomba.dying = True

    def mario_hit(self):
        self.lives_left -= 1
        if self.lives_left == 0:
            self.game.finished = True
