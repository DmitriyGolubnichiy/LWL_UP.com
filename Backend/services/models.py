
from django.db import models



class Service(models.Model):
    name = models.CharField(max_length = 256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    duration = models.PositiveIntegerField()
    lesson_duration = models.PositiveIntegerField()
    image = models.ImageField(upload_to='service_images')

    def __str__(self):
        return f'Тариф: {self.name}'