from codecs import backslashreplace_errors
from django.db import models


COLLEGE_NAME = (
    ('ABESEC', 'ABES EC'),
    ('ABESIT', 'ABES IT'),
    ('KIET', 'KIET'),
    ('AKGEC', 'AKG EC'),

)

GENDER = (
    ('M', 'MALE'),
    ('F', 'FEMALE'), 
    
)

DOMAIN_CHOICE = (
    ('EDUCATION', 'EDUCATION'),
    ('SOCIAL MEDIA', 'SOCIAL MEDIA'),
    ('HEALTHCARE', 'HEALTHCARE'),
    ('TECHNOLOGY', 'TECHNOLOGY'),
)


# Create your models here.
class Hackathon(models.Model):
    teamname = models.CharField(max_length=100)
    collegename = models.CharField(max_length=100, choices=COLLEGE_NAME)
    domain = models.CharField(max_length=50, choices=DOMAIN_CHOICE)
    leadername = models.CharField(max_length=100)
    leaderemail = models.EmailField()
    leadernumber = models.CharField(max_length=10)
    leadergender = models.CharField(max_length=10, choices=GENDER ) 
    branch = models.CharField(max_length=50)
    year = models.CharField(max_length=10)
    
    member2name = models.CharField(max_length=100)
    member2gender = models.CharField(max_length=10, choices=GENDER )
    
    member3name = models.CharField(max_length=100)
    member3gender = models.CharField(max_length=10, choices=GENDER )
    
    member4name = models.CharField(max_length=100)
    member4gender = models.CharField(max_length=10, choices=GENDER )
    
    member5name = models.CharField(max_length=100)
    member5gender = models.CharField(max_length=10, choices=GENDER )
    amount = models.ImageField(upload_to='media/', blank = True)
    transactionid = models.CharField(max_length=100)
    
    date = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.teamname
    
    

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    team = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
    
    
