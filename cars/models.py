from django.db import models

class Cars(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    color = models.CharField(max_length=100, default='black')
    descriptions = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name