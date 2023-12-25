from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def base(request):
    return render(request, 'base.html')

def tailwind(request):
    return render(request, 'pages/tailwind.html')

def about(request):
    return render(request,'pages/about.html', {'fname': 'Nilo', 'lname': 'Cara', 'pname':'JNB, ZA'})

def home(request, id=None):
    # If id is provided, you can use it in your view logic
    if id == 'my_projects':
        return render(request, 'pages/home.html', {'id': id })
        
def home(request):
    return render(request,'pages/home.html',
                  {'home_hero_h1': 'Technology Simplified', 
                   'home_hero_p':'An Innovative IT Solutions Agency',
                   'home_hero_p2': '#Cloud Migratation, #Data Management, Networking, #Hardware',
                   'logo':'Frontend',
                   'logo_favicon':'Fe.',
                   'logo_sub_title':'Software Engineering',
                   'Section2_P1': "Throughout my diverse journey, I've consistently sought meaningful opportunities and embraced challenges. From owning a small business to being recognized as Employee of the Year at Gijima, earning a Service Excellence merit at SouthernSun, and achieving top rank at Stellenbosch University's Software Engineering Bootcamp, my dedication to problem-solving and helping others has remained unwavering. With over 15 years in the tech industry, I transitioned from a junior support analyst to a Group Operations Manager at Standard Bank Group before taking a hiatus in 2017 for a personal project. Returning in 2019 as a freelance software developer, I've honed expertise in Python, JavaScript, HTML, CSS, MySQL, AWS, and continue to explore new frameworks and languages. I excel as a well-rounded front-end developer using JavaScript and web development tools, occasionally delving into backend solutions with Node or Python, and have recently joined Hyperion Dev with Stellenbosch University and Harvard University's CS50 to further advance my career as a software engineer."
                   })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            user_email = form.cleaned_data["email"]
            
            subject = 'New Contact Form Submission'
            message = f'Name: {form.cleaned_data["name"]}\nEmail: {user_email}\nPhone Number: +27 82 8888 2222 {form.cleaned_data["phone_number"]}\nMessage: {form.cleaned_data["message"]}\n\nCompany: {settings.COMPANY_CONTACT_NAME}\nContact Person: {settings.PERSONAL_CONTACT_NAME}'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [user_email, settings.EMAIL_HOST_USER]

            send_mail(subject, message, from_email, recipient_list)
            # You can add a success message or redirect to a thank-you page
            return redirect('thank_you_page')
    else:
        form = ContactForm()

    return render(request, 'pages/contact.html', {'form': form})

def thank_you_page(request):
    return render(request, 'pages/thanku.html')