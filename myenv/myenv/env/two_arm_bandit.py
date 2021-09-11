from numpy import random
from gym import Env
from gym.spaces import Discrete
from gym.utils import seeding

class twoArmBandit(Env):

    def __init__(self, prob):
        # action can be taken-> left, right
        self.action_space = Discrete(2)
        # S+ states
        self.ob_state = Discrete(3)
        # start state
        self.state = 1
        # episode length
        self.ep_len = 0
        #prob contains alpha, beta
        self.prob = prob

    def step(self, action):
        if action == 1:                                # obtain the state of agent after he chooses right
            bin_action = random.binomial(1,self.prob[1])    # the next state will be determined by Bin(prob[1])

        else:                                          # obtain the state of agent after he chooses left
            bin_action = random.binomial(1,1-self.prob[0])    # the next state will be determined by Bin(prob[0])

        reward = 0
        if bin_action == action:
            reward = 1

        self.state = 2 * bin_action  # sets the terminal state of the agent
        self.ep_len += 1
        return self.state, bin_action, reward

    def render(self):
        pass

    def reset(self):
        self.state = 1
        self.ep_len = 0

    def _seed(self, seed=None):
        self.np_random, seed = seeding.np.random(seed)
        return [seed]