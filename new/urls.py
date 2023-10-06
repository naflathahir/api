from django.urls import path
from.import views
urlpatterns=[
    path("",views.index,name="index"),
    path("hello/<int:id>",views.hello,name="hello"),
]