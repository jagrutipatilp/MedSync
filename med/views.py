from audioop import reverse
import re

from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import requires_csrf_token
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django import forms
import requests
from django.http import JsonResponse

from django.shortcuts import render
import requests




def home(request):
    tips = [
    {
        'heading': 'Stay Hydrated',
        'description': 'Drink plenty of water throughout the day to keep your body hydrated and maintain optimal health.',
        'image': 'https://img.freepik.com/free-photo/sportsman-drinking-water-training_342744-656.jpg?w=1060&t=st=1684573301~exp=1684573901~hmac=6fce23c360089d44c1b62dfe3bc306259e3464e2eb4cda126eec59e0388f0f79'
    },
    {
        'heading': 'Eat a Balanced Diet',
        'description': 'Include a variety of fruits, vegetables, whole grains, lean proteins, and healthy fats in your meals for a well-rounded diet.',
        'image': 'https://img.freepik.com/free-photo/medium-shot-woman-with-food-clock_23-2148996315.jpg?w=996&t=st=1684573412~exp=1684574012~hmac=c0e9c8359525763c3b9cacbaf5fc98bc4be9c6d5d594b14b71520eae73a1a8ed'
    },
    {
        'heading': 'Get Regular Exercise',
        'description': 'Engage in physical activities like walking, jogging, or cycling to improve cardiovascular health and maintain a healthy weight.',
        'image': 'https://img.freepik.com/free-photo/sports-girl-black-top-training-autumn-park_1157-28606.jpg?size=626&ext=jpg&ga=GA1.2.1598203751.1684572758&semt=ais'
    },
    {
        'heading': 'Practice Portion Control',
        'description': 'Be mindful of portion sizes to avoid overeating and maintain a healthy calorie intake.',
        'image': 'https://img.freepik.com/free-vector/information-analysis-monitoring-economy-manager-progress-productive-vector-illustration_1284-46953.jpg?size=626&ext=jpg&ga=GA1.1.1598203751.1684572758&semt=ais'
    },
    {
        'heading': 'Prioritize Sleep',
        'description': 'Aim for 7-8 hours of quality sleep each night to promote physical and mental well-being.',
        'image': 'https://img.freepik.com/free-photo/woman-home_144627-26481.jpg?size=626&ext=jpg&ga=GA1.1.1598203751.1684572758&semt=ais'
    },
    {
        'heading': 'Manage Stress',
        'description': 'Find healthy ways to manage stress, such as practicing relaxation techniques, exercise, or engaging in hobbies.',
        'image': 'https://img.freepik.com/free-photo/brunet-man-sitting-desk-surrounded-with-gadgets-papers_273609-41515.jpg?size=626&ext=jpg&ga=GA1.2.1598203751.1684572758&semt=ais'
    },
    {
        'heading': 'Limit Processed Foods',
        'description': 'Reduce your intake of processed and packaged foods high in added sugars, sodium, and unhealthy fats.',
        'image': 'https://img.freepik.com/free-photo/top-view-unhealthy-food-snacks_23-2148541053.jpg?size=626&ext=jpg&ga=GA1.1.1598203751.1684572758&semt=ais'
    },
    {
        'heading': 'Practice Good Hygiene',
        'description': 'Wash your hands frequently, maintain oral hygiene, and keep your surroundings clean to prevent the spread of germs.',
        'image': 'https://img.freepik.com/free-photo/boy-wearing-medical-mask-washing-his-hands-side-view_23-2148511130.jpg?size=626&ext=jpg&ga=GA1.1.1598203751.1684572758&semt=ais'
    },
    {
        'heading': 'Practice Mindfulness',
        'description': 'Take time for self-care, practice meditation, or engage in activities that bring you joy and peace of mind.',
        'image': 'https://img.freepik.com/free-photo/full-shot-woman-meditating-with-candles_23-2148897863.jpg?size=626&ext=jpg&ga=GA1.2.1598203751.1684572758&semt=ais'
    },
    {
        'heading': 'Limit Sugary Beverages',
        'description': 'Reduce your consumption of sugary drinks like soda, energy drinks, and fruit juices, and opt for water or healthier alternatives.',
        'image': 'https://img.freepik.com/free-photo/front-view-hamburger-with-sweets_23-2148262949.jpg?size=626&ext=jpg&ga=GA1.2.1598203751.1684572758&semt=ais'
    },
    {
        'heading': 'Practice Safe Sex',
        'description': 'Use protection and get regular check-ups to prevent sexually transmitted infections and maintain sexual health.',
        'image': 'https://img.freepik.com/free-photo/couple-with-sexual-toy-bed_23-2149352531.jpg?size=626&ext=jpg&ga=GA1.2.1598203751.1684572758&semt=ais'
    },
    ]
   

    # Set the interval (in seconds) between displaying each health tip
    interval = 5

    context = {
        'tips': tips,
        'interval': interval,
        }
    return render(request, "index.html",context)


def about_view(request):
    return render(request, 'about_page.html')

def success_view(request):
    return render(request,  'success.html')

def login_view(request):
    return render(request, 'login.html')

def newsevents_view(request):
    return render(request, 'newsevents.html')

def remedies_view(request):
    return render(request, 'remedies.html')

def signin_view(request):
    return render(request, 'signin.html')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

def fillhistory_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # process form data...
            return redirect('signin.html')
        else:
            pass
            # handle form errors...
    else:
        form = LoginForm()
    
    context = {'form': form}
    return render(request, 'fillhistory.html', context)

def contactus_view(request):
    return render(request, 'contactus.html')

def terms_view(request):
    return render(request, 'termsofuse.html')

def privacy_view(request):
    return render(request, 'privacy_policy.html')


