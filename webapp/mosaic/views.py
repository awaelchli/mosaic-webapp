from django.shortcuts import render
import time
import os
from webapp import settings
from mosaic.src.main import mosaic


ALLOWED_FILE_FORMATS = ['.jpg', '.jpeg', '.png']


def home(request):
    if request.method == 'POST' and request.FILES['upload_image']:
        image_file = request.FILES['upload_image'].read()
        image_name, file_ext = os.path.splitext(str(request.FILES['upload_image']))

        input_filename = time.strftime(image_name + '_input_%Y%m%d-%H%M%S' + file_ext)
        output_filename = time.strftime(image_name + '_mosaic_%Y%m%d-%H%M%S' + file_ext)

        mosaics_path = os.path.join(settings.MEDIA_ROOT, 'tmp', 'mosaics')
        mosaics_url = os.path.join(settings.MEDIA_URL, 'tmp', 'mosaics')

        input_file = os.path.join(mosaics_path, input_filename)
        output_file = os.path.join(mosaics_path, output_filename)
        output_url = os.path.join(mosaics_url, output_filename)

        os.makedirs(mosaics_path, exist_ok=True)

        with open(input_file, 'wb') as f:
            f.write(image_file)

        error_msg = ''

        if file_ext.lower() not in ALLOWED_FILE_FORMATS:
            error_msg = 'Invalid file format. Allowed formats are: ' + ', '.join(ALLOWED_FILE_FORMATS).replace('.', '')
        else:
            mosaic(input_file, output_file)

        return render(request, 'main.html', {
            'output_file_url': output_url,
            'error_message': error_msg,
            'success': not error_msg,
        })
    return render(request, 'main.html')

