historique_operations = []

def afficher_historique(historique):#fonction qui affiche l'historique
    print("Historique des opérations et résultats :")
    for operation, result in historique: #ici
        print(f"{operation} = {result}")

def effacer_historique(): #fonction qui supprime l'historique
    global historique_operations #une variable dans une fonction n'étant pas accessible en dehors de ctte foonction, ici le mot clé global permet à la variable 'historique_opérations' d'être accessible à l'extérieur de la fonction
                                    #Dans ce cas précis, global 'historique_operations' indique que la fonction 'effacer_historique' va modifier la variable 'historique_operations' qui se trouve dans l'espace global du programme. 
    historique_operations = [] #ici j'affiche la variable 'historique_operations' qui est vide, elle est exécutée quand la fonction 'effacer_historique()' est appelée 
    print("L'historique a été effacé.")

while True:
    nombre = [] #variable qui va contenir mes données d'entrée sous forme de liste

    while True: #boucle qui va récuperer les données entré par l'utilisateur
        entree = input("Entrez un nombre ou '=' pour quitter  : ") #ici l'utilisateur va devoir entrer un nombre

        if entree == '=': #lors du input de 'entree', l'utilisateur pourras appuyer sur 'q' pour quitter, celui ci est opéré par cette boucle
            break

        operateur = input("Entrer opérateur '+, -, *, /' ou '=' pour quitter (attention, le reste des opérateurs doivent être identiques) :") #ici l'utilisateur va devoir entrer un opérateur '+, -, *, /'

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
            operation = f"{nombre[index - 1]} + {nombre[index + 1]}"                                                    
            nombre = nombre[:index - 1] + [addition] + nombre[index + 2:]# cette ligne modifie la liste 'nombre' en remplaçant les éléments impliqués dans l'opération addition réalisé précédemment
                                                                            #Si je suppose que mon 'index = 1':
                                                                            #'nombre[:index - 1]' sélectionne une portion de la liste 'nombre' depuis le début jusqu'à l'élément précédant le premier nombre impliqué dans l'opération. Ici, cela sélectionne '[]' car il n'y a pas d'éléments avant le premier nombre
                                                                            #'[addition]' contient le résultat du premier opération d'addition, qui, dans mon cas, est '[10]'
                                                                            #'nombre[index + 2:]' sélectionne une portion de la liste nombre depuis l'élément suivant le premier nombre impliqué dans l'opération jusqu'à la fin de la liste. Ici, ça sélectionne '[4, '+', 4]'.
            historique_operations.append((operation, addition))#ici je stocke sous forme de tuple, l'operation sous forme de str et le résultat de l'addition                                                            
        resultat = nombre[0] # Ici j'assigne la première valeur de la niste 'nombre' à la variable 'resultat'
        afficher_historique(historique_operations)   
    elif '-' in nombre:
        while '-' in nombre:
            index = nombre.index('-')
            soustraction = nombre[index - 1] - nombre[index + 1]
            operation = f"{nombre[index - 1]} - {nombre[index + 1]}"
            nombre = nombre[:index - 1] + [soustraction] + nombre[index + 2:]
            historique_operations.append((operation, soustraction))
        resultat = nombre[0]
        afficher_historique(historique_operations)
    elif '*' in nombre:
        while '*' in nombre:
            index = nombre.index('*')
            multiplication = nombre[index - 1] * nombre[index + 1]
            operation = f"{nombre[index - 1]} * {nombre[index + 1]}"
            nombre = nombre[:index - 1] + [multiplication] + nombre[index + 2:]
            historique_operations.append((operation, multiplication))
        resultat = nombre[0]
        afficher_historique(historique_operations)
    elif '/' in nombre:
        while '/' in nombre:
            index = nombre.index('/')
            if nombre[index + 1] == 0 or nombre[index - 1] == 0:
                print("Division par '0' impossible")
                break
            division = nombre[index - 1] / nombre[index + 1]
            operation = f"{nombre[index - 1]} / {nombre[index + 1]}"
            nombre = nombre[:index - 1] + [division] + nombre[index + 2:]
            historique_operations.append((operation, division))
        resultat = nombre[0]
        afficher_historique(historique_operations)

    if resultat is not None:
        print(f"Résultat de l'opération:", resultat)
    choix = input("Voulez-vous effectuer une autre opération ? (Oui/Non): ").lower()
    if choix != 'oui':
        break
    choix = input("Voulez-vous effacer l'historique ? (Effacer/Non): ").lower()
    if choix == 'effacer':
        effacer_historique()#ici j'appelle ma fonction 'effacer_historique()' lorsque l'utilateur écrit 'effacer'
    


