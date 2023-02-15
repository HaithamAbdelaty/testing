import unittest
def degree (d):
    if d < 0 :
        return("invalid")
    elif d >= 0 and d < 50 :
        return("faild")
    elif d >= 50 and d < 65 :
        return("passed") 
    elif d >= 65 and d < 75 :
        return("good")
    elif d >= 75 and d < 85 :
        return("v.good")
    elif d >= 85 and d < 100 :
        return("excellent")
    elif d >= 100 :
        return("in")    
    else:
        return("not from degree")
