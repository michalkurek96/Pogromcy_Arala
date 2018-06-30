import numpy as np
import random 
def random_matrix_of_numbers(n):
    a = []
    max_number = 20
    for i in range (n):
        temp = []
        for j in range (n):
            temp.append(max_number*random.random())
        a.append(temp)
    print(a)

def random_matrix_of_matrix(n):
    

random_matrix_of_numbers(2)
