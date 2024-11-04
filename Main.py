job 4 
import string  #importation de la fonction string qui cpermet de manipuler des chaine de caractere #

alphabet = list(string.ascii_lowercase)  #constante qui contient toute les lettres de l'alphabet dans la fonction string#

print(alphabet)#affichage de la list#

import string


 job 5 #
alphabet = list(string.ascii_lowercase)

alphabetinversé = alphabet [::-1]#prendre la liste en commencant par la fin avec "[::-1]"

print(alphabetinversé)
 
# job6 #
#ma_string= "je suis une string"

#print(ma_string)

# job 7#
#num1 = 40 
#num2 = 2

#print(num1+num2)

# job8 #
#num1 = 3
#num2 = 14

#print(num1*num2)

# job 9 #

#produit1 = ["pomme","2","10"]
#produit2 = ["poire","1","7"]
#produit = produit1 + produit2

#print ("produit1 :" , produit1)
#print("produit2",produit2)

#prixunitaire_pomme = float(produit[1])
#prixunitaire_poire = float(produit[4])

#quantitepomme = int(produit[2])
#nomduproduit = input("quel fruit voulez vous ?")

#if nomduproduit == "pomme" and quantitepomme > 0:
#    quantitevoulue = int(input("combien en voulez vous ?"))
#    prixtotal = prixunitaire_pomme * quantitevoulue * 1.1
 #   print("prix total pour ", quantitevoulue, "pomme" , prixtotal)

#elif nomduproduit == "poire" and int(produit[5]) > 0:
#    quantitevoulue = int(input("combien en voulez vous ?"))
 #   prixtotal = prixunitaire_poire * quantitevoulue
 #   print("prix total pour" , quantitevoulue , "poire =" , prixtotal)
#else:
#    print("hassoul")





#job 1
#for i in range(21):
 #print(i)
 
 
 
 #job 2

#for i in range(21): 
# if i % 2 == 1 :
#  print(i)


#job 3#

#for i in range(21):
#  print(i**2)

#job4#

#n = int(input("veuillez choisir un nombre :"))

#for i in range(n+1):
    #print("\ntable de " , i )
    #for b in range(11):
   
    #print(i,"*",b ,"=" , i*b)


#job 5#

#N=1

#while N > 13:
  #n= n+1
 # print(N)#
 

#job6#

#n = int(input("choisir un nombre"))
#i=0
#while i <= n:
  #print(i*7)
  #i=i+1


 #for i in range (1,13):
    #print ("tour",i,i*3-2)


#r=0
#for i in range (1,12):
   # r=r+2
    #print(r+2)
    
#for i in range (30):
   # if i % 2 == 1 :
    # print("nombre pair :", i )

    #else: 

     #print("nombre impaire:",i)





#job 1#

#valeur1 = int(input("veuillez choisir un nombre :"))

#valeur2 =int(input("veuillez choisir un nombre :"))

#if valeur1 == valeur2 :
    #print(valeur1 ," est egals a ", valeur2 )
#else :
 #print(" elles ne sont pas egaux")#
    

#job 2 #
#age = int(input("veuillez rentrer votre age:"))

#if age >= 18 :
    #print("tu as ", age ,"ans tu peux voter")

#else :
    #print("tu n'as pas l'age  ")

#exclus = (26 , 37 ,88)

#i=0
#for i in range(101):
      #if i not in exclus:
         #print(i)



#i = 0 

#for i in range(101): 
    #if i %3 == 0 :
        #print("fizz")
    #elif i %5 == 0:
        #print("buzz")
   
    #else: 
        #print(i) 

#job 5#

#def nombrepremier(hassoul):
  #  for n in range (2,hassoul):
       # if hassoul %  n == 0:
      #   return False
    #return True
#for x in range(2,1010):
      #if nombrepremier(x): 
           #print(x)


#job 6#

    
#i=int(input("veuillez rentrer un nombre"))
 
#if i % 2 == 0 :
    # print(i ,"est un nombre pair" )

#else: 
    
    # print(i,"est un  nombre impaire")

#job 7#

#i=1 
#x = str("abcdefghijklmnopqrstuvwxyz"*10)

#while i != len(x):
 #i=i+1
 #print(x[0:i])


#job 8#

#longueurA = int(input("qu'elle est la longueur de a:"))
#longueurB = int(input("qu'elle est la longueur de b:"))
#longueurC = int(input("qu'elle est la longueur de c:"))
#angleDroit = str(input("y a t'il un angle droit ?"))

#if longueurA == longueurB != longueurC:
 #print( "ce triangle est isocele")
#elif longueurB == longueurA == longueurC:
 #print("ce triangle est equilateral")

#elif angleDroit == True:
# print ("ceci est un triangle ")

#else:
 # angleDroit == False
  #print("autre triangle")



