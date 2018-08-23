from . import views
from django.urls import path

app_name = "comments"
urlpatterns = [
    path('post/<int:post_id>/comment/', views.post_comment, name='comment'),
]
