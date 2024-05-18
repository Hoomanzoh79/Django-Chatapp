from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "chat/index.html"


def room_view(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})