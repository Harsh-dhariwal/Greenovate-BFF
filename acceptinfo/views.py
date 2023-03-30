from django.shortcuts import render
from .forms import Electricityform

def calc(request):
    if request.method == 'POST':
        form = Electricityform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = Electricityform()
    return render(request, 'e_info.html', {'form': form})
