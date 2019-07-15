from django.shortcuts import render
import os


# Create your views here.
def index(request):
    pics = []
    for img in os.listdir('./interface/static'):
        if img.endswith('png'):
            pics.append('/static/' + img)
    context = {}
    context['main'] = pics
    return render(request, 'interface/qrcode.html', context=context)


if __name__ == '__main__':
    print(os.curdir)
