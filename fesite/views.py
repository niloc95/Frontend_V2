from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from .mailchimp_utils import subscribe_user
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.generic import View
import os
#from .utils import common_context

# Create your views here.

def common_context():
    return {
        'home_hero_h1': 'Pushing the boundaries on innovation', 
        'home_hero_p': 'Assisting businesses to invest in their digital future on their own terms.',
        'home_hero_p2': 'Your technology partner',
        'post_h1': 'How we can help you',
        'post_h2': 'We transform ideas into impact.',
        'logo': 'Frontend',
        'logo_favicon': 'Fe.',
        'logo_sub_title': 'Software Engineering',
        'Section2_P1': "Throughout my diverse journey, I've consistently sought meaningful opportunities and embraced challenges. From owning a small business to being recognized as Employee of the Year at Gijima, earning a Service Excellence merit at SouthernSun, and achieving top rank at Stellenbosch University's Software Engineering Bootcamp, my dedication to problem-solving and helping others has remained unwavering. With over 15 years in the tech industry, I transitioned from a junior support analyst to a Group Operations Manager at Standard Bank Group before taking a hiatus in 2017 for a personal project. Returning in 2019 as a freelance software developer, I've honed expertise in Python, JavaScript, HTML, CSS, MySQL, AWS, and continue to explore new frameworks and languages. I excel as a well-rounded front-end developer using JavaScript and web development tools, occasionally delving into backend solutions with Node or Python, and have recently joined Hyperion Dev with Stellenbosch University and Harvard University's CS50 to further advance my career as a software engineer.",
        'webdev_banner_headline': 'Whether you\'re in the process of migrating your website or seeking ongoing optimization, we\'re here with you every step of the way.',
        'webdev_banner_tags': '#WordPress, #React, #Django, #_Next',
        'terms_page_heading':'Terms of Use',
        'terms_general':'These Terms of Use ("Terms") govern your use of Frontend Software Engineering\'s website (the "Website"), accessible at [https://frontend.co.za]. By accessing or using the Website, you agree to be bound by these Terms. If you do not agree to these Terms, please refrain from using the Website.',
        'P1':'1. Use of the Website',
        '1_1_Use_of_the_Website':'1.1. You must be at least 18 years old to use this Website. By using the Website, you represent and warrant that you are at least 18 years old.',
        '1_2_Use_of_the_Website':'1.2. You agree to use the Website only for lawful purposes and in accordance with these Terms. You shall not use the Website in any way that violates any applicable laws or regulations.',
        '1_3_Use_of_the_Website':'You agree not to reproduce, duplicate, copy, sell, resell, or exploit any portion of the Website without our express written permission.',
        'P2':'2. User Accounts',
        '2_User_Accounts':'2.1. In order to access certain features of the Website, you may be required to create an account. You agree to provide accurate, current, and complete information during the registration process and to update such information to keep it accurate, current, and complete.',
        '2_1_User_Accounts':'2.2. You are responsible for maintaining the confidentiality of your account and password and for restricting access to your computer or device. You agree to accept responsibility for all activities that occur under your account or password.',
        'P3':'3. Intellectual Property',
        '3_Intellectual_Property':'3.1. The Website and its original content, features, and functionality are owned by Frontend Dev (Pty)Ltd and are protected by international copyright, trademark, patent, trade secret, and other intellectual property or proprietary rights laws.',
        '3_2_Intellectual_Property':'3.2. You may not modify, publish, transmit, participate in the transfer or sale of, create derivative works from, distribute, display, reproduce, or perform, or in any way exploit in any format whatsoever any of the Website\'s content, in whole or in part, without our prior written consent.',
        'P4':'4. Limitation of Liability',
        'Limitation_of_Liability':'4.1. To the fullest extent permitted by applicable law, in no event shall Frontend Dev (Pty)Ltd, its affiliates, officers, directors, employees, agents, suppliers, or licensors be liable for any indirect, incidental, special, consequential, or punitive damages, including without limitation, loss of profits, data, use, goodwill, or other intangible losses, resulting from (i) your access to or use of or inability to access or use the Website; (ii) any conduct or content of any third party on the Website; (iii) any content obtained from the Website; and (iv) unauthorized access, use, or alteration of your transmissions or content, whether based on warranty, contract, tort (including negligence), or any other legal theory, whether or not we have been informed of the possibility of such damage, and even if a remedy set forth herein is found to have failed of its essential purpose.',
        'P5':'5. Governing Law',
        '5_Governing_Law':'5.1. These Terms shall be governed by and construed in accordance with the laws of the Republic of South Africa, without regard to its conflict of law provisions.',
        'P6':'6. Changes to Terms',
        '6_Changes_to_Terms':'6.1. We reserve the right, at our sole discretion, to modify or replace these Terms at any time. If a revision is material, we will provide at least 30 days\' notice prior to any new terms taking effect. What constitutes a material change will be determined at our sole discretion.',
        'P7':'7. Contact Us',
        '7_Contact_Us':'7.1. If you have any questions about these Terms, please contact us at help@frontend.co.za.',
        'Closing':'By accessing or using the Website, you agree to be bound by these Terms of Use.',
        'P8':'8 .Email Disclamer',
        '8_Email_disclamer':'8.1. This email and any attachments are confidential and may be privileged. If you are not the intended recipient, please notify the sender immediately and delete the email from your system. Any unauthorized use, dissemination, or copying of this email is prohibited. The views, opinions, and information expressed in this email are solely those of the sender and do not necessarily represent those of Frontend Dev (Pty)Ltd. While we take precautions to ensure that our emails are free from viruses, we accept no liability for any damage caused by any virus transmitted by this email. Recipients should perform their own virus checks. Email communication is not secure and may be intercepted or altered. Frontend Dev (Pty)Ltd cannot guarantee the confidentiality or integrity of this email transmission.',
        '':'',
        '':'',
        '':'',

    }

