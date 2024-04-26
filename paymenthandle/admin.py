# from django.contrib import admin

# from .models import Payment

# admin.site.register(Payment)

#new try -----------------

from django.contrib import admin
from .models import Payment



class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name','check_in','check_out','payment_option', 'amount', 'card_number', 'expiry_date', 'cvv', 'phone_number','promo_code','num_rooms','room_type',)
    
   

admin.site.register(Payment, PaymentAdmin)

