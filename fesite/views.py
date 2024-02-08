from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def common_context():
    return {
        'home_hero_h1': 'An innovative IT solutions practice', 
        'home_hero_p': 'Assisting businesses to invest in their digital future on their own terms.',
        'home_hero_p2': '#Cloud Migration, #Data Management, #Networking, #Hardware',
        'logo': 'Frontend',
        'logo_favicon': 'Fe.',
        'logo_sub_title': 'Software Engineering',
        'Section2_P1': "Throughout my diverse journey, I've consistently sought meaningful opportunities and embraced challenges. From owning a small business to being recognized as Employee of the Year at Gijima, earning a Service Excellence merit at SouthernSun, and achieving top rank at Stellenbosch University's Software Engineering Bootcamp, my dedication to problem-solving and helping others has remained unwavering. With over 15 years in the tech industry, I transitioned from a junior support analyst to a Group Operations Manager at Standard Bank Group before taking a hiatus in 2017 for a personal project. Returning in 2019 as a freelance software developer, I've honed expertise in Python, JavaScript, HTML, CSS, MySQL, AWS, and continue to explore new frameworks and languages. I excel as a well-rounded front-end developer using JavaScript and web development tools, occasionally delving into backend solutions with Node or Python, and have recently joined Hyperion Dev with Stellenbosch University and Harvard University's CS50 to further advance my career as a software engineer.",
        'webdev_banner_headline': 'Whether you\'re in the process of migrating your website or seeking ongoing optimization, we\'re here with you every step of the way.',
        'webdev_banner_tags': '#WordPress, #React, #Django, #_Next',
    }

def base(request):
    return render(request, 'base.html')

def home(request, id=None):
    context = common_context()
    form = ContactForm()  # Instantiate the contact form
    
    if id == 'my_projects':
        context['id'] = id
    
    # If the request method is POST, process the form data
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            user_email = form.cleaned_data["email"]
            
            subject = 'Website contact submission'
            message = f'Name: {form.cleaned_data["name"]}\nEmail: {user_email}\nPhone Number: {form.cleaned_data["phone_number"]}\nMessage: {form.cleaned_data["message"]}\nCompany: {settings.COMPANY_CONTACT_NAME}\nContact Person: {settings.PERSONAL_CONTACT_NAME}'
            from_email = settings.FROM_NAME
            recipient_list = [user_email, settings.EMAIL_HOST_USER]

            send_mail(subject, message, from_email, recipient_list)
            # Additional processing like sending emails can be done here
            return redirect('thank_you_page')  # Redirect to thank you page after form submission

    # Add the form to the context
    context['form'] = form
    
    return render(request, 'pages/home.html', context)

def tailwind(request):
    return render(request, 'pages/tailwind.html')

def about(request):
    return render(request,'pages/about.html', {'fname': 'Nilo', 'lname': 'Cara', 'pname':'JNB, ZA'})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            user_email = form.cleaned_data["email"]
            
            subject = 'Website contact submission'
            message = f'Name: {form.cleaned_data["name"]}\nEmail: {user_email}\nPhone Number: {form.cleaned_data["phone_number"]}\nMessage: {form.cleaned_data["message"]}\nCompany: {settings.COMPANY_CONTACT_NAME}\nContact Person: {settings.PERSONAL_CONTACT_NAME}'
            from_email = settings.FROM_NAME
            recipient_list = [user_email, settings.EMAIL_HOST_USER]

            send_mail(subject, message, from_email, recipient_list)
            # You can add a success message or redirect to a thank-you page
            return redirect('thank_you_page')
    else:
        form = ContactForm()

    context = {
        'form': form,
        **common_context(),  # Merge common context
    }

    return render(request, 'pages/contact.html', context)

def thank_you_page(request):
    return render(request, 'pages/thanku.html')