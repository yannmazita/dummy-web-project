from django.core.management.base import BaseCommand
from datetime import datetime
from ...models import (
    Adherents,
    Arbitre,
    Archives,
    Catalogue,
    Categories,
    Contacts,
    Courriels,
    Creneaux,
    Documents,
    Entraine,
    Entrainements,
    Equipes,
    Joue,
    Matchs,
    Postes,
    Salles,
    Telephones,
)


def noneReplace(model, value):
    """Replaces None values in model definition.
    Args:
        model: The model.
        value: The value of the id key in the model.
    Returns:
        Either None or model.objects.get(id=value)
    """
    if value is None:
        return None
    else:
        return model.objects.get(id=value)


def ajouterCategories():
    data = [
        (1, "M7", "Baby", None, 2009, 80),
        (2, "M9", "Pupilles", 2007, 2008, 100),
        (3, "M11", "Poussins", 2005, 2006, 100),
        (4, "M13", "Benjamins", 2003, 2004, 100),
        (5, "M15", "Minimes", 2001, 2002, 115),
        (6, "M17", "Cadets", 1999, 2000, 115),
        (7, "M20", "Juniors et Espoirs", 1996, 1998, 125),
        (8, "Seniors", None, 1995, None, 135),
        (9, "FSGT", None, 1995, None, 105),
    ]

    for item in data:
        category = Categories(
            id=item[0],
            categorie=item[1],
            description=item[2],
            annee_deb=item[3],
            annee_fin=item[4],
            tarif=item[5],
        )
        category.save()
    print("Categorie table handled")


def ajouterEquipes():
    data = [
        (
            1,
            1,
            "M7 (Ecole de volley)",
            0,
            0,
            0,
            0,
            "./img/equipes/ecole_volley.jpg",
            "t",
        ),
        (
            2,
            2,
            "M9 (Ecole de volley)",
            0,
            0,
            0,
            0,
            "./img/equipes/ecole_volley.jpg",
            "t",
        ),
        (3, 3, "M11 (Poussins / Poussines)", 0, 0, 0, 0, "./img/equipes/m11.jpg", "t"),
        (4, 4, "M13 M (Benjamins)", 0, 0, 0, 0, None, "t"),
        (5, 4, "M13 F (Benjamines)", 0, 0, 0, 0, "./img/equipes/m13f.jpg", "t"),
        (6, 5, "M15 M (Minimes M)", 0, 0, 0, 0, None, "t"),
        (7, 5, "M15 F (Minimes F)", 0, 0, 0, 0, "./img/equipes/m15f.jpg", "t"),
        (8, 7, "M20 F (Juniors F)", 0, 0, 0, 0, None, "t"),
        (
            22,
            3,
            "M11F2 (Poussines)",
            None,
            None,
            None,
            None,
            "./img/equipes/amours.jpg",
            "t",
        ),
        (
            23,
            3,
            "M11 2 (Poussins)",
            None,
            None,
            None,
            None,
            "./img/equipes/amours.jpg",
            "t",
        ),
    ]

    for item in data:
        equipe = Equipes(
            id=item[0],
            id_categorie=noneReplace(Categories, item[1]),
            nom=item[2],
            points=item[3],
            victoires=item[4],
            defaites=item[5],
            nulls=item[6],
            photo=item[7],
            club=item[8],
        )
        equipe.save()
    print("Equipes table handled")


def ajouterPostes():
    data = [
        (1, "Président(e)", "Le chef"),
        (2, "Secrétaire", "Ben un poste de secrétaire quoi ..."),
        (3, "Comptable", "Le chef"),
        (4, "Entraineur referent", "Le referent des entraineurs"),
    ]

    for item in data:
        poste = Postes(id=item[0], designation=item[1], description=item[2])
        poste.save()

    print("Postes table handled")


