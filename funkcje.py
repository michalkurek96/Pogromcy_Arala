import random 
def random_matrix_of_numbers(n):
    a = []
    max_number = 20
    for i in range (n):
        temp = []
        for j in range (n):
            temp.append(max_number*random.random())
        a.append(temp)
    print("nasza macierz liczb:")
    print(a)

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
    print("nasza macierz macierzy:")
    print(matrix)

random_matrix_of_numbers(2)
random_matrix_of_matrix(2, 2)
