from django.shortcuts import render
from .forms import carbon_emmision
import requests
from .models import carbon_emmission,comp_database

def min_cal(request):
    if request.method == 'POST':
        form = carbon_emmision(request.POST)
        if form.is_valid():
           # form.save()
            #data = form.cleaned_data
            #getting all the data from the form
            
            
            
            company_name=request.POST['company_name']
            print("company name is",company_name)
            
            
            
            
            paperuse = request.POST['paper_use']
            url = "https://carbonfootprint1.p.rapidapi.com/TreeEquivalent"

            querystring = {"weight":str(paperuse),"unit":"kg"}

            headers = {
	            'X-RapidAPI-Key': 'b6cf2142c1mshb1b4161195ee8c4p11d867jsn69e16bcf63a1',
                'X-RapidAPI-Host': 'carbonfootprint1.p.rapidapi.com'
                }

            response = requests.request("GET", url, headers=headers, params=querystring)
            response_data = response.json()
            
            tree_eq=int(response_data['numberOfTrees'])
            tree_eq=1
            
            
            print(response.text)
            
            
            
            
            
            
            
            trad_hydro_amount = request.POST['traditional_hydro_use']
            location=request.POST['traditional_hydro_location']
            url = "https://carbonfootprint1.p.rapidapi.com/TraditionalHydroToCarbonFootprint"

            querystring = {"consumption":str(trad_hydro_amount),"location":str(location)}

            response = requests.request("GET", url, headers=headers, params=querystring)
            response_data = response.json()
            traditional_hydro_emmision=int(response_data['carbonEquivalent'])

            print(response.text)
            # print("company name is",field)
            
            
            solar_energy = request.POST['solar_energy']
            hydroelectric_energy = request.POST['hydroelectric_energy']
            wind_energy = request.POST['wind_energy']
            biomass_energy = request.POST['biomass_energy']
            geothermal_energy = request.POST['geothermal_energy']
            other_clean_energy = request.POST['other_clean_energy']
            
            total_carbonemmision_energy=0;
            
            if solar_energy:
                url = "https://carbonfootprint1.p.rapidapi.com/CleanHydroToCarbonFootprint"
                headers = {
	            "X-RapidAPI-Key": "e5d658079emshade1e85bc8f8b2ep14debejsn9d62bcd9380b",
	            "X-RapidAPI-Host": "carbonfootprint1.p.rapidapi.com"
                }
                querystring = {"energy":"Solar","consumption":str(solar_energy)}


                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()

                total_carbonemmision_energy=total_carbonemmision_energy+int(response_data['carbonEquivalent'])
                print("this is the end result",response_data)
                
                
            if hydroelectric_energy:
                url = "https://carbonfootprint1.p.rapidapi.com/CleanHydroToCarbonFootprint"

                querystring = {"energy":"HydroElectric","consumption":str(hydroelectric_energy)}

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_energy=total_carbonemmision_energy+int(response_data['carbonEquivalent'])
                
            if wind_energy:
                url = "https://carbonfootprint1.p.rapidapi.com/CleanHydroToCarbonFootprint"

                querystring = {"energy":" Wind","consumption":"500"}


                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_energy=total_carbonemmision_energy+int(response_data['carbonEquivalent'])
                print(response.text)
                
                
            if biomass_energy:
                url = "https://carbonfootprint1.p.rapidapi.com/CleanHydroToCarbonFootprint"

                querystring = {"energy":"Biomass","consumption":str(biomass_energy)}


                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_energy=total_carbonemmision_energy+int(response_data['carbonEquivalent'])
                print(response.text)

            if geothermal_energy:
                url = "https://carbonfootprint1.p.rapidapi.com/CleanHydroToCarbonFootprint"

                querystring = {"energy":"Biomass","consumption":str(geothermal_energy)}

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_energy=total_carbonemmision_energy+int(response_data['carbonEquivalent'])
                print(response.text)
            if other_clean_energy:
                url = "https://carbonfootprint1.p.rapidapi.com/CleanHydroToCarbonFootprint"

                querystring = {"energy":"Other","consumption":str(other_clean_energy)}

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_energy=total_carbonemmision_energy+int(response_data['carbonEquivalent'])
                print(response.text)
                
            print("total carbon emmision is",total_carbonemmision_energy)
        
          
            fuel_petrol = request.POST['Fuel_petrol']
            fuel_diesel = request.POST['Fuel_Diesel']  
            fuel_LPG=request.POST['Fuel_LPG']  
            total_carbonemmision_fuel=0
            
            if fuel_petrol:
                url = "https://carbonfootprint1.p.rapidapi.com/FuelToCO2e"

                querystring = {"type":"Petrol","litres":str(fuel_petrol)}

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_fuel=total_carbonemmision_fuel+int(response_data['carbonEquivalent'])
                print(response.text)
            if fuel_diesel:
                url = "https://carbonfootprint1.p.rapidapi.com/FuelToCO2e"

                querystring = {"type":"Diesel","litres":str(fuel_diesel)}

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_fuel=total_carbonemmision_fuel+int(response_data['carbonEquivalent'])
                print(response.text)
            if fuel_LPG:
                url = "https://carbonfootprint1.p.rapidapi.com/FuelToCO2e"

                querystring = {"type":"LPG","litres":str(fuel_LPG)}

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_fuel=total_carbonemmision_fuel+int(response_data['carbonEquivalent'])
                print(response.text)
            print("total carbon emmision is",total_carbonemmision_fuel)
            
            
            
            total_carbonemmision_cars=0
                
            SmallDieselCar = request.POST['SmallDieselCar']
            MediumDieselCar = request.POST['MediumDieselCar']
            LargeDieselCar = request.POST['LargeDieselCar']
            MediumHybridCar = request.POST['MediumHybridCar']
            LargeHybridCar = request.POST['LargeHybridCar']
            MediumLPGCar = request.POST['MediumLPGCar']
            LargeLPGCar = request.POST['LargeLPGCar']
            MediumCNGCar = request.POST['MediumCNGCar']
            SmallPetrolVan = request.POST['SmallPetrolVan']  
            LargePetrolVan=request.POST['LargePetrolVan']   
            SmallDieselVan=request.POST['SmallDieselVan']
            MediumPetrolCar=request.POST['MediumPetrolCar']   
            LargePetrolCar=request.POST['LargePetrolCar']  
            SmallMotorBike=request.POST['SmallMotorBike']  
            MediumMotorBike = request.POST['MediumMotorBike'] 
            LargeMotorBike=request.POST['LargeMotorBike'] 
            LargeCNGCar=request.POST['LargeCNGCar']
            MediumDieselVan=1
            # request.POST['MediumDieselVan']
            LargeDieselVan=request.POST['LargeDieselVan']
            LPGVan=request.POST['LPGVan']
            CNGVan=request.POST['CNGVan']
            SmallPetrolCar=request.POST['SmallPetrolCar']
            
            if SmallPetrolCar:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromCarTravel"

                querystring = {"distance":str(SmallPetrolCar),"vehicle":"SmallPetrolCar"} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_cars=total_carbonemmision_cars+int(response_data['carbonEquivalent'])
                print(response.text)
            if CNGVan:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromCarTravel"

                querystring = {"distance":str(CNGVan),"vehicle":"CNGVan"} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_cars=total_carbonemmision_cars+int(response_data['carbonEquivalent'])
                print(response.text)
            
            
            if LPGVan:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromCarTravel"

                querystring = {"distance":str(LPGVan),"vehicle":"LPGVan"} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_cars=total_carbonemmision_cars+int(response_data['carbonEquivalent'])
                print(response.text)
            
            
            if SmallDieselCar:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromCarTravel"

                querystring = {"distance":str(SmallDieselCar),"vehicle":"SmallDieselCar"} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_cars=total_carbonemmision_cars+int(response_data['carbonEquivalent'])
                print(response.text)  
            
            if MediumDieselCar:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromCarTravel"

                querystring = {"distance":str(MediumDieselCar),"vehicle":"MediumDieselCar"} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_cars=total_carbonemmision_cars+int(response_data['carbonEquivalent'])
                print(response.text)
                
            if LargeDieselCar:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromCarTravel"

                querystring = {"distance":str(LargeDieselCar),"vehicle":"LargeDieselCar"} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_cars=total_carbonemmision_cars+int(response_data['carbonEquivalent'])
                print(response.text)
            
            if MediumHybridCar:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromCarTravel"

                querystring = {"distance":str(MediumHybridCar),"vehicle":"MediumHybridCar"} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_cars=total_carbonemmision_cars+int(response_data['carbonEquivalent'])
                print(response.text)
            if LargeHybridCar:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromCarTravel"

                querystring = {"distance":str(LargeHybridCar),"vehicle":"LargeHybridCar"} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_cars=total_carbonemmision_cars+int(response_data['carbonEquivalent'])
                print(response.text)
                
            if MediumLPGCar:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromCarTravel"

                querystring = {"distance":str(MediumLPGCar),"vehicle":"MediumLPGCar"} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_cars=total_carbonemmision_cars+int(response_data['carbonEquivalent'])
                print(response.text)
            
            if LargeLPGCar:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromCarTravel"

                querystring = {"distance":str(LargeLPGCar),"vehicle":"LargeLPGCar"} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_cars=total_carbonemmision_cars+int(response_data['carbonEquivalent'])
                print(response.text)
                
            if MediumCNGCar:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromCarTravel"

                querystring = {"distance":str(MediumCNGCar),"vehicle":"MediumCNGCar"} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_cars=total_carbonemmision_cars+int(response_data['carbonEquivalent'])
                print(response.text)
            if LargeCNGCar:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromCarTravel"

                querystring = {"distance":str(LargeCNGCar),"vehicle":"LargeCNGCar"} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_cars=total_carbonemmision_cars+int(response_data['carbonEquivalent'])
                print(response.text)
            if SmallPetrolVan:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromCarTravel"

                querystring = {"distance":str(SmallPetrolVan),"vehicle":"SmallPetrolVan"} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_cars=total_carbonemmision_cars+int(response_data['carbonEquivalent'])
                print(response.text)
            if LargePetrolVan:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromCarTravel"

                querystring = {"distance":str(LargePetrolVan),"vehicle":"LargePetrolVan"} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_cars=total_carbonemmision_cars+int(response_data['carbonEquivalent'])
                print(response.text)
            if SmallDieselVan:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromCarTravel"

                querystring = {"distance":str(SmallDieselVan),"vehicle":"SmallDieselVan"} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_cars=total_carbonemmision_cars+int(response_data['carbonEquivalent'])
                print(response.text)
                
            if MediumPetrolCar:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromCarTravel"

                querystring = {"distance":str(MediumPetrolCar),"vehicle":"MediumPetrolCar"} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_cars=total_carbonemmision_cars+int(response_data['carbonEquivalent'])
                print(response.text)
            if LargePetrolCar:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromCarTravel"

                querystring = {"distance":str(LargePetrolCar),"vehicle":"LargePetrolCar"} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_cars=total_carbonemmision_cars+int(response_data['carbonEquivalent'])
                print(response.text)
            if SmallMotorBike:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromCarTravel"

                querystring = {"distance":str(SmallMotorBike),"vehicle":"SmallMotorBike"} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_cars=total_carbonemmision_cars+int(response_data['carbonEquivalent'])
                print(response.text)
            if LargeMotorBike:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromCarTravel"

                querystring = {"distance":str(LargeMotorBike),"vehicle":"LargeMotorBike"} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_cars=total_carbonemmision_cars+int(response_data['carbonEquivalent'])
                print(response.text)
            # if MediumDieselVan:
            #     url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromCarTravel"

            #     querystring = {"distance":str(MediumDieselVan),"vehicle":"MediumDieselVan"} 

            #     response = requests.request("GET", url, headers=headers, params=querystring)
            #     response_data = response.json()
            #     total_carbonemmision_cars=total_carbonemmision_cars+int(response_data['carbonEquivalent'])
            #     print(response.text)
            if LargeDieselVan:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromCarTravel"

                querystring = {"distance":str(LargeDieselVan),"vehicle":"LargeDieselVan"} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_cars=total_carbonemmision_cars+int(response_data['carbonEquivalent'])
                print(response.text)
                
                
            DomesticFlight = request.POST.get('DomesticFlight')
            ShortEconomyClassFlight = request.POST.get('ShortEconomyClassFlight')
            ShortBusinessClassFlight= request.POST.get('ShortBusinessClassFlight')
            LongEconomyClassFlight= request.POST.get('LongEconomyClassFlight')  
            LongPremiumClassFlight= request.POST.get('LongPremiumClassFlight')   
            LongBusinessClassFlight=  request.POST.get('LongBusinessClassFlight')  
            LongFirstClassFlight = request.POST.get('LongFirstClassFlight')
            total_carbonemmision_flights=0
            
            
            if DomesticFlight:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromFlight"

                querystring = {"distance":str(DomesticFlight),"type":"DomesticFlight"}
                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_flights=total_carbonemmision_flights+int(response_data['carbonEquivalent'])
                print(response.text)
            if ShortEconomyClassFlight:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromFlight"

                querystring = {"distance":str(ShortEconomyClassFlight),"type":"ShortEconomyClassFlight"}
                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_flights=total_carbonemmision_flights+int(response_data['carbonEquivalent'])
                print(response.text)
            if ShortBusinessClassFlight:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromFlight"

                querystring = {"distance":str(ShortBusinessClassFlight),"type":"ShortBusinessClassFlight"}
                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_flights=total_carbonemmision_flights+int(response_data['carbonEquivalent'])
                print(response.text)
            if LongEconomyClassFlight:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromFlight"

                querystring = {"distance":str(LongEconomyClassFlight),"type":"LongEconomyClassFlight"}
                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_flights=total_carbonemmision_flights+int(response_data['carbonEquivalent'])
                print(response.text)
            if LongPremiumClassFlight:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromFlight"

                querystring = {"distance":str(LongPremiumClassFlight),"type":"LongPremiumClassFlight"}
                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_flights=total_carbonemmision_flights+int(response_data['carbonEquivalent'])
                print(response.text)
            if LongBusinessClassFlight:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromFlight"

                querystring = {"distance":str(LongBusinessClassFlight),"type":"LongBusinessClassFlight"}
                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_flights=total_carbonemmision_flights+int(response_data['carbonEquivalent'])
                print(response.text)
            if LongFirstClassFlight:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromFlight"

                querystring = {"distance":str(LongFirstClassFlight),"type":"LongFirstClassFlight"}
                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_flights=total_carbonemmision_flights+int(response_data['carbonEquivalent'])
                print(response.text)
            
            SmallMotorBike= request.POST.get('SmallMotorBike')  
            MediumMotorBike= request.POST.get('MediumMotorBike')  
            LargeMotorBike = request.POST.get('LargeMotorBike')  
            Taxi= request.POST.get('Taxi')   
            ClassicBus= request.POST.get('ClassicBus')   
            EcoBus = request.POST.get('EcoBus')  
            Coach= request.POST.get('Coach')   
            NationalTrain= request.POST.get('NationalTrain')   
            LightRail=  request.POST.get('LightRail')   
            Subway= request.POST.get('Subway') 
            total_carbonemmision_othervehicles=0
            if SmallMotorBike:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromMotorBike"

                querystring = {"type":"SmallMotorBike","distance":str(SmallMotorBike)} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_othervehicles=total_carbonemmision_othervehicles+int(response_data['carbonEquivalent'])
                print(response.text)
            if MediumMotorBike:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromMotorBike"

                querystring = {"type":"MediumMotorBike","distance":str(MediumMotorBike)} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_othervehicles=total_carbonemmision_othervehicles+int(response_data['carbonEquivalent'])
                print(response.text)
            if LargeMotorBike:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromMotorBike"

                querystring = {"type":"LargeMotorBike","distance":str(LargeMotorBike)} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_othervehicles=total_carbonemmision_othervehicles+int(response_data['carbonEquivalent'])
                print(response.text)
            if Taxi:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromPublicTransit"

                querystring = {"type":"Taxi","distance":str(Taxi)} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_othervehicles=total_carbonemmision_othervehicles+int(response_data['carbonEquivalent'])
                print(response.text)
            if ClassicBus:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromPublicTransit"

                querystring = {"type":"ClassicBus","distance":str(ClassicBus)} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_othervehicles=total_carbonemmision_othervehicles+int(response_data['carbonEquivalent'])
                print(response.text)
            if EcoBus:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromPublicTransit"

                querystring = {"type":"EcoBus","distance":str(EcoBus)} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_othervehicles=total_carbonemmision_othervehicles+int(response_data['carbonEquivalent'])
                print(response.text)
            if Coach:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromPublicTransit"

                querystring = {"type":"Coach","distance":str(Coach)} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_othervehicles=total_carbonemmision_othervehicles+int(response_data['carbonEquivalent'])
                print(response.text)
            if NationalTrain:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromPublicTransit"

                querystring = {"type":"NationalTrain","distance":str(NationalTrain)} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_othervehicles=total_carbonemmision_othervehicles+int(response_data['carbonEquivalent'])
                print(response.text)
            if LightRail:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromPublicTransit"

                querystring = {"type":"LightRail","distance":str(LightRail)} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_othervehicles=total_carbonemmision_othervehicles+int(response_data['carbonEquivalent'])
                print(response.text)
            if Subway:
                url = "https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromPublicTransit"

                querystring = {"type":"Subway","distance":str(Subway)} 

                response = requests.request("GET", url, headers=headers, params=querystring)
                response_data = response.json()
                total_carbonemmision_othervehicles=total_carbonemmision_othervehicles+int(response_data['carbonEquivalent'])
                print(response.text)  

            print("total_carbonemmision_othervehicles",total_carbonemmision_othervehicles)
            purchased_heat= request.POST.get('purchased_heat')
            purchased_heat_emmision=purchased_heat*3
            
            purchased_cooling= request.POST.get('purchased_cooling')
            purchased_cooling_emmision=purchased_cooling*2
            
