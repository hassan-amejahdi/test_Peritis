"""Vous pouvez accomplir cette tâche en utilisant Python en lisant le fichier d'entrée,
 en vérifiant chaque adresse IP et en écrivant
 les adresses IP correctes dans un fichier et les adresses IP incorrectes
 dans un autre fichier.
 Voici un exemple de code pour cela :"""
 
 import re

# Fonction pour vérifier si une adresse IP est correcte
def is_valid_ip(ip):
    # Utilisez une expression régulière pour vérifier si l'IP est valide
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    if re.match(pattern, ip):
        parts = ip.split('.')
        # Vérifiez si chaque partie est comprise entre 0 et 255
        if all(0 <= int(part) <= 255 for part in parts):
            return True
    return False

# Ouvrez le fichier d'entrée en lecture
with open('input.txt', 'r') as input_file:
    correct_ips = []
    incorrect_ips = []
    for line in input_file:
        ips = line.split()
        for ip in ips:
            if is_valid_ip(ip):
                correct_ips.append(ip)
            else:
                incorrect_ips.append(ip)

# Écrivez les adresses IP correctes dans un fichier
with open('correct_ips.txt', 'w') as correct_file:
    correct_file.write('\n'.join(correct_ips))

# Écrivez les adresses IP incorrectes dans un fichier
with open('incorrect_ips.txt', 'w') as incorrect_file:
    incorrect_file.write('\n'.join(incorrect_ips))
