from django.db import models

class HospitalAgent(models.Model):
    
    name = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField()
    address = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateTimeField()
    def __str__(self):
        return self.name
    

    class Meta:
        db_table = "HospitalAgent"


