from datetime import datetime
import os
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

# Create your views here.
from django.http import HttpResponse
from blog.models import FileControl


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def getpath():
    return static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


def upload(request):
    if request.method == 'POST':

        title = request.POST['type']
        files = request.FILES.getlist('files')
        if files:
            for file in files:
                types = file.name.split('.')
                name = types[0]
                type = types[1]
                # path = settings.MEDIA_ROOT
                # content = file.chunks()
                # with open(where, 'wb') as f:
                #     for i in content:
                #         f.write(i)
                timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
                file_extension = os.path.splitext(file.name)[1]
                new_filename = f'{timestamp}{file_extension}'

                print(file, name)
                if not os.path.exists(f'media/{type}/'):
                    os.makedirs(f'media/{type}/')
                with open(f'media/{type}/{new_filename}', 'wb+') as destination:
                    # 将上传的文件内容写入新文件
                    for chunk in file.chunks():
                        destination.write(chunk)

                    FileControl.objects.create(
                        type=type, name=name, suffix_name=type, flie_path=destination.name)
        return HttpResponse('----上传成功！')
