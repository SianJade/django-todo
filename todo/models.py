from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)
    
    """
    To give items in model the names given when when initially created in the
    admin panel (create website, plan website, launch)
    """
    def __str__(self):
        return self.name