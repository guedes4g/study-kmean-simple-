import random

def generate(number = 10, t = 100, b=0):
    points = []
    for i in range(0,number):
        points.append([random.randint(b,t), random.randint(b,t)])
        
    return points