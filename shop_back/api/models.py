from django.db import models


# Create your models here.

import django.db


class Category(django.db.models.Model):
    name = django.db.models.CharField(max_length=50)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Product(django.db.models.Model):
    name = django.db.models.CharField(max_length=50)
    price = django.db.models.FloatField()
    description = django.db.models.TextField(default='')
    count = django.db.models.IntegerField()
    # category = django.db.models.ForeignKey(Category, on_delete=django.db.models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'count': self.count,
            'description': self.description
            }
