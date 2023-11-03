from rest_framework import serializers
from .models import Adherents, Equipes


class AdherentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Adherents
        fields = [
            "id_categorie",
            "id_poste",
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
            "id_categorie",
            "nom",
            "points",
            "victoires",
            "defaites",
            "nulls",
            "photo",
            "club",
        ]
