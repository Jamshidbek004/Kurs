from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Kurs(models.Model):
    name = models.CharField(max_length=20)
    fayl = models.FileField(upload_to='darslik/', null=True, blank=True)
    fayl_uy = models.FileField(upload_to='darslik/', null=True, blank=True)
    yonalish = models.ForeignKey('Yonalish', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Yonalish(models.Model):
    name = models.CharField(max_length=100)
    rasm = models.ImageField(upload_to='rasm/',null=True, blank=True)

    def __str__(self):
        return self.name


class Oquvchi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telraqam = models.CharField(max_length=14)
    bio = models.TextField()
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    sana = models.DateField(auto_now=True)

    def __str__(self):
        return self.bio


class Oy(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Tolov(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tolovqilgansana = models.DateField()
    oy = models.ForeignKey(Oy, on_delete=models.CASCADE)
    tolovmiqdor = models.IntegerField()







