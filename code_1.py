#définition des fonctions lire, analyse et fichier

def lire(nomfichier, liste_note1, liste_note2, liste_note4, liste_note5) :
    '''
    lis un fichier contenant des commentaires et des notes e classes chaque mots d'un commentaire dans la list correspondant a la note du commentaire 

    pre nom du fichier possédant les commentaires 

    post commentaire = liste contenant tous les commentaires et 4 listes contenant leur mots associé a leur noms 
    '''
    fichier = open(nomfichier, 'r') #ouvre le fichier nomfichier en mode lecture
    donnees = fichier.readlines() #recopie toutes les infos du fichier et les stocks dans cette liste
    fichier.close()
    commentaires = [] #une liste allant acceuillir tous les commentaires
    for element in donnees : #une boucle découpant la liste donnes pour ajouter chaque commentaires sous forme de liste contenant chaque mots en élément et la note en premier element 
        element = element.rstrip("\n") #decoupe chaque ligne en une liste
        ligne = element.split(" ") #decoupe chaque mots du commentaire en elements de la liste 
        ligne.pop(0) #retire le premier element de la liste qui est "-"
        commentaires.append(ligne) #ajoute cette liste correspondant à un commentaire dans la liste commentaires 
    
    for commentaire in commentaires : #ajoute les mots du commentaire à la liste correspondant aux étoiles
        for i in range (1, len(commentaire)) :
            if commentaire[0] == "1" :
                liste_note1.append(commentaire[i])
            elif commentaire[0] == "2" :
                liste_note2.append(commentaire[i])
            elif commentaire[0] == "4" :
                liste_note4.append(commentaire[i])
            elif commentaire[0] == "5" :
                liste_note5.append(commentaire[i])
            else :
                pass
    return(commentaires, liste_note1, liste_note2, liste_note4, liste_note5)

def analyse(nomfichier, liste_note1, liste_note2, liste_note4, liste_note5, valeur) :
    """
    extraire les commentaires du fichier « nomfichier », puis de 
    comparer si les mots lus pour chaque commentaire sont contenus dans une des 4 listes 
    précédemment définies et passées en paramètres « liste_note1, liste_note2, liste_note4, 
    liste_note5

    pre annalyser les commentaire situé dans fichieranalyse et utilisé les données du fichier nomfichier

    post renvoie une liste contenant les notes et le commentaire associé
    """
    commentaires = lire(valeur, liste_note1, liste_note2, liste_note4, liste_note5)[0] #recupere les informations de la foncion lire et les stocks dans une variable pour le fichier a analysé
    liste_note1 = lire(nomfichier, liste_note1, liste_note2, liste_note4, liste_note5)[1] #recupere les informations de la foncion lire et les stocks dans des variables pour le fichier de référence
    liste_note2 = lire(nomfichier, liste_note1, liste_note2, liste_note4, liste_note5)[2]
    liste_note4 = lire(nomfichier, liste_note1, liste_note2, liste_note4, liste_note5)[3]
    liste_note5 = lire(nomfichier, liste_note1, liste_note2, liste_note4, liste_note5)[4]

    commentaireavecnote = [] #initialise la liste qui contiendra le commentaire avec sa note et sa mention
    data = [] #initialise la liste qui contiendra toutes les listes des commentaires

    score = 0 #initialisie la note du mot a 0
    for commentaire in commentaires : #commentaire prend la valeur du commentaire sous forme de liste
        for i in range (1, len(commentaire)) : #prend la longueur de l phrase
            if len(commentaire[i]) >= 3 : #verifie si le mot possédent plus de 3 lettres (pour supprime les mos innutiles)
                for note in liste_note1 : #va tester si le mot est dans la liste liste_note1 et si oui le score est soustrait de 2
                    if commentaire[i] == note :
                        score = score - 2
                    else :
                        pass
                for note in liste_note2 :#va tester si le mot est dans la liste liste_note2 et si oui le score est soustrait de 1
                    if commentaire[i] == note :
                        score = score - 1
                    else :
                        pass
                for note in liste_note4 :#va tester si le mot est dans la liste liste_note4 et si oui le score est ajouté de 1
                    if commentaire[i] == note :
                        score = score + 1
                    else :
                        pass
                for note in liste_note5 :#va tester si le mot est dans la liste liste_note5 et si oui le score est ajouté de 2
                    if commentaire[i] == note :
                        score = score + 2
                    else :
                        pass
            else :
                pass
        score = score // len(commentaire)#divise le score par la longueur du commentaire pour faire une moyenne
        phrase = " ".join(commentaire) #fonction pour créer une jolie phrase
        
        if score < -10 :  #regarde le score et note le commentaire a 1, 2, 3, 4, ou 5 étoiles en focntion du score (+mention)
            commentaireavecnote.append(1)
            commentaireavecnote.append("très médiocre")
        elif score < 0 :
            commentaireavecnote.append(2)
            commentaireavecnote.append("médiocre")
        elif score >= 0 and score <5 :
            commentaireavecnote.append(3)
            commentaireavecnote.append("moyen")
        elif score >+ 5 and score <= 10 :
            commentaireavecnote.append(4)
            commentaireavecnote.append("bon")
        else :
            commentaireavecnote.append(5)
            commentaireavecnote.append("trés bon")

        commentaireavecnote.append(phrase) #ajoute le commentaire à la fin de la liste
        data.append(tuple(commentaireavecnote)) #ajoute la liste contenant le commentaire la note et la mention sdous forme de tuple pour qu'elle ne soit pas modifié
        commentaireavecnote.clear() #vide la liste 

        score = 0 #reinitialise le score à 0 pour préparer un nouveau commentaire

    return(data)

def fichier(nomfichier, valeur) :
    '''
    créer un fichier texte nomé analyse contenant les commenaire du fichier valeur associé à leur note analysé par l'IA

    pre : nomfichier est le dossier dans lequel on se refére pour entrainer l'IA et valeur est le fichier à analysée

    post : 
    '''
    data = analyse(nomfichier, liste_note1, liste_note2, liste_note4, liste_note5, valeur) #recupere la liste créé par la fonction analyse
    fichier = open("./analyse_IA.txt", 'w') #créé un fichier nomé analyse_IA.txt en mode ecriture
    fichier.write("Dossier analyse :\n note : \t evaluation: \t commentaire : \n") #ecris la mise en page = debut de page
    for commentaire in data : #créer une boucle ou commentaire prend la valeur de chaque commentaires présent dans data
        for ecrit in commentaire : #ecrit prend la valeur de chaque element dans commentaire 
            fichier.write(str(ecrit)) #ecrit cette element dans le fichier texte
            fichier.write("\t") #les separent d'une tabulation
        fichier.write("\n") #separe chaque commentaire par un retour à la ligne
    fichier.close() #ferme le fichier 
    print("tout est bon") #informe l'utilisateur que le programme est fini


#programme principale

liste_note1 = [] #défini les liste 
liste_note2 = [] #défini les liste 
liste_note4 = [] #défini les liste 
liste_note5 = [] #défini les liste 

nomfichier = "./commentaires.txt"   #= fichier des valeures à utiliser pour entrainer notre IA
valeur = "./inconnus.txt"  #= fichier à analyser
fichier(nomfichier, valeur) #faire marcher le programme