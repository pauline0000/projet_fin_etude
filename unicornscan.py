import os

def unicorn_scan():
    # Demander à l'utilisateur l'adresse IP à scanner
    ip_address = input("Entrez l'adresse IP à scanner : ")

    # Commande Unicornscan pour scanner les ports UDP et TCP
    command = f"sudo unicornscan -mU -mT -p 1-1000 {ip_address}:a"


    # Exécuter la commande et récupérer les résultats
    results_udp_tcp = os.popen(command).read()


    # Afficher les résultats de chaque scan
    print("Résultats du scan UDP et TCP :")
    print(results_udp_tcp)


# Exemple d'utilisation du script
unicorn_scan()
