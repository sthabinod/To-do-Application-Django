from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name="index"),
    path('list_added/',views.list_added,name="list_added"),
    path('list_delete/',views.list_delete,name="list_delete")
]