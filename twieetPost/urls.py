from django.urls import path
from . import views

urlpatterns = [
    path('',views.twieet_list,name="twieet_list"),
    path('createtweet/',views.create_twieet,name="twieet_create"),
    path('edit/<int:twieet_id>',views.twieet_edit,name="twieet_edit"),
    path('delete/<int:twieet_id>',views.twieet_delete,name="twieet_delete"),
]

