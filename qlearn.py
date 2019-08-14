import globals
import os
import pandas
import numpy as np


class QLearnAI:

    def __init__(self, epsilon, reward, lr, discount, min_val, max_val, states, actions):
        self.states = states
        self.actions = actions
        self.epsilon = epsilon
        self.reward = reward
        self.lr = lr
        self.discount = discount
        self.min_val = min_val
        self.max_val = max_val
        if os.path.isfile(os.path.join(globals.game_folder, 'qtable.npy')):
            print('File Found')
            self.Q = np.load(os.path.join(globals.game_folder, 'qtable.npy'))
            state_names = list()
            for i in range(0, states):
                state_names.append(str(i))
            action_names = ['U', 'D', 'L', 'R']
            df = pandas.DataFrame(self.Q, index=state_names, columns=action_names)
            print(df)
        else:
            print('File Not Found')
            self.Q = np.zeros((states, actions))
        self.maxQ = np.zeros((states, actions))

    def max_q(self, s_):
        max_reward = self.min_val
        for action in range(0, self.actions):
            if self.Q[s_, action] > max_reward:
                max_reward = self.Q[s_, action]
        return max_reward

    def update_q_value(self, s, a, s_):
        new_value = (1 - self.lr) * self.Q[s, a] + self.lr * (self.reward + self.discount * self.max_q(s_))
        if new_value < self.min_val:
            self.Q[s, a] = self.min_val
        elif new_value > self.max_val:
            self.Q[s, a] = self.max_val
        else:
            self.Q[s, a] = new_value
