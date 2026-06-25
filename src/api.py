utilisateurs = []

def ajouter_utilisateur(nom, email):
    utilisateurs.append({"nom": nom, "email": email})
    return utilisateurs

def chercher_utilisateur(email):
    return next((u for u in utilisateurs if u["email"] == email), None)

def supprimer_utilisateur(email):
    global utilisateurs
    utilisateurs = [u for u in utilisateurs if u["email"] != email]
    return utilisateurs
