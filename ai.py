import random
from qlearn import QLearnAI


class AI(QLearnAI):

    e = 0.1
    r = 0.0
    lr_ = 0.3
    d = 0.9
    min_ = -10000
    max_ = 10000

    def __init__(self, player, game_table, rows, cols):
        QLearnAI.__init__(self, AI.e, AI.r, AI.lr_, AI.d, AI.min_, AI.max_, rows * cols, 4)
        self.player = player
        self.game_table = game_table
        self.rows = rows
        self.cols = cols

    def run(self):
        # get initial state
        s = self.get_state()
        # determine whether to explore or exploit
        if random.uniform(0, 1) < self.epsilon:
            a = random.randint(0, self.actions-1)
        else:
            max_index = 0
            max_value = self.min_val
            for i in range(0, self.actions):
                val = self.Q[s, i]
                if val > max_value:
                    max_index = i
                    max_value = val
            a = max_index
        # do action
        self.do_action(a)
        self.update_board()
        # get new state
        s_ = self.get_state()
        # determine reward based off old_state and new_state
        self.reward = self.get_reward(s_)
        # update q value
        self.update_q_value(s, a, s_)

    def do_action(self, action):
        if action == 0:
            self.player.up()
        elif action == 1:
            self.player.down()
        elif action == 2:
            self.player.left()
        elif action == 3:
            self.player.right()

    def get_reward(self, s_):
        if s_ == self.states - 1:
            self.player.reset_move()
            self.reset()
            return 1000
        elif s_ == 0:
            return -200
        return -1

    def get_state(self):
        iterations = 0
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                if self.player.current_index == (i, j):
                    return iterations
                iterations += 1

    def update_board(self):
        if self.player.new_index is not None:
            if not self.check_errors(self.player.new_index):
                self.game_table[self.player.current_index[0], self.player.current_index[1]] = 0
                self.game_table[self.player.new_index[0], self.player.new_index[1]] = 1
                self.player.confirm_move()
            else:
                self.player.reset_move()
                self.reset()

    def check_errors(self, new_index):
        if new_index[0] < 0 or new_index[0] >= self.rows or new_index[1] < 0 or new_index[1] >= self.cols:
            return True
        elif self.game_table[new_index[0], new_index[1]] == 2:
            return True
        return False

    def reset(self):
        self.game_table[self.player.current_index[0], self.player.current_index[1]] = 0
        self.game_table[0, 0] = 1
        self.player.current_index = (0, 0)
