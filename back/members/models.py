from django.db import models


class Member(models.Model):
    """Model used to manage club members, licenses players and volunteers."""

    class Upgrade(models.IntegerChoices):
        SIMPLE = 1
        DOUBLE = 2
        TRIPLE = 3

    class Status(models.TextChoices):
        PRESIDENT = "PRES"
        SECRETARY = "SEC"
        REFEREE = "REF"
        MANAGER = "MAN"

    class Credentials(models.IntegerChoices):
        ADMIN = 1
        CLUB = 2
        BASIC = 3

    licenseNumber = models.IntegerField()
    lastname = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    dateOfBirth = models.DateField()
    email = models.CharField(
        max_length=255
    )  # several emails possible, need to change type ?
    telephone = models.CharField(
        max_length=255
    )  # several numbers possibles, need to change type ?
    category = models.IntegerField(default=Upgrade.SIMPLE, choices=Upgrade.choices)  # type: ignore
    # category = models.IntegerField(choices=Upgrade.choices)
    referee = models.BooleanField()
    manager = models.CharField(max_length=255, null=True)
    director = models.CharField(max_length=4, choices=Status.choices)
    credentials = models.IntegerField(choices=Credentials.choices)
