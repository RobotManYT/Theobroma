from django.db import models
from django.db.models.functions import Lower

# Create your models here.
class UnitType(models.Model):
    name = models.CharField(max_length=15)  # Mass, Volume, Custom, etc.

class Unit(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=4, unique=True)

    unit_type = models.ForeignKey(UnitType, on_delete=models.RESTRICT)

    base_unit = models.ForeignKey("self", null=True, blank=True, on_delete=models.RESTRICT)

    ratio_to_base = models.FloatField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("name"),
                name="unique_unit_name_case_insensitive",
            ),
        ]

    def __str__(self):
        return f"Unit - NAME: {self.name}; SYMBOL: {self.symbol}; UNIT_TYPE: {self.unit_type}; BASE_UNIT: {self.base_unit}; RATIO_TO_BASE: {self.ratio_to_base}"



class FoodCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                Lower("name"),
                name="unique_category_name_case_insensitive",
            ),
        ]

    def __str__(self):
        return f"Food category - NAME: {self.name}"

class CategoryAttribute(models.Model):
    class DataType(models.TextChoices):
        STRING = "str", "String"
        INTEGER = "int", "Integer"
        DECIMAL = "dec", "Decimal"
        BOOLEAN = "bool", "Boolean"
        # CUSTOM - Eventually, if needed

    name = models.CharField(max_length=50)

    category = models.ForeignKey(
        FoodCategory,
        on_delete=models.CASCADE,
        related_name="attributes"
    )

    data_type = models.CharField(
        max_length=5,
        choices=DataType.choices,
        default=DataType.STRING
    )