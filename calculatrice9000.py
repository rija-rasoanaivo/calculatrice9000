nombre = [] #variable qui va contenir mes données d'entrée sous forme de liste

while True: #boucle qui va récuperer les données entré par l'utilisateur
    entree = input("Entrez un nombre ou '=' pour quitter  : ") #ici l'utilisateur va devoir entrer un nombre
    
    if entree == '=': #lors du input de 'entree', l'utilisateur pourras appuyer sur 'q' pour quitter, celui ci est opéré par cette boucle
        break    

    operateur = input("Entrer opérateur '+, -, *, /' ou '=' pour quitter :") #ici l'utilisateur va devoir entrer un opérateur '+, -, *, /'

    if operateur == '=': #lors du input de 'operateur', l'utilisateur pourras appuyer sur 'q' pour quitter, celui ci est opéré par cette boucle
        break 
    else:
        nombre.append(float(entree)) #ici le module .append va stocker chaques 'entree' dans ma liste 'nombre' sous forme de float
        nombre.append(str(operateur)) #ici le module .append va stocker chaques 'operateur' dans ma liste 'nombre' sous forme de chaîne de caractère

if entree != '=': #cette condition permet de verifier si la dernière donnée d'entrée n'est pas égal à 'q' 
                    #Cette condition est utilisée pour s'assurer que si l'utilisateur quitte le programme en entrant 'q' après avoir saisi un nombre
    nombre.append(float(entree)) #cette ligne est utilisée pour ajouter le dernier nombre saisie par l'utilisateur

print("Données d'entrée :", nombre) #ici la donnée d'entrée nombre va être printé  

resultat = None #ici nous partons d'une variable vide qui sera définie par None
#J'initialise une boucle qui va me permettre de réaliser des calculs simple avec plusieurs nombres dans la liste
if '+' in nombre: #si il y a une présence d'un string '+' dans ma liste nombre, on rentre dans la sous boucle while
    while '+' in nombre: #ici la boucle while me recupère chaque '+' dans la liste nombre
        index = nombre.index('+') #j'utilise ici la méthode index() qui va permettre de rechercher les positions à laquelle l'élément '+' apparaît dans la liste 'nombre'
                                    #exemple 'nombre=[5, '+', 5, '+', 4, '+', 4]' l'exécution de 'index = nombre.index('+')' donnera au premier '+' l'index 1, le deuxième '+' l'index 3, le troisième '+' l'index5
        addition = nombre[index - 1] + nombre[index + 1] #il s'agit ici d'une instruction 'addition' qui va permettre d'additionner deux valeurs de la liste 'nombre' basés avant et après l'index '+' trouvé dans l'instruction précédent
                                                            #nombre[index-1] fait référence au nombre situé avant notre index '+', nombre[index+1] fait référence au nombre situé après notre index '+'
        nombre = nombre[:index - 1] + [addition] + nombre[index + 2:]# cette ligne modifie la liste 'nombre' en remplaçant les éléments impliqués dans l'opération addition réalisé précédemment
                                                                        #Si je suppose que mon 'index = 1':
                                                                        #'nombre[:index - 1]' sélectionne une portion de la liste 'nombre' depuis le début jusqu'à l'élément précédant le premier nombre impliqué dans l'opération. Ici, cela sélectionne '[]' car il n'y a pas d'éléments avant le premier nombre
                                                                        #'[addition]' contient le résultat du premier opération d'addition, qui, dans mon cas, est '[10]'
                                                                        #'nombre[index + 2:]' sélectionne une portion de la liste nombre depuis l'élément suivant le premier nombre impliqué dans l'opération jusqu'à la fin de la liste. Ici, ça sélectionne '[4, '+', 4]'.
    resultat = nombre[0] # Ici j'assigne la première valeur de la niste 'nombre' à la variable 'resultat'
elif '-' in nombre:
    while '-' in nombre:
        index = nombre.index('-')
        soustraction = nombre[index - 1] - nombre[index + 1]
        nombre = nombre[:index - 1] + [soustraction] + nombre[index + 2:]
    resultat = nombre[0]
elif '*' in nombre:
    while '*' in nombre:
        index = nombre.index('*')
        mutiplication = nombre[index - 1] * nombre[index + 1]
        nombre = nombre[:index - 1] + [mutiplication] + nombre[index + 2:]
    resultat = nombre[0]
elif '/' in nombre:
    while '/' in nombre:
        index = nombre.index('/')
        if nombre[index + 1] == 0:
            print("Division par zéro impossible")
            break  # Arrête la boucle si une division par zéro est détectée
        division = nombre[index - 1] / nombre[index + 1]
        nombre = nombre[:index - 1] + [division] + nombre[index + 2:]
    resultat = nombre[0]

if resultat is not None:
    print("Résultat de l'opération :", resultat)
