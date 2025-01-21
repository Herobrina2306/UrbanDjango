from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegistr

# Create your views here.

users = ['Eva', 'Sasha', 'Misha', 'Adam']
info = {"error": ''}


def sign_up_by_django(request):
    if request.method == 'POST':
        form = UserRegistr(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password1 = form.cleaned_data['password']
            password2 = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password1 == password2:
                if int(age) > 17:
                    if name not in users:
                        info[name] = [password1, age]
                        return HttpResponse(f'Приветствуем {name}', )
                    else:
                        info['error'] = 'Пользователь уже существует'
                        return render(request, "fifth_task/registration_page.html", {'error': info['error'], 'form': form})
                else:
                    info['error'] = 'Вы должны быть старше 18'
                    return render(request, "fifth_task/registration_page.html", {'error': info['error'], 'form': form})
            else:
                info['error'] = "Пароли не совпадают"
                return render(request, "fifth_task/registration_page.html", {'error': info['error'], 'form': form})
        context = {
            'form': form,
            'info': info
        }
        return render(request, "fifth_task/registration_page.html", context)
    else:
        form = UserRegistr()
        context = {
            'form': form,
            'info': info
        }
        return render(request, "fifth_task/registration_page.html", context)


def sign_up_by_html(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('repeat_password')
        age = request.POST.get('age')
        if password1 == password2:
            if int(age) > 17:
                if name not in users:
                    info[name] = [password1, age]
                    return HttpResponse(f'Приветствуем {name}', )
                else:
                    info['error'] = 'Пользователь уже существует'
                    return render(request, "fifth_task/registration_page.html", {'error': info['error']})
            else:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, "fifth_task/registration_page.html", {'error': info['error']})
        else:
            info['error'] = "Пароли не совпадают"
            return render(request, "fifth_task/registration_page.html", {'error': info['error']})
    context = {
        'info': info
        }

    return render(request, "fifth_task/registration_page.html", context)
