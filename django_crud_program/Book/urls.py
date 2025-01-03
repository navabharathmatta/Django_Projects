from django.urls import path
from .views import *
urlpatterns = [
    path("read/",Booklist),
    path("create/",post_Book),
    path("update/<int:id>/",update_Book),
    path("delete/<int:id>/",delete_Book),
]