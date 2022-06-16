from django.contrib import admin

from imageApp.models import Image

# Register your models here.
@admin.register(Image)
class imageAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'upload_date']