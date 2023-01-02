from django.shortcuts import render, redirect
from .models import basmala
from .forms import basmalaform

# Create your views here.

def basmalaviews(request):
    basmala_form = basmalaform(request.POST or None)
    if request.method == 'POST':
        if basmala_form.is_valid:
            simpan_data = basmala.objects.create(
                ketua = basmala_form.cleaned_data.get('asilah'),
                sekretaris = basmala_form.cleaned_data.get('jawaban'),
                bendahara = basmala_form.cleaned_data.get('iktirod'),
                divisi = basmala_form.cleaned_data.get('keputusan'),
            )
            return redirect('basmala:basmalaList')
    context = {
        'form':basmala_form
    }
    return render(request, 'basmala.html', context)


