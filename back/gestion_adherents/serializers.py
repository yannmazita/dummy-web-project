from rest_framework import serializers
from .models import (
    Adherents,
    Arbitre,
    Catalogue,
    Categories,
    Contacts,
    Courriels,
    Creneaux,
    Documents,
    Entraine,
    Entrainements,
    Equipes,
    Matchs,
    Postes,
    Salles,
    Telephones,
)


class AdherentsSerializer(serializers.HyperlinkedModelSerializer):
    categorie = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.all())  # type: ignore
    poste = serializers.PrimaryKeyRelatedField(queryset=Postes.objects.all())  # type: ignore

    # categorie_id = serializers.PrimaryKeyRelatedField(read_only=True)  # type: ignore
    # categorie_id = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.values_list("id"))    # type: ignore
    # categorie_id = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.filter(pk=id))    # type: ignore
    # categorie_id = serializers.HyperlinkedRelatedField(view_name="categories-detail", queryset=Categories.objects.all())  # type: ignore

    class Meta:
        model = Adherents
        fields = [
            "url",
            "id",
            "categorie",
            "poste",
            "login",
            "mdp",
            "nom",
            "prenom",
            "no_licence",
            "date_naissance",
            "genre",
            "surclassement",
            "habilitation",
            "arbitre",
            "entraineur",
        ]


class AdherentsPublicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Adherents
        fields = [
            "url",
            "id",
            "no_licence",
            "nom",
            "prenom",
            "surclassement",
            "arbitre",
            "entraineur",
        ]


class ArbitreSerializer(serializers.HyperlinkedModelSerializer):
    adherent = serializers.PrimaryKeyRelatedField(queryset=Arbitre.objects.all())  # type: ignore
    match = serializers.PrimaryKeyRelatedField(queryset=Matchs.objects.all())  # type: ignore

    class Meta:
        model = Arbitre
        fields = [
            "url",
            "id",
            "adherent",
            "match",
        ]


class ArchivesSerializer(serializers.HyperlinkedModelSerializer):
    createur = serializers.PrimaryKeyRelatedField(queryset=Adherents.objects.all())  # type: ignore
    validateur = serializers.PrimaryKeyRelatedField(queryset=Adherents.objects.all())  # type: ignore

    class Meta:
        model = Entraine
        fields = [
            "url",
            "id",
            "titre",
            "type",
            "lien_photo",
            "contenu",
            "lien_document",
            "createur",
            "date_creation",
            "validateur",
            "date_validation",
        ]


class CatalogueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catalogue
        fields = [
            "url",
            "id",
            "designation",
            "des_comp",
            "taille",
            "coloris",
            "prix",
            "lien_photo",
        ]


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = [
            "url",
            "id",
            "categorie",
            "description",
            "annee_deb",
            "annee_fin",
            "tarif",
        ]


class DocumentsSerializer(serializers.HyperlinkedModelSerializer):
    createur = serializers.PrimaryKeyRelatedField(queryset=Adherents.objects.all())  # type: ignore
    validateur = serializers.PrimaryKeyRelatedField(queryset=Adherents.objects.all())  # type: ignore
    equipe = serializers.PrimaryKeyRelatedField(queryset=Equipes.objects.all())  # type: ignore

    class Meta:
        model = Documents
        fields = [
            "url",
            "id",
            "titre",
            "type",
            "lien_photo",
            "contenu",
            "lien_document",
            "createur",
            "date_creation",
            "validateur",
            "date_validation",
            "equipe",
        ]


class EntraineSerializer(serializers.HyperlinkedModelSerializer):
    entraineur = serializers.PrimaryKeyRelatedField(queryset=Adherents.objects.all())  # type: ignore
    equipe = serializers.PrimaryKeyRelatedField(queryset=Equipes.objects.all())  # type: ignore

    class Meta:
        model = Entraine
        fields = [
            "url",
            "id",
            "entraineur",
            "equipe",
            "ordre",
        ]


class EntrainementsSerializer(serializers.HyperlinkedModelSerializer):
    equipe = serializers.PrimaryKeyRelatedField(queryset=Equipes.objects.all())  # type: ignore
    entraineur = serializers.PrimaryKeyRelatedField(queryset=Entraine.objects.all())  # type: ignore
    creneau = serializers.PrimaryKeyRelatedField(queryset=Creneaux.objects.all())  # type: ignore

    class Meta:
        model = Entrainements
        fields = [
            "url",
            "id",
            "equipe",
            "entraineur",
            "creneau",
        ]


class EquipesSerializer(serializers.HyperlinkedModelSerializer):
    categorie = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.all())  # type: ignore

    class Meta:
        model = Equipes
        fields = [
            "url",
            "id",
            "categorie",
            "nom",
            "points",
            "victoires",
            "defaites",
            "nulls",
            "photo",
            "club",
        ]


class PostesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Postes
        fields = [
            "url",
            "id",
            "designation",
            "description",
        ]


class CourrielsSerializer(serializers.HyperlinkedModelSerializer):
    contact = serializers.PrimaryKeyRelatedField(queryset=Contacts.objects.all())  # type: ignore

    class Meta:
        model = Courriels
        fields = [
            "url",
            "id",
            "contact",
            "courriel",
            "ordre",
        ]


class TelephonesSerializer(serializers.HyperlinkedModelSerializer):
    contact = serializers.PrimaryKeyRelatedField(queryset=Contacts.objects.all())  # type: ignore

    class Meta:
        model = Telephones
        fields = [
            "url",
            "id",
            "contact",
            "type",
            "remarque",
            "ordre",
        ]


class ContactsSerializer(serializers.HyperlinkedModelSerializer):
    adherent = serializers.PrimaryKeyRelatedField(queryset=Adherents.objects.all())  # type: ignore

    class Meta:
        model = Contacts
        fields = [
            "url",
            "id",
            "adherent",
            "nom",
            "prenom",
            "adresse",
            "code_postal",
            "ville",
            "complement",
            "remarque",
            "ordre",
        ]


class CreneauxSerializer(serializers.HyperlinkedModelSerializer):
    salle = serializers.PrimaryKeyRelatedField(queryset=Salles.objects.all())  # type: ignore

    class Meta:
        model = Creneaux
        fields = [
            "url",
            "id",
            "salle",
            "debut",
            "fin",
        ]


class MatchsSerializer(serializers.HyperlinkedModelSerializer):
    equipe_a = serializers.PrimaryKeyRelatedField(queryset=Equipes.objects.all())  # type: ignore
    creneau = serializerj.PrimaryKeyRelatedField(queryset=Creneaux.objects.all())  # type: ignore
    # nom_equipe_b may need to relate to the nom column in Equipes, however it isn't a primary key

    class Meta:
        model = Matchs
        fields = [
            "url",
            "id",
            "equipa_a",
            "creneau",
            "score_a",
            "score_b",
            "duree",
            "nom_equipe_b",
        ]