#x=5 
#if x > 5 :
 #print("plus grand")
#else:
 #print("plus petit ")


#x=12
#y=10
#if x < 10 or y >5 :
 #print("vrai")
#else:
 #print("faux")

#x= 5 
#not x >10

#job1#

#def my_print_hello(  ):
 #   print("hellp world")
#my_print_hello()

#job 2#

#def my_print_name(name):

 #   print(name)
#my_print_name(name= "jean")

#job 3#


#def add(a,b):
 #   print(a+b)
#add(8,9)

#job4#

#def gethello():
 #   return "hello la plateforme"
#print(gethello())


#job 5#



#def calcule(num1,operator, num2):
   # if operator == "*":
       #return num1*num2
    #elif operator == "+":
       #return num1+num2
    #elif operator == "-":
       #return num1- num2
    #else:
        #return"MOTORSPORT"

#print(calcule(5,"*",5))

#job 6#

#def nombre(nombre):
    #if nombre > 0:
        #print("superieur")
    #else:
         #print ("inferieur")  
#nombre(-5)
    
#job 7#

#def ye (langage:str):
  #  if langage =="python" :
  #      print("tu es un developpeur web")
    #elif langage =="Javascript":
    #    print("tu es un developpeur IA")
    #elif langage =="Java":
    #    print("tu es un developpeur logiciel")
   # elif langage =="reactjs":
        #print("tu es un developpeur mobile")
    #else : 
        #print("un jour, je serai le meilleur developpeur...")
#ye ( langage = "Java")


#job 8#

#def e(type:str, saison:str):
    #if type == "fruit" and saison == "hiver":
    #    print("orange mandarine et kiwi")
    #elif type== "fruit" and saison =="ete":
    #    print("poire fraise cassis")
    #elif type == "legume" and saison == "hiver":
     #   print("carotte , topinambour, endive")
    #elif type == "legume" and saison == "ete":
   #     print("artichaut aubergine , navet")
  #  else:
 #       print("KAYAKO BEME")
#e( type= "fruit" ,saison="f")

#job 9 #

#def moyenne(note1 = int(input("rentrez une note :")),note2 =  int(input("rentrez une note :")),note3 =  int(input("rentrez une note :"))):
 #   return (note1+note2+note3)/3
#moyenneetudiant=moyenne()
#if moyenneetudiant > 15:
 #   print("bonne eleve")
#elif moyenneetudiant >11  :
 #   print("ok")
#elif moyenneetudiant <=8:
 #   print("bof ")
#else:
    #print("rentez des notes valides")
    
    # job 10#

#def nmbr(nombre):

    #if nombre  %2 ==0 and nombre >0 and nombre %1==0 :
    #    print("pair")
    #elif nombre >0 and nombre %1==0 :
   #  print("impair" )
  #  else:
 #       print("non")
#nmbr(-2)

#job 11#

#def voiture(time:int):
    #print(time*)








#fruit= ["pomme," "cerise," "orange"]
#def fonction():
 #  return fruit
#print(fonction())


#def fonction():
 #  fruit= ["pomme," ,"cerise,", "orange"] 
  # print(fruit[1])
#fonction()


#def fonction():
   #fruit= ["pomme," ,"cerise,", "orange"]
  # fruit.append("melon")
 #  print(fruit)
#fonction()

#def fonction():
   #fruit= ["pomme," ,"cerise,", "orange"]
   #fruit.append("melon")
   #fruit.insert(2,"mangue")
   #print(fruit)
#fonction()

#kaykobeme=[1,2,3,4,5,6,7,8,9]
#print(kaykobeme)

#def afoumamé():
  #  kaykobeme[3]=kaykobeme[2]+ kaykobeme[4]
 #   print(kaykobeme[3])
#afoumamé()
#print(kaykobeme)

#l=[1,2,3,4,5,6,7,8,9]
#l[0]=l[8] 
#l[8]= 1
#print(l)


#l=[8, 24,48,2,16]
#compteur= len([i for i in l if i %3==0])
#print(compteur)

def longueur_liste(liste):
    compteur = 0
    for _ in liste:
        compteur += 1
    return compteur

def trier_liste(liste):
    n = longueur_liste(liste)  # Calculer la longueur de la liste sans utiliser len
    
    # Tri par sélection
    for i in range(n):
        # Trouver l'index du plus petit élément restant dans la liste
        min_index = i
        for j in range(i + 1, n):
            if liste[j] < liste[min_index]:
                min_index = j
        # Échanger l'élément minimum avec le premier élément non trié
        temp = liste[i]
        liste[i] = liste[min_index]
        liste[min_index] = temp

    return liste

# Exemple de liste
L = [8, 24, 48, 2, 16]

# Appel de la fonction et affichage du résultat
resultat = trier_liste(L)
print("Liste triée :", resultat)
