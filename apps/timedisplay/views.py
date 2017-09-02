from django.shortcuts import render, HttpResponse
from django.utils.timezone import datetime
def index(request):
    time = datetime.now()
    print (time)
    context = {
    "time": time
    }
    return render(request,'timedisplay/index.html', context)
