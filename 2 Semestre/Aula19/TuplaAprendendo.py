sports = ("Futebol","Vôlei","Basquete","Golf", "Judô", "Beisebol","Poker")
i = 0

print("PRINT USANDO WHILE")
while i < len(sports):
    print(sports[i])
    i = i + 1

print("\n\nPRINT USANDO FOR")
for c in sports:
    print(c)