import datetime
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.http import HttpResponse
from .forms import CarForm, DriverForm, ClientForm
from .models import *
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required


menu = [{'title': "О сайте", 'url_name': 'main:about'},
        {'title': "Машины парка", 'url_name': 'main:cars'},
        {'title': "Водители парка", 'url_name': 'main:drivers'},
        {'title': "Клиенты", 'url_name': 'main:clients'},
        {'title': "Сотрудники", 'url_name': 'main:employee_list'},

]

def index(request):
    title = 'Главная страница'
    context = {'title': title, 'menu': menu}
    return render(request, 'main/index.html', context=context)

def about(request):
    title = 'О сайте'
    context = {'title': title, 'menu': menu}
    return render(request, 'main/about.html', context=context)
  
    
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

@login_required
def drivers(request):
    title = 'Водители'
    context = {'title': title, 'menu': menu}
    return render(request, 'main/drivers.html', context=context)

@login_required
def clients(request):
    title = 'Клиенты'
    clients = Client.objects.all()
    paginator = Paginator(clients, 2)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'title': title, 'menu': menu, 'clients': clients, 'page_obj': page_obj}

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



class EmployeeList(ListView):
    model = Employee
    template_name = 'main/employee_list.html'
    context_object_name = 'employees'
    paginate_by = 4
    
    def get_context_data(self, **kwargs):
        # получение общего контекста из родительского класса
        context = super().get_context_data(**kwargs)
        # изменение родительского контекста (добавление ключей словаря)
        
        context['title'] = 'Сотрудники'
        context["count"] = Employee.objects.count()
        context['menu'] = menu
        return context


class EmployeeDetail(DetailView):
    model = Employee
    template_name = 'main/employee_detail.html'
    context_object_name = 'employee' 

    def get_context_data(self, **kwargs):
        # получение общего контекста из родительского класса
        context = super().get_context_data(**kwargs)
        context['title'] = 'Информация о сотруднике'
        context['menu'] = menu

        return context


class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'main/employee_form.html'
    

class EmployeeUpdate(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'main/employee_update.html'
    

class EmployeeDelete(DeleteView):
    model = Employee
    template_name = 'main/delete.html'
    success_url = reverse_lazy('main:employee_list')
    

    
    


        