import datetime
from django.http import HttpResponse
from .forms import CarForm, DriverForm, ClientForm
from .models import Car, Client, Driver
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
# Create your views here.
from django.views.generic import ListView, CreateView, DetailView

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Машины парка", 'url_name': 'cars'},
        {'title': "Водители парка", 'url_name': 'drivers'},
        {'title': "Клиенты", 'url_name': 'clients'}
]

def index(request):
    title = 'Главная страница'
    context = {'title': title, 'menu': menu}
    return render(request, 'main/index.html', context=context)

def about(request):
    title = 'О сайте'
    context = {'title': title, 'menu': menu}
    return render(request, 'main/about.html', context=context)

@csrf_protect
def login(request):
    title = 'Войти'
    context = {'title': title, 'menu': menu}
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        return HttpResponse(f'Login - {username}, Password - {password}')
        
    
    if request.method == 'GET':
        return render(request, 'main/login.html', context=context)
    
    
def contacts(request, id):
    url_id = id
    name = request.GET.get('name')
    age = request.GET.get('age')
    get_params = {'name': name, 'age': age}
    return HttpResponse(f'Page contacts, url_parametr_id = {url_id}, get_params - {get_params}')

def cars(request):
    title = 'Машины'
    car = Car.objects.all()

    context = {'title': title, 'menu': menu, 'cars': car}
    return render(request, 'main/cars.html', context=context)

def drivers(request):
    title = 'Водители'
    context = {'title': title, 'menu': menu}
    return render(request, 'main/drivers.html', context=context)

def clients(request):
    title = 'Клиенты'
    clients = Client.objects.all()
    context = {'title': title, 'menu': menu, 'clients': clients}
    return render(request, 'main/clients.html', context=context)

def add_car(request):
    if request.method =='GET':
        title = 'Добавить машину'
        form = CarForm()
        context = {'title': title, 'menu': menu, 'form': form}
        return render(request, 'main/car_add.html', context=context)
    
    if request.method == 'POST':
        carform = CarForm(request.POST)
        if carform.is_valid():
            car = Car()
            car.brand = carform.cleaned_data['brand']
            car.model = carform.cleaned_data['model']
            car.color = carform.cleaned_data['color']
            car.power = carform.cleaned_data['power']
            car.year = carform.cleaned_data['year']
            car.save()
        return cars(request)

def add_driver(request):
    title='Добавить водителя'
    form = DriverForm()
    context = {'title': title, 'menu': menu, 'form': form}
    return render(request, 'main/driver_add.html', context=context)

def add_client(request):
    title = 'Добавить клиента'
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            age = datetime.date.today().year - form.cleaned_data['birthday'].year
            instance.age = age
            instance.save()
            
            return clients(request)
    else:
        form = ClientForm()
    context = {'title': title, 'menu': menu, 'form': form}
    
    return render(request, 'main/client_add.html', context=context)
    

def car_detail(request, pk):
    car = Car.objects.get(pk=pk)
    title = 'Car detail'
    context = {'object': car, 'title': title}
    
    return render(request, 'main/car_detail.html', context=context)




class CarList(ListView):
    model = Car



        