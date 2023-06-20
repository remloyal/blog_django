from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("updateArticle", views.index, name="updateArticle"),

    path("upload", views.upload),
]

# 文件上传的路径
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
