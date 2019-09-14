from django import forms

from mosaic.models import Mosaic
from mosaic.models import QUALITY_CHOICES


class MosaicForm(forms.ModelForm):
    quality = forms.ChoiceField(choices=QUALITY_CHOICES, widget=forms.RadioSelect(), initial='medium')

    class Meta:
        model = Mosaic
        fields = ('uploaded_file', 'quality')
