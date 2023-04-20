from django.shortcuts import render

from django.http import HttpResponse

from app.models import *

from app.forms import *

# Create your views here.

def insert_topic(request):
    TFO=TOPICFORM()
    d={'TFO':TFO}
    if request.method=='POST':
        TFD=TOPICFORM(request.POST)
        if TFD.is_valid():
            topic_name=TFD.cleaned_data['topic_name']
        TO=TOPIC.objects.get_or_create(topic_name=topic_name)[0]
        TO.save()

        TD=TOPIC.objects.all()
        d1={'TD':TD}
        return render(request,'display_topic.html',d1)

    return render(request,'insert_topic.html',d)
