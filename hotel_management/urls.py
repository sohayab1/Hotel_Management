"""
URL configuration for hotel_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from hotel_management import views
from django.conf import settings
from django.conf.urls.static import static
from .views import help_page, chat_with_ai,send_query_to_employee,homepage, news_details, best_hotel, world_tourist_spot, event_management,customer_service, terms_conditions, facilities, contact, aboutus, customer_view, customer_register
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotel.urls')),
    path('', homepage, name='HomePage'),
    path('help_page/', help_page, name='help_page'),
    path('chat/', chat_with_ai, name='chat_with_ai'),
    path('send_query/', send_query_to_employee, name='send_query_to_employee'),
    path('news&details/',news_details,name='News&Details'),
    path('besthotel/', best_hotel, name='BestHotel'),
    path('worldtouristspot/', world_tourist_spot, name='WorldTouristSpot'),
    path('eventmanagement/', event_management, name='EventManagement'),
    path('customerservice/', customer_service, name='CustomerService'),
    path('terms&conditions/', terms_conditions, name='Terms&Conditions'),
    path('facilities/', facilities, name='Facilities'),
    path('contact/', contact, name='Contact'),
    path('aboutus/', aboutus, name='AboutUs'),
    path('customerview/', customer_view, name='Customer'),
    path('customerregister/', customer_register, name='Customer'),
    path('auth/',include('auth_app.urls')),
    path("",include("paymenthandle.urls"))
   
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


