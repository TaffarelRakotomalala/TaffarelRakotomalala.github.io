from django.shortcuts import render
from .models import *

def CommandeTailleCouleur1(T, refy, loko):
    s = 0
    for i in T:
        if (i.taille == refy) and (i.couleur1 == loko):
            s = s + 1
    return s

def CommandeTaille2(T, refy):
    s = 0
    for i in T:
        if i.taille == refy:
            s = s + 1
    return s

def PrixAvance(T):
    p = 0
    for i in T:
        p = p + i.avance
    return p
def PrixReste(T):
    p = 0
    for i in T:
        p = p + i.reste
    return p
    

def test(request):
    return render(request, 'blog/test.html')

def principal(request):
    client1 = InfoPerso1.objects.all().order_by('id')
    client2 = InfoPerso2.objects.all().order_by('id')
    return render(request, 'blog/main.html', locals())

def infocommande(request):
    commande1 = InfoCommande1.objects.all()
    commande2 = InfoCommande2.objects.all()
    return render(request, 'blog/commande.html', locals())

def info(request):
    commande1 = InfoCommande1.objects.all()
    commande2 = InfoCommande2.objects.all()
    t1 = len(commande1)
    t2 = len(commande2)

    #----------------- Couleur Rouge -------------------
    s1r1 = CommandeTailleCouleur1(commande1, "S","Rouge")
    m1r1 = CommandeTailleCouleur1(commande1, "M","Rouge")
    l1r1 = CommandeTailleCouleur1(commande1, "L","Rouge")
    xl1r1 = CommandeTailleCouleur1(commande1, "XL","Rouge")
    xxl1r1 = CommandeTailleCouleur1(commande1, "XXL","Rouge")
    autre1r1 = CommandeTailleCouleur1(commande1, "Autre", "Rouge")

    #----------------- Couleur Blanc -------------------
    s1b1 = CommandeTailleCouleur1(commande1, "S","Blanc")
    m1b1 = CommandeTailleCouleur1(commande1, "M","Blanc")
    l1b1 = CommandeTailleCouleur1(commande1, "L","Blanc")
    xl1b1 = CommandeTailleCouleur1(commande1, "XL","Blanc")
    xxl1b1 = CommandeTailleCouleur1(commande1, "XXL","Blanc")
    autre1b1 = CommandeTailleCouleur1(commande1, "Autre", "Blanc")

    #----------------- Couleur Jaune -------------------
    s1j1 = CommandeTailleCouleur1(commande1, "S","Jaune")
    m1j1 = CommandeTailleCouleur1(commande1, "M","Jaune")
    l1j1 = CommandeTailleCouleur1(commande1, "L","Jaune")
    xl1j1 = CommandeTailleCouleur1(commande1, "XL","Jaune")
    xxl1j1 = CommandeTailleCouleur1(commande1, "XXL","Jaune")
    autre1j1 = CommandeTailleCouleur1(commande1, "Autre", "Jaune")

    #--------------- Taille pour le T-shirt 2 ----------------
    s2 = CommandeTaille2(commande2, "S")
    m2 = CommandeTaille2(commande2, "M")
    l2 = CommandeTaille2(commande2, "L")
    xl2 = CommandeTaille2(commande2, "XL")
    xxl2 = CommandeTaille2(commande2, "XXL")
    autre2 = CommandeTaille2(commande2, "Autre")

    # -------------- Total Avance et reste --------------------
    avance1 = PrixAvance(commande1)
    reste1 = PrixReste(commande1)

    avance2 = PrixAvance(commande2)
    reste2 = PrixReste(commande2)


    return render(request, 'blog/informations.html', locals())

