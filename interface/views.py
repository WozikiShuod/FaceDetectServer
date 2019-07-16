from django.shortcuts import render
from django.conf import settings
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


def pictures_save(request):
    obj = dict();
    if request.method == 'POST':
        student_name = str(request.POST.get('username'))
        files = request.FILES.getlist('photo')
        if not files:
            obj['error'] = '没有图片上传'
        else:
            dirs = settings.MEDIA_ROOT+student_name
            folder = os.path.exists(dirs)
            if not folder:
                os.makedirs(dirs)
            try:
                for file in files:
                    img_name = file.name
                    test = file.file.read()
                    with open(f'{dirs}'+'\\'+img_name, 'wb') as f:
                        f.write(test)
            except Exception as e:
                obj['error'] = e
    return render(request, 'interface/Pictures_Save.html')