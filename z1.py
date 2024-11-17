def load_seats_from_file():
    seats = []
    try:
        with open('kino.csv', 'rt') as plik_odczyt:
            for line in plik_odczyt:
                _, status = line.strip().split('. ', 1)
                seats.append(None if status == "wolne" else status)
    except FileNotFoundError:
        print("Plik 'kino.csv' nie istnieje. Tworzę nowy.")
    return seats

def save_seats_to_file(seats: list):
    with open('kino.csv', 'wt') as plik_zapis:
        for idx, seat in enumerate(seats, 1):  # zaczynamy numerację od 1
            seat_status = "wolne" if seat is None else seat
            plik_zapis.write(f"{idx}. {seat_status}\n")

def print_seats(seats: list):
    print("Miejsca:")
    for idx, seat in enumerate(seats, 1):
        status = "wolne" if seat is None else seat
        print(f"{idx}. {status}")

def add_reservation(seats: list):
    try:
        seat_number = int(input("Wybierz numer miejsca do rezerwacji (1-10): "))
        if seats[seat_number - 1] is None:
            seats[seat_number - 1] = "zajęte"
            print(f"Miejsce {seat_number} zostało zarezerwowane.")
        else:
            print(f"Miejsce {seat_number} jest już zajęte.")
    except (ValueError, IndexError):
        print("Nieprawidłowy numer miejsca.")

def remove_reservation(seats: list):
    try:
        seat_number = int(input("Wybierz numer miejsca do usunięcia rezerwacji (1-10): "))
        if seats[seat_number - 1] == "zajęte":
            seats[seat_number - 1] = None
            print(f"Rezerwacja na miejscu {seat_number} została usunięta.")
        else:
            print(f"Miejsce {seat_number} nie jest zarezerwowane.")
    except (ValueError, IndexError):
        print("Nieprawidłowy numer miejsca.")

def modify_reservation(seats: list):
    try:
        seat_number = int(input("Wybierz numer miejsca do modyfikacji (1-10): "))
        if seats[seat_number - 1] == "zajęte":
            new_status = input("Wprowadź nowy status (zajęte/wolne): ")
            if new_status in ["zajęte", "wolne"]:
                seats[seat_number - 1] = new_status if new_status == "zajęte" else None
                print(f"Status miejsca {seat_number} został zmieniony.")
            else:
                print("Nieprawidłowy status.")
        else:
            print(f"Miejsce {seat_number} nie jest zarezerwowane.")
    except (ValueError, IndexError):
        print("Nieprawidłowy numer miejsca.")

def check_availability(seats: list):
    available_seats = [i + 1 for i, seat in enumerate(seats) if seat is None]
    if available_seats:
        print("Dostępne miejsca:", available_seats)
    else:
        print("Brak dostępnych miejsc.")

def add_multiple_reservations(seats: list):
    try:
        seat_numbers = list(map(int, input("Wprowadź numery miejsc do rezerwacji (oddzielone spacją): ").split()))
        for seat_number in seat_numbers:
            if seats[seat_number - 1] is None:
                seats[seat_number - 1] = "zajęte"
                print(f"Miejsce {seat_number} zostało zarezerwowane.")
            else:
                print(f"Miejsce {seat_number} jest już zajęte.")
    except (ValueError, IndexError):
        print("Nieprawidłowe numery miejsc.")

def cancel_all_reservations(seats: list):
    for i in range(len(seats)):
        seats[i] = None
    print("Wszystkie rezerwacje zostały anulowane.")

def main():
    seats = load_seats_from_file()  # Wczytanie stanów z pliku
    while True:
        print("\nMenu:")
        print("1. Wyświetl miejsca")
        print("2. Zarezerwuj miejsce")
        print("3. Usun rezerwacje")
        print("4. Modyfikuj miejsce")
        print("5. Wyjście z programu")
        print("6. Sprawdzanie dostępności wielu miejsc")
        print("7. Dodawanie wielokrotnej rezerwacji")
        print("8. Anulowanie wszystkich rezerwacji")

        try:
            choice = int(input("Wybierz opcję: "))
            if choice == 1:
                print_seats(seats)
            elif choice == 2:
                add_reservation(seats)
            elif choice == 3:
                remove_reservation(seats)
            elif choice == 4:
                modify_reservation(seats)
            elif choice == 5:
                print("Koniec programu")
                break
            elif choice == 6:
                check_availability(seats)
            elif choice == 7:
                add_multiple_reservations(seats)
            elif choice == 8:
                cancel_all_reservations(seats)
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")
            
            # Zapisanie stanu po każdej operacji
            save_seats_to_file(seats)

        except ValueError:
            print("Proszę podać prawidłowy numer opcji (1-8)")

if __name__ == "__main__":
    main()


