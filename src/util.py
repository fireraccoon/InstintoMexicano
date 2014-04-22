
# GEt angle between 2 points
import math


def getAngle(x1, y1, x2, y2):
    # Return value is 0 for right, 90 for up, 180 for left, and 270 for down (and all values between 0 and 360)
    rise = y1 - y2
    run = x1 - x2
    angle = math.atan2(run, rise)  # get the angle in radians
    angle *= 180 / math.pi  # convert to degrees
    angle = (angle + 90) % 360  # adjust for a right-facing sprite
    return angle