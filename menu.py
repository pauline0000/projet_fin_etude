import os


while True:
    # Menu principal
    print("Menu principal :")
    print("1. Test d'intrusion")
    print("2. Scrapping vulnérabilités critiques")
    print("5. Quitter")

    # Demande de choix de l'utilisateur
    choix = input("Choisissez une option : ")

    # Sous-menu de l'option 1
    if choix == "1":
        while True:
            print("Test d'intrusion :")
            print("1. Reconnaissance")
            print("2. Enumération")
            print("3. Scan de vulnérabilités")
            print("4. Retour au menu principal")

            # Demande de choix de l'utilisateur dans le sous-menu
            sous_choix = input("Choisissez une option : ")

            # Traitement des choix dans le sous-menu de l'option 1
            if sous_choix == "1":
                print("Reconnaissance :")
                print("La reconnaissance correspond à l'étape de collecte d'information sur les systèmes cibles")
                os.system('python nmap1.py')
                os.system('python grecon.py')
                sherlock_path = "/sherlock/sherlock/sherlock/sherlock.py"
                username = input("Entrez un nom d'utilisateur : ") 
                os.system(f"python {sherlock_path} {username}")

            elif sous_choix == "2":
                print("Enumération :")
                print("L'énumération est une partie importante car elle permet de comprendre quels appareils se trouvent sur votre réseau, où ils se trouvent et quels services ils offrent")
                os.system('python enumeration2.py')

            elif sous_choix == "3":
                print("Scan de vulnérabilités :")
                os.system('python scanvuln.py') 

            elif sous_choix == "4":
                break  # Retour au menu principal

            else:
                print("Choix invalide")

    # Sous-menu de l'option 2
    elif choix == "2":
        while True:
            print("Scrapping des dernières vulnérabilités critiques :")
            print("1. Lancer le scraping")
            print("2. Retour au menu principal")

            # Demande de choix de l'utilisateur dans le sous-menu
            sous_choix = input("Choisissez une option : ")

            # Traitement des choix dans le sous-menu de l'option 2
            if sous_choix == "1":
                print("Lancement du scraping :")
                os.system('python nist5.py')

            elif sous_choix == "2":
                break  # Retour au menu principal

            else:
                print("Choix invalide")

    # Quitter le programme
    elif choix == "5":
        print("Vous venez de quitter le menu")
        break

    # Choix invalide
    else:
        print("Choix invalide")
