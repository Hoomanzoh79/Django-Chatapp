from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Q

from .models import Room


def message(request, user1, user2):
    user1_obj = get_object_or_404(get_user_model(), username=user1)
    user2_obj = get_object_or_404(get_user_model(), username=user2)

    if (
        Room.objects.select_related("user1", "user2")
        .filter(Q(name__icontains=user1) & Q(name__icontains=user2))
        .exists()
    ):

        room = Room.objects.get(Q(name__icontains=user1) & Q(name__icontains=user2))
        if request.user != room.user1 and request.user != room.user2:
            return HttpResponseBadRequest("You cant't join this private chat!")

    else:
        room_name = f"{user1}and{user2}"
        room = Room.objects.create(name=room_name)

        room.user1 = user1_obj
        room.user2 = user2_obj
        room.save()

    return render(
        request,
        "chat/room.html",
        {
            "room": room,
            "target_user": user2_obj,
        },
    )
