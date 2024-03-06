import unittest
from unittest import mock 
import io

class Media(object):
    def __init__(self, titre, auteur, date_parution):
        self._titre = titre
        self._auteur = auteur
        self._date_parution = date_parution

    def get_titre(self):
        return self._titre

    def set_titre(self, titre):
        self._titre = titre

    def get_auteur(self):
        return self._auteur

    def set_auteur(self, auteur):
        self._auteur = auteur

    def get_date_parution(self):
        return self._date_parution

    def set_date_parution(self, date_parution):
        self._date_parution = date_parution

    def __str__(self):
        return f"{self._titre} par {self._auteur}, paru en {self._date_parution}"



class Livre(Media):
    def __init__(self, titre, auteur, date_parution, nombre_pages, editeur):
        super().__init__(titre, auteur, date_parution)
        self._nombre_pages = nombre_pages
        self._editeur = editeur

    def get_nombre_pages(self):
        return self._nombre_pages

    def set_nombre_pages(self, nombre_pages):
        self._nombre_pages = nombre_pages

    def get_editeur(self):
        return self._editeur

    def set_editeur(self, editeur):
        self._editeur = editeur


class CD(Media):
    def __init__(self, titre, auteur, date_parution, duree, nombre_morceaux):
        super().__init__(titre, auteur, date_parution)
        self._duree = duree
        self._nombre_morceaux = nombre_morceaux

    def get_duree(self):
        return self._duree

    def set_duree(self, duree):
        self._duree = duree

    def get_nombre_morceaux(self):
        return self._nombre_morceaux

    def set_nombre_morceaux(self, nombre_morceaux):
        self._nombre_morceaux = nombre_morceaux


class DVD(Media):
    def __init__(self, titre, auteur, date_parution, duree):
        super().__init__(titre, auteur, date_parution)
        self._duree = duree

    def get_duree(self):
        return self._duree

    def set_duree(self, duree):
        self._duree = duree

class Mediatheque:
    def __init__(self):
        self.collection = []

    def ajouter_media(self, media):
        self.collection.append(media)

    def lister_medias_par_auteur(self, auteur):
        return [media for media in self.collection if media.auteur == auteur]

    def supprimer_media(self, titre, auteur):
        self.collection = [media for media in self.collection if not (media.titre == titre and media.auteur == auteur)]

    def marquer_comme_prete(self, titre, auteur, ami):
        for media in self.collection:
            if media.titre == titre and media.auteur == auteur:
                media.prete_a = ami
                return True
        return False

    def compter_medias_prete(self):
        return len([media for media in self.collection if hasattr(media, 'prete_a')])

    def supprimer_medias_par_auteur(self, auteur):
        self.collection = [media for media in self.collection if media.auteur != auteur]

    def ajouter_media_interactif(self):
        type_media = input("Entrez le type de média (Livre, CD, DVD, ArticleDeMagazine): ")
        titre = input("Entrez le titre: ")
        auteur = input("Entrez l'auteur: ")
        date_parution = input("Entrez la date de parution: ")

        if type_media.lower() == 'livre':
            nombre_pages = input("Entrez le nombre de pages: ")
            editeur = input("Entrez l'éditeur: ")
            media = Livre(titre, auteur, date_parution, nombre_pages, editeur)

        elif type_media.lower() == 'cd':
            duree = input("Entrez la durée: ")
            nombre_morceaux = input("Entrez le nombre de morceaux: ")
            media = CD(titre, auteur, date_parution, duree, nombre_morceaux)

        elif type_media.lower() == 'dvd':
            duree = input("Entrez la durée: ")
            media = DVD(titre, auteur, date_parution, duree)

        elif type_media.lower() == 'article de magazine':
            nom_magazine = input("Entrez le nom du magazine: ")
            numero_magazine = input("Entrez le numéro du magazine: ")
            intervalle_pages = input("Entrez l'intervalle des pages: ")
            media = ArticleDeMagazine(titre, auteur, date_parution, nom_magazine, numero_magazine, intervalle_pages)

        else:
            print("Type de média inconnu")
            return

        self.ajouter_media(media)
        print(f"{type_media} '{titre}' ajoute avec succes.")

    def afficher_medias(self):
        if not self.collection:
            print("La médiathèque est vide.")
        else:
            for media in self.collection:
                print(media)

class ArticleDeMagazine(Media):
    def __init__(self, titre, auteur, date_parution, nom_magazine, numero_magazine, intervalle_pages):
        super().__init__(titre, auteur, date_parution)
        self._nom_magazine = nom_magazine
        self._numero_magazine = numero_magazine
        self._intervalle_pages = intervalle_pages
    
    def get_nom_magazine(self):
        return self.nom_magazine

    def set_nom_magazine(self, nom_magazine):
        self._nom_magazine = nom_magazine

    def get_numero_magazine(self):
        return self._numero_magazine

    def set_numero_magazine(self, numero_magazine):
        self._numero_magazine = numero_magazine

    def get_intervalle_pages(self):
        return self._intervalle_pages

    def set_intervalle_pages(self, intervalle_pages):
        self._intervalle_pages = intervalle_pages

    def __str__(self):
        return f"{self._titre} par {self._auteur}, paru dans {self._nom_magazine} n°{self._numero_magazine}, pages {self._intervalle_pages}"


