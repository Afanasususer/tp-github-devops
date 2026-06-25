utilisateurs = []

def ajouter_utilisateur(nom, email):
    utilisateurs.append({"nom": nom, "email": email})
    return utilisateurs

def chercher_utilisateur(email):
    return next((u for u in utilisateurs if u["email"] == email), None)
