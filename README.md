# projet_fin_etude
Introduction 

Dans le cadre de notre master cybersécurité au sein de Sup de Vinci Paris, il nous a été demander de rendre notre projet de fin d’étude qui portait sur l’automatisation d’actions d’un analyste Red Team. 
Il a également été demandé de rendre le code source documenter et aussi d’un rapport complet (comment il s’utilise).

En effet, il nous a été demander pour cette année de rendre un travail sur l’automatisation des actions Red Team d’un analyste SOC. 
J’ai donc choisi de faire principalement tout mon projet avec le langage Python. En effet, c’est un des langages qui possède une syntaxe assez simple pour coder. De plus, Python possède une grande bibliothèque notamment avec de nombreux modules pour effectuer différentes tâches. Même s’il est vrai que j’avais envie de partir sur des playbook Ansible au début, mais je me suis vite rendu compte que ça n’allait pas être simple. 

J’ai également décider de stocker mes scripts sur une machine Kali Linux (une des dernières versions : 2022.4) en local. Effectivement, l’avantage qu’à la machine Kali Linux, c’est qu’elle offre déjà des outils intéressants.  

Nous allons alors nous demander : en quoi est-ce important d’automatiser des actions d’un analyse Red Team ?

Nous allons alors commencer par rappeler qu’elles sont les actions d’un analyse Red team. Puis nous allons voir le déroulement de l’automatisation d’un test d’intrusion, le scrapping des 20 dernières vulnérabilités critiques grâce au site NVD. 















Rappel du contexte : actions d’un analyse Red Team

Il est important de rappeler ce qu’est une Red Team et qu’elles sont les actions d’un analyste au sein de celle-ci. 


Tout d’abord, une Red team en cybersécurité correspond à une équipe de professionnels de la sécurité informatique chargée de simuler des attaques réelles sur les systèmes d'information d'une organisation pour tester leur niveau de sécurité. Leur objectif est de repérer les failles et les vulnérabilités du système, afin que l'organisation puisse les corriger avant qu'un attaquant réel ne les exploite.
Les membres de la Red Team sont des experts en sécurité informatique, qui utilisent des techniques et des outils sophistiqués pour simuler des attaques réelles sur le système de l'organisation. 



Ensuite, un analyste de la Red Team est chargé de simuler une attaque d'un adversaire potentiel sur le système d'information de l'organisation. 
Un analyste de la Red Team peut effectuer plusieurs actions comme la reconnaissance (active et passive) pour obtenir des informations sur l’organisation cible, tels que les noms de domaine, adresses IP, les utilisateurs, les vulnérabilités connues. 
De plus, l'analyste de la Red Team utilise des techniques d'ingénierie sociale pour tromper les employés de l'organisation et obtenir des informations sensibles telles que des mots de passe, des identifiants.
Il effectue également des tests de vulnérabilité pour identifier les vulnérabilités dans le système de l'organisation, en utilisant des outils d'analyse et d'audit de vulnérabilités automatisés, ainsi que des tests manuels.
De plus, il exploite les vulnérabilités identifiées pour obtenir un accès non autorisé au système de l'organisation.
Enfin, l'analyste de la Red Team prépare un rapport d'analyse détaillant les vulnérabilités identifiées, les méthodes d'attaque utilisées, les données récupérées et les recommandations pour améliorer la sécurité du système.








1 - Automatisation d’un test d’intrusion

1.1 - Reconnaissance 

Pour automatiser un test d’intrusion j’ai choisi principalement des outils cités dans la certification CEH. 
La première étape consiste à faire de la reconnaissance. Cette étape consiste à collecter des informations sur les systèmes cibles, y compris les adresses IP, les noms d'hôtes, les services en cours d'exécution, les applications web, les pare-feu, etc. Cette étape peut être effectuée à l'aide d'outils tels que Nmap, reconnaissance DNS, recherches sur les réseaux sociaux.
1.1.1 - Nmap

Pour commencer la reconnaissance j’ai décidé de faire un script nmap qui permet de scanner les ports qui sont ouverts et notamment à travers le biais d’un affichage de services importants. 
Pour rappel nmap est un outil de reconnaissance et de scan de port utilisé pour découvrir les hôtes et les services sur un réseau. 
Explication du code pour le script nmap -

 

