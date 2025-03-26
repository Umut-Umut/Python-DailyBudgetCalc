from DB import *
from datetime import date


# constants
BUTCE = 1
GUN = 0


butce : float = 0
gun : int = 0
kalan_gun : int = 0


def main():
    # Initialize the database
    db = init()

    # Main loop
    global butce, gun, kalan_gun
    while True:
        # Print the values
        print("#" * 20, "Gunluk Butce Calculator")
        print("Butce : ", butce)
        print("Kalan Gun : ", kalan_gun)
        print("Gunluk Butce : ", butce / kalan_gun)
        
        print("1.Bilgileri Guncelle")
        print("2.Cikis")
        
        # Get the user's choice
        secim = input("Secim : ")
        if secim.isdigit():
            secim = int(secim)
            if secim == 1:
                # Get the new values from the user
                print("#" * 20, "Yeni Bilgileri Girin")
                values = get_values()
                butce = values[BUTCE]
                gun = values[GUN]

                db.update_values(gun, butce, 0)

                init()
            elif secim == 2:
                # Exit the program
                break


def init() -> DB:
    db = DB("main")
    db.create_table()

    # Get the values from the database
    global butce, gun, kalan_gun
    values = db.get_values()
    if not values:
        # If there is no values in the database, get the values from the user
        print("No values found!")
        values = get_values()
        butce = values[BUTCE]
        gun = values[GUN]

        db.insert_values(gun, butce, 0)
    else:
        # If there is values in the database, get the values from the database
        gun = values[GUN]
        butce = values[BUTCE]

    # Calculate the remaining days
    bugun = date.today()
    if bugun.day > gun:
        gelecek = date(bugun.year, bugun.month + 1, gun)
    else:
        gelecek = date(bugun.year, bugun.month, gun)
    
    kalan_gun = (gelecek - bugun).days

    return db


def get_values() -> list:
    values : list = [0, 0]

    def get_butce():
        nonlocal values

        inp : str = input("Butce : ")
        if inp.isdigit():
            values[BUTCE] = float(inp)
            return True
        else:
            print("Please enter a number!")
            return False
                    
    def get_day():
        nonlocal values

        inp : str = input("Gun : ")
        if inp.isdigit():
            values[GUN] = int(inp)
            return True
        else:
            print("Please enter a number!")
            return False

    while True:
        if get_butce():
            if get_day():
                return values


if __name__ == "__main__":
    main()