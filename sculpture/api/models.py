from django.db import models

# Create your models here.
class Sculpture(models.Model):

    # Material choices
    ALUMINIUM = 0
    BRASS = 1
    BRONZE = 2
    CLAY = 3
    MARBLE = 4
    STONE = 5
    WOOD = 6
    MATERIAL_CHOICES = [
        (ALUMINIUM, 'Aluminium'),
        (BRASS, 'Brass'),
        (BRONZE, 'Bronze'),
        (CLAY, 'Clay'),
        (MARBLE, 'Marble'),
        (STONE, 'Stone'),
        (WOOD, 'Wood')
    ]
    
    # Transport choices
    AIRWAYS = 0
    ROADWAYS = 1
    WATERWAYS = 2
    TRANSPORT_CHOICES = [
        (AIRWAYS, 'Airways'),
        (ROADWAYS, 'Roadways'),
        (WATERWAYS, 'Waterways')
    ]
    
    # Customer Information choices
    WEALTHY = 0
    WORKING_CLASS = 1
    CUSTOMER_INFO_CHOICES = [
        (WEALTHY, 'Wealthy'),
        (WORKING_CLASS, 'Working Class')
    ]

    # Yes/No choices
    YES_NO_CHOICES = [
        (0, 'No'),
        (1, 'Yes')
    ]

    # Model fields
    artist_reputation = models.FloatField()
    height = models.FloatField()
    width = models.FloatField()
    weight = models.FloatField()
    material = models.IntegerField(choices=MATERIAL_CHOICES)
    price_of_sculpture = models.FloatField()
    base_shipping_price = models.FloatField()
    international = models.IntegerField(choices=YES_NO_CHOICES)
    express_shipment = models.IntegerField(choices=YES_NO_CHOICES)
    installation_included = models.IntegerField(choices=YES_NO_CHOICES)
    transport = models.IntegerField(choices=TRANSPORT_CHOICES)
    fragile = models.IntegerField(choices=YES_NO_CHOICES)
    customer_information = models.IntegerField(choices=CUSTOMER_INFO_CHOICES)
    remote_location = models.IntegerField(choices=YES_NO_CHOICES)
    scheduled_date = models.FloatField()


    def __str__(self):
        return f"{self.get_material_display()} sculpture by artist with reputation {self.artist_reputation}"
