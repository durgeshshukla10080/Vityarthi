# Car Parking Management System
# My first semester python project

total_slots = 10
rate_per_hour = 20

# this dictionary stores car number and owner name
parked_cars = {}


def park_car():
    if len(parked_cars) >= total_slots:
        print("Sorry, parking is full!")
        return

    car_number = input("Enter car number: ").upper()

    if car_number in parked_cars:
        print("This car is already parked!")
        return

    owner = input("Enter owner name: ")
    parked_cars[car_number] = owner
    print("Car parked successfully!")
    print("Slots left:", total_slots - len(parked_cars))


def remove_car():
    car_number = input("Enter car number: ").upper()

    if car_number not in parked_cars:
        print("Car not found!")
        return

    hours = int(input("How many hours was the car parked? "))
    bill = hours * rate_per_hour

    print("Owner:", parked_cars[car_number])
    print("Total bill: Rs", bill)

    del parked_cars[car_number]
    print("Car removed. Thank you!")


def show_cars():
    if len(parked_cars) == 0:
        print("No cars in parking.")
        return

    print("\nCars currently parked:")
    count = 1
    for car in parked_cars:
        print(count, ".", car, "-", parked_cars[car])
        count = count + 1


def search_car():
    car_number = input("Enter car number to search: ").upper()

    if car_number in parked_cars:
        print("Car is parked. Owner is", parked_cars[car_number])
    else:
        print("Car is not in the parking.")


def show_slots():
    print("Total slots:", total_slots)
    print("Filled slots:", len(parked_cars))
    print("Empty slots:", total_slots - len(parked_cars))


# main program
print("===== CAR PARKING MANAGEMENT =====")

while True:
    print("\n1. Park a car")
    print("2. Remove a car")
    print("3. Show all cars")
    print("4. Search a car")
    print("5. Check empty slots")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        park_car()
    elif choice == "2":
        remove_car()
    elif choice == "3":
        show_cars()
    elif choice == "4":
        search_car()
    elif choice == "5":
        show_slots()
    elif choice == "6":
        print("Thank you for using the system. Bye!")
        break
    else:
        print("Wrong choice, try again.")