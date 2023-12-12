from django.urls import path
from . import views
from .views import contact, thank_you_page


urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('thank-you/', thank_you_page, name='thank_you_page'),

]