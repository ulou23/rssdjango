from django.db import models

# Create your models here.

class URL(models.Model):
    urlinput=models.CharField(max_length=100)

    class Meta:
        db_table='url'

    def __str__(self):
        return self.urlinput