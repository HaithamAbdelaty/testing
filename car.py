import unittest
def car (speed):
    if speed < 0 :
        return("invalid")
    elif speed >= 0 and speed < 40 :
        return("low")
    elif speed >= 40 and speed < 120 :
        return("normal") 
    elif speed >= 120 and speed < 200 :
        return("high")
    elif speed >= 200 and speed < 220 :
        return("v.high")
    elif speed >= 220 :
        return("invalid")
    else:
        return("not from speed")
