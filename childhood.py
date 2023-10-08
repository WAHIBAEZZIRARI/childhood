N1 = float (input("Veuillez saisir N1: "))
N2 = float (input("Veuillez saisir N2: "))
N3 = float (input("Veuillez saisir N3 : "))
Moyenne = (N1+N2+N3)/3
print("La moyenne de L'étudiant est : ", format(Moyenne,".2f"))
if Moyenne < 10:
      print("La mention de l'étudiant est : Insuffisant")
elif Moyenne >=10 and Moyenne < 12:
     print("La mention de l'étudiant est: Passable")
elif Moyenne >=12 and Moyenne < 14:
      print("La mention de l'étudiant est: Assez bien")
elif Moyenne >=14 and Moyenne < 16 :
     print("La mention de l'étudiant est: Bien")
else:
     print("La mention de l'étudiant est: Très bien")https://github.com/Yahyazaizi/the-mention-of-childhood-according-to-the-general-means/tree/main