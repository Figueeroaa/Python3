while True:

    n = int(input("Introduce tu numero:\n "))
    if n < 2:
        print(n, "No es un numero primo.")
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                print(n, "No es un numero primo.")
                break
        else:
            print(n, "si es un numero primo.")