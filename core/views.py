from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Medicine
from .models import AdminProfile
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import PatientProfile


def index(request):
    return render(request, 'index.html')

# SIGNUP
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'User already exists'})

        user = User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'signup.html')


# LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


# DASHBOARD
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')

    medicines = Medicine.objects.filter(user=request.user)

    return render(request, 'dashboard.html', {'medicines': medicines})


# ADD MEDICINE (NOW SAVES DATA)
def add_medicine(request):
    if request.method == "POST":
        name = request.POST.get('name')
        dosage = request.POST.get('dosage')
        time = request.POST.get('time')
        phone = request.POST.get('phone')

        Medicine.objects.create(
            user=request.user,
            name=name,
            dosage=dosage,
            time=time,
            phone=phone
        )

        return redirect('dashboard')

    return render(request, 'addMedicine.html')

# Delete 
def delete_medicine(request, id):
    if request.method == "POST":
        med = get_object_or_404(Medicine, id=id, user=request.user)
        med.delete()
    return redirect('dashboard')


#  LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')

# Profile 
@login_required
def profile(request):
    user = request.user

    # Get admin profile
    admin_profile = AdminProfile.objects.filter(user=user).first()

    # Get patients of this admin
    patients = PatientProfile.objects.filter(admin=user)

    if request.method == "POST":

        # ================= ADMIN SAVE =================
        if request.POST.get("name"):

            if admin_profile:
                admin_profile.name = request.POST.get("name")
                admin_profile.age = request.POST.get("age")
                admin_profile.relation = request.POST.get("relation")
                admin_profile.contact = request.POST.get("contact")
                admin_profile.save()
            else:
                AdminProfile.objects.create(
                    user=user,
                    name=request.POST.get("name"),
                    age=request.POST.get("age"),
                    relation=request.POST.get("relation"),
                    contact=request.POST.get("contact")
                )

            messages.success(request, "Admin profile saved successfully ✅")

        # ================= PATIENT SAVE =================
        if request.POST.get("p_name"):

            PatientProfile.objects.create(
                admin=user,  # ✅ IMPORTANT (requires FK in model)
                name=request.POST.get("p_name"),
                age=request.POST.get("p_age"),
                disease=request.POST.get("p_disease"),
                weight=request.POST.get("p_weight"),
                symptoms=request.POST.get("p_symptoms"),
                medication_duration=request.POST.get("p_duration"),
            )

            messages.success(request, "Patient added successfully ✅")

        return redirect('profile')

    return render(request, "profile.html", {
        "admin_profile": admin_profile,
        "patients": patients
    })

def edit_patient(request, id):
    patient = get_object_or_404(PatientProfile, id=id, admin=request.user)

    if request.method == "POST":
        patient.symptoms = request.POST.get("symptoms")
        patient.medication_duration = request.POST.get("duration")
        patient.save()

    return redirect('profile')

def delete_patient(request, id):
    patient = get_object_or_404(PatientProfile, id=id, admin=request.user)
    patient.delete()
    return redirect('profile')