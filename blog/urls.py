from . import views
from django.urls import path

app_name = "blog"
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>', views.archives, name='archives'),
    path('category/<int:category_id>', views.category, name='category')
]
