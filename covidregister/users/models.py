from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField


class User(AbstractUser):

    name = CharField(_("First and Last Name"), blank=True, max_length=255)
    institution = CharField(_("Institution"), blank=True, max_length=255)
    country = CountryField(blank=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"pk": self.pk})

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.email
