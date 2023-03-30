# assert 10 > 5 # 10 er større enn 5, derfor gjør denne ingenting

# try:
#     assert 10 > 20 # 10 er ikke større enn 20, derfor gir denne en feilmeldig
# except:
#     print("Hei på deg!")

while True:
    try:
        hoyde = int(input("Høyde: "))
        bredde = int(input("Bredde: "))
        break
    except:
        print("Feil: legg inn lengdene i form av heltall, prøv igjen.")

def areal(hoyde, bredde):
    return hoyde * bredde
def omkrets(hoyde, bredde):
    return hoyde + hoyde + bredde + bredde

print(f"Arealet av rektangelet er: {areal(hoyde, bredde)}")


# assert areal(3,2) == 6
# assert areal(3,3) == 9
# assert areal(3,4) == 12
# assert omkrets(3,2) == 10
# assert omkrets(3,3) == 12
# assert omkrets(3,4) == 14




# print("Koden er ferdig")

