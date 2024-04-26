from django.contrib import admin
from .models import Room, Review, Hotel,PromoCode

admin.site.register(Room)
# admin.site.register(Booking)
admin.site.register(Hotel)


class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'start_date', 'end_date')
    search_fields = ('code', 'description')
    list_filter = ('start_date', 'end_date')

admin.site.register(PromoCode, PromoCodeAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['rating', 'comment', 'created_at']  # Adjusted list_display
    list_filter = ['created_at']
    search_fields = ['comment']

admin.site.register(Review, ReviewAdmin)


# Register your models here.
