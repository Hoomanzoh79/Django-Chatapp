from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Room

class ChatIndexView(TemplateView):
    template_name = "chat/chat_index.html"
    redirect_field_name = ""

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["rooms"] = Room.objects.all()
        return context


def room_view(request, room_name):
    chat_room, created = Room.objects.get_or_create(name=room_name)
    return render(request, 'chat/room.html', {
        'room': chat_room,
    })