from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from oquvchi.models import Yonalish, Kurs, Oquvchi, Tolov
from oquvchi.forms import OquvchiForm

# Create your views here.

def asosiy(request):
    asosiy1 = Yonalish.objects.all()
    users = request.user
    oquvchi1 = Oquvchi.objects.filter(user=users)

    try:
        profile_info = Profile.objects.get(user=users)
    except Profile.DoesNotExist:
        profile_info = None  # Yoki default qiymatlarni qo'llashingiz mumkin

    context = {
        'asosiy': asosiy1,
        'profile_info': profile_info,
        'oquvchi': oquvchi1,
    }
    return render(request, 'index.html', context=context)

def yonalish(request, id):
    malumot = Kurs.objects.filter(yonalish=id)
    users = request.user

    try:
        profile_info = Profile.objects.get(user=users)
    except Profile.DoesNotExist:
        profile_info = None  # Yoki default qiymatlarni qo'llashingiz mumkin

    context = {
        'kurs': malumot,
        'profile_info': profile_info,
    }
    return render(request, 'yonalish.html', context=context)

def topshiriq(request, id):
    topshiriq1 = get_object_or_404(Kurs, id=id)
    users = request.user

    try:
        profile_info = Profile.objects.get(user=users)
    except Profile.DoesNotExist:
        profile_info = None  # Yoki default qiymatlarni qo'llashingiz mumkin

    context = {
        'topshiriq': topshiriq1,
        'profile_info': profile_info,
    }
    return render(request, 'topshiriq.html', context=context)

@login_required
def oquvchi_update(request):
    """ O'quvchi ma'lumotlarini tahrirlash """
    yonalishlar = Yonalish.objects.all()

    if request.method == "POST":
        form = OquvchiForm(request.POST, request.FILES)
        if form.is_valid():
            oquvchi = form.save(commit=False)
            oquvchi.user = request.user  # Foydalanuvchining avtomatik olinishi
            oquvchi.save()
            return redirect('asosiy')  # Yoki boshqa bir URL ga yo'naltiring
        else:
            print(form.errors)  # Formaning xatolarini konsolga chiqaramiz
    else:
        form = OquvchiForm()

    context = {
        'form': form,
        'yonalishlar': yonalishlar,
    }

    return render(request, 'oquvchi.html', context=context)

def tolov(request):
    users = request.user

    try:
        profile_info = Profile.objects.get(user=users)
    except Profile.DoesNotExist:
        profile_info = None  # Yoki default qiymatlarni qo'llashingiz mumkin

    tolov1 = Tolov.objects.filter(user=users)

    context = {
        'tolov': tolov1,
        'profile_info': profile_info,
    }
    return render(request, 'tolov.html', context=context)

def help(request):
    return render(request, 'help.html')
