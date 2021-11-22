from django.db import models

# Create your models here.

class Item(models.Model):
    """
        name = setting us as character field with max length of 50 characters
        and null/blank = false means that it cant be empty on any
        level of creation done = takes bullean and set default as false
    """
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # Making sure items show actual name instead of default Item object(#)
    def __str__(self):
        return self.name
