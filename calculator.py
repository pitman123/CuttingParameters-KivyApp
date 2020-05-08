"""...."""

from math import pi


def cuttingSpeed(machined_diameter, cutting_speed):
    score = (machined_diameter * cutting_speed * pi) / 1000
    return score


def spindleSpeed(machined_diameter, cutting_speed):
    score = cutting_speed * 1000 / (machined_diameter * pi)
    return score


def metalRemovalRate(depth_of_cut, feed_per_revolution, cutting_speed):
    score = depth_of_cut * feed_per_revolution * cutting_speed
    return score


def timeInCut(start_diameter, cutting_speed, depth_of_cut, length_of_cut, machined_diameter, feed_per_revolution):
    pass
