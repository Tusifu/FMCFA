from django.db import models

# Create your models here.
class DrugsIssuing(models.Model):

    date = models.DateTimeField()
    drugName = models.CharField(max_length=100, null=True, blank=True)
    unitPrice = models.FloatField()
    totalPrice = models.FloatField()
    quantity = models.IntegerField()


    def __str__(self):
        return self.drugName

    class Meta:
        db_table="DrugIssuing"
    