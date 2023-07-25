from django.urls import path, re_path, register_converter
from . import views

# url reverse에서 name space 역할
app_name = 'instagram1'

class YearConverter:
    regex = r"20\d{2}"

    def to_python(self, value):
        return int(value)
    
    def to_url(self, value):
        return str(value)

register_converter(YearConverter, 'year')

urlpatterns = [
    path('', views.post_list),
    path('<int:pk>/', views.post_detail),
    # re_path(r'(?P<pk>\d+)/$', views.post_detail)
    # path('archives/<int:year>/', views.archives_year),
    # re_path(r'archives/(?P<year>\d{4})/', views.archives_year),
    # re_path(r'archives/(?P<year>20\d{2})/', views.archives_year)
    path('archives/<year:year>/', views.archives_year)
]