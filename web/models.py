import uuid
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image_url = models.URLField(null=False, blank=False)
    slug = models.SlugField(unique=True, max_length=255, null=True, blank=True)
    is_private = models.BooleanField(default=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=500)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return self.name


class Contacto(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_name = models.CharField(max_length=64, null=False, blank=False)
    customer_email = models.EmailField(null=False, blank=False)
    message = models.TextField(null=False, blank=False)


    def __str__(self) -> str:
        return self.customer_name
