from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .models import Position, Employee
from django.contrib import messages
from .forms import PositionForm, EmployeeForm
from django.core.files.storage import FileSystemStorage


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        positions = Position.objects.all()
        employees = Employee.objects.all()
        employees_form = EmployeeForm

        if not positions:
            employees_form = None

        context = {
            'position_form': PositionForm,
            'employee_form': employees_form,
            'positions': positions,
            'employees': employees
        }
        return context


class EmployeesView(View):
    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'put':
            return self.put(*args, **kwargs)
        if method == 'delete':
            return self.delete(*args, **kwargs)
        return super(EmployeesView, self).dispatch(*args, **kwargs)

    def get(self, request, employee_id):
        employee = Employee.objects.filter(id=employee_id).first()
        employee_form = EmployeeForm(initial={
            'name': employee.full_name,
            'email': employee.email,
            'avatar': employee.avatar,
            'address': employee.address,
            'sex': employee.sex,
            'positions': employee.position_id,
        })
        return render(request, 'edit-employee.html',
                      {'employee_form': employee_form, 'avatar': employee.avatar, 'employee_id': employee_id})

    def post(self, request):
        form = EmployeeForm(request.POST, request.FILES)
        if not form.is_valid():
            form.validator(request)
            return HttpResponseRedirect('/')

        data = form.cleaned_data
        employee = Employee(
            full_name=data.get('name'),
            email=data.get('email'),
            avatar=request.FILES['avatar'],
            address=data.get('address'),
            position_id=data.get('positions').id,
        )

        employee.save()
        messages.success(request, 'Insert employee success')
        return HttpResponseRedirect('/')

    def delete(self, request):
        employee_id = request.POST['employee_id']
        model = Employee.objects.filter(id=employee_id)
        model.delete()
        messages.success(request, 'Delete employee success')
        return HttpResponseRedirect('/')

    def put(self, request, employee_id):
        form = EmployeeForm(request.POST, request.FILES)
        if not form.is_valid():
            form.validator(request)
            return HttpResponseRedirect('/employee/' + str(employee_id))

        data = form.cleaned_data
        employee = Employee.objects.filter(id=employee_id).first()
        if request.FILES.get('avatar'):
            fs = FileSystemStorage()
            if fs.exists(employee.avatar):
                fs.delete(employee.avatar)

            employee.avatar = request.FILES['avatar']

        employee.full_name = data.get('name')
        employee.email = data.get('email')
        employee.address = data.get('address')
        employee.position_id = data.get('positions').id

        employee.save()
        messages.success(request, 'Update employee success')
        return HttpResponseRedirect('/employee/' + str(employee_id))


class PositionView(View):
    def dispatch(self, *args, **kwargs):
        method = self.request.POST.get('_method', '').lower()
        if method == 'put':
            return self.put(*args, **kwargs)
        if method == 'delete':
            return self.delete(*args, **kwargs)
        return super(PositionView, self).dispatch(*args, **kwargs)

    def get(self, request, position_id):
        position = Position.objects.filter(id=position_id).first()
        position_form = PositionForm(initial={'name': position.name})
        return render(request, 'edit-position.html', {'position_form': position_form, 'position_id': position_id})

    def post(self, request):
        form = PositionForm(request.POST)
        if not form.is_valid():
            form.validator(request)
            return HttpResponseRedirect('/')

        data = form.cleaned_data
        position = Position(
            name=data.get('name')
        )

        position.save()
        messages.success(request, 'Insert position success')
        return HttpResponseRedirect('/')

    def delete(self, request):
        position_id = request.POST['position_id']
        model = Position.objects.filter(id=position_id)
        model.delete()
        messages.success(request, 'Delete position success')
        return HttpResponseRedirect('/')

    def put(self, request, position_id):
        form = PositionForm(request.POST)
        if not form.is_valid():
            form.validator(request)
            return HttpResponseRedirect('/position/' + str(position_id))

        position = Position.objects.filter(id=position_id).first()
        position.name = form.cleaned_data.get('name')
        position.save()
        messages.success(request, 'Update position success')
        return HttpResponseRedirect('/position/' + str(position_id))



# request to php server
import requests as python_request


def get_user(request):
    token = request.GET['token']
    secret_key = request.GET['secret_key']
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + token
    }

    data = {
        'secret_key': secret_key
    }

    get_response = python_request.post(url='http://localhost:8000/api/verify-secret-key', headers=headers, data=data)
    # data = get_response.json()
    # print(data)
    return HttpResponse(get_response)