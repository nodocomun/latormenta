from django import forms
from .models import Answer


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ('text', 'pic_uri',)
        help_texts = {
            'text': 'Lo que te nazca!',
            'pic_uri': 'Link a una imagen por favor!'}
        labels = {
            'text': 'Texto',
            'pic_uri': 'Imagen'}
