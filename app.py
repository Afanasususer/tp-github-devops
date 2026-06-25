def calculer_imc(poids, taille):
    imc = poids / (taille ** 2)
    if imc < 18.5:
        return imc, "Insuffisance pondérale"
    elif imc < 25:
        return imc, "Poids normal"
    elif imc < 30:
        return imc, "Surpoids"
    else:
        return imc, "Obésité"

def convertir_temperature(valeur, unite):
    if unite.upper() == "C":
        return valeur * 9/5 + 32, "F"
    elif unite.upper() == "F":
        return (valeur - 32) * 5/9, "C"
    else:
        raise ValueError("Unite invalide")

def formater_message(msg, majuscules=False):
    return msg.upper() if majuscules else msg.lower()
