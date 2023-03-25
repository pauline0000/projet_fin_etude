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
