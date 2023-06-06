from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=150, decimal_places=2, default=99.99)

    def __str__(self):
        return self.title
    
    # property decorator is used to define computed properties 
    # or calculated attributes for a model class. 
    # A computed property is not stored in the database 
    # but is calculated on the fly based on other attributes or data.
    # Search Chat GPT for details: property decorator of models in django?
    
    @property
    def sale_price(self):
        return '%.2f' %(float(self.price) * 0.8)
    
    def get_discount(self):
        return '122'

    
    