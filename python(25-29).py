# list comprehension

liste = [1,2,3,4,5,6,7]

liste.append(8)


liste2 = []

for i in liste:
    
    liste2.append(i*2)
    
    
liste3 = [i for i in liste]
liste4 = [i*3 for i in liste]

liste5 = [0 if i == 2 else 1 for i in liste]

liste6 = [5 if i < 5 else 10 for i in liste]

liste7 = [i for i in range(1,21) if i % 2 != 0]

liste8 = [i for i in range(1,21) if i % 3 == 0]

liste9 = []

for i in range(1,51):
    
    if i % 2 == 0:
    
        liste9.append(i)



# Function

# f(x) = 2*x +5

#f(5)

a = 5
cıktı = 2*a + 5

b = 10
cıktı2 = 2*b + 5


def islem(x):
    
    print(2*x + 5)
    
    
    
islem(5)
islem(10)

# f(x,y) = x +y

def topla(x,y):
    
    print("Toplamlari : ",x+y)
    
    
topla(32,45)

def ulke_ismi(ulke):
    
    print("I am from " + ulke)
    
ulke_ismi("Turkey") 
ulke_ismi("germany") 

   
# return

def islem(x):
    
    #print(2*x + 5)
    print("Merhaba")
    return (2*x + 5)
    #print("Merhaba")
    
a = islem(4)
print(a)

def iki_ile_carp(x):
    
    return 2*x

iki_ile_carp(6)

iki_ile_carp(islem(3))


def ad():
    
    x = input("Ad giriniz:")
    return x

ad()

def ulke_ismi(ulke = "Turkey"):
    
    print("I am from " + ulke)
    
ulke_ismi() 
ulke_ismi("germany")


def topla(x,y):
    
    print("Toplamlari : ",x+y)
    
    
topla(5,45,6)


def topla(*x):
    
    toplam = 0
    
    for i in x:
        
        toplam += i
        
    
    print("Toplamlari : ",toplam)

topla(1,2,3,4,5,6,7)

   
# lambda function


def islem(x):
    
    return 2*x + 5

islem(2)

islem2 = lambda x : 2*x + 6

islem2(4)


topla = lambda x,y : x + y

topla(3,5)

carpma = lambda a,b : a*b

carpma(2,7)


son_harf = lambda string_ifade : string_ifade[-1:]

son_harf("ali")
son_harf("ömer")



# global & local değişken

a = 5

def fonk():
    
    b = 3
    
    print(b)
    
    
    
fonk()
print(b)

def fonk2():
    
    global c
    
    c = 7
    
    return c

fonk2()

print(c)


d = 8

def fonk3():
    
    global d
    
    d = 9
    
    return d

fonk3()

print(d)


e = 5

e = 4

f = 4

def fonk4():
    
    f = 2
    
    return f

fonk4()

print(f)





























    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



















