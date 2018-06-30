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
			suma=suma+macierz[j][i]		# kolejnosc [numer wiersza][numer kolumny]
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
			suma=suma+macierz[i][j]		# kolejnosc [numer wiersza][numer kolumny]
			j=j+1	# nie wiem czy dziala j++
		if(suma-1>RK_epsilon):
			czy_zno=0
		i=i+1	# nie wiem czy dziala i++
	return czy_zno