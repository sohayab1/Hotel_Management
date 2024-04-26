from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views
from .views import  HotelSearchView1,show_review, hotel_detail1, hotel_list,hotel_detail,RoomListView, BookingList, RoomDetailView,RoomDetailView1, review_success, review, HotelSearchView, HotelSelectionView
app_name='hotel'

urlpatterns=[
    path('room_list/',RoomListView, name='RoomList'), #view er Roomlist ke room_list hishebe view korbe
    path('room_list1/',views.RoomListView1, name='RoomList1'),
    path('booking_list/',BookingList.as_view(), name='BookingList'), # view er BookingList ke booking_list hishebe url nibe 
    path('room/<str:selected_room_type>/', views.room_detail_view, name='room_detail'),
    path('room/<str:selected_room_type>/', views.room_detail_view1, name='room_detail1'),
    path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView'),
    path('room/<category>', RoomDetailView1.as_view(), name='RoomDetailView1'),
    path('review/', review, name='review'),
    path('review_success/', review_success, name='review_success'),
    path('hotel_search_results/', HotelSearchView.as_view(), name='hotel_search'),
    path('hotel-selection/', HotelSelectionView.as_view(), name='hotel_selection'),
    path('hotel_list/', hotel_list, name='hotel_list'),
    path('hotel_detail/<id>/', hotel_detail, name='hotel_detail'),
    path('hotel_search_results1/', HotelSearchView1.as_view(), name='hotel_search1'),
    path('hotel_detail1/<id>/', hotel_detail1, name='hotel_detail1'),
    path('show_review/', show_review, name='show_review'),
    path('auth/',include('auth_app.urls'))
    

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#url--views