from django.db import models


class Categories(models.Model):
    categorie = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    annee_deb = models.IntegerField(null=True, blank=True)
    annee_fin = models.IntegerField(null=True, blank=True)
    tarif = models.IntegerField(null=True, blank=True)


class Equipes(models.Model):
    categorie = models.ForeignKey(
        Categories, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    points = models.IntegerField(null=True)
    victoires = models.IntegerField(null=True)
    defaites = models.IntegerField(null=True)
    nulls = models.IntegerField(null=True)
    photo = models.CharField(max_length=255, null=True)
    club = models.BooleanField()


class Postes(models.Model):
    designation = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Adherents(models.Model):
    class Surclassement(models.IntegerChoices):
        SIMPLE = 1
        DOUBLE = 2
        TRIPLE = 3

    class Habilitation(models.IntegerChoices):
        ADMIN = 1
        CLUB = 2
        BASIC = 3

    categorie = models.ForeignKey(
        Categories, on_delete=models.CASCADE)
    poste = models.ForeignKey(
        Postes, on_delete=models.CASCADE, null=True)
    login = models.CharField(max_length=255, null=True)
    mdp = models.CharField(max_length=255, null=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    no_licence = models.IntegerField(unique=True)
    date_naissance = models.DateField()
    genre = models.CharField(max_length=255)
    surclassement = models.IntegerField(
        default=Surclassement.SIMPLE, choices=Surclassement.choices  # type: ignore
    )
    habilitation = models.IntegerField(choices=Habilitation.choices)
    arbitre = models.BooleanField()
    entraineur = models.BooleanField()


class Archives(models.Model):
    titre = models.CharField(max_length=255)
    type = models.CharField(max_length=255, null=True, blank=True)
    lien_photo = models.CharField(max_length=255, null=True, blank=True)
    contenu = models.CharField(max_length=255, null=True, blank=True)
    lien_document = models.CharField(max_length=255, null=True, blank=True)
    createur = models.ForeignKey(
        Adherents, on_delete=models.CASCADE, related_name="+")
    date_creation = models.DateField()
    validateur = models.ForeignKey(
        Adherents, on_delete=models.CASCADE)
    date_validation = models.DateField(null=True, blank=True)


class Entraine(models.Model):
    entraineur = models.ForeignKey(
        Adherents, on_delete=models.CASCADE)
    equipe = models.ForeignKey(
        Equipes, on_delete=models.CASCADE)
    ordre = models.IntegerField(null=True, blank=True)


class Joue(models.Model):
    adherent = models.ForeignKey(
        Adherents, on_delete=models.CASCADE)
    equipe = models.ForeignKey(
        Equipes, on_delete=models.CASCADE)


class Contacts(models.Model):
    adherent = models.ForeignKey(
        Adherents, on_delete=models.CASCADE)
    nom = models.CharField(max_length=255, null=True, blank=True)
    prenom = models.CharField(max_length=255, null=True, blank=True)
    adresse = models.CharField(max_length=255, null=True, blank=True)
    code_postal = models.CharField(max_length=255, null=True, blank=True)
    ville = models.CharField(max_length=255, null=True, blank=True)
    complement = models.CharField(max_length=255, null=True, blank=True)
    remarque = models.CharField(max_length=255, null=True, blank=True)
    ordre = models.IntegerField(null=True, blank=True)


class Courriels(models.Model):
    contact = models.ForeignKey(
        Contacts, on_delete=models.CASCADE)
    courriel = models.CharField(max_length=255)
    ordre = models.IntegerField(null=True, blank=True)


class Telephones(models.Model):
    contact = models.ForeignKey(
        Contacts, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    remarque = models.CharField(max_length=255)
    ordre = models.IntegerField()


class Documents(models.Model):
    titre = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    lien_photo = models.CharField(max_length=255, null=True, blank=True)
    contenu = models.CharField(max_length=255, null=True, blank=True)
    lien_document = models.CharField(max_length=255, null=True, blank=True)
    createur = models.ForeignKey(
        Adherents, on_delete=models.CASCADE, related_name="+")
    date_creation = models.DateField()
    validateur = models.ForeignKey(
        Adherents, on_delete=models.CASCADE)
    date_validation = models.DateField(null=True, blank=True)
    equipe = models.ForeignKey(
        Equipes, on_delete=models.CASCADE)


class Catalogue(models.Model):
    designation = models.CharField(max_length=255, null=True, blank=True)
    des_comp = models.CharField(max_length=255, null=True, blank=True)
    taille = models.CharField(max_length=255, null=True, blank=True)
    coloris = models.CharField(max_length=255, null=True, blank=True)
    prix = models.IntegerField(null=True, blank=True)
    lien_photo = models.CharField(max_length=255, null=True, blank=True)


class Salles(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255, null=True)
    code_postal = models.CharField(max_length=255, null=True)
    ville = models.CharField(max_length=255, null=True)
    complement = models.CharField(max_length=255, null=True)


class Creneaux(models.Model):
    salle = models.ForeignKey(Salles, on_delete=models.CASCADE)
    debut = models.DateField()
    fin = models.DateField()


class Matchs(models.Model):
    equipe_a = models.ForeignKey(
        Equipes, on_delete=models.CASCADE)
    creneau = models.ForeignKey(
        Creneaux, on_delete=models.CASCADE)
    score_a = models.IntegerField(null=True)
    score_b = models.IntegerField(null=True)
    duree = models.DurationField(null=True)
    nom_equipe_b = models.CharField(max_length=255)
    # nom_equipe_b may need to relate to the nom column in Equipes, however it isn't a primary key


class Arbitre(models.Model):
    adherent = models.ForeignKey(
        Adherents, on_delete=models.CASCADE, related_name="+")
    match = models.ForeignKey(Matchs, on_delete=models.CASCADE)


class Entrainements(models.Model):
    equipe = models.ForeignKey(
        Equipes, on_delete=models.CASCADE)
    entraineur = models.ForeignKey(
        Entraine, on_delete=models.CASCADE)
    creneau = models.ForeignKey(
        Creneaux, on_delete=models.CASCADE)
