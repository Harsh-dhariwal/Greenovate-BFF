from django import forms
from .models import comp_database




class carbon_emmision(forms.ModelForm):
    class Meta:
        model = comp_database
        fields = ('company_name','paper_use','traditional_hydro_use','traditional_hydro_location',
                  'solar_energy','wind_energy','hydroelectric_energy','biomass_energy',
                  'geothermal_energy','other_clean_energy','Fuel_petrol','Fuel_Diesel',
                  'Fuel_LPG','SmallDieselCar', 'MediumDieselCar', 'LargeDieselCar', 
                  'MediumHybridCar', 'LargeHybridCar', 'MediumLPGCar', 'LargeLPGCar', 
                  'MediumCNGCar', 'LargeCNGCar', 'SmallPetrolVan', 'LargePetrolVan', 'SmallDielselVan', 
                  'MediumDielselVan', 'LargeDielselVan', 'LPGVan', 'CNGVan', 'SmallPetrolCar', 
                  'MediumPetrolCar', 'LargePetrolCar', 'SmallMotorBike', 'MediumMotorBike', 'LargeMotorBike',
                  'DomesticFlight', 'ShortEconomyClassFlight', 'ShortBusinessClassFlight',
                 'LongEconomyClassFlight','LongPremiumClassFlight', 
                 'LongBusinessClassFlight', 'LongFirstClassFlight',
                 'SmallMotorBike', 'MediumMotorBike', 'LargeMotorBike',
                 'Taxi', 'ClassicBus', 'EcoBus', 'Coach', 
                 'NationalTrain', 'LightRail', 'Subway', 'FerryOnFoot', 'FerryInCar'
                  
                  )
