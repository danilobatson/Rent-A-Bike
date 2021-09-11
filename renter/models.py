from django.db import models
import datetime



# Create your models here.

BASE_PRICE = 25.00
TANDEM_SURCHARGE = 15.00
ELECTRIC_SURCHARGE = 25.00
class Bike(models.Model):
  BIKE_TYPE_CHOICES = [
    (BASE_PRICE, 25.00),
    (TANDEM_SURCHARGE, 15.00),
    (ELECTRIC_SURCHARGE, 25.00)
  ]
  def __str__(self):
    return self.bike_type + " - " + self.color

  color = models.CharField(max_length=10 default = '')
  bike_type = models.CharField(
      max_length=2, choices=BIKE_TYPE_CHOICES, default=STANDARD)


class Renter(models.Model):
  def __str__(self):
    return (f'{self.first_name} {self.last_name} - #{self.phone}')
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  phone = models.CharField(max_length=15)
  vip_num = models.IntegerField(default=0)


class Rental(models.Model):
  def __str__(self):
    return (f'{self.first_name} {self.last_name} - #{self.phone}')

  bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
  renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
  last_name = models.CharField(max_length=30)
  date = models.DateField(default=datetime.date.today())
  price = models.FloatField(default=0)

  def calc_price(self):
    curr_price = BASE_PRICE
# Start with the fields:

# bike which is a foreign key for the Bike model
# upon the foreign key’s deletion, it should cascade
# renter which is a foreign key for the Renter model
# upon the foreign key’s deletion, it should cascade
# date a date field which defaults to today’s date (datetime.date.today)
# price a float field which defaults to 0.0
