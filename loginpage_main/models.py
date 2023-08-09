from django.db import models
from phone_field import PhoneField

# Create your models here.
class Home(models.Model):
    # home_text = models.CharField(max_length=100)
    first_name = models.CharField(max_length=25,blank=False)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=40, null=True)
    phone_num = PhoneField(blank=True, null=True)
    address = models.CharField(max_length=25, null=True)
    id = models.AutoField(primary_key=True)



    def __str__(self):

        return  '%d %s %s %s %s %s'%(self.id, self.first_name, self.last_name,self.email, self.phone_num,self.address)

