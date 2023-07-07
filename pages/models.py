from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/%Y/%m/%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.title
