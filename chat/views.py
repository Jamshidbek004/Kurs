from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from chat.models import Message
from chat.forms import MessageForm

@login_required
def chat_home(request, username=None):
    users = User.objects.exclude(username=request.user.username)

    if username:
        selected_user = User.objects.get(username=username)
        messages = Message.objects.filter(sender=request.user, receiver=selected_user) | Message.objects.filter(
            sender=selected_user, receiver=request.user)
        messages = messages.order_by('timestamp')
    else:
        selected_user = None
        messages = None

    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.sender = request.user
            new_message.receiver = selected_user
            new_message.save()
            return redirect('chat_home', username=username)
    else:
        form = MessageForm()

    context = {
        'users': users,
        'selected_user': selected_user,
        'messages': messages,
        'form': form,
    }

    return render(request, 'xabar.html', context=context)
