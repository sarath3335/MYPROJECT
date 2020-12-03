from django.shortcuts import render, redirect
from .models import Post
from .forms import UserRegistrationForm
from django.contrib import messages


def index(request):
    return render(request, 'app1/base.html')


# def optin(request):
#     return render(request, 'app1/optin.html')
def noti(request):
    return render(request, 'app1/noti.html')



# def tlogin(request):
#     return render(request, 'app1/tlogin.html')



# def slogin(request):
#     form = UserRegistrationForm(request.POST)
#     return render(request, 'app1/slogin.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created ! You are now able to log in ')
            print(username)
            return redirect('base')
        # return redirect('signup')

    else:
        form = UserRegistrationForm()
    return render(request, 'app1/signup.html' ,{'form':form})
    # context = {
    #     'form': form,
    # }
    # return render(request, 'app1/signup.html', context)

# def noti(request):
#     if request.methode == "POST":
#         name = request.POST.get('Fname')
#         country = request.POST.get('country')
#         email = request.POST.get('email')
#         print(name)
#         print(country)
#         print(email)
#         return render(request, 'app1/noti.html')
#
#     else:
#          return render(request, 'app1/noti.html')
