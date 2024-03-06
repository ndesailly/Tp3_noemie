from logiciel import *
def main():
    mediatheque = Mediatheque()
    while True:
        action = input("Voulez-vous ajouter un média ? (oui/non) : ")
        if action.lower() == 'oui':
            mediatheque.ajouter_media_interactif()
        else:
            break

    afficher = input("Voulez-vous afficher la collection de médias ? (oui/non) : ")
    if afficher.lower() == 'oui':
        mediatheque.afficher_medias()

if __name__ == "__main__":
    #unittest.main()
    main()