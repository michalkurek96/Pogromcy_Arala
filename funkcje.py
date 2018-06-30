import numpy as np

RK_epsilon=0.000001
# wykorzystywana do sprawdzania macierzy w postaci array
def RK_sprMacierzPionowa(macierz):
	suma=0
	i=0
	j=0
	czy_zno=1	#czy_znormalizowana
	size=macierz.shape[0]	# macierz kwadratowa - nie ma znaczenia, ktory wymiar wybiore
	while(i<size and czy_zno):
		suma=0
		while(j<size):
			suma=suma+macierz[j][i]		# kolejnosc [numer wiersza][numer kolumny]
			j=j+1	# nie wiem czy dziala j++
		if(suma-1>RK_epsilon):
			czy_zno=0
		i=i+1	# nie wiem czy dziala i++
	return czy_zno
# wykorzystywana do sprawdzania macierzy w postaci array
def RK_sprMacierzPozioma(macierz):
	suma=0
	i=0
	j=0
	czy_zno=1	#czy_znormalizowana
	size=macierz.shape[0]	# macierz kwadratowa - nie ma znaczenia, ktory wymiar wybiore	
	while(i<size and czy_zno):
		suma=0
		while(j<size):
			suma=suma+macierz[i][j]		# kolejnosc [numer wiersza][numer kolumny]
			j=j+1	# nie wiem czy dziala j++
		if(suma-1>RK_epsilon):
			czy_zno=0
		i=i+1	# nie wiem czy dziala i++
	return czy_zno

# sprawdzenie dlugosci listy
def RK_dlugoscListy(listaList):
	i=0
	for j in listaList:
		i=i+1
	return i
	
# wykorzystywana do sprawdzania macierzy w postaci listy
def RK_sprListaPionowa(listaList):
	suma=0
	i=0
	j=0
	czy_zno=1	#czy_znormalizowana
	size=RK_dlugoscListy(listaList)	# macierz kwadratowa - nie ma znaczenia, ktory wymiar wybiore
	while(i<size and czy_zno):
		suma=0
		while(j<size):
			suma=suma+listaList[j][i]		# kolejnosc [numer wiersza][numer kolumny]
			j=j+1	# nie wiem czy dziala j++
		if(suma-1>RK_epsilon):
			czy_zno=0
		i=i+1	# nie wiem czy dziala i++
	return czy_zno
# wykorzystywana do sprawdzania macierzy w postaci array
def RK_sprListaPozioma(listaList):
	suma=0
	i=0
	j=0
	czy_zno=1	#czy_znormalizowana
	size=RK_dlugoscListy(listaList)	# macierz kwadratowa - nie ma znaczenia, ktory wymiar wybiore
	while(i<size and czy_zno):
		suma=0
		while(j<size):
			suma=suma+listaList[i][j]		# kolejnosc [numer wiersza][numer kolumny]
			j=j+1	# nie wiem czy dziala j++
		if(suma-1>RK_epsilon):
			czy_zno=0
		i=i+1	# nie wiem czy dziala i++
	return czy_zno


import random 
def random_matrix_of_numbers(n):
    matrix = []
    max_number = 20
    for i in range (n):
        temp = []
        for j in range (n):
            temp.append(max_number*random.random())
        matrix.append(temp)
    return matrix

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
        return matrix

		
# Dominik
def Normalizacja(MacierzLiczb, WymiarN, CzyWiersz: bool):
	for Ix1 in range(0,WymiarN):			# dla każdego wrs/kol
		if CzyWiersz: 
			# Obliczanie sumy
			Suma = sum(MacierzLiczb[Ix1])
			# Dzielenie przez sumę
			for Ix2 in range(0,WymiarN):		# dla każdego elementu
				MacierzLiczb[Ix1][Ix2] /= Suma		
		else:
			# Obliczanie sumy
			Suma=0
			for Ix2 in range(0,WymiarN):
				Suma+=MacierzLiczb[Ix1][Ix2]
			# Dzielenie przez sumę
			for Ix2 in range(0,WymiarN):		# dla każdego elementu
				MacierzLiczb[Ix2][Ix1] /= Suma		
				
def WypiszWektorSum(MacierzLiczb, WymiarN, CzyWiersz: bool):
	for Ix1 in range(0,WymiarN):
		if CzyWiersz:
			print(sum(MacierzLiczb[Ix1]))
		else:
			Suma=0
			for Ix2 in range(0,WymiarN):
				Suma+=MacierzLiczb[Ix1][Ix2]
			print(Suma)