from django.urls import path

from . import views

app_name = 'auction'
urlpatterns = [
    path('create_account', views.create_account, name='create_account'),
    path('login', views.login, name='login_detail'),
    path('login_submit', views.login_submit, name='login_submit'),
    path('listings', views.listings, name='listings'),
    path('listing_detail/<int:listing_id>', views.listing_detail, name='listing_detail'),
]