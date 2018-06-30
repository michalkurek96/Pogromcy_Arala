import funkcje as f

N = 100
matrix = f.random_matrix_of_numbers(N)
#for i in range (N):
    #print(matrix[i])
for n in range (255):
    print('n=', n)
    if(f.RK_sprListaPozioma(matrix)==1):
        if(f.RK_sprListaPozioma(matrix)==1):
            break
    if(n%2==0):
        f.Normalizacja(matrix, N, True)
    else:
        f.Normalizacja(matrix, N, False)

#for i in range (N):
    #print(matrix[i])
#f.WypiszWektorSum(matrix, N, True)
#f.WypiszWektorSum(matrix, N, False)
