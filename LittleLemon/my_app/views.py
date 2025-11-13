from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer,MenuItemSerializer,BookingSerializer
from .models import MenuItem,Booking


# Create your views here.
def test(request):
    return HttpResponse('hello world')

def index(request):
    return render(request,'index.html',{})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MenuItemView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

    # def has_permission(self,request):
    #     if request.method == 'POST':
    #         return request.user and request.user.is_staff
    #     return True
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def has_permission(self,request):
        if request.method in ['PUT','DELETE']:
            return request.user and request.user.is_staff
        return True
    
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return HttpResponse({'message':'This view is protected'})
