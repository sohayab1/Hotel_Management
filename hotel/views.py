from django.shortcuts import render ,get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import ListView, FormView , View, DetailView
from django.urls import reverse

from .models import  Room,Booking, Review, Hotel, PromoCode
from .forms import  AvailabilityForm, ReviewForm

from hotel.booking_functions.availability import check_availability

# Create your views here.
from .models import PromoCode

def homepage(request):
    promo_codes = PromoCode.objects.all()  # Assuming you have a PromoCode model
    return render(request, 'index.html', {'promo_codes': promo_codes})

class HotelSelectionView(View):
    def get(self, request, hotel_id):
        try:
            hotel = Hotel.objects.get(id=hotel_id)
            return redirect('room_list', hotel_id=hotel.id)
        except Hotel.DoesNotExist:
            return render(request, 'hotel_not_found.html')
        
class HotelSearchView(View):
    def get(self, request):
        query = request.GET.get('query', '')
        hotels = Hotel.objects.filter(location__icontains=query) | Hotel.objects.filter(name__icontains=query)
        return render(request, 'hotel_search_results.html', {'hotels': hotels, 'query': query})
    
class HotelSearchView1(View):
    def get(self, request):
        query = request.GET.get('query', '')
        hotels = Hotel.objects.filter(location__icontains=query) | Hotel.objects.filter(name__icontains=query)
        return render(request, 'hotel_search_results1.html', {'hotels': hotels, 'query': query})

def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel_list.html', {'hotels': hotels})

def hotel_detail(request, id):
    hotel = get_object_or_404(Hotel, id=id)
    rooms = Room.objects.filter(id=id)
  
    return render(request, 'hotel_detail.html', {'hotel': hotel, 'rooms':rooms})

def hotel_detail1(request, id):
    hotel = get_object_or_404(Hotel, id=id)
    rooms = Room.objects.filter(id=id)
  
    return render(request, 'hotel_detail1.html', {'hotel': hotel, 'rooms':rooms})

def RoomListView(request) : 
    room=Room.objects.all()[0]
    room_categories= dict(room.Room_Categories)
    
    room_values=room_categories.values()
    room_list=[]
    for room_category in room_categories:
        room=room_categories.get(room_category)
        room_url=reverse('hotel:RoomDetailView' , kwargs={'category':room_category})
        
        # print(room,room_url)
        room_list.append((room,room_url))
        
        
        
    
    context={
        "room_list":room_list,
    }
    print(room_list)
    return render(request, 'room_list_view.html',context)

def RoomListView(request) : 
    room=Room.objects.all()[0]
    room_categories= dict(room.Room_Categories)
    
    room_values=room_categories.values()
    room_list=[]
    for room_category in room_categories:
        room=room_categories.get(room_category)
        room_url=reverse('hotel:RoomDetailView' , kwargs={'category':room_category})
        
        # print(room,room_url)
        room_list.append((room,room_url))
        
        
        
    
    context={
        "room_list":room_list,
    }
    print(room_list)
    return render(request, 'room_list_view.html',context)

def RoomListView1(request) : 
    room=Room.objects.all()[0]
    room_categories= dict(room.Room_Categories)
    
    room_values=room_categories.values()
    room_list=[]
    for room_category in room_categories:
        room=room_categories.get(room_category)
        room_url=reverse('hotel:RoomDetailView1' , kwargs={'category':room_category})
        
        # print(room,room_url)
        room_list.append((room,room_url))
        
        
        
    
    context={
        "room_list":room_list,
    }
    print(room_list)
    return render(request, 'room_list_view1.html',context)




class BookingList(ListView) :
    model=Booking


class RoomDetailView(View):
    def get(self, request, *args , **kwargs):
        category=self.kwargs.get('category', None)
        form=AvailabilityForm()

        room_list=Room.objects.filter(category=category) 

        if len(room_list)>0:
            room=room_list[0]
            room_category= dict(room.Room_Categories).get(room.category,None)
            context={
            'room_category': room_category,
            'form': form,
            'selected_room_type': category ,
            }
            return render(request, 'room_detail_view.html', context)

        else:
            return HttpResponse('Category Does Not Exist')


    def post(self, request, *args , **kwargs):
        category=self.kwargs.get('category', None)
        room_list=Room.objects.filter(category=category) 
        form=AvailabilityForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data

        available_rooms=[]
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)


        if len(available_rooms)>0:
         room=available_rooms[0]
         booking=Booking.objects.create(
            user=self.request.user,
            room =room,
            check_in=data['check_in'],
            check_out=data['check_out']

         )

         booking.save() 
         return HttpResponse(booking)
        else :
            return HttpResponse('All of This category of rooms are booked !! Try Another One..Good Luck !!')


class RoomDetailView1(View):
    def get(self, request, *args , **kwargs):
        category=self.kwargs.get('category', None)
        form=AvailabilityForm()

        room_list=Room.objects.filter(category=category) 

        if len(room_list)>0:
            room=room_list[0]
            room_category= dict(room.Room_Categories).get(room.category,None)
            context={
            'room_category': room_category,
            'form': form,
            'selected_room_type': category ,
            }
            return render(request, 'room_detail_view1.html', context)

        else:
            return HttpResponse('Category Does Not Exist')


    def post(self, request, *args , **kwargs):
        category=self.kwargs.get('category', None)
        room_list=Room.objects.filter(category=category) 
        form=AvailabilityForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data

        available_rooms=[]
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)


        if len(available_rooms)>0:
         room=available_rooms[0]
         booking=Booking.objects.create(
            user=self.request.user,
            room =room,
            check_in=data['check_in'],
            check_out=data['check_out']

         )

         booking.save() 
         return HttpResponse(booking)
        else :
            return HttpResponse('All of This category of rooms are booked !! Try Another One..Good Luck !!')

       
        
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review.objects.create(
            rating=form.cleaned_data['rating'],
            comment=form.cleaned_data['comment']
            )
            
            return redirect('hotel:review_success')
    else:
        form = ReviewForm()
    return render(request, 'review.html', {'form': form})

def review_success(request):
    return render(request, 'review_success.html')



def show_review(request):
    reviews = Review.objects.all()
    return render(request, 'show_review.html', {'reviews': reviews})

def room_detail_view(request, selected_room_type):
    # Your code to handle room booking
    # Assuming selected_room_type is determined dynamically
    
    # Pass the selected room type to the payment form view
    room_options = [
        {'value': 'NAC', 'label': 'Non AC'},
        {'value': 'YAC', 'label': 'AC'},
        {'value': 'DEL', 'label': 'Deluxe'},
        {'value': 'KIN', 'label': 'King'},
        {'value': 'QUE', 'label': 'Queen'},
    ]
    return render(request, 'payment_form.html', {'selected_room_type': selected_room_type, 'room_options': room_options})

def room_detail_view1(request, selected_room_type):
    # Your code to handle room booking
    # Assuming selected_room_type is determined dynamically
    
    # Pass the selected room type to the payment form view
    room_options = [
        {'value': 'NAC', 'label': 'Non AC'},
        {'value': 'YAC', 'label': 'AC'},
        {'value': 'DEL', 'label': 'Deluxe'},
        {'value': 'KIN', 'label': 'King'},
        {'value': 'QUE', 'label': 'Queen'},
    ]
    return render(request, 'room_detail_view1.html', {'selected_room_type': selected_room_type, 'room_options': room_options})