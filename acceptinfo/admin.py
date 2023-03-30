from django.contrib import admin
from .models import Energy_generation,gas,pipeline,facility,other,fugitive_gases,water,equipment,transportation,vehicles,product


# Register your models here.
admin.site.register(Energy_generation)
admin.site.register(gas)
admin.site.register(pipeline)
admin.site.register(facility)
admin.site.register(other)
admin.site.register(fugitive_gases)
admin.site.register(water)
admin.site.register(equipment)
admin.site.register(transportation)
admin.site.register(vehicles)
admin.site.register(product)

