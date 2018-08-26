from django.contrib import admin
from mysite import models

class PostAdmin(admin.ModelAdmin):
    list_display = ('name',)
# Register your models here.

admin.site.register(models.Maker,PostAdmin)
admin.site.register(models.PModel,PostAdmin)
admin.site.register(models.Product)
admin.site.register(models.PPhoto)

