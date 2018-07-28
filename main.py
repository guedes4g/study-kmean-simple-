from genereateRandomPoints import generate
from kmean import Kmean
from plot import plot
'''
points = generate(number=3)
km = Kmean(points = points)
for i in range(len(km.groups)):
    print(km.groups[i].__dict__)
'''
def main():
    points = generate(number=30, t = 10000000)
    km = Kmean(points = points, groups=3)
    for i in range(len(km.groups)):
        print(km.groups[i].__dict__)
    plot(km)

if __name__ == "__main__":
    main()