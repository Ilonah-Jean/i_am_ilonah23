from django import forms # type: ignore
from .models import Plant
from crispy_forms.helper import FormHelper # type: ignore
from crispy_forms.layout import Submit # type: ignore

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'price', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super(PlantForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))
