import numpy as np
import random 
def get_random(n):
    a = []
    max_number = 20
    for i in range (n):
        temp = []
        for j in range (n):
            temp.append(max_number*random.random())
        a.append(temp)
    print(a)

get_random(2)
