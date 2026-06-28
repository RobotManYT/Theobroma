from django.db import models

# Create your models here.
class UnitType(models.Model):
    name = models.CharField(max_length=15)  # Mass, Volume, Custom, etc.

class Unit(models.Model):
    unit_name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=4)

    unit_type = models.ForeignKey(UnitType, on_delete=models.RESTRICT)

    base_unit = models.ForeignKey("self", null=True, blank=True, on_delete=models.RESTRICT)

    ratio_to_base = models.FloatField(default=1)