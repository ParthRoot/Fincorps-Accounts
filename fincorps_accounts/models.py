from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    
    def __str__(self):
        return self.username
    
class General_Ledger(models.Model):
    date = models.DateField()
    accounts = models.CharField(max_length=30)
    details = models.CharField(max_length=200)
    debit = models.FloatField(null=True)
    credit = models.FloatField(null=True)
    
    
    
    