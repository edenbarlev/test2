from django.db import models
from .validators import validate_file_extension


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True )
    document = models.FileField(upload_to='documents/', blank=True, validators=[validate_file_extension])
    description2 = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    isittrue = models.BooleanField(blank=True)
