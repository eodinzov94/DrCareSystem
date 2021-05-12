from django.contrib import admin
from patient.models import *
# Register your models here.
admin.site.register(HealthParameters)
admin.site.register(Questionnaire)
admin.site.register(Visit)
admin.site.register(Patient)