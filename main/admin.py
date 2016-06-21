from django.contrib import admin
from main.models import Chirp

class ChirpAdmin(admin.ModelAdmin):
    list_display = ["body", "bird", "created"]
    search_fields = ['body']

admin.site.register(Chirp, ChirpAdmin)
