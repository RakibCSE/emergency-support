from django.urls import path, re_path

from rest_framework.urlpatterns import format_suffix_patterns

from service import views


app_name = 'service'

urlpatterns = [
    path('', views.home, name='home'),
    path('help-me/', views.get_service, name="get-service"),
    path('api/v1/seekers/', views.ServiceSeekerList.as_view(), name="seeker-data"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
