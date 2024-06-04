from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()       #get list of all user object
    serializer_class = UserSerializer   #what kind of data to create a user
    permission_classes = [AllowAny]     #which classes can call this view


class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    #get the notes created by the author alone.
    #this only gets the notes a user wrote themselves, not others
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)