class RobotsTxtView(View):
    def get(self, request, *args, **kwargs):
        # Path to your robots.txt file
        robots_file_path = os.path.join(settings.BASE_DIR, 'robots.txt')

        # Read the contents of the robots.txt file
        try:
            with open(robots_file_path, 'r') as f:
                robots_txt = f.read()
        except FileNotFoundError:
            robots_txt = "User-agent: *\nAllow: /"

        # Return the contents of robots.txt
        return HttpResponse(robots_txt, content_type='text/plain')

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

            subject = 'Inquiry Regarding Our Services'
            from_email = settings.CONTACT_EMAIL
            to_email = [user_email]

            # Render HTML template
            html_message = render_to_string('pages/email_template.html', {
                'name': form.cleaned_data["name"],
                'email': user_email,
                'phone_number': form.cleaned_data["phone_number"],
                'message': form.cleaned_data["message"],
                'company': settings.COMPANY_CONTACT_NAME,
                'contact_person': settings.PERSONAL_CONTACT_NAME,
            })

            # Create and send email
            email = EmailMultiAlternatives(subject, subject, from_email, to_email, bcc=[settings.CONTACT_EMAIL])
            email.attach_alternative(html_message, "text/html")

            attachment = request.FILES.get('attachment')
            if attachment:
                email.attach(attachment.name, attachment.read(), attachment.content_type)

            email.send()

            # Redirect to thank-you page
            return redirect('thank_you_page')
    else:
        form = ContactForm()

    context = {
        'form': form,
        **common_context(),  # Merge common context
    }
    
    return render(request, 'pages/home.html', context)

def tailwind(request):
    context = common_context()
    return render(request, 'pages/tailwind.html', context)

def nof(request):
    context = common_context()
    return render(request, '404.html', context)

def not_found_404_view(request, exception):
    context = common_context()
    return render(request, '404.html', {}, status=404, context=context)

def terms(request):
    context = common_context()
    return render(request, 'pages/terms.html', context)

def about(request):
    return render(request,'pages/about.html', {'fname': 'Nilo', 'lname': 'Cara', 'pname':'JNB, ZA'})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            user_email = form.cleaned_data["email"]

            subject = 'Inquiry Regarding Our Services'
            from_email = settings.CONTACT_EMAIL
            to_email = [user_email]

            # Render HTML template
            html_message = render_to_string('pages/email_template.html', {
                'name': form.cleaned_data["name"],
                'email': user_email,
                'phone_number': form.cleaned_data["phone_number"],
                'message': form.cleaned_data["message"],
                'company': settings.COMPANY_CONTACT_NAME,
                'contact_person': settings.PERSONAL_CONTACT_NAME,
            })

            # Create and send email
            email = EmailMultiAlternatives(subject, subject, from_email, to_email, bcc=[settings.CONTACT_EMAIL])
            email.attach_alternative(html_message, "text/html")

            attachment = request.FILES.get('attachment')
            if attachment:
                email.attach(attachment.name, attachment.read(), attachment.content_type)
            
            email.send()

            # Redirect to thank-you page
            return redirect('thank_you_page')
    else:
        form = ContactForm()

    context = {
        'form': form,
        **common_context(),  # Merge common context
    }

    return render(request, 'pages/contact.html', context)

def thank_you_page(request):
    context = common_context()
    return render(request, 'pages/thanku.html', context)

from .mailchimp_utils import subscribe_user

def subscribe(request):
    context = common_context()
    if request.method == 'POST':
        email = request.POST.get('email')
        subscribe_user(email)
        # Optionally, you can handle success or error messages here
    return render(request, 'pages/subs.html', context)