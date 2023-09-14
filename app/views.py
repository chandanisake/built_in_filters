from django.shortcuts import render

# Create your views here.
import datetime
def built_in_filters(request):
    data='heLlO woRlD iM pRound TO bE InDiAn'
    dt=datetime.datetime.now()
    d={'data':data,'dt':dt,'c':1}
    return render(request,'built_in_filters.html',d)
