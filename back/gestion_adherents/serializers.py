from rest_framework import serializers
from .models import Adherents, Categories, Equipes


class AdherentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Adherents
        fields = [
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
            "categorie_id",
            "nom",
            "points",
            "victoires",
            "defaites",
            "nulls",
            "photo",
            "club",
        ]


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = [
            "categorie",
            "description",
            "annee_deb",
            "annee_fin",
            "tarif",
        ]
