minuto = 10
segundo = 59

print("10 : 00")


while minuto > 0:
    minuto -= 1
    segundo = 59
    while segundo >= 0:
        print(minuto, ":", str(segundo).zfill(2))
        segundo -= 1
