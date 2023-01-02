from django.db import models

# Create your models here.

class basmala(models.Model):
    ketua = models.CharField(max_length=100)
    sekretaris = models.CharField(max_length=50)
    bendahara = models.CharField(max_length=50)
    divisi = models.IntegerField(null=True)

    def __str__(self):
        return self.ketua

