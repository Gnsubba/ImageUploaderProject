from dataclasses import fields
from django.forms import ModelForm
from imageApp.models import Image

class imageForm(ModelForm):
    class Meta:
        model = Image
        fields = "__all__"