from django.db import models


QUALITY_CHOICES = [
    ('small', 'Small (~2 minutes)'),
    ('medium', 'Medium (~5 minutes)'),
    ('large', 'Large (~10 minutes)'),
    ('original', 'Original size')
]


class Mosaic(models.Model):
    uploaded_file = models.ImageField(verbose_name='File', upload_to='inputs/')
    mosaic_file = models.ImageField(upload_to='outputs/', blank=True)
    quality = models.CharField(max_length=255, choices=QUALITY_CHOICES, default='small')
