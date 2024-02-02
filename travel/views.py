from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, AddAgencyForm, AddAgencyAdminForm, AddBusForm, AddTripsForm
from django.contrib.auth.models import auth
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import Group
from .models import Agency, User, Bus

# Create your views here.
def home(request):
    return render(request, 'travel/index.html')



def registerForm(request):
    groups = Group.objects.all()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            ugroup = request.POST.get('group')
            group = Group.objects.get(name=ugroup)
            user = form.save()
            user.groups.add(group)
            login(request, user)
            return redirect('home')
    else: 
        form = RegistrationForm()
    return render(request, 'travel/register.html', {'form':form, 'groups':groups})


def loginPage(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            
    return render(request, 'travel/login.html', {'form': form})



def user_logout(request):
    auth.logout(request)
    return redirect('login')


def notautorized(request):
    
    return render(request, 'travel/notautorize.html')





@login_required(login_url='login')
def dashboard(request):
    # user = User.objects.filter(id=2)
    # groups = rGroup.objects.all()
    print(request.user)
    if request.user.groups.filter(name='travel-admin').exists():

        return redirect('travel-a-dashboard')
    elif request.user.groups.filter(name='agency-admin').exists():
        return redirect('agency-a-dashboard')
    elif request.user.groups.filter(name='agency-branch-admin').exists():
        return redirect('agency-b-dashboard')
    elif request.user.groups.filter(name='onsite-ticket-tellers').exists():
        return redirect('onsite-t-dashboard')
    elif request.user.groups.filter(name='customers').exists():
        return redirect('customer-dashboard')
    else:
        return redirect('login')
    return render(request, 'travel/dashboard1.html')

@login_required(login_url='login')
def travelADashboard(request):
    groups = Group.objects.all()
    if request.user.groups.filter(name='travel-admin').exists():
        print('liav')
    else:
        messages.success(request, "Not autorice..")
        return redirect('notautorized')

    return render(request, 'travel/travel_dashboard.html', {'groups':groups})

@login_required(login_url='login')
def agencyAdminDashboard(request):
    if request.user.groups.filter(name='agency-admin').exists():
        pass
    return render(request, 'travel/dashboard2.html')

@login_required(login_url='login')
def agencyBDashboard(request):
    
    return render(request, 'travel/dashboard3.html')

@login_required(login_url='login')
def onsiteTellerDashboard(request):
    
    return render(request, 'travel/dashboard4.html')

@login_required(login_url='login')
def customerDashboard(request):
    
    return render(request, 'travel/dashboard5.html')



def addAgency(request):

    if request.method == 'POST':
        form = AddAgencyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agencies_list')
    else:
        form = AddAgencyForm()


    context = {'form':form}
    return render(request, 'travel/add_agency.html', context)

def addAgencyAdmin(request):
    groups = Group.objects.all()

    if request.method == 'POST':
        form = AddAgencyAdminForm(request.POST)
        if form.is_valid():
            ugroup = request.POST.get('group')
            group = Group.objects.get(name=ugroup)
            user = form.save()
            user.groups.add(group)
            return redirect('agencies_list')
    else:
        form = AddAgencyAdminForm()


    context = {'form':form, 'groups':groups}
    return render(request, 'travel/add_agency_admin.html', context)


def agencyList(request):
    agencies = Agency.objects.all()
    
    print(agencies)
    agencyAdmin = User.objects.all()
    # print(agencyA)
    context={'agencies':agencies, 'agencyAdmin': agencyAdmin}
    return render(request, 'travel/agency_list.html', context)


def addbuses(request):
    if request.method == 'POST':
        form = AddBusForm(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = AddBusForm()

    context = {'form': form}
    return render(request, 'travel/add_busses.html', context)


def busList(request):
    agencies = Agency.objects.all()
    buses = Bus.objects.all()

    context = {'agencies': agencies, 'buses': buses}
    return render(request, 'travel/bus_list.html', context)


def addTrips(request):
    if request.method == 'POST':
        pass
    else:
        form = AddTripsForm
    context = {'form':form}
    return render(request, 'travel/add_trip.html', context)