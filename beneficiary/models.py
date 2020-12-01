from django.db import models
# Create your models here.
class Beneficiary(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField()
    address = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateTimeField()
    province = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    sector = models.CharField(max_length=100, null=True, blank=True)
    cell = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    

    class Meta:
        db_table = "Beneficiary"
