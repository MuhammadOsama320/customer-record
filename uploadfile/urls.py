from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [

    path('', views.UploadFileView.as_view(), name='index'),
    path('file_upload/', csrf_exempt(views.UploadFileView.as_view()), name='excel_to_json'),
    path('list/', views.DataView.as_view(), name='data')
]
