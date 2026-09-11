with open("results.txt", "w") as archivo:

    contador = 0

    for numero in range(1, 251):
        es_primo = True

        if numero == 1:
            es_primo = False
        else:
            for divisor in range(2, numero):
                if numero % divisor == 0:
                    es_primo = False
                    break

        if es_primo:
            print(numero, end=" ")
            archivo.write(str(numero) + " ")
            contador += 1

            if contador == 10:
                print()
                archivo.write("\n")
                contador = 0