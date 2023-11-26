def chiffrement_cesar(texte, decalage):
    texte_chiffre = ""
    for char in texte:
        if char.isalpha():
            
            if char.isupper():
                texte_chiffre += chr((ord(char) + decalage - ord('A')) % 26 + ord('A'))
            
            else:
                texte_chiffre += chr((ord(char) + decalage - ord('a')) % 26 + ord('a'))
        else:
            texte_chiffre += char
    return texte_chiffre

def dechiffrement_cesar(texte_chiffre, decalage):
    return chiffrement_cesar(texte_chiffre, -decalage)


operation = input("Voulez-vous chiffrer (C) ou déchiffrer (D) : ").upper()
texte_original = input("Entrez le texte : ")
decalage = int(input("Entrez le décalage : "))


if operation == "C":
    texte_resultat = chiffrement_cesar(texte_original, decalage)
    print("Texte chiffré:", texte_resultat)
elif operation == "D":
    texte_resultat = dechiffrement_cesar(texte_original, decalage)
    print("Texte déchiffré:", texte_resultat)
else:
    print("Opération non reconnue. Veuillez entrer 'C' pour chiffrer ou 'D' pour déchiffrer.")
