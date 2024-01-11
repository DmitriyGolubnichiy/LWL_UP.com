
from django.db import models

from users.models import User


class Service(models.Model):
    name = models.CharField(max_length = 256)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    duration = models.PositiveIntegerField()
    lesson_duration = models.PositiveIntegerField()
    image = models.ImageField(upload_to='service_images')

    def __str__(self):
        return f'Тариф: {self.name}'

class Basket(models.Model):
    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    service = models.ForeignKey(to=Service,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Тарифы для {self.user.username} | Тариф: {self.service.name}'

    def sum(self):
        return self.service.price * self.quantity