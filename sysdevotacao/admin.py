from django.contrib import admin
from .models import turmas,escola
# Register your models here.
@admin.register(turmas)
class turmasAdmin(admin.ModelAdmin):
    list_display = ('id','titulo')

@admin.register(escola)
class escolaAdmin(admin.ModelAdmin):
    list_display = ('id',)

