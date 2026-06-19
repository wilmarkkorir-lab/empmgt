from django.http import HttpResponse
from rest_framework.decorators import api_view

# Create your views here.


def home(request):
    return HttpResponse("welcome to Django")
def introduction(request):
    return HttpResponse("New url for views")

@api_view([ 'POST'])
def add(request):
    try:
        num1 = float(request.data.get('num1', 0))
        num2 = float(request.data.get('num2', 0))
        total = num1 + num2
        return HttpResponse(f"The sum of {num1} and {num2} is {total}")
    except (ValueError, TypeError):
        return HttpResponse("Invalid input. Please provide numeric values for 'num1' and 'num2'.", status=400)


    