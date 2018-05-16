# -*- coding: utf-8 -*-
from Vehicles import Vehicle, add_new_vehicle, list_all_vehicles, edit_number_of_kilometers_or_date_service, delete_vehicle, save_vehicles_in_txt

def main():
    print "Dobrodošl v programu za urejanje vaših avtomobilov"
    print ""

    vehicles = []
    while True:
        print ""
        print "Izberite opcijo:"
        print "a) Dodajte novo vozilo"
        print "b) Ogled seznama vozil"
        print "c) Uredite število prevoženih kilometrov ali datum servisa."
        print "d) Izbrišite vozilo iz seznama."
        print "e) Shrani vozila v txt datoteko."
        print ""
        selection = raw_input("Izberite opcijo (a, b, c, d or e): ")
        print ""

        if selection.lower() == "a":
            add_new_vehicle(vehicles)
        elif selection.lower() == "b":
            list_all_vehicles(vehicles)
        elif selection.lower() == "c":
            if not vehicles:
                print "Nimate vozil v vašem seznamu."
            else:
                edit_number_of_kilometers_or_date_service(vehicles)
        elif selection.lower() == "d":
            if not vehicles:
                print "Nimate vozil v vašem seznamu."
            else:
                delete_vehicle(vehicles)
        elif selection.lower() == "e":
            save_vehicles_in_txt(vehicles)
        else:
            print "Niste izprali pravilne opcije. Poskusite ponovno"

if __name__ == "__main__":
    main()
