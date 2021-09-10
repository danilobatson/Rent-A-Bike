from django.db import models

# Create your models here.

class Renter(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  phone = models.IntegerField()
  vip_num = models.IntegerField()

#   first_name (the first name of the renter)
# last_name (the last name of the renter)
# phone (the phone number of the renter)
# vip_num (renter’s VIP status and number)
