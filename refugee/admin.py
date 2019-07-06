from django.contrib import admin

from .models.refugee import Refugee
from .models.location import Location
from .models.qa import Qa
from .models.story import Story


admin.site.register(Refugee)
admin.site.register(Location)
admin.site.register(Qa)
admin.site.register(Story)
