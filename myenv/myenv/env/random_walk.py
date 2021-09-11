from gym import Env
from gym.spaces import Discrete
from numpy import random
from gym.utils import seeding

class randomWalk(Env):

    def __init__(self, a=3):
        # action can be taken-> left, right
        self.action_space = Discrete(2)
        # S+ states
        self.observation_space = Discrete(7)
        # start state
        self.state = a
        # episode length
        self.ep_len = 0

    def step(self, action,state):
        action = random.random()
        if action > 0.5:
            state +=1
        else:
            state -=1
        self.state = state    
        if self.state == 6:
            reward = 1
        else:
            reward = 0
        self.ep_len += 1
        return self.state, action, reward

    def render(self):
        pass
    
    def _seed(self, seed=None):
        self.np_random, seed = seeding.np.random(seed)
        return [seed]
    
    def reset(self):
        self.state = 3
        self.ep_len = 0
        return self.state

