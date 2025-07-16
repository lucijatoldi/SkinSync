import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .ontologija import g, simptomi, dijelovi_tijela
from .utils import pronadji_dijagnoze, generiraj_pdf
from .models import Profile


def home_view(request):
    profile_url = None
    static_default_image_path = os.path.join(settings.STATIC_URL, 'images/default.png')

    if request.user.is_authenticated:
        if request.user.profile and request.user.profile.profile_image:
            profile_url = request.user.profile.profile_image.url
        else:
            profile_url = static_default_image_path
    else:
        profile_url = static_default_image_path

    context = {
        'simptomi': simptomi,
        'dijelovi_tijela': dijelovi_tijela,
        'profile_url': profile_url,
    }
    
    return render(request, 'index.html', context)

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.error(request, 'Lozinke se ne podudaraju!')
            return redirect('register') 

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Korisničko ime je već zauzeto!')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        login(request, user)
        messages.success(request, 'Uspješno ste se registrirali i prijavili!')
        return redirect('home') 
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request, user) 
            request.session['username'] = username 
            return redirect('profile') 
        else:
            return render(request, 'login.html', {'error': 'Neispravno korisničko ime ili lozinka'})
    return render(request, 'login.html')

def logout_view(request):
    request.session.flush()
    return redirect('home')

@login_required(login_url='login')
def profile_view(request):
    profile_url = None
    static_default_image_path = os.path.join(settings.STATIC_URL, 'images/default.png')

    if request.user.is_authenticated:
        if request.user.profile and request.user.profile.profile_image:
            profile_url = request.user.profile.profile_image.url
        else:
            profile_url = static_default_image_path
    else:
        profile_url = static_default_image_path

    username = request.user.username
    pdf_path_on_disk = os.path.join(settings.MEDIA_ROOT, 'uploads', username, 'dijagnoza.pdf')
    pdf_exists = os.path.exists(pdf_path_on_disk)
    
    pdf_url = None
    if pdf_exists:
        pdf_url = f"{settings.MEDIA_URL}uploads/{username}/dijagnoza.pdf"
    else:
        pass

    context = {
        'profile_url': profile_url,
        'pdf_exists': pdf_exists,
        'pdf_url': pdf_url,
    }

    return render(request, 'profile.html', context)


@login_required 
def update_profile_view(request):
    if request.method == 'POST':
        if 'profile-picture' in request.FILES:
            uploaded_image = request.FILES['profile-picture']
            
            request.user.profile.profile_image = uploaded_image
            request.user.profile.save()
            
            messages.success(request, 'Profilna slika je uspješno ažurirana!')
            return redirect('profile')

    return redirect('profile')


def dijagnoza_view(request):
    if request.method == 'POST':
        odabrani_simptomi = request.POST.getlist('simptomi')
        odabrani_dijelovi = request.POST.getlist('dio_tijela')

        dijagnoze_info = pronadji_dijagnoze(g, odabrani_simptomi, odabrani_dijelovi)

        profile_url = None
        static_default_image_path = os.path.join(settings.STATIC_URL, 'images/default.png')

        if request.user.is_authenticated:
            if request.user.profile and request.user.profile.profile_image:
                profile_url = request.user.profile.profile_image.url
            else:
                profile_url = static_default_image_path
        else:
            profile_url = static_default_image_path

        if request.user.is_authenticated:
            username = request.user.username
            generiraj_pdf(username, dijagnoze_info)

        context = {
            'dijagnoze_info': dijagnoze_info,
            'profile_url': profile_url,
        }

        return render(request, 'rezultat.html', context)
    
    return redirect('home')

