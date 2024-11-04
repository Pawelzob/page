
#funkcja suma , dodawanie dwoch liczb 

def suma(x:float,y:float) ->float:
    return (x+y)


print(suma(2,4))


# pi * r *r
PI = 3.14
def pole_kola(PI:float , r:float) ->float:
    global x
    x =5
    return PI * r *r

print(pole_kola(PI, 5))
print(x)



def witaj(imie:str, powitanie:str = 'siemano') ->str:
    wynik = suma(3,4)
    return f"{powitanie}, {imie}"

print(witaj("Pablo" , "Witaj krolu zloty"))


def silnia(n:int) ->int:
    if n==0:
        return 1
    return n * silnia(n-1)

print(silnia(5))


def pi()->float:
    return 3.14

print(pi())


def suma_wielu(*args:int)->int:
    return sum(args)

print(suma_wielu(5,1,5,2,5,12,5))


#funkcja przekształcajaca celsjusz na fahrenheit

Tfah =9/5
def celcjusz_to_fanhrenheit(C):
    return(C *Tfah +32)

print(celcjusz_to_fanhrenheit(-20))


#funkcja filtrujaca liczby parzyste (we:listam wy:lista)

def filtr_l_parzystych(numbers: list[int])->list[int]:
    return [num for num in numbers if num%2 ==0] 
   

print(filtr_l_parzystych([2,3,4,5]))


