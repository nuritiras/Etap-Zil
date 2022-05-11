from django.contrib import admin
from .models import DuyuruModel,SaatModel,OgrenciMelodiModel,OgretmenMelodiModel,CikisMelodiModel

# Register your models here.
admin.site.register(DuyuruModel)
admin.site.register(SaatModel)
admin.site.register(OgrenciMelodiModel)
admin.site.register(OgretmenMelodiModel)
admin.site.register(CikisMelodiModel)
