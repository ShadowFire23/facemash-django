from django.db import models

class Kayitlar(models.Model):
    Ad_Soyad = models.CharField(max_length=100)
    Fotograf = models.ImageField(verbose_name="Add File")

    def __str__(self):
        return self.Ad_Soyad