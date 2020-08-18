from django.contrib import admin
from .models import  Rdv
from collections import OrderedDict
from datetime import date
from rendez_vous.models import Rdv




# Register your models here


class RdvAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'date', 'heure', 'status')
    search_fields = ('nom', 'prenom')
    fieldsets = (
        ('        ', {
            'fields': ['status', ]
        }),

        ('          ', {
            'fields': [('nom', 'prenom'), ('date', 'heure')]
        }),
    )
    list_editable=('status', )
    ordering= ('date',)


    

"""
class HeureAdmin(admin.ModelAdmin):
    ordering=('heure',)

"""
admin.site.register(Rdv, RdvAdmin)
#admin.site.register(Heure, HeureAdmin)







