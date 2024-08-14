from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import UserEditForm, ProfileEditForm
from accounts.forms import UserRegistrationForm
from accounts.models import Profile

# Foydalanuvchi shaxsiy profilini ko'rsatish funksiyasi
@login_required
def dashboard_view(request):
    users = request.user
    # Profil mavjud emasligi xatolarini ushlash
    profile_info = Profile.objects.get(user=users)
    context = {
        "user": users,
        "profile_info": profile_info
    }
    return render(request, "pages/user_profile.html", context=context)

# Foydalanuvchi ro'yxatdan o'tish funksiyasi
def user_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            # Yangi foydalanuvchi uchun profil yaratish
            Profile.objects.create(user=new_user)
            context = {"new_user": new_user}
            return render(request, "account/register_done.html", context)
    else:
        user_form = UserRegistrationForm()

    context = {"user_form": user_form}
    return render(request, "account/register.html", context)

# Foydalanuvchi profilini va ma'lumotlarini tahrirlash funksiyasi
@login_required
def edit_user(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('asosiy')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=profile)

    return render(request, "account/profile_edit.html", {
        "user_form": user_form,
        "profile_form": profile_form,
        "profile_info": profile
    })
