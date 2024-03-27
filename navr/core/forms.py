from django import forms
from .models import Member

from .models import Phones
# from django.contrib.auth.

class MyForm(forms.Form):
    field1 = forms.CharField(label='Políčko 1', max_length=100)
    field2 = forms.IntegerField(label='Políčko 2')

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ["firstname", "lastname"]


class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phones
        fields = ["phonenumber", "phonetype"]

