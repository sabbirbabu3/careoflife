from django.db import models

# Create your models here.
class ContactUs(models.Model):
    name=models.CharField(max_length=25)
    phone=models.CharField(max_length=12)
    problem=models.TextField()

    def __str__(self) -> str:
        return self.name
    # name contactuss assilo tai aita likhlam
    class Meta:
        verbose_name_plural = "contact us"