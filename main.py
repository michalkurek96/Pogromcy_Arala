import funkcje as f

N = 4
matrix = f.random_matrix_of_numbers(N)
for n in range (255):
    if(f.RK_sprListaPozioma(matrix)==1):
        if(f.RK_sprListaPozioma(matrix)==1):
            break
    if(n%2==0):
        f.normalizacja(matrix, N, true)
    else:
        f.normalizacja(matrix, N, false)

print(matrix)