def ajouterAdherents():
    data = [
        (
            1,
            1,
            None,
            "azlouni.sirine",
            "123",
            "AZLOUNI",
            "Sirine",
            4568792,
            "2008-11-25",
            "F",
            1,
            3,
            "f",
            "f",
        ),
        (
            2,
            1,
            None,
            "delmotte.camille",
            "123",
            "DELMOTTE",
            "Camille",
            456443,
            "2009-05-21",
            "F",
            1,
            3,
            "f",
            "f",
        ),
        (
            3,
            1,
            None,
            "guers.louna",
            "123",
            "GUERS",
            "Louna",
            3467924,
            "2007-04-12",
            "F",
            0,
            3,
            "f",
            "f",
        ),
        (
            4,
            1,
            None,
            "journade.mathieu",
            "123",
            "JOURNADE",
            "Mathieu",
            2467923,
            "2008-08-10",
            "M",
            0,
            3,
            "f",
            "f",
        ),
        (
            5,
            1,
            None,
            "legal.camille",
            "123",
            "LEGAL",
            "Camille",
            288924,
            "2009-01-05",
            "F",
            0,
            3,
            "f",
            "f",
        ),
        (
            6,
            2,
            None,
            "lemetayer.gaetane",
            "123",
            "LEMETAYER",
            "Gaetane",
            8534456,
            "2007-02-18",
            "F",
            0,
            3,
            "f",
            "f",
        ),
        (
            7,
            2,
            None,
            "vigier.maxens",
            "123",
            "VIGIER",
            "Maxens",
            259335,
            "2010-03-13",
            "M",
            0,
            3,
            "f",
            "f",
        ),
        (
            8,
            2,
            None,
            "virgili.margaux",
            "123",
            "VIRGILI",
            "Margaux",
            1464931,
            "2008-11-27",
            "F",
            0,
            3,
            "f",
            "f",
        ),
        (
            0,
            3,
            None,
            "test",
            "test",
            "admin",
            "grand chef",
            0,
            "2005-10-10",
            "M",
            1,
            1,
            "f",
            "f",
        ),
    ]

    for item in data:
        print(f"\nid_poste={item[2]}\n")
        adherent = Adherents(
            id=item[0],
            id_categorie=noneReplace(Categories, item[1]),
            id_poste=noneReplace(Postes, item[2]),
            login=item[3],
            mdp=item[4],
            nom=item[5],
            prenom=item[6],
            no_licence=item[7],
            date_naissance=item[8],
            genre=item[9],
            surclassement=item[10],
            habilitation=item[11],
            arbitre=item[12],
            entraineur=item[13],
        )
        adherent.save()
    print("Adherents table handled")


def ajouterArchives():
    data = [
        (
            1,
            "R1 féminines championnes !",
            "A",
            "",
            "Nos R1 filles sont championnes régionales",
            "",
            0,
            "2016-05-30",
            0,
            "2016-05-31",
        ),
        (
            2,
            "R1 masculin champions !",
            "A",
            "",
            "Nos R1 garçons sont champions région",
            "",
            0,
            "2016-05-31",
            0,
            "2016-05-31",
        ),
        (
            3,
            "Victoire des M11",
            "A",
            "./img/articles/m11.jpg",
            "Superbe victoire des M11 au TQO ;-)",
            "",
            0,
            "2016-05-31",
            0,
            "2016-05-31",
        ),
        (
            4,
            "M11F test",
            "A",
            "./img/articles/amourJuB.jpg",
            "test blabla trop cool",
            "",
            1,
            "2016-06-09",
            0,
            "2016-06-09",
        ),
    ]

    for item in data:
        archive = Archives(
            id=item[0],
            titre=item[1],
            type=item[2],
            lien_photo=item[3],
            contenu=item[4],
            lien_document=item[5],
            id_createur=noneReplace(Adherents, item[6]),
            date_creation=item[7],
            id_validateur=noneReplace(Adherents, item[8]),
            date_validation=item[9],
        )
        archive.save()
    print("Archives table handled")


def ajouterEntraine():
    entraine = Entraine(
        id_entraineur=noneReplace(Adherents, 1),
        id_equipe=noneReplace(Equipes, 1),
        ordre=1,
    )

    entraine.save()
    print("Entraine table handled")


def ajouterJoue():
    joue = Joue(
        id_adherent=noneReplace(Adherents, 4),
        id_equipe=noneReplace(Equipes, 3),
    )

    joue.save()
    print("Joue table handled")


def ajouterContacts():
    contact = Contacts(
        id=1,
        id_adherent=noneReplace(Adherents, 1),
        nom="AZLOUNI",
        prenom="Sirine",
        adresse="adresse",
        code_postal=31000,
        ville="Toulouse",
        complement=None,
        remarque=None,
        ordre=0,
    )

    contact.save()
    print("Contact table handled")


def ajouterCourriels():
    courriel1 = Courriels(
        id_contact=noneReplace(Contacts, 1),
        courriel="azlouni.sirine@hotmail.fr",
        ordre=None,
    )

    courriel2 = Courriels(
        id_contact=noneReplace(Contacts, 1),
        courriel="azlouni.sirine@gmail.com",
        ordre=None,
    )

    courriel1.save()
    courriel2.save()
    print("Courriels table handled")


