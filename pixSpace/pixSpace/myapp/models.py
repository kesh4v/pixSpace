from django.db import models

# Create your categories model here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.title

# Create your Image model here.

class Image(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images')
    added_date = models.DateTimeField()
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

