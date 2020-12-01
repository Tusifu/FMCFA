from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    address = models.CharField(max_length=100,blank=True, null=True)


    def __str__(self):
        return self.name


    class Meta:
        db_table = "Hospital"

    
