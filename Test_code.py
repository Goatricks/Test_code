liste_de_nombres = input("Enter a list of numbers separated by comma: ")
liste_de_nombres = liste_de_nombres.split(',')
def somme(liste_de_nombres):
  resultat =0
  for i in liste_de_nombres:
    resultat = resultat + int(i)

  return resultat
def moyenne(liste_de_nombres):
  resultat =0
  for nombre in liste_de_nombres:
    resultat = somme(liste_de_nombres) / len(liste_de_nombres)

  return resultat
moyenne (liste_de_nombres)

def au_dessus_de_la_moyenne(liste_de_nombres):
  resultat = 0
  for nombre in liste_de_nombres:
    if int(nombre) > moyenne(liste_de_nombres):
      resultat = resultat + 1

  return resultat
au_dessus_de_la_moyenne(liste_de_nombres)

def nombres_pairs(liste_de_nombres):
  resultat = 0
  idx = 0
  while (idx < len(liste_de_nombres)):
    if int(liste_de_nombres[idx]) % 2 == 0:
      resultat +=1
    idx += 1

  return resultat
nombres_pairs (liste_de_nombres)



print("la somme des nombres est: ", somme(liste_de_nombres))
print("la moyenne des nombres est:", moyenne(liste_de_nombres))
print("le nombre de nombres au dessus de la moyenne est:", au_dessus_de_la_moyenne(liste_de_nombres))
print("le nombre de nombres pairs est:", nombres_pairs(liste_de_nombres))
