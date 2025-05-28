from django.db import models

# Create your models here.

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=100)
    last_update = models.DateField()

    class Meta:
        db_table = 'country'
        managed = False

    def __str__(self):
        return self.country

class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    last_update = models.DateField()
    capital = models.BooleanField(default=False)
    picture = models.BinaryField(null=True, blank=True)  # Pour stocker les images
    
    class Meta:
        db_table = 'city'
        managed = False

    def __str__(self):
        return self.city