from django.shortcuts import render

# Create your views here.

def main_page(request):
    return render(request, "third_task/main_p.html")


def table_of_contents(request):
    return render(request, 'third_task/table_of_contens.html')

def donat(request):
    return render(request, 'third_task/donat.html')
