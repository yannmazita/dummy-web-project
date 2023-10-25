from rest_framework import routers, serializers
from .models import Member


class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = [
            "licenseNumber",
            "lastname",
            "firstname",
            "dateOfBirth",
            "email",
            "telephone",
            "category",
            "referee",
            "manager",
            "director",
            "credentials",
        ]
