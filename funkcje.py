import random 
def random_matrix_of_numbers(n):
<<<<<<< HEAD
    a = []
=======
    matrix = []
>>>>>>> master
    max_number = 20
    for i in range (n):
        temp = []
        for j in range (n):
            temp.append(max_number*random.random())
<<<<<<< HEAD
        a.append(temp)
=======
        matrix.append(temp)
    return matrix
>>>>>>> master

def random_matrix_of_matrix(n, N):
    max_number = 20
    matrix = []
    for i in range (N):
        temp = []
        for j in range (N):
            small_matrix = []
            for k in range(n):
                temp2 = []
                for l in range(n):
                    temp2.append(max_number*random.random())
                small_matrix.append(temp2)
            temp.append(small_matrix)
        matrix.append(temp)
<<<<<<< HEAD
=======
        return matrix
>>>>>>> master

