from django.contrib import admin
from .models import Profile

# Register your models here.
#admin.site.register(Profile)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user_id', 'location', 'secteur_activite', 'structure_juridique', 'business_model', 'taille','Portee_geographique']
    ordering = ('pk',)
    list_filter = ('location', 'secteur_activite', 'structure_juridique', 'business_model', 'taille','Portee_geographique')
    search_fields = ('user_id', 'location', 'secteur_activite', 'structure_juridique', 'business_model', 'taille',)