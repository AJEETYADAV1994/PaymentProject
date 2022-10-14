from django.contrib import admin

# Register your models here.
from .models import Coffee
# admin.site.register(Coffee)

class AdminCoffe(admin.ModelAdmin):
    list_display=['name','amount','payment_id','paid']
admin.site.register(Coffee,AdminCoffe)