from django.db import models


class Categories(models.Model):
    categorie = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    annee_deb = models.IntegerField(null=True)
    annee_fin = models.IntegerField(null=True)
    tarif = models.IntegerField(null=True)


class Equipes(models.Model):
    id_categorie = models.ForeignKey(Categories, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    points = models.IntegerField()
    victoires = models.IntegerField()
    defaites = models.IntegerField()
    nulls = models.IntegerField()
    photo = models.CharField(max_length=255)
    club = models.BooleanField()


class Postes(models.Model):
    designation = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Adherents(models.Model):
    class Surclassement(models.IntegerChoices):
        SIMPLE = 1
        DOUBLE = 2
        TRIPLE = 3

    class Status(models.TextChoices):
        PRESIDENT = "PRES"
        SECRETARY = "SEC"
        REFEREE = "REF"
        MANAGER = "MAN"

    class Habilitation(models.IntegerChoices):
        ADMIN = 1
        CLUB = 2
        BASIC = 3

    id_categorie = models.ForeignKey(Categories, on_delete=models.CASCADE)
    id_poste = models.ForeignKey(Postes, on_delete=models.CASCADE)
    login = models.CharField(max_length=255)
    mdp = models.CharField(max_length=255)
    nom = models.CharField(max_length=255, null=True)
    prenom = models.CharField(max_length=255, null=True)
    no_licence = models.IntegerField(null=True)
    date_naissance = models.DateField()
    genre = models.CharField(max_length=255)
    surclassement = models.IntegerField(
        default=Surclassement.SIMPLE, choices=Surclassement.choices  # type: ignore
    )
    director = models.CharField(max_length=4, choices=Status.choices)
    habilitation = models.IntegerField(choices=Habilitation.choices)
    arbitre = models.BooleanField()
    entraineur = models.BooleanField()


class Archives(models.Model):
    titre = models.CharField(max_length=255)
    type = models.CharField(max_length=255, null=True)
    lien_photo = models.CharField(max_length=255, null=True)
    contenu = models.CharField(max_length=255, null=True)
    lien_document = models.CharField(max_length=255, null=True)
    id_createur = models.ForeignKey(Adherents, on_delete=models.CASCADE, related_name="+")
    date_creation = models.DateField()
    id_validateur = models.ForeignKey(Adherents, on_delete=models.CASCADE)
    date_validation = models.DateField(null=True)


class Entraine(models.Model):
    id_entraineur = models.ForeignKey(Adherents, on_delete=models.CASCADE)
    id_equipe = models.ForeignKey(Equipes, on_delete=models.CASCADE)
    ordre = models.IntegerField(null=True)


class Joue(models.Model):
    id_adherent = models.ForeignKey(Adherents, on_delete=models.CASCADE)
    idlinux_equipe = models.ForeignKey(Equipes, on_delete=models.CASCADE)


class Contacts(models.Model):
    id_adherent = models.ForeignKey(Adherents, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255, null=True)
    prenom = models.CharField(max_length=255, null=True)
    adresse = models.CharField(max_length=255, null=True)
    code_postal = models.CharField(max_length=255, null=True)
    ville = models.CharField(max_length=255, null=True)
    complement = models.CharField(max_length=255, null=True)
    remarque = models.CharField(max_length=255, null=True)
    ordre = models.IntegerField(null=True)


class Courriels(models.Model):
    id_contact = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    courriel = models.CharField(max_length=255)
    ordre = models.IntegerField(null=True)


class Telephones(models.Model):
    id_contact = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    remarque = models.CharField(max_length=255)
    ordre = models.IntegerField()


class Documents(models.Model):
    titre = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    lien_photo = models.CharField(max_length=255, null=True)
    contenu = models.CharField(max_length=255, null=True)
    lien_document = models.CharField(max_length=255, null=True)
    id_createur = models.ForeignKey(Adherents, on_delete=models.CASCADE, related_name="+")
    date_creation = models.DateField()
    id_validateur = models.ForeignKey(Adherents, on_delete=models.CASCADE)
    date_validation = models.DateField(null=True)
    id_equipe = models.ForeignKey(Equipes, on_delete=models.CASCADE)


class Catalogue(models.Model):
    designation = models.CharField(max_length=255, null=True)
    des_comp = models.CharField(max_length=255, null=True)
    taille = models.CharField(max_length=255, null=True)
    prix = models.IntegerField(null=True)
    lien_photo = models.CharField(max_length=255, null=True)


class Salles(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    code_postal = models.CharField(max_length=255)
    vlle = models.CharField(max_length=255)
    complement = models.CharField(max_length=255)


class Creneaux(models.Model):
    id_salle = models.ForeignKey(Salles, on_delete=models.CASCADE)
    debut = models.DateField()
    fin = models.DateField()


class Matchs(models.Model):
    id_equipe_a = models.IntegerField()
    id_creneau = models.ForeignKey(Creneaux, on_delete=models.CASCADE)
    score_a = models.IntegerField()
    score_b = models.IntegerField()
    duree = models.DateField()
    nom_equipe_b = models.CharField(max_length=255)


class Arbitre(models.Model):
    id_adherent = models.ForeignKey(Adherents, on_delete=models.CASCADE, related_name="+")
    id_match = models.ForeignKey(Matchs, on_delete=models.CASCADE)


class Entrainements(models.Model):
    id_equipe = models.ForeignKey(Equipes, on_delete=models.CASCADE)
    id_entraineur = models.ForeignKey(Adherents, on_delete=models.CASCADE)
    id_creneau = models.ForeignKey(Creneaux, on_delete=models.CASCADE)
