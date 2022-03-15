def main_routine():
    dog_count = 0
    drop_off = input("Are you here to drop off a dog? (Y/N): ").upper()
    while drop_off != "N":
        drop_off = sell_spot()


def sell_spot():
    confrim = input("Will you like to check in your dog for today? Cost is $15.00 (Y/N): ").upper()
    if confrim != "N":
        name_of_dog = input("What is your dogs name? ")













#main function
print("-----------DogsRus Booking Service-----------")
main_routine()


