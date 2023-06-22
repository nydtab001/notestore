from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny

from .serializers import NoteSerializer
from .models import Note


# Create your views here.


class NoteListCreate(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NoteGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
