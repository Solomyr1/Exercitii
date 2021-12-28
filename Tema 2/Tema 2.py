#Ex 1
x = 5
y = 10

print("suma este", x+y)

#Ex 2
a = 20                #integer
b = 10.               #float
proiect = "Pytho"     #string

#Ex 3
restanta = 0
notaFinala = 10.0
laborator = "introducere in informatica"

print(type(restanta))
print(type(notaFinala))
print(type(laborator))

#Ex 4
c = 3
d = 4
print(c*d)

#Ex 5 [?]
fraza = "5789"
print("lungimea numarului", len(fraza))
print("primul numar", fraza [0])


#Ex 6 [?] - Ar trebui folosit "in"?
fraza_3 = "Emma is good developer. Emma is a writer"
print(fraza_3.find("Emma"))

#Ex 7 [?]
fraza_1 = "eu merg la mare"
print("lungimea frazei fraza_1 este", len(fraza_1))
print("substring", fraza_1[0:2])

#Ex 8
fraza_2 = "eu merg la mare"
print("lungimea frazei fraza_2 este", len(fraza_2))

#Ex 9 [?]
fraza_4 = "restart"
print(fraza_4.replace("r", "$"))

#Ex 10 [?]
totalMoney = 1000
quantity = 3
price = 450
print("I have f'(total money) so I can buy f'(quantity) football for f'(price) dollars")

#Ex 11
L = input("lungimea dreptunghiului")
print(L)
l = input("latimea dreptunghiului")
print(l)
print("perimentul este", int(L)+int(L)+int(l)+int(l))
print("aria este", int(L)*int(l))

pi = 3.14
R = input("raza cercului este")
p = 2
print("aria este", float(pi)*float(R))

#Ex 12
e = 'foo\'bar'
f = """foo'bar"""
g = "foo'bar"
h = 'foo"bar'

print(e)
print(f)
print(g)
print(h)

#Rezulta ca respunsurile corecte sunt: 'foo\'bar', """foo'bar""", si "foo'bar", iar 'foo'bar’ da direct eroare

#Ex 13
username = input("username is")
password = input("password is")
print("The password for user Paul is", len(password), "characters long")

#Ex 14
o, p, q = input("Enter three names: ").split()
print("First name is: ", o)
print("Second name is : ", p)
print("Last name is : ", q)
print()

#Ex 15
r = 458.541315
print("Original Number: ", r)
print("Formatted Number: "+"{:.2f}".format(r));
print()
