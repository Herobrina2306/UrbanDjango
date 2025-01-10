from django.shortcuts import render


# Create your views here.

def main_page(request):
    title = 'Главная страница'
    text = 'Рада приветствовать вас на моём маленьком сайте посвящённом книге "Сказка, да на современный лад"'
    context = {
        'title': title,
        'text': text
    }

    return render(request, "fourth_task/main_p.html", context)


def table_of_contents(request):
    title = 'Оглавление'
    button = 'Читать'
    chapter = ['Присказка. Владислав Иванович, сын Ивана Быковича ',
               'Глава 1. На работе лучше вдвоём ',
               'Глава 2. Новые знакомства из старых времён ',
               'Глава 3. И в метро нечисть водится ',
               'Глава ожидается ']
    context = {
        'title': title,
        'button': button,
        'chapter': chapter
    }
    return render(request, 'fourth_task/table_of_contens.html', context)


def donat(request):
    title = 'Донат'
    text = 'P.S. Денюжка пойдёт на плату художнику и редактору.'
    button = 'Донат'
    context = {
        'title': title,
        'text': text,
        'button': button
    }
    return render(request, 'fourth_task/donat.html', context)
