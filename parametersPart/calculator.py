"""
    The "calculator.py" module, containing all method to calculating different sort of cutting parameters.
"""

from math import pi


##############################################################
# All calculating for turning
##############################################################

def cuttingSpeed(machined_diameter, cutting_speed):
    """Method to calculating cutting speed."""
    score = (machined_diameter * cutting_speed * pi) / 1000
    return score


def spindleSpeed(machined_diameter, cutting_speed):
    """Method to calculating spindle speed."""
    score = cutting_speed * 1000 / (machined_diameter * pi)
    return score


def metalRemovalRate(depth_of_cut, feed_per_revolution, cutting_speed):
    """Method to calculating metal removal rate."""
    score = depth_of_cut * feed_per_revolution * cutting_speed
    return score


def timeInCut(start_diameter, cutting_speed, depth_of_cut, length_of_cut, machined_diameter, feed_per_revolution):
    """Method to calculating time in cut. """
    # I'm working on it
    pass

##############################################################
# All calculating for milling
##############################################################

# Add!!