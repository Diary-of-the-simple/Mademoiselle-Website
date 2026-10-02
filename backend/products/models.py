from django.db import models
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
    #text fields
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    description = models.TextField()

    #number field
    price = models.DecimalField(max_digits=10, decimal_places=2)

    #boolean
    is_active = models.BooleanField(default=True)

    #datetime
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)