from django.db import models


QUALITY_CHOICES = [
    ('small', 'Small'),
    ('medium', 'Medium'),
    ('large', 'Large'),
    ('original', 'Original size')
]


class Mosaic(models.Model):
    uploaded_file = models.ImageField(verbose_name='File', upload_to='inputs/')
    mosaic_file = models.ImageField(upload_to='outputs/', blank=True)
    quality = models.CharField(max_length=255, choices=QUALITY_CHOICES, default='small')
