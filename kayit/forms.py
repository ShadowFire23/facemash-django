from django import forms
from .models import Kayitlar

class KayitlarForm(forms.ModelForm):

    class Meta:
        model = Kayitlar
        fields = ('Ad_Soyad','Fotograf',)
