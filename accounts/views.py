from django.shortcuts import render,redirect
from .form import SignupForm,UserActivateForm
from .models import Profile, UserAdress,UserPhoneNumper
from django.core.mail import send_mail

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data('username')
            email = form.cleaned_data('email')
            myform = form.save()


            profile = Profile.objects.get(user__username=username)
            profile.active = False
            profile.save()

            # send email
            send_mail(
                supject = 'Activate Your Account',
                messagw = f'use this code {profile.code} to activate your account',
                recipient_list=[email],
                fail_silently=False,
            )
            return redirect(f'/account/{username}/activate')

    else:
        form = SignupForm()
    return render(request,'registration/signup.html',{'form':form})


def user_activate(request,username):
    profile = Profile.objects.get(user__username=username)
    if request.method == 'POST':
        form = UserActivateForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data('code')
            if profile.code == code:
                profile.activate = True
                profile.code = ''
                profile.code_user = True
                return redirect('/accounts/login')

    else:
        form = UserActivateForm()
    return render(request,'registration/activate.html',{'form':form})



def profile(request):
    profile = Profile.objects.get(user=request.user)
    user_adress = UserAdress.objects.filter(user=request.user)
    phone_numbers = UserPhoneNumper.objects.filter(user=request.user)

    return render(request, 'registration/profile.html',{'profile':profile,'user_adress':user_adress,'phone_numbers':phone_numbers})
