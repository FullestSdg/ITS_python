nord_sud:int = int(input("Inserisci il numero di veicoli che arrivano da nord/sud: "))
est_ovest:int = int(input("Inserisci il numero di veicoli che arrivano da est/ovest: "))

soglia:int = 70

if nord_sud > soglia and est_ovest > soglia:
    time_ns = 50
    time_eo = 50

    print(f"Il tempo assegnato a nord_sud è: {time_ns}\nIl tempo assegnato a est_ovest è: {time_eo}")

elif nord_sud > soglia:
    time_ns = 60
    time_eo = 40

    print(f"Il tempo assegnato a nord_sud è: {time_ns}\nIl tempo assegnato a est_ovest è: {time_eo}")

elif est_ovest > soglia:
    time_ns = 40
    time_eo = 60

    print(f"Il tempo assegnato a nord_sud è: {time_ns}\nIl tempo assegnato a est_ovest è: {time_eo}")

else:
    time_ns = (nord_sud / (nord_sud + est_ovest)) * 100
    time_eo = (est_ovest / (nord_sud + est_ovest)) * 100

    print(f"Il tempo assegnato a nord_sud è: {time_ns}\nIl tempo assegnato a est_ovest è: {time_eo}")