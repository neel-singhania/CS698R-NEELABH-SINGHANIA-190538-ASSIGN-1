from gym import Env
from gym.spaces import Discrete
from numpy import random
from gym.utils import seeding

class tenArmBandit(Env):

    def __init__(self,gauss):
        # action can be taken-> left, right
        self.action_space = Discrete(10)
        # S+ states
        self.ob_state = Discrete(11)
        # start state
        self.state = 0
        # episode length
        self.ep_len = 0
        #reward function
        self.prob = gauss

    def step(self, action):
        reward = random.normal(self.prob[action],1)
        self.state = 1 + action
        self.ep_len += 1
        return self.state,action, reward

    def render(self):
        pass

    def reset(self):
        self.state = 1
        self.ep_len = 0
    
    def _seed(self, seed=None):
        self.np_random, seed = seeding.np.random(seed)
        return [seed]