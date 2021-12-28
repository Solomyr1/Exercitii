#Putem folosi concatenarea si pentru a lega fraze

print("merg"+ "sa iau mingea cu numarul" + "7")

a = a+1                                              #a=5, deci incrementare. Ne ajuta sa suprascriem
a += 1                                               #aceeasi incrementare

print(f'suma e 1')                                   #cauta peste tot daca e fraza cu numele respectiv
print('numarul ce apare e {}'.format(a))             #face acelasi lucru ca mai sus, dar acoladele si functia o sa caute peste tot

fraza = 1213
print("primul numar", fraza [0])                     #cand vrem sa verificam pozitia a ceva, folosim paranteze patrate
                                                     #folosim 0 pentru ca de acolo incepe numaratoarea,

fraza_1 = "eu merg la mare"
print("substring", fraza_1[0:2])                     #trebuie sa pun 2 in loc de 1, pentru ca el numara ultima - 1
print("substring numere pozitie para", fraza_1[::2])   # "::" = merge pana la final, "::2"=merge pana la final din 2 in 2
print("substring", fraza_1[-3])                      #ne arata al treilea caracter de la final
print("substring numere pozitie para", fraza_1[::-1]) #ne afiseaza tot sirul invers. Sau din 2 in 2 invers [::-2]

fraza_3 = "Emma is good developer. Emma is a writer"
print(fraza_3.find("g"))                               #asa ne arata pozitia pe care e g, nu ne cauta de cate ori e litera

pi = 3.14
R = input("raza cercului este")                        #putem scrie R = int(input("raza cercului este") ca sa definim la inceput
p = 2
print("raza este", float(pi)*float(R))                 #ca sa se poata calcula asa, trebuie sa facem fiecare variabila la fel

assert a==b                                           #functia assert e pentru a verifica diferite lucruri. Folosita de testeri
assert a!=b
in                                                     #cauta daca un string e in alt string
assert a > 18 and a < 55                               #ne spune daca si si sunt adevarate, dar nu ne printeaza, ci doar merge
assert a > 18 or a < 55