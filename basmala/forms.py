from django import forms

class basmalaform(forms.Form):
    ketua = forms.CharField(max_length=50)
    sekretaris = forms.CharField(max_length=40)
    bendahara = forms.CharField(widget=forms.Textarea)
    divisi = forms.BooleanField()
