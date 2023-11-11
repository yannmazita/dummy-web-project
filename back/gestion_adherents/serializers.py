from rest_framework import serializers
from .models import Adherents, Categories, Entraine, Equipes, Postes


class AdherentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Adherents
        fields = [
            "id",
            "categorie_id",
            "poste_id",
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
            "id",
            "no_licence",
            "nom",
            "prenom",
            "surclassement",
            "arbitre",
            "entraineur",
        ]


class EquipesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Equipes
        fields = [
            "id",
            "categorie_id",
            "nom",
            "points",
            "victoires",
            "defaites",
            "nulls",
            "photo",
            "club",
        ]


class EntraineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entraine
        fields = [
            "id",
            "entraineur_id",
            "equipe_id",
        ]


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = [
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
            "id",
            "designation",
            "description",
        ]
