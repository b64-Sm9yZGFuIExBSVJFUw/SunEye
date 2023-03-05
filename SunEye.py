from socket import * #Pour connexions
import optparse #Pour --help
import os
from termcolor import colored
from threading import * #Pour threads

#Prompt
prompt = "<(SUNEYE)> ~"

#Tentative de connexion à un port
def essaiPort(host, port):
        try: #Connexion....
                s = socket(AF_INET, SOCK_STREAM) #Création de socket IPv4 TCP
                s.connect((host,port)) #Connexion
                print(colored(prompt+" Le port " + str(port) +" est ouvert!", "green"))
        except: #Connexion échouée : Port fermé
                pass

#Scan de ports
def portScan(host, ports):
        print(colored("\n"+prompt+" Ports choisis:[ ","magenta"), end='')
        for port in ports:
                print(colored(str(port)+ " ", "magenta"), end='')

        print(colored(" ]","magenta"))

        try:
                print(colored(prompt+" Tentative de résolution (HOSTNAME -> IP)...", "blue"))
                ip = gethostbyname(host) #Résolution si adresse donnée
        except Exception:
                print(colored(prompt+ " Impossible de résoudre l'hôte "+host, "red"))
        try:
                print(colored(prompt+" Tentative de résolution (IP -> HOSTNAME)...\n", "blue"))
                hostname = gethostbyaddr(ip)
                print(colored(prompt+" Résultats de scans pour "+hostname[0]+" (IP="+ip+")", "yellow")) #Il s'agit d'une liste, le premier est l'hostname
        except: #Si pas d'hostname
                print(colored(prompt+" Résultats de scans pour "+ ip + ":", "yellow"))

        print(colored(prompt+" Scan en cours...\n","yellow"))
        setdefaulttimeout(0.5) #Evite l'attente

        #Début de scan
        for port in ports:
                #Un thread pour un scan
                t = Thread(target=essaiPort, args=(host, int(port)))
                t.start() #Lancement


def main():
        parser = optparse.OptionParser('Utilisation: ' + '-H <HOST> -p <PORT1>,<PORT2>....')
        parser.add_option('-H', dest="host", type='string', help="L'hôte") #Après le -H le contenu sera dans la variable host
        parser.add_option('-p', dest="port", type='string', help="Les ports séparés par des virgules")  # Après le -p le contenu sera dans la variable port
        (options, args) = parser.parse_args()

        #Récupération "réelle" des valeurs
        host = options.host
        port = str(options.port).split(',') #Les différents ports en tableau

        #Si paramètres incorrects (vides)
        if host == None or port[0] == None:
                print(parser.usage) #Affichage help
                exit(0)
        portScan(host, port)

if __name__ == '__main__':
        os.system("clear")
        print(colored("\t\t ___ _   _ _  _ _____   _____\n" +
              "\t\t/ __| | | | \| | __\ \ / / __|\n" +
              "\t\t\__ \ |_| | .` | _| \ V /| _|\n" +
              "\t\t|___/\___/|_|\_|___| |_| |___|\n","yellow"))

        print(colored("\t\tPort scanner by b64-Sm9yZGFuIExBSVJFUw\n\n","yellow"))

        main()
