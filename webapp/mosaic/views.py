from django.shortcuts import render
import time
import os

from mosaic.src.utils import convert_quality
from webapp import settings
from mosaic.src.main import mosaic
from mosaic.forms import MosaicForm


def upload(request):
    if request.method == 'POST':
        form = MosaicForm(request.POST, request.FILES)
        if form.is_valid():
            mosaic_processed = form.save()
            image_name, file_ext = os.path.splitext(os.path.basename(mosaic_processed.uploaded_file.path))
            os.makedirs(os.path.join(settings.MEDIA_ROOT, 'mosaics'), exist_ok=True)
            input_file = os.path.join(settings.MEDIA_ROOT, mosaic_processed.uploaded_file.path)
            output_file = os.path.join(settings.MEDIA_ROOT, 'mosaics', image_name + file_ext)
            quality = mosaic_processed.quality
            mosaic(input_file, output_file, height=convert_quality(quality))

            mosaic_processed.mosaic_file = output_file
            mosaic_processed.save()

            return render(request, 'upload.html', {
                'form': MosaicForm(),
                'mosaic': mosaic_processed,
            })
    else:
        form = MosaicForm()
    return render(request, 'upload.html', {
        'form': form,
    })