def ajouterDocuments():
    data = [
        (
            1,
            "Test article",
            "A",
            "./img/articles/m11.jpg",
            "blabla bla",
            None,
            0,
            "2016-05-30",
            0,
            "2016-05-30",
            3,
        ),
        (
            2,
            "M13F article",
            "A",
            "./img/articles/m13f.jpg",
            "Super match des MF ce Week-end !",
            None,
            0,
            "2016-05-31",
            0,
            "2016-05-31",
            4,
        ),
        (
            7,
            "Victoire des M11 2",
            "A",
            "./img/articles/amours2016.JPG",
            "test",
            None,
            0,
            "2016-06-09",
            0,
            "2016-06-09",
            23,
        ),
    ]

    for item in data:
        document = Documents(
            id=item[0],
            titre=item[1],
            type=item[2],
            lien_photo=item[3],
            contenu=item[4],
            lien_document=item[5],
            id_createur=noneReplace(Adherents, item[6]),
            date_creation=datetime.strptime(item[7], "%Y-%m-%d"),
            id_validateur=noneReplace(Adherents, item[8]),
            date_validation=datetime.strptime(item[9], "%Y-%m-%d"),
            id_equipe=noneReplace(Equipes, item[10]),
        )
        document.save()
    print("Documents table handled")


def ajouterCatalogues():
    """Model field des_comp needs to be defined in spec, useless function as of now."""
    if False:
        data = [
            (1, "Ballon MOLTEN", None, None, None, 20, "./img/boutique/ballon.png"),
            (
                2,
                "Genouillères ASICS",
                None,
                "S",
                "Bleu foncé",
                10,
                "./img/boutique/genouilleres.jpg",
            ),
            (
                3,
                "Genouillères ASICS",
                None,
                "M",
                "Bleu foncé",
                10,
                "./img/boutique/genouilleres.jpg",
            ),
            (
                4,
                "Genouillères ASICS",
                None,
                "L",
                "Bleu foncé",
                10,
                "./img/boutique/genouilleres.jpg",
            ),
            (
                5,
                "Genouillères coque",
                None,
                "M",
                "Noir",
                24,
                "./img/boutique/genouilleres_coque.png",
            ),
            (
                6,
                "Genouillères coque",
                None,
                "L",
                "Noir",
                24,
                "./img/boutique/genouilleres_coque.png",
            ),
            (
                7,
                "Genouillères coque",
                None,
                "XL",
                "Noir",
                24,
                "./img/boutique/genouilleres_coque.png",
            ),
            (
                8,
                "Short Garçon ASICS ZONA",
                None,
                "XS",
                "Noir",
                18,
                "./img/boutique/short_garcon.png",
            ),
            (
                9,
                "Short Garçon ASICS ZONA",
                "S",
                "Noir",
                18,
                "./img/boutique/short_garcon.png",
            ),
            (
                10,
                "Short Garçon ASICS ZONA",
                "M",
                "Noir",
                18,
                "./img/boutique/short_garcon.png",
            ),
            (
                11,
                "Short Garçon ASICS ZONA",
                "L",
                "Noir",
                18,
                "./img/boutique/short_garcon.png",
            ),
            (
                12,
                "Short Garçon ASICS ZONA",
                "XL",
                "Noir",
                18,
                "./img/boutique/short_garcon.png",
            ),
            (
                13,
                "Short Garçon ASICS ZONA",
                "XXL",
                "Noir",
                18,
                "./img/boutique/short_garcon.png",
            ),
            (
                14,
                "Short cuissard Fille ASICS",
                "XS",
                "Noir",
                18,
                "./img/boutique/short_filles.png",
            ),
            (
                15,
                "Short cuissard Fille ASICS",
                "S",
                "Noir",
                18,
                "./img/boutique/short_filles.png",
            ),
            (
                16,
                "Short cuissard Fille ASICS",
                "M",
                "Noir",
                18,
                "./img/boutique/short_filles.png",
            ),
            (
                17,
                "Short cuissard Fille ASICS",
                "L",
                "Noir",
                18,
                "./img/boutique/short_filles.png",
            ),
            (
                18,
                "Short cuissard Fille ASICS",
                "XL",
                "Noir",
                18,
                "./img/boutique/short_filles.png",
            ),
            (
                19,
                "Short cuissard Fille ASICS",
                "XXL",
                "Noir",
                18,
                "./img/boutique/short_filles.png",
            ),
            (
                20,
                "Tee-shirt Classic",
                "Flocage club + prénom",
                "4A",
                "Noir",
                10,
                "./img/boutique/tee_shirt.jpg",
            ),
            (
                21,
                "Tee-shirt Classic",
                "Flocage club + prénom",
                "8A",
                "Noir",
                10,
                "./img/boutique/tee_shirt.jpg",
            ),
            (
                22,
                "Tee-shirt Classic",
                "Flocage club + prénom",
                "10A",
                "Noir",
                10,
                "./img/boutique/tee_shirt.jpg",
            ),
            (
                23,
                "Tee-shirt Classic",
                "Flocage club + prénom",
                "12A",
                "Noir",
                10,
                "./img/boutique/tee_shirt.jpg",
            ),
            (
                24,
                "Tee-shirt Classic",
                "Flocage club + prénom",
                "S",
                "Noir",
                10,
                "./img/boutique/tee_shirt.jpg",
            ),
            (
                25,
                "Tee-shirt Classic",
                "Flocage club + prénom",
                "M",
                "Noir",
                10,
                "./img/boutique/tee_shirt.jpg",
            ),
            (
                26,
                "Tee-shirt Classic",
                "Flocage club + prénom",
                "L",
                "Noir",
                10,
                "./img/boutique/tee_shirt.jpg",
            ),
            (
                27,
                "Tee-shirt Classic",
                "Flocage club + prénom",
                "XL",
                "Noir",
                10,
                "./img/boutique/tee_shirt.jpg",
            ),
            (
                28,
                "Tee-shirt Classic",
                "Flocage club + prénom",
                "XXL",
                "Noir",
                10,
                "./img/boutique/tee_shirt.jpg",
            ),
            (
                29,
                "Tee-shirt Classic",
                "Flocage club + prénom",
                "XXXL",
                "Noir",
                10,
                "./img/boutique/tee_shirt.jpg",
            ),
            (
                30,
                "SAC 60x30x38 cm",
                "70 L floqué club",
                None,
                "Rouge et Noir",
                20,
                "./img/boutique/sac.png",
            ),
        ]

        for item in data:
            product = Catalogue(
                id=item[0],
                designation=item[1],
                des_comp=item[2],
                taille=item[3],
                coloris=item[4],
                prix=item[5],
                lien_photo=item[6],
            )
            product.save()
        print("Catalogue table handled")


