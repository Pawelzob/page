

def print_seats(seats : list): #funkcja pokazuje wolne i zajete miejsca
    j = 1
    for i in seats:
        if i==None:
            print(f"{j} Wolne")
        else:
            print(f"{j} Zajete przez {i}")
        j +=1
    
def add_reservation(seats : list): # funkcja dodaje rezerwacje do wybranych miejsc
    try:
        #uzytkownik podaje miejsce i imie ktore chce zarezerwowac
        imie = str(input("Podaj imie: "))
        numer = int(input("Podaj numer miejsca: "))
       
       # sprawdzanie czy numer nie jest wiekszy od 10 i miejszy od 1
        if numer >10 or numer<1:
            print("Numer jest po za zakresem (1-10)")
            return seats
        #dodawanie imienia do listy
        if seats[numer-1] is None:
            seats[numer-1]=imie
            print("")
            print(f"Miejsce zostało zajete przez {imie} na numerze {numer}")
              #niepowodzenie dodawania     
        else:
            print("Zajete")
            return seats
    except ValueError:
            print("Prosze podac prawidlowy numer ")
    
            
def remove_reservation(seats : list):    # funkcaj usuwa zarezerwowane miejsce 
        try: 
             #wprowadzanie numeru ktore chce sie zmienic
            numer = int(input("Podaj numer miejsca które chcesz usunąć: "))
             # sprawdzanie czy numer nie jest wiekszy od 10 i miejszy od 1
            if numer >10 or numer<1:
                print("Numer jest po za zakresem (1-10)")
                return seats
                #usuwanie uzytkowanika z wybranego miejsca
            if seats[numer-1] is not None:
                seats[numer-1] = None
                print("Rezerwacja została usunieta")
                return seats
            #sprawdzanie czy miejsca ma rezerwacje
            else:
                print("Miejsce nie ma rezerwacji")
                return seats
        except ValueError:
            print("Prosze podac prawidlowy numer ")
        

def modify_rezervation(seats : list): # modyfikacja zarezerwowanego miejsca
        try:
            #wprowadzanie numeru ktore chce sie zmienic
            numer = int(input("Podaj numer miejsca które chcesz zmienić: "))

            #dodałem zmienna ktora przechowuje imie wybranego miejsca
            reservation = seats[numer -1]

            # sprawdzanie czy numer nie jest wiekszy od 10 i miejszy od 1
            if numer >10 or numer<1:
                print("Numer jest po za zakresem (1-10)")
                return seats
            
                #sprawdzanie czy miejsce jest wolne
            if seats[numer -1] is None:
                print("Miejsce jest wolne")
                return seats
            
            else:# usuwanie starego miejsca
                seats[numer -1] = None

            #uzytkownik wprowadza nowy numer miejsca
            new_number = int(input("Podaj nowy numer miejsca: ")) 
            if seats[new_number-1] is None:

                #zapis nowej rezerwacji
                seats[new_number-1]= reservation
                print("Miejsce zostało zmienione")
                return seats
            
            else:#niepowodzenie jezeli miejsce bylo juz wczesniej zajete
                print("Te miejce jest zajete")
                return seats
        
        except ValueError:
            print("Prosze podac prawidlowy numer ")
        

def check_availability(seats:list): #Sprawdzanie dostepnosci wielu miejsc
    try:
            #ile chcesz prowadzic numerow
        ile_numerow  = int(input("Ile chcesz sprawdzic numerów: "))

            #uzytkownik wprowadza wybrane numery 
        for _ in range(ile_numerow):
            number = int(input("Podaj wybrane numery: "))
            
            
           #wypisywanie wybranych miejsc
            if seats[number-1] is None:
                print(f"Miejsce {number} wolne")
            else: print(f"Miejsce zajete przez: ",seats[number-1])
        

    except ValueError:
            print("Prosze podac prawidlowy numer ")

