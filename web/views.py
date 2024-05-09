from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from web.models import Flan
from web.forms import ContactForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


# Create your views here.

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes_publicos})


def about(request):
    return render(request, 'about.html', {})


@login_required
def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes_privados})


def contacto(request):
    return render(request, 'contacto.html', {})


def contact_view(request):
    if request.method == 'POST':  # Si el usuario ha enviado el formulario(self, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacto_exitoso')
    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})


def contact_view_exito(request):
    return render(request, 'contacto_exitoso.html', {})


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


def CustomRegisterView(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        username = request.POST.get('uname')
        if  password != password2:
            messages.warning(request,'Las contraseñas no coinciden!')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.warning(request,'El Email ya existe!')
            return redirect('register')
        else:
            user = User(email=email,password=password,first_name=firstname,
            last_name=lastname,username=username)
            user.set_password(password)
            user.save()
            new_user = authenticate(username=username,
                                    password=password,
                                    )
            login(request, new_user)

            return redirect('index')
    return render(request, 'registration/register.html')


class CustomLogoutView(LogoutView):
    next_page = '/'


def flan_details(request, flan_id):
    flan = get_object_or_404(Flan, pk=flan_id)
    return render(request, 'flan_details.html', {'flan': flan})
