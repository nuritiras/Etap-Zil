from django.contrib import admin
from .models import okulzili

class ZilAdmin(admin.ModelAdmin):
    list_display =('id','name','description','isPublished')
    list_display_links =('id','name')
    list_filter = ('description',)
    list_editable =('isPublished',)
    serach_fields =('name','description',)

# Register your models here.
admin.site.register(okulzili,ZilAdmin)