#             entry=carbon_emmision(
#                 company_name,
#                                   tree_eq,
#                                   traditional_hydro_emmision,
#                 location,
#                 solar_energy,
#                 wind_energy,
#                 hydroelectric_energy,
#                 biomass_energy,
#                 geothermal_energy,
#                 other_clean_energy,
#                 fuel_petrol,
#                 fuel_diesel,
#                 fuel_LPG,
#                 SmallDieselCar,
#                 MediumDieselCar ,
#                     LargeDieselCar,   
#                 MediumHybridCar,  
# LargeHybridCar,   
# MediumLPGCar,  
# LargeLPGCar, 
# MediumCNGCar,
# LargeCNGCar, 
# SmallPetrolVan,  
# LargePetrolVan,
# SmallDieselVan,
# MediumDieselVan,
# LargeDieselVan,
# LPGVan,
# CNGVan,
# SmallPetrolCar,
# MediumPetrolCar,
# LargePetrolCar,  
# SmallMotorBike,  
# MediumMotorBike,   
# LargeMotorBike,
# DomesticFlight,
# ShortEconomyClassFlight,  
# ShortBusinessClassFlight,  
# LongEconomyClassFlight,   
# LongPremiumClassFlight,   
# LongBusinessClassFlight,   
# LongFirstClassFlight,  
# Taxi,   
# ClassicBus,   
# EcoBus,   
# Coach,   
# NationalTrain,   
# LightRail,   
# Subway,
# purchased_heat,   
# purchased_cooling)
#             entry.save()
            return render(request, 'dashboard.html')
    else:
        form = carbon_emmision()
    return render(request, 'accept_info.html', {'form': form})
