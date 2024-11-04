animal = "cat"
match animal:
    case "dog":
        print("hał hał")
    case "cat":
        print("miał miał")
    case _:
        print("zwierze nie znane!")

def tuple_info(data):
    match data:
        case(x,y):
            print(f"Tuple 2 elementowy: {x}, {y}")
        case(x,y,z):
            print(f"tuple 3 ele,amtowy: {x}, {y}, {z}")
        case _:
            print("Nie znany rozmiar tuple")

tuple_info((1,2))
tuple_info((5,6,7))

def number_category(n):
    match n:
        case x if x< 0:
            return "Wartosc ujemna"
        case x if x == 0:
            return "zero"
        case x if x>0:
            return "wartosc wieksza od zero"

print(number_category(3))
wartosc = number_category(0)
print(wartosc)
print(number_category(-5))