def ajouterSalles():
    data = [
        (1, "gymnase Rivière", "4 rue d’Estujats", 31830, "Plaisance du Touch", None),
        (2, "Gymnase Monestié", "rue des fauvettes", 31830, "Plaisance du Touch", None),
        (3, "Exterieur", None, None, None, None),
    ]
    for item in data:
        salle = Salles(
            id=item[0],
            nom=item[1],
            adresse=item[2],
            code_postal=item[3],
            ville=item[4],
            complement=item[5],
        )
        salle.save()
    print("Salles table handled")


def ajouterCreneaux():
    data = [
        (1, 1, "2016-05-02 10:30:00", "2016-05-02 12:00:00"),
        (2, 2, "2016-05-09 10:30:00", "2016-05-09 12:00:00"),
        (3, 2, "2016-05-16 10:30:00", "2016-05-16 12:00:00"),
        (6, 1, "2016-05-28 10:00:00", "2016-05-28 12:00:00"),
        (7, 1, "2016-05-28 10:00:00", "2016-05-28 12:00:00"),
        (8, 1, "2016-06-04 10:00:00", "2016-06-04 12:00:00"),
        (10, 3, "2016-06-18 10:00:00", "2016-06-18 12:00:00"),
        (11, 3, "2016-06-18 10:00:00", "2016-06-18 12:00:00"),
        (12, 1, "2016-11-12 10:00:00", "2016-11-12 12:05:00"),
    ]

    for item in data:
        creneau = Creneaux(
            id=item[0],
            id_salle=noneReplace(Salles, item[1]),
            debut=datetime.strptime(item[2], "%Y-%m-%d %H:%M:%S"),
            fin=datetime.strptime(item[3], "%Y-%m-%d %H:%M:%S"),
        )
        creneau.save()
    print("Creneaux table handled")


def ajouterMatchs():
    data = [
        (1, 4, 1, 1, 2, None, "Portet"),
        (2, 5, 2, 0, 0, None, "L'Union"),
        (3, 6, 3, 1, 0, None, "Fonsorbes"),
        (4, 3, 7, None, None, None, "TOAC"),
        (5, 5, 8, None, None, None, "L'Union"),
        (7, 3, 10, None, None, None, "TOAC"),
        (8, 23, 11, None, None, None, "L'Union"),
        (9, 23, 12, None, None, None, "TOAC"),
    ]

    for item in data:
        match = Matchs(
            id=item[0],
            id_equipe_a=item[1],
            id_creneau=noneReplace(Creneaux, item[2]),
            score_a=item[3],
            score_b=item[4],
            duree=item[5],
            nom_equipe_b=item[6],
        )
        match.save()
    print("Matchs table handled")


class Command(BaseCommand):
    help = "Populates the database with relevant data."

    def handle(self, *args, **kwargs):
        ajouterCategories()
        ajouterEquipes()
        ajouterPostes()
        ajouterAdherents()
        ajouterArchives()
        ajouterEntraine()
        ajouterJoue()
        ajouterContacts()
        ajouterCourriels()
        ajouterDocuments()
        ajouterCatalogues()
        ajouterSalles()
        ajouterCreneaux()
        ajouterMatchs()
        print("Database has been populated")
