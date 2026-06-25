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