class TestMediatheque(unittest.TestCase):
    def setUp(self):

        self.mediatheque = Mediatheque()
        self.livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943, 96, "Gallimard")
        self.cd = CD("Random Access Memories", "Daft Punk", 2013, 74, 13)
        self.dvd = DVD("Inception", "Christopher Nolan", 2010, 148)
        self.mediatheque.ajouter_media(self.livre)
        self.mediatheque.ajouter_media(self.cd)
        self.mediatheque.ajouter_media(self.dvd)

    def test_ajouter_media(self):
        self.assertEqual(len(self.mediatheque.collection), 3)

    def test_supprimer_media(self):
        self.mediatheque.supprimer_media("Le Petit Prince", "Antoine de Saint-Exupéry")
        self.assertEqual(len(self.mediatheque.collection), 2)

    def test_supprimer_medias_par_auteur(self):
        # Tester la suppression de tous les médias d'un auteur donné
        self.mediatheque.ajouter_media(Livre("Vol de Nuit", "Antoine de Saint-Exupéry", 1931, 157, "Gallimard"))
        self.mediatheque.supprimer_medias_par_auteur("Antoine de Saint-Exupéry")
        self.assertEqual(self.mediatheque.lister_medias_par_auteur("Antoine de Saint-Exupéry"), [])

    def test_marquer_comme_prete(self):
        # Tester le marquage d'un média comme prêté
        reussite = self.mediatheque.marquer_comme_prete("Inception", "Christopher Nolan", "Alice")
        self.assertTrue(reussite)
        # Vérifier si le média est marqué comme prêté
        for media in self.mediatheque.collection:
            if media.titre == "Inception" and media.auteur == "Christopher Nolan":
                self.assertEqual(media.prete_a, "Alice")

    def test_compter_medias_prete(self):
        # Tester le comptage des médias prêtés
        self.mediatheque.marquer_comme_prete("Inception", "Christopher Nolan", "Alice")
        self.mediatheque.marquer_comme_prete("Random Access Memories", "Daft Punk", "Bob")
        self.assertEqual(self.mediatheque.compter_medias_prete(), 2)

    def test_lister_medias_par_auteur(self):
        # Ajouter un autre média par le même auteur pour tester
        autre_livre = Livre("Vol de Nuit", "Antoine de Saint-Exupéry", 1931, 157, "Gallimard")
        self.mediatheque.ajouter_media(autre_livre)
        result = self.mediatheque.lister_medias_par_auteur("Antoine de Saint-Exupéry")
        self.assertIn(self.livre, result)
        self.assertIn(autre_livre, result)

    def test_ajouter_article_magazine(self):
        article_magazine = ArticleDeMagazine("Science et Vie", "Marie Curie", 2021, "Nature", 451, "100-105")
        self.mediatheque.ajouter_media(article_magazine)
        self.assertIn(article_magazine, self.mediatheque.collection)

    @mock.patch('builtins.input')
    def test_ajouter_media_interactif(self, mock_input):
        # Définir les entrées simulées pour un média spécifique (par exemple, un Livre)
        mock_input.side_effect = ['Livre', 'Guerre et Paix', 'Léon Tolstoï', '1869', '1225', 'L\'éditeur']

        # Appeler la méthode ajouter_media_interactif
        self.mediatheque.ajouter_media_interactif()

        # Vérifier que le média a bien été ajouté à la collection
        self.assertEqual(len(self.mediatheque.collection), 4)  # 3 initialement + 1 ajouté
        self.assertIsInstance(self.mediatheque.collection[-1], Livre)
        self.assertEqual(self.mediatheque.collection[-1].titre, 'Guerre et Paix')

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_afficher_medias(self, mock_stdout):
        # Ajouter des médias pour tester l'affichage
        self.mediatheque.ajouter_media(self.livre)
        self.mediatheque.ajouter_media(self.cd)
        self.mediatheque.ajouter_media(self.dvd)

        # Appeler la méthode afficher_medias
        self.mediatheque.afficher_medias()

        # Récupérer le résultat de l'affichage
        result = mock_stdout.getvalue()

        # Vérifier que chaque média est correctement affiché
        self.assertIn("Le Petit Prince par Antoine de Saint-Exupéry", result)
        self.assertIn("Random Access Memories par Daft Punk", result)
        self.assertIn("Inception par Christopher Nolan", result)

