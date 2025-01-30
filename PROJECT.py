import re

def check_password_strength(password):
    strength = 0
    remarks = []

    # Vérification de la longueur
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("🔴 Moins de 8 caractères.")

    # Vérification des chiffres
    if re.search(r'\d', password):
        strength += 1
    else:
        remarks.append("🔴 Aucun chiffre.")

    # Vérification des majuscules
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        remarks.append("🔴 Aucune majuscule.")

    # Vérification des minuscules
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        remarks.append("🔴 Aucune minuscule.")

    # Vérification des caractères spéciaux
    if re.search(r'[@$!%*?&]', password):
        strength += 1
    else:
        remarks.append("🔴 Aucun caractère spécial (@, $, !, %, *, ?, &).")

    # Affichage du résultat
    if strength == 5:
        return "🟢 Mot de passe fort !"
    elif 3 <= strength < 5:
        return "🟡 Mot de passe moyen. " + " ".join(remarks)
    else:
        return "🔴 Mot de passe faible. " + " ".join(remarks)

# Test du programme
if __name__ == "__main__":
    pwd = input("🔑 Entrez un mot de passe : ")
    print(check_password_strength(pwd))
