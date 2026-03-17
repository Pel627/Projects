import re

def check_password(password):
    score = 0
    feedback = []

    # Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Muy corta")

    # Upercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Faltan mayúsculas")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Faltan minúsculas")

    # Numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Faltan números")

    # Simbols
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Faltan símbolos")

    # Final test
    if score >= 6:
        strength = "Muy fuerte"
    elif score >= 4:
        strength = "Fuerte"
    elif score >= 3:
        strength = "Media"
    else:
        strength = "Débil"

    return strength, feedback


password = input("Ingresá una contraseña: ")
strength, feedback = check_password(password)

print(f"\nNivel de seguridad: {strength}")

if feedback:
    print("Sugerencias:")
    for f in feedback:
        print(f"- {f}")
