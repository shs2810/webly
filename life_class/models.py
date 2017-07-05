from django.db import models
# Create your models here.
class Life_class(models.Model):
    month = models.IntegerField()
    year = models.IntegerField()
    sex = models.CharField(max_length=10)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title