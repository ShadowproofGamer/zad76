plik1 = open("szyfr1.txt")
dane1=plik1.read().strip('\n').split()
klucz1 = []
for i in dane1[6::]:
    klucz1.append(int(i))
    dane1.remove(i)
plik1.close()

plik2 = open("szyfr2.txt")
dane2=plik2.read().strip().split()
klucz2 = []
for j in dane2[1::]:
    klucz2.append(int(j))
    dane2.remove(j)
plik2.close()

plik3 = open("szyfr3.txt")
dane3=plik3.read().strip().split()
plik3.close()

#print(dane1, klucz1, dane2, klucz2, dane3)



def szyfrowanie(slowo1, klucz):
    slowo_temp = []
    local_wynik = ''
    for ij in slowo1:
        slowo_temp.append(ij)

    for ii in range(0, len(slowo_temp), 1):
        temp = slowo_temp[ii]
        slowo_temp[ii] = slowo_temp[klucz[ii % (len(klucz))]-1]
        slowo_temp[klucz[ii % (len(klucz))]-1] = temp

    for ik in slowo_temp:
        local_wynik+=ik

    return local_wynik

def deszyfr(slowo, klucz):
    klucz*=10
    temp_klucz = []
    temp_wynik = ''
    slowo_temp = []
    for ii in range(len(slowo)):
        temp_klucz.append(klucz[ii])
    print(temp_klucz, len(slowo))
    print(slowo)
    for ij in slowo:
        slowo_temp.append(ij)
    for ik in range(len(slowo_temp)-1, -1, -1):

        temp = slowo_temp[ik]
        slowo_temp[ik] = slowo_temp[temp_klucz[ik]-1]
        slowo_temp[temp_klucz[ik]-1] = temp

    for il in slowo_temp:
        temp_wynik+=il

    return temp_wynik


wynik1 = open("wyniki_szyfr_1.txt", 'w+')
for k in dane1:
    wynik1.write(szyfrowanie(k, klucz1) + '\n')

wynik2 = open("wyniki_szyfr_2.txt", "w+")
wynik2.write(szyfrowanie(dane2[0], klucz2)+'\n')

wynik3 = open("wyniki_szyfr_3.txt", "w+")
wynik3.write(deszyfr(dane3[0], [6, 2, 4, 1, 5, 3]))



