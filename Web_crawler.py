import requests

class web_crawler:



    def get_website(self):
        r = requests.get('https://ksh.nesa-sg.ch/loginto.php?pageid=9999&mode=2&lang=de', auth=('ajidan.jegatheeswaran', '10Scheisse'))
        print(r.status_code)
        print(r.text)

    def log_in(self, benutzername, passwort):
        #Sicherstellung, dass Benutzername und Passwort Strings sind
        if not isinstance(benutzername, str):
            benutzername = str(benutzername)

        if not isinstance(passwort, str):
            passwort = str(passwort)

        # Benutzernamen und Passwort definieren
        bp = {'login': 'ajidan.jegatheeswaran', 'passwort': '10Scheisse'}

        #Post-Methode
        r = requests.post('index.php?pageid=', data=bp)

        #Printen
        print(r.text)

    def get_page(self):
        pass


    if __name__ == '__main__':
        log_in()