1	 	On importe le module nmap avec l’instruction import

2	 	On commence par demander à l’utilisateur d’entrer l’adresse IP à scanner avec le module input(), pour qu’il y ait une interaction. 

3	 	On créer un objet nmap.PortScanner, qui est une classe qui définit le module nmap qu’on a importé plus haut.

4	 	Cette ligne de code utilise la méthode scan de l'objet nmap.PortScanner pour effectuer un scan de ports sur l'adresse IP spécifiée dans la variable target_ip. L'argument -F spécifie que nous souhaitons effectuer un scan de ports rapide.
5	 	Pour afficher les résultats du scan de ports, on va utiliser une boucle for qui parcourt tous les hôtes scannés (nm.all_hosts()). 

6	 	La liste des ports à afficher est stockée dans la variable port_list. Si le port est ouvert pour le protocole en cours, le code affiche le numéro de port et son état. J’ai choisi de prendre les ports les plus courants. 

1.1.2 - GRecon

Ensuite, dans l’étape de la reconnaissance il est également important de recueillir des informations au niveau des sous domaines, des pages d’inscriptions, etc. J’ai donc utilisé de choisir l’outil GRecon qui permet de recueillir toutes ces informations nécessaires à la reconnaissance. 
Pour rappel GRecon est un outil python simple qui automatise le processus de Google Based Redon AKA Google Dorking. Grâce à cet outil on peut trouver : des sous-domaines, des sous-sous-domaines, des pages d’incription/de connexion, des listes de répertoires, des documents exposés (pdf, xls, docx…), des entrées WordPress, également des collages de sites (enregistrements à patsebin, Ghostbin...)
Explication pour la partie GRecon -

Pour la partie GRecon j’ai pris un script qui existait déjà notamment sur GitHub. Puis j’ai effectué quelques étapes avant d’avoir l’outil complètement fonctionnel : 
- J’ai d’abord créé un dossier pour pouvoir recevoir les fichiers correspondant à l’outil GRecon (mkdir GRecon)
- Puis je l’ai cloné depuis GitHub avec la commande git clone https://github.com/adnane-X-tebbaa/GRecon.git dans un répertoire qui s’appelle GRecon
- Puis j’ai installé les packages requis pour exécuter l'outil qui se trouve dans le fichier qui se nomme requirements.txt (python3 -m pip install -r requirements.txt)
J’ai ensuite fait des tests pour voir si le script grecon.py fonctionnait bien. 
Dans le menu final, je l’ai rajouté afin qu’il s’exécute avec toutes les options. C’est avec l’instruction os.system que j’ai pu le faire exécuter (voir partie ). Cependant, j’ai eu quelques soucis, je devais mettre tous les fichiers téléchargés sur GitHub dans le répertoire où se trouvait mon script du menu final. 
 

1.1.3 – Sherlock

 

Ensuite, dans l’étape de reconnaissance il est également important de pouvoir rechercher des noms d’utilisateurs à travers une large gamme de réseaux sociaux comme Twitter, LinkedIn, et Instagram par exemple. C’est grâce à l’outil Sherlock que l’on va pouvoir effectuer ce travail de recherche. 
Pour cet outil j’ai procédé de la même façon de l’outil GRecon. 
Explication pour la partie Sherlock -
J’ai effectué les mêmes étapes que pour l’outil GRecon. J’ai cloné l’outil dans un répertoire puis une fois que tout était fonctionnel j’ai mis tous les fichiers dans le répertoire / (root) pour qu’il puisse fonctionner dans mon script où se trouve le menu final. 
 
Dans le menu final, j’ai codé pour faire en sorte que l’utilisateur puisse entrer un nom d’utilisateur et que ensuite l’outil Sherlock se lance en fonction de cette demande. 

1.2 – Scan de port  

Cette étape consiste à utiliser plusieurs outils de scan de ports pour identifier les ports ouverts sur les systèmes cibles. Les ports ouverts peuvent indiquer les services en cours d'exécution sur le système, ce qui peut aider à identifier les vulnérabilités potentielles. 

