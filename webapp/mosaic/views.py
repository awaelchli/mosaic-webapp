from django.shortcuts import render
import time
import os

from mosaic.src.utils import convert_quality
from webapp import settings
from mosaic.src.main import mosaic
from PIL import Image
from mosaic.forms import MosaicForm

ALLOWED_FILE_FORMATS = ['.jpg', '.jpeg', '.png']


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

        print("URL" + output_url)
        print("FILE" + output_file)
        print("NAME" + output_filename)

        try:
            print(Image.open(output_url).size[0])
        except:
            print("blablablöu111111111111111111111111111111111111")


        error_msg = ''

        if file_ext.lower() not in ALLOWED_FILE_FORMATS:
            error_msg = 'Invalid file format. Allowed formats are: ' + ', '.join(ALLOWED_FILE_FORMATS).replace('.', '')
        else:
            mosaic(input_file, output_file,)

        return render(request, 'main.html', {
            'output_file_url': output_url,
            'error_message': error_msg,
            'success': not error_msg,
        })
    return render(request, 'main.html')

    # def setFileName(self, inputname):
    #     ID = ""
    #     for i in range(0, 6):
    #         ID += str(random.randint(0, 9))
    #
    #     rawfilename = os.path.splitext(inputname)
    #     result = rawfilename[0] + "_image_" + ID + rawfilename[1]
    #     return result
