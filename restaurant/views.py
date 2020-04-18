from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
from items.models import FoodProducts

# Create your views here.

def index(request):
    coffeeproduct = FoodProducts.objects.all().filter(section=4)

    mainproduct = FoodProducts.objects.all().filter(section=1)

    beverages = FoodProducts.objects.all().filter(section=3)

    deserts = FoodProducts.objects.all().filter(section=2)
    context = {
        'coffeeproduct': coffeeproduct,
        'mainproduct' : mainproduct,
        'beverages' : beverages,
        'deserts' : deserts
    }
    return render(request, 'pages/index.html', context)



def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id= request.user.id
            has_contacted = Contact.objects.all().filter(name=name,email=email,subject=subject,message=message)
            if has_contacted:
                messages.error(request,"You have already made an enquiry")
                return redirect('contact')
        contact = Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
        messages.success(request, "Your request has been submitted")
        return redirect('contact')        
    return render(request, 'pages/contact.html')    



 