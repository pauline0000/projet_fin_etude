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
