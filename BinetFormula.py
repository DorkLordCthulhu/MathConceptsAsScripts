import math

class Fibonacci:
    def __init__(self, target):
        self.target = target

#This usses the Binet formula to calculate and specified place in the fibonacci sequence
    def findfibplace(self):
        a = math.sqrt(5)
        b = pow(((1+a)/2),self.target)
        c = pow(((1-a)/2), self.target)
        result = (1/a)*(b-c)
        return result


if __name__ == '__main__':
    targetednumber = int(input("Welcome to the Binet Formula via python. What place are you searching for?"))
    x = Fibonacci(targetednumber)
    print (f"{x.findfibplace()} is number {targetednumber} in the fibonacci sequence")
