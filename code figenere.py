alpha=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
mot_origine=None
mot_sepa=None
texte_chiffré=None
mot_ord=None
def entrer_mot(mot_origine):
    mot_origine=int(input("entrer 5 caracteres"))
    return mot_origine

def separer_mot(mot_origine,mot_sepa,sep=" "):
    mot_sepa=[]
    current=""
    for char in mot_origine:
        if char==sep:
            mot_sepa.append(current)
            current=""
        else:
            current+= char
            mot_sepa.append(current)
            current=""
    return mot_sepa

def ord_mot(mot_sepa,mot_ord):
    for i in range(len(mot_origine)):
        a=ord(mot_sepa[i])
        mot_ord.append(a)

def conv(mot_sepa,alpha,mot_finale,texte_chiffré):
    for i in range(len(mot_sepa)):
        b=mot_ord[i]-65
        
       