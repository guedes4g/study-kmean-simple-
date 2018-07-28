import random
import math

class Group:
    def __init__(self, pos = None):
        if pos == None:
            self.position = [random.randint(0,100), random.randint(0,100)]
        else:
            self.position = pos 
        self.points = []

class Kmean:
    def __init__(self, points, iterations=1000, groups = 2):
        self.points = points
        self.iterations = iterations
        self.groups = self.init_groups(n=groups)
        self.run()

    def init_groups(self, n):
        g = []
        for _ in range(0,n):
            g.append(Group())
        return g

    def clear_groups(self):
        for i in range(len(self.groups)):
            self.groups[i].points = []
        
    def calculate_distance(self, a, b):
        return math.sqrt(math.pow(a[0]-b[0],2) + math.pow(a[1]-b[1], 2))

    def find_the_closest_group(self, point):
        closest_group = self.groups[0]
        closest_distance = self.calculate_distance(point, closest_group.position)
        for i in range(1,len(self.groups)):
            aux = self.calculate_distance(point, self.groups[i].position)
            if(aux < closest_distance):
                closest_distance = aux
                closest_group = self.groups[i]
        closest_group.points.append(point)
            
    def recalculate_group_position(self, group):
        n = len(group.points)
        if n == 0:
            return
        x = 0
        y = 0
        for i in range(n):
            x = x + group.points[i][0]
            y = y + group.points[i][1]
        x = x/n
        y = y/n
        group.position = [x, y]

    def run(self):
        for _ in range(self.iterations):
            self.clear_groups()

            for i in range(len(self.points)):
                self.find_the_closest_group(self.points[i])
            for i in range(len(self.groups)):
                self.recalculate_group_position(self.groups[i])
            
        
