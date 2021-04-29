from django.urls import path

from . import views

app_name = 'auction'
urlpatterns = [
    path('create_account', views.create_account, name='create_account'),
    path('create_account_submit', views.create_account_submit, name='create_account_submit'),
    path('pending_verification', views.pending_verification, name='pending_verification'),
    path('login', views.login, name='login_detail'),
    path('login_submit', views.login_submit, name='login_submit'),
    path('listings', views.listings, name='listings'),
    path('listing_detail/<int:listing_id>', views.listing_detail, name='listing_detail'),
    path('bid_submit', views.bid_submit, name='bid_submit'),
    path('bid_confirmed', views.bid_confirmed, name='bid_confirmed'),
    path('user_account', views.user_account, name='user_account'),
]