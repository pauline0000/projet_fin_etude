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
