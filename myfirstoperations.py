# Python Rekenmachine maken.
while True:
        print("Rekenmachine")

        print("Selecteer a.u.b. operations")
        print("1. plus")
        print("2. aftrekken")
        print("3. keer")
        print("4. delen")

# Neem input van de gebruiker
        select = int(input("kies de operations form: "))

        number1 = int(input("Type hier eerste nummer: "))
        number2 = int(input("Type hier de tweede nummer: "))

        if select == 1:
            print(number1 + number2)

        elif select == 2:
            print(number1 - number2)
    
        elif select == 3:
            print(number1 * number2)
    
        elif select == 4:
            print(number1 / number2)
        else:
            print("Invalid input")



