from django.db import models # type: ignore

class Plant(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='plant_images/', blank=True, null=True)

    def __str__(self):
        return self.name
