from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='Product')
    description = models.TextField()


    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            pass

    def __str__(self):
        return self.name
