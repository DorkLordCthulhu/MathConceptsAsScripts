import math

class PrimeCounter:
    def __init__(self, max_number):
        self.max_num = max_number
        self.prime_set = []
        # self.number_set is a Bool list where all==True and it's length==max. By the end, only Primes will still==True
        self.number_set = [True for i in range(self.max_num+1)]

#This takes all numbers from 2 to square route of your max, and looks for their multiples, starting with the lowest
#value, 2. if a number is a multiple, it's value in self.number_set is changed to False. After it finds all that
#number's multiples, it moves on to the next lowest number that still==True.
    def prime_sniffer(self):
        square_root_max = int(math.sqrt(self.max_num))
        for i in range(2, (square_root_max+1)):
            if self.number_set[i]:
                multiple_of_target = pow(i, 2)
                while multiple_of_target <= self.max_num:
                    self.number_set[multiple_of_target] = False
                    multiple_of_target += i

#This looks through number_set after only prime numbers == True. If it's a prime, it pulls their index spot into a new
#list, giving us the number of primes found, as well as their values
    def list_primes(self):
        for i in range(2, len(self.number_set)):
            if self.number_set[i]==True:
               self.prime_set.append(i)
        return f"There are {len(self.prime_set)} prime numbers between 2 and {self.max_num}. They are {self.prime_set}."


if __name__ == '__main__':
    max = 100000
    x = PrimeCounter(max)
    x.prime_sniffer()
    print(x.list_primes())
