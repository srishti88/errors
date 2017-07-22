from django.conf.urls import url
from login import views

urlpatterns = [
    url('',views.sign_up_view)
]