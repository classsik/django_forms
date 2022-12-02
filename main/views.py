from django.shortcuts import render
from django.http import HttpResponse
from .forms import OrderForm


def home(request):
    return render(request, 'main/index.html', {})


def appointment(request):
    name = request.GET.get('name', None)
    email = request.GET.get('email', None)
    phone = request.GET.get('phone', None)
    service = request.GET.get('service', None)
    text = request.GET.get('text', None)

    return HttpResponse(f"""
<p>Имя: {name}</p>    
<p>Email: {email}</p>    
<p>Телефон: {phone}</p>    
<p>Сервис: {service}</p>    
<p>Текст: {text}</p>    
""")


def order(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        email = request.POST.get('email', None)
        adress = request.POST.get('adress', None)

        result = f"""{first_name} {last_name}, проверьте адрес доставки: {adress}"""

        return HttpResponse(result)
    else:
        form = OrderForm()
        return render(request, 'main/form.html', {'form': form})
