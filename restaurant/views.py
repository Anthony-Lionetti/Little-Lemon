from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import MenuSerializer, BookingSerializer
from .models import Menu

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer