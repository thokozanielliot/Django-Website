from django.db import models

# Create your models here.
CHOICES =(("Business","Business"), ("Individual","Individual"),)
class  Blacklist(models.Model):
    first_name =models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    account_name = models.CharField(max_length=100)
    section = models.CharField(max_length=20, choices=CHOICES)
    institution = models.CharField(max_length=100) 
    account_manager = models.CharField(max_length=150)
    date_blacklisted = models.DateField()

    def __str__(self):
        return self.first_name
    
    class Meta:
        db_table = "blacklist"