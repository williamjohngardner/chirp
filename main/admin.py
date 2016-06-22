from django.contrib import admin
from main.models import Chirp, StopWord, Profile

class ChirpAdmin(admin.ModelAdmin):
    list_display = ["body", "bird", "created"]
    search_fields = ['body']

admin.site.register(Chirp, ChirpAdmin)



class StopAdmin(admin.ModelAdmin):
    list_display = ["word"]
    search_fields = ['word']

admin.site.register(StopWord, StopAdmin)

admin.site.register(Profile)
