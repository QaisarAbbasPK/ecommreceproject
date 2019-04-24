from django.contrib import admin

from .models import Nut, Oil, PastaNoodle, Offer, ContactUs


class NutAdmin(admin.ModelAdmin):
      list_display = ('name','image','price','discount')

class OilAdmin(admin.ModelAdmin):
      list_display = ('name','image','price','discount')


class PastaNoodleAdmin(admin.ModelAdmin):

      list_display = ('name','image','price','discount')
      
class OfferAdmin(admin.ModelAdmin):

      list_display = ('name','image','price','saveprice')

class ContactUsAdmin(admin.ModelAdmin):

      list_display = ('name','subject','email','massege')             
                  

# Register your models here.

admin.site.register(Nut, NutAdmin)
admin.site.register(Oil, OilAdmin)
admin.site.register(PastaNoodle, PastaNoodleAdmin)
admin.site.register(Offer,OfferAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
