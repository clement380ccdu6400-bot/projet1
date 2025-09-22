alpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def entrer_mot():
    mot = input("entrer mot:")
    return mot

def entrer_clef():
    clef=int(input("entrer une clef:"))
    return clef

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

def conv_cesar(mot_sepa,mot_conteur,clef):
    mot_conv = []
    cont=0
    for x in mot_sepa:
        if x in alpha:
            x=alpha[(mot_conteur[cont%len(mot_conteur)]-clef)%26]
            cont+=1
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
mot_sepa = separer_mot(mot)
mot_conteur=cont_mot(mot_sepa,alpha)
mot_conv = conv_cesar(mot_sepa,mot_conteur,clef)
texte_dechiffre = texte_final(mot_conv)

print("Texte dechiffré :", texte_dechiffre)

