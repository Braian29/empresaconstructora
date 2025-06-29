from django.db import models
from django.utils.translation import gettext_lazy as _

class ContactForm(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    email = models.EmailField(_("Email"))
    phone = models.CharField(_("Phone"), max_length=20, blank=True)
    subject = models.CharField(_("Subject"), max_length=255)
    message = models.TextField(_("Message"))

    def __str__(self):
        return f"Message from {self.name} about {self.subject}"

    class Meta:
        verbose_name = _("Contact Form Submission")
        verbose_name_plural = _("Contact Form Submissions")

class ContactInfo(models.Model):
    address = models.CharField(_("Address"), max_length=255, blank=True)
    phone_number = models.CharField(_("Phone Number"), max_length=20)
    email = models.EmailField(_("Email"))
    instagram = models.URLField(_("Instagram Link"), blank=True)
    latitude = models.FloatField(_("Latitude"), blank=True, null=True)
    longitude = models.FloatField(_("Longitude"), blank=True, null=True)
    schedule = models.CharField(_("Schedule"), max_length=255, blank=True)

    def __str__(self):
        return "Contact Information"