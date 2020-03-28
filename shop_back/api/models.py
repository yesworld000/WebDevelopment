from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.id,
                               self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    description = models.TextField(default='')
    count = models.IntegerField(default=10)
    category = models.ForeignKey(Category, null=True,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.name,
                               self.description)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'count': self.count
        }
