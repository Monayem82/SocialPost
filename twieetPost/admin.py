from django.contrib import admin
from . models import TwieetModel

class TwieetAdmin(admin.ModelAdmin):
    list_display=['user','text','photos','created_at','updated_at']


admin.site.register(TwieetModel,TwieetAdmin)
