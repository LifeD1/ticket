from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerForm, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('notautorized/', views.notautorized, name='notautorized'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('travel-a-dashboard/', views.travelADashboard, name='travel-a-dashboard'),
    path('agency-a-dashboard/', views.agencyAdminDashboard, name='agency-a-dashboard'),
    path('agency-b-dashboard/', views.agencyBDashboard, name='agency-b-dashboard'),
    path('onsite-t-dashboard/', views.onsiteTellerDashboard, name='onsite-t-dashboard'),
    path('customer-dashboard/', views.customerDashboard, name='customer-dashboard'),
    path('agencies/', views.agencyList, name='agencies'),
    path('add-agency/', views.addAgency, name='add-agency'),
    path('add-agency-admin/', views.addAgencyAdmin, name='add-agency-admin'),
    path('add-buses/', views.addbuses, name='add-buses'),
    path('bus-list/', views.busList, name='bus-list'),
    # path('add-bus-layout/', views.addbuses, name='add-bus-layout'),
    path('addtrips/', views.addTrips, name='addtrips'),

]