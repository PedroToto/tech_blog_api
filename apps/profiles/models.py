from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from apps.common.models import TimeStampModel

User = get_user_model()

class Profile(TimeStampModel):
    class Gender(models.TextChoices):
        MALE = ("M", _("Male"),)
        FEMALE = ("F", _("Female"),)
        UNSAID = ("NS", _("Not Specified"),)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = PhoneNumberField(
        verbose_name=_("Phone number"), 
        max_length=30, 
        default="+12125552368"
    )
    about_me = models.TextField(
        verbose_name=_("About me"),
        default="Say something about"
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=Gender.UNSAID,
        max_length=20,
    )
    country = CountryField(verbose_name=_("Country"),
                           default="HTI",
                           null=False
    )
    city = models.CharField(
        verbose_name=_("City"),
        max_length=180,
        default="Cap Haitien",
        blank=False,
        null=False,
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile photo"), 
        default="/profile_default.png")
    twitter_handle = models.CharField(
        verbose_name=_("Twitter handle"),
        max_length=20, 
        blank=True
    )
    followers = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="following",
        blank=True
    )

    def __str__(self):
        return f"{self.user.first_name}'s Profile"
    
    def follow(self, profile):
        self.followers.add(profile)

    def unfollow(self, profile):
        self.followers.remove(profile)

    def check_following(self, profile):
        return self.followers.filter(pkid=profile.pkid).exists()

    