Ici, nous allons utiliser l’outil unicornscan. Unicornscan est un outil de scan de port rapide et évolutif. Il est capable de scanner plusieurs cibles en même temps. Il peut également être utilisé pour scanner les ports UDP. Il fallait au préalable installer les paquets correspondant à l’outil pour pouvoir ensuite lancer le script qui scan les ports. 

Dans mon script j’ai utilisé plusieurs commandes lier à l’outil pour avoir une meilleure verbosité au niveau des résultats de scan de ports. 

Explication du script avec Unicornscan -











Enumération : Cette étape consiste à recueillir des informations plus détaillées sur les services et les applications en cours d'exécution sur les systèmes cibles. Cela peut être fait en utilisant des outils tels que NetBIOS, SNMP, LDAP, SMB, etc.

Scan de vulnérabilité : Cette étape consiste à utiliser des outils de scan de vulnérabilités pour détecter les vulnérabilités sur les systèmes cibles. Les outils tels que Nessus, OpenVAS, Nexpose peuvent être utilisés pour effectuer un scan de vulnérabilité.

Analyse des résultats et exploitation : Cette étape consiste à analyser les résultats du scan de vulnérabilité pour identifier les vulnérabilités et les exploiter pour démontrer l'impact de la vulnérabilité. Cela peut être fait en utilisant des outils d'exploitation tels que Metasploit, Core Impact, etc.

2 – Scrapping des dernières vulnérabilités critiques up-to-date

C’est important pour un analyse Red team d’automatiser le scrapping des dernières vulnérabilités critiques up-to-date, car ça lui permet de gagner du temps. De plus, cela permet d’avoir les dernières vulnérabilités mises à jour en temps réel. 
C’est pour cela que j’ai choisi d’intégrer un script en python dans mon menu principal. Il permet d’afficher grâce à l’API du site NVD toutes les dernières vulnérabilités à partir du mois en cours (et à jour) et affiche des informations sur chacune d’entre elles puis exclusivement celles qui ont un impact de type CRITICAL ou HIGH. 
De plus, j’ai ajouté dans mon script nist5.py, une partie qui permet d’envoyer à l’adresse mail que l’utilisateur à rempli, tous les résultats.  

Explication du script pour récupérer les dernières vulnérabilités (à jour) par mail -

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

# Afficher les informations sur chaque vulnérabilité
for result in data['result']['CVE_Items']:
    # Récupérer les informations sur l'impact
    impact = result['impact']

    # Vérifier si la clé 'baseMetricV3' existe dans la réponse
    if 'baseMetricV3' in impact:
        severity = impact['baseMetricV3']['cvssV3']['baseSeverity']

        # Vérifier si l'impact est critique ou élevé
        if severity in ['CRITICAL', 'HIGH']:
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

# Demander l'email de l'utilisateur
email = input("Entrez votre adresse e-mail : ")

# Envoyer les résultats par email
gmail_user = "pauline.stephan5@gmail.com"
gmail_password = "nuxstodowonobbcv"

msg = MIMEMultipart()
msg['From'] = gmail_user
msg['To'] = email
msg['Subject'] = "Rapport des vulnérabilités récentes"

body = vulnerabilities_info
msg.attach(MIMEText(body, 'plain'))

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    text = msg.as_string()
    server.sendmail(gmail_user, email, text)
    server.quit()
    print(f"Les informations sur les vulnérabilités ont été envoyées avec succès à {email}.")
except Exception as e:
    print(f"Une erreur s'est produite lors de l'envoi de l'email : {str(e)}")
```





4 – Conclusion


5 - Sources des sites utilisés

Code beautity - https://codebeautify.org/python-formatter-beautifier# : pour mon code en python (notamment pour les indentations et les espaces)

Pypi - https://pypi.org/ : pour les modules à installer 

GRecon - https://github.com/TebbaaX/GRecon + https://www.geeksforgeeks.org/grecon-automates-the-process-of-google-dorking-on-linux/ : pour pouvoir intégrer l’outil Grecon dans mon script principal

Site NVD - https://nvd.nist.gov/vuln/full-listing/2023/3 : pour l’API du site

Site Kali - https://www.kali.org/tools/unicornscan/#unicornscan : pour Unicornscan
