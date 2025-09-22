alpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def entrer_mot():
    mot = input("Entrer le mot en MAJUSCULES : ")
    return mot

def entrer_clef():
    clef=input("entrer une clef")
    return clef

def separer_clef(clef):
    clef_sepa=[]
    for p in clef:
        clef_sepa.append(p)
    return clef_sepa
    
def conv_clef(clef_sepa):
    clef_conv=[]
    for j in range(len(clef_sepa)):
        if j in alpha:
            clef_conv.append(ord(j)-65)
        else:
            clef_conv.append(j)
    return clef_conv

def separer_mot(mot):
    mot_sepa = []
    for c in mot:
        mot_sepa.append(c)
    return mot_sepa

def cont_mot(mot_sepa,alpha):
    mot_conteur=[]
    for a in mot_sepa:
        if a in alpha:
            for i in range(26):
                if alpha[i]==a:
                    mot_conteur.append(i)
        else:
            mot_conteur.append(a)
    return mot_conteur

def ord_mot(mot_sepa,alpha):
    mot_ord = []
    for c in mot_sepa:
        if c in alpha:
            mot_ord.append(ord(c) - 65)
        else:
            mot_ord.append(c)
    return mot_ord

def conv_vigenere(mot_ord,mot_conteur,clef_conv):
    mot_conv = []
    cont=0
    for x in mot_ord:
        if isinstance(x,int):
            x=alpha[(mot_conteur[cont%len(mot_conteur)]+clef_conv[cont])%26]
            cont=cont+1
            mot_conv.append(x)
        else:
            cont=cont+1
            mot_conv.append(x)
    return mot_conv

def texte_final(mot_conv):
    texte = ""
    for x in mot_conv:
            texte += str(x)
    return texte


#code principal
mot = entrer_mot()
clef=entrer_clef()
clef_sepa=separer_clef(clef)
clef_conv=conv_clef(clef_sepa)
mot_sepa = separer_mot(mot)
mot_conteur=cont_mot(mot_sepa,alpha)
mot_ord = ord_mot(mot_sepa,alpha)
mot_conv = conv_vigenere(mot_ord,mot_conteur,clef_conv)
texte_chiffre = texte_final(mot_conv)

print("Texte chiffré :", texte_chiffre)

