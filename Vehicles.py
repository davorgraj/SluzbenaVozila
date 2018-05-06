# -*- coding: utf-8 -*-
class Vehicle(object):

    def __init__(self, vehicle_brand, vehicle_model, number_of_kilometers, date_service):
        self.vehicle_brand = vehicle_brand
        self.vehicle_model = vehicle_model
        self.number_of_kilometers = number_of_kilometers
        self.date_service = date_service

    def get_vehicle_full_name(self):
        return self.vehicle_brand + " " + self.vehicle_model


def add_new_vehicle(vehicles):
    vehicle_brand = raw_input("Vpišite znamko vozila: ")
    vehicle_model = raw_input("Vpišite model vozila: ")
    number_of_kilometers = raw_input("Vpištite prevožene kilometre: ")
    date_service = raw_input("Vpišite datum servisa: ")

    new_vehicle = Vehicle(vehicle_brand=vehicle_brand, vehicle_model=vehicle_model, number_of_kilometers=number_of_kilometers, date_service=date_service)
    vehicles.append(new_vehicle)

    print "Vozilo " + vehicle_brand + " ste uspešno dodali na vaš seznam."


def list_all_vehicles(vehicles):

    for key, vehicle in enumerate(vehicles):
        print "Znamka vozila: " + vehicle.vehicle_brand
        print "Model vozila: " + vehicle.vehicle_model
        print "Prevoženi kilometri: " + vehicle.number_of_kilometers
        print "Datum servisa: " + vehicle.date_service
        print ""
    if not vehicles:
        print "Nimate vozil v vašem seznamu"
        print ""


def edit_number_of_kilometers_or_date_service(vehicles):
    while True:
        print "Kaj želite urediti?"
        print "a) Število kilometrov"
        print "b) Datum servisa"
        print "c) Izhod iz urejevalnika"

        selection = raw_input("Izberite opcijo (a, b ali c): ")

        if selection.lower() == "a":
            for index, vehicle in enumerate(vehicles):
                print "ID: " + str(index) + " - " + vehicle.get_vehicle_full_name()

            print ""
            selected_vehicle_id = raw_input("Vpišite ID vozila: ")
            selected_vehicle = vehicles[int(selected_vehicle_id)]

            print ""
            new_number_of_kilometers = raw_input("Vnesite novo število kilometrov %s: " % selected_vehicle.get_vehicle_full_name())
            selected_vehicle.number_of_kilometers = new_number_of_kilometers

            print ""
            print "Uspešno posodobljeno!"

        if selection.lower() == "b":
            for index, vehicle in enumerate(vehicles):
                print "ID: " + str(index) + " - " + vehicle.get_vehicle_full_name()

            print ""
            selected_vehicle_id = raw_input("Vpišite ID vozila: ")
            selected_vehicle = vehicles[int(selected_vehicle_id)]

            print ""
            new_date_service = raw_input("Vnesite novo število kilometrov %s: " % selected_vehicle.get_vehicle_full_name())
            selected_vehicle.date_service = new_date_service

            print ""
            print "Uspešno posodobljeno!"

        elif selection.lower() == "c":
            break
        else:
            continue


def delete_vehicle(vehicles):
    print "Izberite ID vozila ki ga želite izbrisati:"

    for index, vehicle in enumerate(vehicles):
        print "ID: " + str(index) + " - " + vehicle.get_vehicle_full_name()

    print ""
    selected_vehicle_id = raw_input("Vpišite ID vozila: ")
    selected_vehicle = vehicles[int(selected_vehicle_id)]

    vehicles.remove(selected_vehicle)
    print ""
    print "Avtomobil uspešno izbrisan!"


vehicles = []


def save_vehicles_in_txt(vehicles):
    text_file = open("vehicles.txt", "w+")
    for vehicle in vehicles:
        text_file.write("Znamka: " + vehicle.vehicle_brand + "\n")
        text_file.write("Model: " + vehicle.vehicle_model + "\n")
        text_file.write("Število prevoženih kilometrov: " + vehicle.number_of_kilometers + "\n")
        text_file.write("Datum servisa: " + vehicle.date_service + "\n")
        text_file.write("\n")
    text_file.close()
    print "Uspešno shranjeno!"