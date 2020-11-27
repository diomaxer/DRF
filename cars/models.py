from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Car(models.Model):
    vin = models.CharField(verbose_name="Vin", max_length=50, db_index=True)
    colour = models.CharField(verbose_name="Colour", max_length=50)
    brand = models.CharField(verbose_name="Brand", max_length=50)
    CAR_TYPES = (
        (1, "Седан"),
        (2, "Хетчбек"),
        (3, "Универсал"),
        (4, "Купе"),
    )
    car_type = models.IntegerField(verbose_name="Car_Type", choices=CAR_TYPES)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
