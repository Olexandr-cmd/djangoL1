from django.db import models


# Create your models here.


class Users:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
