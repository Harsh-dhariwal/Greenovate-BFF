from django.shortcuts import render
from .forms import carbon_emmision

def min_cal(request):
    if request.method == 'POST':
        form = carbon_emmision(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = carbon_emmision()
    return render(request, 'accept_info.html', {'form': form})
