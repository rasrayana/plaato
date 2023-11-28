from django.shortcuts import render
from apps.base.models import Settings,Slide,About,History,Reservation,Team

# Create your views here.
def index(request):
    settings = Settings.objects.latest('id')
    slide = Slide.objects.all()
    about = About.objects.latest("id")
    history = History.objects.latest("id")
    reservation = Reservation.objects.latest('id')
    team = Team.objects.all()
    return render(request,'index.html', locals())