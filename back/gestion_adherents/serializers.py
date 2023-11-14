from rest_framework import serializers
from .models import (
    Adherents,
    Categories,
    Contacts,
    Courriels,
    Entraine,
    Equipes,
    Postes,
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
