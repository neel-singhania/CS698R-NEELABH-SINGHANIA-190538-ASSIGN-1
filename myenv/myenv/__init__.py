import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='TwoArmBandit-v0',
    entry_point='myenv.env:twoArmBandit',
)

register(
    id='TenArmBandit-v0',
    entry_point='myenv.env:tenArmBandit',
)

register(
    id='RandomWalk-v0',
    entry_point='myenv.env:randomWalk',
)