from unittest import result
from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseNotFound

# Create your views here.
def TestQLND(request):
    return render(request, 'QLND_template.html')

articles = {
    'NhapThongTin': 'Nhập thông tin người dùng'
}

def news_view(request,topic):
    try:
        return HttpResponse(articles[topic])
    except:
        result = 'No page for that topic'
        return HttpResponseNotFound(result)
        raise Http404('404 PAGE NOT FOUND')
