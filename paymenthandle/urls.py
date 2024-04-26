from django.urls import path
from . import views
from .views import generate_pdf
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('payment/', views.process_payment, name='process_payment'),
    
   path('payment/success/<str:name>/<int:num_rooms>/<str:room_type>/<str:payment_option>/<amount>/', views.payment_success, name='payment_success'),

    path('generate_pdf/<str:name>/<int:num_rooms>/<str:room_type>/<str:payment_option>/<amount>/', generate_pdf, name='generate_pdf'),
    path('get_hotel_name/', views.get_hotel_name, name='get_hotel_name'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)