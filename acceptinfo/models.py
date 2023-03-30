from django.db import models

class Energy_generation(models.Model):
    company_name=models.CharField(max_length=100)
    E_coal=models.IntegerField()
    E_hydro=models.IntegerField()
    E_nuclear=models.IntegerField()
    E_petroleum=models.IntegerField()
    E_wind=models.IntegerField()
    E_others=models.IntegerField()




class gas(models.Model):
    company_name=models.CharField(max_length=100)
    blast_furnace_gas=models.IntegerField()
    coke_ovens_gas=models.IntegerField()
    gas_works_gas=models.IntegerField()
    natural_gas=models.IntegerField()
    diesel_oil=models.IntegerField()
    
    
class pipeline(models.Model):
    company_name=models.CharField(max_length=100)
    pipeline_transport=models.IntegerField()
    

class facility(models.Model):
    company_name=models.CharField(max_length=100)
    education_facility=models.IntegerField()
    food_sale_facility=models.IntegerField()
    healthcare_facility=models.IntegerField()
    lodging_facility=models.IntegerField()
    manufacturing_facility=models.IntegerField()
    office_facility=models.IntegerField()
    other_facility=models.IntegerField()
    
    
class other(models.Model):
    company_name=models.CharField(max_length=100)
    residental_maintainance=models.IntegerField()
    non_residential_maintainance=models.IntegerField()
    hotel_and_retaurant_service=models.IntegerField()
    
class fugitive_gases(models.Model):
    company_name=models.CharField(max_length=100)
    purchased_steam=models.IntegerField()
    domestic_heating=models.IntegerField()
    
class water(models.Model):
    company_name=models.CharField(max_length=100)
    water_supply=models.IntegerField()
    water_treatment=models.IntegerField()
    collected_and_purified_water=models.IntegerField()
    
class equipment(models.Model):
    company_name=models.CharField(max_length=100)
    electrical_machine=models.IntegerField()
    medical_precision_instruments=models.IntegerField()
    radio_television=models.IntegerField()
    rental_equipment=models.IntegerField()
    others=models.IntegerField()
    office_computers=models.IntegerField()
    
class product(models.Model):
    company_name=models.CharField(max_length=100)
    private_household_goods=models.IntegerField()
    beverages=models.IntegerField()
    dairy_products=models.IntegerField()
    fish_products=models.IntegerField()
    other_food_products=models.IntegerField()
    furniture=models.IntegerField()
    leather_goods=models.IntegerField()
    meat_goods=models.IntegerField()
    processed_rice=models.IntegerField()
    sugar_products=models.IntegerField()
    vegetable_oil=models.IntegerField()
    wearing_apparel=models.IntegerField()
    retail_trade=models.IntegerField()
    retail_trade_others=models.IntegerField()
    paper_products=models.IntegerField()
    textile=models.IntegerField()
    

class vehicles(models.Model):
    company_name=models.CharField(max_length=100)
    diesel_distance=models.IntegerField()
    gasoline_distance=models.IntegerField()
    electric_distance=models.IntegerField()
    cng_distance=models.IntegerField()
    lpg_distance=models.IntegerField()
    bus_distance=models.IntegerField()
    business_taxi_distance=models.IntegerField()
    
class transportation(models.Model):
    company_name=models.CharField(max_length=100)
    warehouse=models.IntegerField()
    upstream_transportation=models.IntegerField()
    air_freight=models.IntegerField()
    water_freight=models.IntegerField()
    rail=models.IntegerField()
    inland_transportation=models.IntegerField()
    other=models.IntegerField()
    
    
    
    
    
    
    
    