def add_multiple_reservations(seats: list):  # Funkcja pozwala na dodawanie wielu rezerwacji
    try:
        while True:
            ile_miejsc = int(input("Ile miejsc chcesz zarezerwować: "))

            for i in range(ile_miejsc):
                while True:  # Pętla, aby powtarzać wprowadzanie numeru miejsca, jeśli jest zajęte
                    numer = int(input(f"Podaj numer miejsca {i + 1}: "))
                    if seats[numer - 1] is None:
                        imie = str(input("Podaj imię: "))
                        seats[numer - 1] = imie
                        break  # Wyjście z pętli, gdy miejsce zostanie poprawnie zarezerwowane
                    else:
                        print("To miejsce jest zajęte, wprowadź inne.")

            # Opcjonalnie: zapytaj, czy użytkownik chce dokonać kolejnych rezerwacji
            kontynuuj = input("Czy chcesz dokonać kolejnych rezerwacji? (tak/nie): ").lower()
            if kontynuuj != "tak":
                break

    except ValueError:
        print("Wprowadziłeś nieprawidłowe dane. Spróbuj ponownie.")
    except IndexError:
        print("Podałeś numer miejsca spoza zakresu. Spróbuj ponownie.")

def cancel_all_reservations(seats: list):
    imie = input("Podaj swoje imię, aby anulować wszystkie rezerwacje: ")

    # Przechodzimy przez listę miejsc i usuwamy rezerwacje przypisane do podanego imienia
    anulowane = 0
    for i in range(len(seats)):
        if seats[i] == imie:
            seats[i] = None  # Anulowanie rezerwacji
            anulowane += 1

    if anulowane > 0:
        print(f"Wszystkie rezerwacje dla {imie} zostały anulowane.")
    else:
        print(f"Nie znaleziono żadnych rezerwacji dla {imie}.")


def save_seats_to_file(seats: list):
    with open('kino.csv', 'wt') as plik_zapis:
        seats = ["wolne" if element is None else element for element in seats]
        for idx, seat in enumerate(seats, 1):  # zaczynamy numerację od 1
            plik_zapis.write(f"{idx}. {seat}\n")

            
def load_seats_from_file():
    seats=[]
    try:
        with open('kino.csv', 'rt') as plik_odczyt:
            for line in plik_odczyt:
                # Usuwamy ewentualne białe znaki na końcu i dzielimy linie na numer i stan
                _, status = line.strip().split('. ', 1)
                seats.append(None if status == "wolne" else status)
    except FileNotFoundError:
        print("Plik 'kino.csv' nie istnieje. Tworzę nowy.")
        seats = [None]*10
    return seats
     
   

          
    
        

           

  





def main(): #funkcja ktora robi za menu aplikacji
     seats = load_seats_from_file()
     while True: # petla wyswietlajaca menu
        print("\nMenu:")
        print("1. Wyświetl miejsca")
        print("2. Zarezerwuj miejsce")
        print("3. Usun rezerwacje")
        print("4. Modyfikuj miejsce")
        print("5. Wyjscie z programu")
        print("6. Sprawdzanie dostepnosci wielu miejsc")
        print("7. Dodawanie wielokrotnej rezerwacji")
        print("8. Anulowanie wszystkich rezerwacji")

            #tutaj uzytkownik wprowadza numer (1-5) i wykonuje sie wybrana funkcja
        try:
           
            
            choice = int(input("Wybierz opcje: "))
            if choice == 1:
                print_seats(seats)             
            elif choice == 2 :
                add_reservation(seats)
            elif choice ==3:
                remove_reservation(seats)
            elif choice == 4:
                modify_rezervation(seats)
            elif choice == 5:
                print("Koniec programu")
                break
            elif choice ==6:
                check_availability(seats)
            elif choice ==7:
                 add_multiple_reservations(seats)
            elif choice == 8:
                cancel_all_reservations(seats)
            elif choice == 9:
                save_seats_to_file(seats)
                
            #obsługa błedów
            else:
                print("Nieprawidłowy wybór. Sprobuj ponownie")
            save_seats_to_file(seats)
        except ValueError:
            print("Prosze podac prawidlowy numer opcji (1-5)")

if __name__ == "__main__":
    main()



          
        




