from django.shortcuts import render, redirect
from .models import Nut, Oil, PastaNoodle, Offer, ContactUs

# Create your views here.


def home(request):

    nutget   = Nut.objects.all()
    oilget   = Oil.objects.all()
    pastaget = PastaNoodle.objects.all()
    offerget = Offer.objects.all()

    context = {
        'title':'Grocery Shop create in Django Python Technolgies',
        'nutget':nutget,
        'oilget':oilget,
        'pastaget':pastaget,
        'offerget':offerget,
    }
    
    return render(request, 'src/index.html', context)







def about(request):

    return render(request, 'src/about.html')



def checkout(request):

    return render(request, 'src/checkout.html')


def contact(request):

    return render(request, 'src/contact.html') 
    

def faqs(request):

    return render(request, 'src/faqs.html')
def help(request):

    return render(request, 'src/help.html') 
    

def payment(request):

    return render(request, 'src/payment.html')

def privacy(request):

    return render(request, 'src/privacy.html') 


def product(request):

    return render(request, 'src/product.html')


def product2(request):

    return render(request, 'src/product2.html')

def single(request):

    return render(request, 'src/single.html')

def terms(request):

    return render(request, 'src/terms.html')


def single2(request):

    return render(request, 'src/single2.html')


def message(request):

        name    = request.POST['name']
        subject = request.POST['subject']
        email   = request.POST['email']
        message = request.POST['message']

        recive = ContactUs(name=name, subject=subject, email=email, massege=message)

        recive.save()

        return redirect('/')

    



