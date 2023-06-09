# Projet de fin d'études
rédigé par Pauline STEPHAN - Classe Master Cybersécurité A - Sup de Vinci

## Sommaire 
- [Introduction](#introduction)
- [Rappel du contexte : actions d’un analyse Red Team](#rappel-du-contexte--actions-dun-analyse-red-team)
- [1 - Automatisation d’un test d’intrusion](#1---automatisation-dun-test-dintrusion)
- [2 - Scrapping des dernières vulnérabilités critiques up-to-date](#2---scrapping-des-dernières-vulnérabilités-critiques-up-to-date)
- [Conclusion](#conclusion)
- [Points d'améliorations](#points-daméliorations)
- [Sources des sites utilisés](#sources-des-sites-utilisés)
- [Code source final](#code-source-final)

## Introduction 

Dans le cadre de notre master cybersécurité au sein de Sup de Vinci Paris, il nous a été demander de rendre notre projet de fin d’étude qui portait sur l’automatisation d’actions d’un analyste Red Team. 
Il a également été demandé de rendre le code source documenter et aussi d’un rapport complet (comment il s’utilise). C'est pour cela que j'ai créer un Github afin de mettre mon code complet et également le Readme qui est pratique pour pouvoir tout expliquer. 

En effet, il nous a été demander pour cette année de rendre un travail sur l’automatisation des actions Red Team d’un analyste SOC. 
J’ai donc choisi de faire principalement tout mon projet avec le langage Python. En effet, c’est un des langages qui possède une syntaxe assez simple pour coder. De plus, Python possède une grande bibliothèque notamment avec de nombreux modules pour effectuer différentes tâches. Même s’il est vrai que j’avais envie de partir sur des playbook Ansible au début, mais je me suis vite rendu compte que ça n’allait pas être simple. 

⚙️ J’ai également décider de stocker mes scripts sur une machine Kali Linux (une des dernières versions : 2022.4) en local. Effectivement, l’avantage qu’à la machine Kali Linux, c’est qu’elle offre déjà des outils intéressants concernant les actions Red Team.  


:question: Nous allons alors nous demander : en quoi est-ce important d’automatiser des actions d’un analyse Red Team ?

Nous allons alors commencer par rappeler qu’elles sont les actions d’un analyse Red team. Puis nous allons voir le déroulement de l’automatisation d’un test d’intrusion, le scrapping des 20 dernières vulnérabilités critiques grâce à l'API du site NVD. 

*⚠ Il est possible que j'aie utilisé des outils déjà existants sur Github pour certaines parties, tels que sublister, GRecon et Sherlock, car ces outils étaient pertinents et n'étaient pas disponibles sur la VM Kali Linux. Cependant, pour la plupart des tâches, j'ai utilisé des outils qui étaient déjà présents sur la machine Kali.*

## **Rappel du contexte : actions d’un analyse Red Team**

Il est important de rappeler ce qu’est une Red Team et qu’elles sont les actions d’un analyste au sein de celle-ci. 


Tout d’abord, une Red team en cybersécurité correspond à une équipe de professionnels de la sécurité informatique chargée de simuler des attaques réelles sur les systèmes d'information d'une organisation pour tester leur niveau de sécurité. Leur objectif est de repérer les failles et les vulnérabilités du système, afin que l'organisation puisse les corriger avant qu'un attaquant réel ne les exploite.
Les membres de la Red Team sont des experts en sécurité informatique, qui utilisent des techniques et des outils sophistiqués pour simuler des attaques réelles sur le système de l'organisation. 



Ensuite, un analyste de la Red Team est chargé de simuler une attaque d'un adversaire potentiel sur le système d'information de l'organisation. 
Un analyste de la Red Team peut effectuer plusieurs actions comme la reconnaissance (active et passive) pour obtenir des informations sur l’organisation cible, tels que les noms de domaine, adresses IP, les utilisateurs, les vulnérabilités connues. 

De plus, l'analyste de la Red Team utilise des techniques d'ingénierie sociale pour tromper les employés de l'organisation et obtenir des informations sensibles telles que des mots de passe, des identifiants.
Il effectue également des tests de vulnérabilité pour identifier les vulnérabilités dans le système de l'organisation, en utilisant des outils d'analyse et d'audit de vulnérabilités automatisés, ainsi que des tests manuels.

De plus, il exploite les vulnérabilités identifiées pour obtenir un accès non autorisé au système de l'organisation.

Enfin, l'analyste de la Red Team prépare un rapport d'analyse détaillant les vulnérabilités identifiées, les méthodes d'attaque utilisées, les données récupérées et les recommandations pour améliorer la sécurité du système.



# 1 - Automatisation d’un test d’intrusion

## 1.1 - Reconnaissance 

Pour automatiser un test d’intrusion j’ai choisi principalement des outils cités dans la certification CEH. 
La première étape consiste à faire de la reconnaissance. Cette étape consiste à collecter des informations sur les systèmes cibles, y compris les adresses IP, les noms d'hôtes, les services en cours d'exécution, les applications web, les pare-feu, etc. Cette étape peut être effectuée à l'aide d'outils tels que Nmap, reconnaissance DNS, recherches sur les réseaux sociaux.

### 1.1.1 - Nmap

Pour commencer la reconnaissance j’ai décidé de faire un script nmap qui permet de scanner les ports qui sont ouverts et notamment à travers le biais d’un affichage de services importants. 
Pour rappel nmap est un outil de reconnaissance et de scan de port utilisé pour découvrir les hôtes et les services sur un réseau. 

Explication du code pour le script nmap -

```
import nmap

# Demander à l'utilisateur d'entrer l'adresse IP à scanner
target_ip = input("Entrez l'adresse IP à scanner : ")

# Créer un objet nmap.PortScanner
nm = nmap.PortScanner()

# Effectuer un scan de port sur l'adresse IP spécifiée
nm.scan(target_ip, arguments='-F')

# Afficher les résultats du scan
for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)

        # Afficher les ports les plus courants pour le protocole en cours
        port_list = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 1433, 1521, 3306, 3389, 5432, 8080]
        for port in port_list:
            if port in nm[host][proto]:
                print('Port : %s\tState : %s' % (port, nm[host][proto][port]['state']))
 ```

- On importe le module nmap avec l’instruction *import*
- On commence par demander à l’utilisateur d’entrer l’adresse IP à scanner avec le module *input()*, pour qu’il y ait une interaction. 
- On créer un objet nmap.PortScanner, qui est une classe qui définit le module *nmap* qu’on a importé plus haut.
- Cette ligne de code utilise la méthode scan de l'objet *nmap.PortScanner* pour effectuer un scan de ports sur l'adresse IP spécifiée dans la variable *target_ip*.
- L'argument *-F* spécifie que nous souhaitons effectuer un scan de ports rapide.
- Pour afficher les résultats du scan de ports, on va utiliser une boucle for qui parcourt tous les hôtes scannés *(nm.all_hosts())*. 
- La liste des ports à afficher est stockée dans la variable *port_list*. Si le port est ouvert pour le protocole en cours, le code affiche le numéro de port et son état. J’ai choisi de prendre les ports les plus courants. 

### 1.1.2 - GRecon

Ensuite, dans l’étape de la reconnaissance il est également important de recueillir des informations au niveau des sous domaines, des pages d’inscriptions, etc. J’ai donc utilisé de choisir l’outil GRecon qui permet de recueillir toutes ces informations nécessaires à la reconnaissance. 
Pour rappel GRecon est un outil python simple qui automatise le processus de Google Based Redon AKA Google Dorking. Grâce à cet outil on peut trouver : des sous-domaines, des sous-sous-domaines, des pages d’incription/de connexion, des listes de répertoires, des documents exposés (pdf, xls, docx…), des entrées WordPress, également des collages de sites (enregistrements à patsebin, Ghostbin...)
Explication pour la partie GRecon -

Pour la partie GRecon j’ai pris un script qui existait déjà notamment sur GitHub. Puis j’ai effectué quelques étapes avant d’avoir l’outil complètement fonctionnel : 
- J’ai d’abord créé un dossier pour pouvoir recevoir les fichiers correspondant à l’outil GRecon (mkdir GRecon)
- Puis je l’ai cloné depuis GitHub avec la commande git clone https://github.com/adnane-X-tebbaa/GRecon.git dans un répertoire qui s’appelle GRecon
- Puis j’ai installé les packages requis pour exécuter l'outil qui se trouve dans le fichier qui se nomme requirements.txt (python3 -m pip install -r requirements.txt)
J’ai ensuite fait des tests pour voir si le script grecon.py fonctionnait bien. 
Dans le menu final, je l’ai rajouté afin qu’il s’exécute avec toutes les options. C’est avec l’instruction os.system que j’ai pu le faire exécuter (voir partie ). Cependant, j’ai eu quelques soucis, je devais mettre tous les fichiers téléchargés sur GitHub dans le répertoire où se trouvait mon script du menu final. 
 

### 1.1.3 - Sherlock

 

Ensuite, dans l’étape de reconnaissance il est également important de pouvoir rechercher des noms d’utilisateurs à travers une large gamme de réseaux sociaux comme Twitter, LinkedIn, et Instagram par exemple. C’est grâce à l’outil Sherlock que l’on va pouvoir effectuer ce travail de recherche. 
Pour cet outil j’ai procédé de la même façon de l’outil GRecon. 
Explication pour la partie Sherlock -
J’ai effectué les mêmes étapes que pour l’outil GRecon. J’ai cloné l’outil dans un répertoire puis une fois que tout était fonctionnel j’ai mis tous les fichiers dans le répertoire / (root) pour qu’il puisse fonctionner dans mon script où se trouve le menu final. 
 
Dans le menu final, j’ai codé pour faire en sorte que l’utilisateur puisse entrer un nom d’utilisateur et que ensuite l’outil Sherlock se lance en fonction de cette demande. 

## 1.2 - Scan de port  

Cette étape consiste à utiliser plusieurs outils de scan de ports pour identifier les ports ouverts sur les systèmes cibles. Les ports ouverts peuvent indiquer les services en cours d'exécution sur le système, ce qui peut aider à identifier les vulnérabilités potentielles. 

Ici, nous allons utiliser l’outil unicornscan. Unicornscan est un outil de scan de port rapide et évolutif. Il est capable de scanner plusieurs cibles en même temps. Il peut également être utilisé pour scanner les ports UDP. Il fallait au préalable installer les paquets correspondant à l’outil pour pouvoir ensuite lancer le script qui scan les ports. 

Dans mon script j’ai utilisé plusieurs commandes lier à l’outil pour avoir une meilleure verbosité au niveau des résultats de scan de ports. 


### Explication du script avec Unicornscan -

```
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
```

- Demande à l'utilisateur de saisir une adresse IP, puis utilise la commande Unicornscan pour scanner les ports UDP et TCP de cette adresse IP
- La commande Unicornscan est générée en utilisant la fonction *f-string* pour remplacer l'adresse IP dans la commande
- Utilise les options *-mU* et *-mT* pour spécifier que les ports UDP et TCP doivent être scannés + l'option *-p* pour spécifier la plage de ports à scanner (ici, les ports de 1 à 1000)
- Les résultats sont stockés dans une variable *results_udp_tcp* à l'aide de la fonction *os.popen()*, qui exécute la commande Unicornscan et retourne



## 1.3 - Enumération 
L'énumération en cybersécurité est le processus de collecte d'informations sur une cible spécifique, comme un système informatique, un réseau, une application, un site web ou même une organisation, dans le but de préparer une attaque ou de vérifier la sécurité de la cible.


Pré-requis : enum4linux, fierce

### Explication du code -  

```
import subprocess

#Demander l'adresse cible à l'utilisateur
target = input("Entrez l'adresse cible : ")

#Liste des commandes à exécuter
commands = [
f"whois {target}",
f"nslookup {target}",
f"nslookup -query=MX {target}",
f"dig {target}",
f"dig -t MX {target}",
f"nmap -sn {target}",
f"nmap -p 21,22,25,80,110,143,161,443 {target}",
f"nmap -sV {target}",
f"nmap -O {target}",
f"nmap -sU -p 123 --open {target}",
f"nmap -p 389 {target} && echo 'Le port LDAP est ouvert' || echo 'Le port LDAP est fermé'",
f"enum4linux -a {target}",
f"fierce --domain {target}"
]

#Exécuter chaque commande et afficher le résultat
for command in commands:
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)
```

- Demande d'abord à l'utilisateur l'adresse cible sur laquelle les commandes seront exécutées
- Exécute chaque commande de la liste *"commands"* en utilisant le module *"subprocess"* de Python
- La sortie est capturée à l'aide de l'option *"capture_output=True"* et retournée sous forme de texte à l'aide de l'option *"text=True"* dans la méthode *"subprocess.run"*
- Les commandes sont utilisées pour effectuer différentes tâches de reconnaissance et de découverte de services, telles que la récupération d'informations WHOIS, la résolution DNS, la numérisation de ports et la recherche d'informations sur les services disponibles sur la cible
- Une boucle "for" exécute chaque commande dans la liste et stocke le résultat dans une variable "result"

## 1.4 - Scan de vulnérabilité

Le scan de vulnérabilité est une étape importante dans le cadre d'une opération de Red Team. En effet, le but de la Red Team est de tester la sécurité d'un système, d'une infrastructure ou d'une application en imitant les techniques et les tactiques d'un attaquant réel.
Pour cela j'ai utilisé un outil qui était déja présent sur la VM Kali Linux. 

Il s'agit de WPScan. WPScan est un outil open-source de test de sécurité pour WordPress. Il permet de scanner des sites WordPress pour détecter les vulnérabilités et les failles de sécurité connues. De plus, j'ai ajouté dans ce script que si ça ne correspondait pas à un site wordpress, il fallait executer la commande nikto -h sur une url cible. 

Au début, j'étais partie sur l'automatisation de Nessus avec son API. Seulement, je n'ai pas réussi à configurer. 

### Explication du code -
```
import subprocess

# Demander à l'utilisateur l'URL cible
url = input("Entrez l'URL cible : ")

# Lancer la commande wpscan avec l'URL cible
wpscan_command = f"wpscan --url {url}"
wpscan_result = subprocess.run(wpscan_command, shell=True, capture_output=True, text=True)

# Vérifier si le résultat de wpscan contient le message d'erreur "Scan Aborted: The target is responding with a 403, this might be due to a WAF"
if "Scan Aborted: The target is responding with a 403, this might be due to a WAF" in wpscan_result.stdout:
    # Si oui, lancer la commande nikto avec l'URL cible
    nikto_command = f"nikto -h {url}"
    subprocess.run(nikto_command, shell=True)
else:
    # Si non, afficher le résultat de wpscan
    print(wpscan_result.stdout)
```
- Utilise la bibliothèque Python *subprocess* pour lancer des commandes dans le terminal
- Demandé à l'utilisateur l'URL cible qui sera stockée dans la variable *cible*
- Utilise la commande *wpscan* pour effectuer une vérification de sécurité sur le site web
- Le résultat de la commande wpscan est stocké dans la variable *wpscan_result* à l'aide de la fonction subprocess.run()
- Vérifie si le résultat de la commande wpscan contient le message d'erreur *"Scan Aborted: The target is responding with a 403, this might be due to a WAF"*. Si le message d'erreur est présent, le script lance la commande *nikto -h* sur l'URL cible.
- Sinon, si le message d'erreur n'est pas présent, le script affiche le résultat de la commande wpscan à l'aide de la fonction print()

## 1.5 - Analyse des résultats et exploitation 

Cette étape consiste à analyser les résultats du scan de vulnérabilité pour identifier les vulnérabilités et les exploiter pour démontrer l'impact de la vulnérabilité. Malheuresement, je n'ai pas eu le temps de réaliser cette partie. De plus, n'ayant pas d'URL de test je considère que cela est complexe. Cependant, de nombreux outils d'exploitation peut être utilisé comme Metasploit par exemple.

Nous allons maintenant passer à la deuxième et dernière action d'un analyste Red Team que j'ai automatisé : le scrapping des dernières vulnérabilités critiques up-to-date. 
                                 
 # 2 - Scrapping des dernières vulnérabilités critiques up-to-date

C’est important pour un analyse Red team d’automatiser le scrapping des dernières vulnérabilités critiques up-to-date, car ça lui permet de gagner du temps. De plus, cela permet d’avoir les dernières vulnérabilités mises à jour en temps réel. Le scraping (ou scrapping) est une technique informatique qui consiste à extraire des données d'un site web en les récupérant de manière automatique.

C’est pour cela que j’ai choisi d’intégrer un script en python dans mon menu principal. Il permet d’afficher grâce à l’API du site NVD toutes les dernières vulnérabilités à partir du mois en cours (et à jour) et affiche des informations sur chacune d’entre elles puis exclusivement celles qui ont un impact de type CRITICAL ou HIGH. 

J'ai donc ajouté dans mon script nist6.py dans mon menu principal. J'ai notamment ajouté une partie qui permet d’envoyer les résultats à l’adresse mail que l’utilisateur à rempli, et que si il y a pas de vulnérabilités critiques à jour, rien ne lui est envoyé. 

Je tiens à préciser qu'il m'a fallu générer plus de 6 versions de scripts avant d'avoir un script python fonctionnel. 

```
import requests
import json
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Obtenir la date actuelle et la convertir en format requis pour l'API NVD
now = datetime.now()
year = str(now.year)
month = str(now.month).zfill(2)
day = str(now.day).zfill(2)
start_date = f"{year}-{month}-01T00:00:00:000 UTC-00:00"
end_date = f"{year}-{month}-{day}T23:59:59:999 UTC-00:00"

# URL de l'API NVD pour récupérer les vulnérabilités récentes
url = f"https://services.nvd.nist.gov/rest/json/cves/1.0?resultsPerPage=20&pubStartDate={start_date}&pubEndDate={end_date}"

# Faire la demande HTTP GET
response = requests.get(url)

# Convertir la réponse JSON en objet Python
data = json.loads(response.text)

# Créer un string pour stocker les informations sur les vulnérabilités
vulnerabilities_info = ""

# Afficher les informations sur chaque vulnérabilité ayant un impact assigné
vulnerabilities_found = False
for result in data['result']['CVE_Items']:
    # Récupérer les informations sur l'impact
    impact = result['impact']

    # Vérifier si la clé 'baseMetricV3' existe dans la réponse
    if 'baseMetricV3' in impact:
        severity = impact['baseMetricV3']['cvssV3']['baseSeverity']

        # Vérifier si l'impact est critique ou élevé
        if severity in ['CRITICAL', 'HIGH']:
            vulnerabilities_found = True
            # Récupérer les informations sur la vulnérabilité
            cve_id = result['cve']['CVE_data_meta']['ID']
            description = result['cve']['description']['description_data'][0]['value']

            # Stocker les informations sur la vulnérabilité dans le string
            vulnerabilities_info += f"ID: {cve_id}\n"
            vulnerabilities_info += f"Description: {description}\n"
            vulnerabilities_info += f"Impact: {severity}\n"
            vulnerabilities_info += "-" * 50 + "\n"

            # Afficher les informations sur la vulnérabilité
            print(f"ID: {cve_id}")
            print(f"Description: {description}")
            print(f"Impact: {severity}")
            print("-" * 50)
    else:
        # Afficher un message d'erreur si la clé 'baseMetricV3' n'existe pas
        print(f"La vulnérabilité {result['cve']['CVE_data_meta']['ID']} n'a pas d'impact assigné.")

# Si aucune vulnérabilité avec impact assigné n'a été trouvée, afficher un message à l'utilisateur
if not vulnerabilities_found:
    print("Il n'y a pas de vulnérabilités critiques ou élevées aujourd'hui.")

# Demander l'email de l'utilisateur si des vulnérabilités ont été trouvées
else:
    email = input("Entrez votre adresse e-mail : ")

    # Envoyer les résultats par email (expéditeur)
    gmail_user = "pauline.stephan5@gmail.com"
    gmail_password = "nuxstodowonobbcv"
    
    #Objet MIMEMultipart qui permet de construire un message e-mail contenant un texte brut
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = email
    msg['Subject'] = "Rapport des vulnérabilités récentes"

    body = vulnerabilities_info
    msg.attach(MIMEText(body, 'plain'))

    #Envoi du message e-mail
    try:
        #Essaie d'abord de se connecter au serveur SMTP de Gmail en utilisant le port 465 et le protocole SSL
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        text = msg.as_string()

        #Envoie le message à l'aide de la méthode sendmail()
        server.sendmail(gmail_user, email, text)
        server.quit()
        print(f"Les informations sur les vulnérabilités ont été envoyées avec succès à {email}.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'envoi de l'email : {str(e)}")
```
## Précisions sur le script pour récupérer les dernières vulnérabilités (à jour) par mail -

- requests : permet de faciliter les requêtes HTTP depuis Python, notamment pour accéder à des API en ligne.

- json : permet de convertir des données JSON en objets Python, ou inversement.

- datetime : fournit des classes pour travailler avec des dates et des heures en Python, notamment pour obtenir la date actuelle.

- smtplib : permet d'envoyer des e-mails depuis Python en utilisant le protocole SMTP.

- email.mime.multipart : fournit des classes pour la création et la manipulation d'e-mails multiparts, qui peuvent inclure des pièces jointes et des parties de texte ou HTML.

- email.mime.text : fournit une classe pour la création de parties de texte pour les e-mails.
                                

- now = datetime.now() : crée un objet datetime représentant la date et l'heure actuelles.

- year = str(now.year) : convertit l'année en chaîne de caractères pour pouvoir l'utiliser dans la construction de la chaîne de date.

- month = str(now.month).zfill(2) : convertit le mois en chaîne de caractères, avec un zéro ajouté devant si nécessaire pour obtenir deux chiffres (par exemple, "03" pour mars).

- day = str(now.day).zfill(2) : convertit le jour en chaîne de caractères, avec un zéro ajouté devant si nécessaire pour obtenir deux chiffres (par exemple, "07" pour le 7ème jour du mois).

- start_date = f"{year}-{month}-01T00:00:00:000 UTC-00:00" : construit une chaîne de date pour le début du mois en cours, en utilisant l'année, le mois et le jour "01", ainsi qu'une heure, des minutes et des secondes de "00" et des millisecondes de "000". La chaîne est également complétée avec le fuseau horaire UTC.

- end_date = f"{year}-{month}-{day}T23:59:59:999 UTC-00:00" : construit une chaîne de date pour la fin du jour en cours, en utilisant l'année, le mois et le jour en cours, ainsi qu'une heure, des minutes et des secondes de "23", des millisecondes de "999" et le fuseau horaire UTC.



# Conclusion

Pour répondre à la problématique, je dirais que c'est important d’automatiser des actions d’un analyse Red Team, car cela fait gagner du temps à l'analyste. De plus, cela permet d'avoir des données à jour et temps réel notamment pour les dernières vulnérabilités critiques. 

# Points d'améliorations

- Avoir une adresse IP ou une URL cible de test pour simuler nos scripts légalement
- Améliorer la partie test d'intrusion, notamment sur les vulnérabilités trouvées, établir un impact en fonction de ce qui est trouvé
- Faire en sorte que les résultats trouvés lors du test d'intrusion soient stockés dans un fichier .txt


# Sources des sites utilisés

Code beautity - https://codebeautify.org/python-formatter-beautifier# : pour mon code en python (notamment pour les indentations et les espaces)

Pypi - https://pypi.org/ : pour les modules à installer 

GRecon - https://github.com/TebbaaX/GRecon + https://www.geeksforgeeks.org/grecon-automates-the-process-of-google-dorking-on-linux/ : pour pouvoir intégrer l’outil Grecon dans mon script principal

Site NVD - https://nvd.nist.gov/vuln/full-listing/2023/3 : pour l’API du site

Site Kali - https://www.kali.org/tools/unicornscan/#unicornscan : pour Unicornscan

# Code source final 
```
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
```
