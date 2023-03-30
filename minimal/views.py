from django.shortcuts import render
from .forms import carbon_emmision
import requests

def min_cal(request):
    if request.method == 'POST':
        form = carbon_emmision(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            #getting all the data from the form
            
            
            
            company_name=request.POST['company_name']
            print("company name is",company_name)
            
            
            
            
            paperuse = data['paper_use']
            url = "https://carbonfootprint1.p.rapidapi.com/TreeEquivalent"

            querystring = {"weight":str(paperuse),"unit":"kg"}

            headers = {
	            "X-RapidAPI-Key": "54caaa891bmsh28b30d3e6519382p1e54dejsnb01e24eac7f5",
	            "X-RapidAPI-Host": "carbonfootprint1.p.rapidapi.com"
                }

            response = requests.request("GET", url, headers=headers, params=querystring)
            print(response.text)
            
            
            
            
            
            
            
            trad_hydro_amount = data['traditional_hydro_use']
            location=data['traditional_hydro_location']
            url = "https://carbonfootprint1.p.rapidapi.com/TraditionalHydroToCarbonFootprint"

            querystring = {"consumption":str(trad_hydro_amount),"location":str(location)}

            response = requests.request("GET", url, headers=headers, params=querystring)

            print(response.text)
            # print("company name is",field)
            
            
            
            
            
            
            return render(request, 'success.html')
    else:
        form = carbon_emmision()
    return render(request, 'accept_info.html', {'form': form})
