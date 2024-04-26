from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from hotel.models import Hotel,Room
from .forms import PaymentForm
from django.core.mail import send_mail, EmailMessage
from django.utils import timezone

from django.conf import settings

from django.http import JsonResponse
from django.contrib import messages
from .models import Payment

# def payment_view(request):
#     # Retrieve hotel ID from the request (adjust this based on your application's logic)
#     id = request.GET.get('id')

#     # Fetch the hotel object based on the provided hotel ID
#     hotel = get_object_or_404(Hotel, id=id)

#     if request.method == 'POST':
#         form = PaymentForm(request.POST)
#         if form.is_valid():
#             # Save the payment with the associated hotel
#             payment = form.save(commit=False)
#             payment.hotel = hotel
#             payment.save()
#             return redirect('payment_success', name=payment.name, num_rooms=payment.num_rooms, room_type=payment.room_type, payment_option=payment.payment_option, amount=payment.amount)
#     else:
#         form = PaymentForm()

#     context = {
#         'form': form,
#         'hotel': hotel
#     }
#     return render(request, 'payment_form.html', context)
def payment_form_view(request):
    id = request.GET.get('id')
    hotel_name = request.GET.get('hotel_name')
    # Add other necessary context data
    context = {
        'id': id,
        'hotel_name': hotel_name,
        # Add other necessary context data
    }
    return render(request, 'payment_form.html', context)
def hotel_detail(request, id):
    # Get hotel details by ID
    hotel = get_object_or_404(Hotel, id=id)
    # Pass hotel ID to payment form view
    return redirect('process_payment', hotel_id=id)

def get_hotel_name(request):
    hotel_id = request.GET.get('id')
    if hotel_id:
        try:
            hotel = Hotel.objects.get(id=hotel_id)
            return JsonResponse({'name': hotel.name})
        except Hotel.DoesNotExist:
            return JsonResponse({'error': 'Hotel not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid hotel ID'}, status=400)
    
def process_payment(request):
    
    if request.method == 'POST':
        payment_option = request.POST.get('payment_option')
        amount = request.POST.get('amount')
        promo_code = request.POST.get('promo_code') 
        name = request.POST.get('name')
        num_rooms=request.POST.get('num_rooms')
        room_type=request.POST.get('room_type')
        check_in=request.POST.get('check_in')
        check_out=request.POST.get('check_out')
        
     
       
      

        
        if payment_option in ['bkash', 'rocket','cash']:
            phone_number = request.POST.get('phone_number')
            payment = Payment(name=name,payment_option=payment_option, amount=amount, phone_number=phone_number, promo_code=promo_code,num_rooms=num_rooms,room_type=room_type,check_in=check_in,check_out=check_out)
        elif payment_option == 'mastercard':
            card_number = request.POST.get('card_number')
            expiry_date = request.POST.get('expiry_date')
            cvv = request.POST.get('cvv')
            payment = Payment(name=name,payment_option=payment_option, amount=amount, card_number=card_number, expiry_date=expiry_date, cvv=cvv, promo_code=promo_code,num_rooms=num_rooms,room_type=room_type,check_in=check_in,check_out=check_out)
        
        
        
        payment.save()
        

        
        return redirect('payment_success', 
                        name=name, 
                        num_rooms=num_rooms, 
                        room_type=room_type, 
                        payment_option=payment_option, 
                        amount=amount) 
       
    else:
        hotel_id = request.GET.get('id')  # Retrieve hotel_id from URL parameters
        hotel = get_object_or_404(Hotel, id=hotel_id)
        hotel_name = hotel.name

        return render(request, 'payment_form.html',  {'hotel_name': hotel_name})

def payment_success(request, name, num_rooms, room_type, payment_option, amount,hotel_name=None):
    
    # Parse amount as float
    amount = float(amount)
    payment_option_images = {
        'cash': '/static/payment/360_F_449229860_uczw7ZS0sw6Ou31yhifld9s0KHkdULcR.jpg',
        'bkash': '/static/payment/1656235199bkash-logo-transparent.jpg',
        'rocket': '/static/payment/dutch-bangla-rocket-logo-B4D1CC458D-seeklogo.com.png',
        'mastercard': '/static/payment/Mastercard_logo.0.jpg',
    }

    # Get the image URL based on the selected payment option
    payment_option_image = payment_option_images.get(payment_option,'')

    if request.method == 'POST':
        # Retrieve payment information from the form
        context = {
            'name': name,
            'num_rooms': num_rooms,
            'room_type': room_type,
            'payment_option': payment_option,
            'amount': amount,
            'payment_option_image': payment_option_image,
            'hotel_name':hotel_name,
            
        }

        # Redirect to the payment success page with parameters in the URL
        return render(request, 'payment_success.html', context)

    else:
        # Handle GET request (display payment success page)
        context = {
            'name': name,
            'num_rooms': num_rooms,
            'room_type': room_type,
            'payment_option': payment_option,
            'amount': amount,
            'payment_option_image': payment_option_image,
            'hotel_name':hotel_name,
            
        }
        return render(request, 'payment_success.html', context)


def generate_pdf(request, name, num_rooms, room_type, payment_option, amount):
    payment_option_images = {
        'bkash': '/static/payment/1656235199bkash-logo-transparent.jpg',
        'rocket': '/static/payment/dutch-bangla-rocket-logo-B4D1CC458D-seeklogo.com.png',
        'mastercard': '/static/payment/Mastercard_logo.0.jpg',
    }

    # Get the image URL based on the selected payment option
    payment_option_image = payment_option_images.get(payment_option, None)

    if not payment_option_image:
        return HttpResponse('Payment option image not found')

    # Render the PDF template with the provided data
    pdf_html = render_to_string('payment_receipt_pdf.html', {
        'name': name,
        'num_rooms': num_rooms,
        'room_type': room_type,
        'payment_option': payment_option,
        'amount': amount,
        'payment_option_image': payment_option_image,
    })

    # Create PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="payment_receipt_{name}_pdf.pdf"'

    # Generate PDF using xhtml2pdf
    pisa_status = pisa.CreatePDF(pdf_html, dest=response)

    if pisa_status.err:
        return HttpResponse('Error generating PDF')

    return response  # Add this return statement to return the PDF response


def send_invoice_email(payment, user_email):
    # Render the invoice HTML template with the payment data
    invoice_html = render_to_string('payment_success.html', {
        'name': payment.name,
        'num_rooms': payment.num_rooms,
        'room_type': payment.room_type,
        'payment_option': payment.payment_option,
        'amount': payment.amount,
        'payment_option_image': payment.payment_option_image
    })

    # Convert HTML to PDF
    pdf_content = pisa.CreatePDF(invoice_html)

    # Send email with PDF attachment
    subject = 'Payment Invoice'
    message = 'Please find attached your payment invoice.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]

    email = EmailMessage(subject, message, email_from, recipient_list)
    email.attach('invoice.pdf', pdf_content, 'application/pdf')

    try:
        email.send()
        print("Invoice email sent successfully.")
    except Exception as e:
        print(f"Failed to send invoice email: {str(e)}")
