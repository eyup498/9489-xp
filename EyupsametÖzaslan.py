# Su hali programı
for derece in range(-5, 136, 5):
    if derece == -5:
        print(f"Derece {derece} : su KATI haldedir.")
    elif derece == 0:
        print(f"Derece {derece} : su SIVI+KATI haldedir.")
    elif 0 < derece <= 100:
        print(f"Derece {derece} : su SIVI haldedir.")
    elif derece == 100:
        print(f"Derece {derece} : su SIVI+GAZ haldedir.")
    else:
        print(f"Derece {derece} : su GAZ haldedir.")
