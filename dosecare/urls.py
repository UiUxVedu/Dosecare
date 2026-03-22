from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-medicine/', views.add_medicine, name='add_medicine'),
    path('logout/', views.logout_view, name='logout'),
    # core/urls.py
    path('delete-medicine/<int:id>/', views.delete_medicine, name='delete_medicine'),
    path('profile/', views.profile, name='profile'),
    path('delete-patient/<int:id>/', views.delete_patient, name='delete_patient'),
    path('edit-patient/<int:id>/', views.edit_patient, name='edit_patient'),
]