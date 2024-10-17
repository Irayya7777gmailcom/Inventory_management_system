from django.db import models



class Item(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=True, null=True)
    quantity= models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    # Add price for each

    def __str__(self):
        return self.name
