from django.http import HttpResponse
from django.shortcuts import render
from hotel.models import PromoCode


def homepage(request):
    
    data={
        'title':'HomePage'
    }
    return render(request,'index.html',data)
def homepage(request):
    promo_codes = PromoCode.objects.all()
    return render(request, 'index.html', {'promo_codes': promo_codes})

def aboutus(request):
    return HttpResponse('1')

def news_details(request):
  return render(request,'news&details.html')

def best_hotel(request):
    return render(request,'besthotel.html')

def world_tourist_spot(request):
    return render(request,'worldtouristspot.html')

def event_management(request):
    return render(request,'eventmanagement.html')

def customer_service(request):
    return render(request,'customerservice.html')

def terms_conditions(request):
    return render(request,'terms&conditions.html')

def facilities(request):
    return render(request,'facilities.html')

def contact(request):
    return render(request,'contact.html')

def aboutus(request):
    return render(request,'aboutus.html')

def customer_view(request):
    return render(request,'customerview.html')

def customer_register(request):
    return render(request,'customerregister.html')

def help_page(request):
    return render(request, 'help_page.html')

def chat_with_ai(request):
    # Here you can implement the logic to interact with AI for generating responses
    # For simplicity, let's assume the AI generates a fixed response
    ai_response = "Hello! How can I assist you today?"
    return render(request, 'chat.html', {'ai_response': ai_response})

def send_query_to_employee(request):
    # Code to handle sending user queries to customer service employees
    # This could involve sending emails, creating tickets in a support system, etc.
    return render(request, 'query_confirmation.html')