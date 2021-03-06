from django.urls import path

from . import views

app_name = 'auction'
urlpatterns = [
    path('create_account', views.create_account, name='create_account'),
    path('create_account_submit', views.create_account_submit, name='create_account_submit'),
    path('pending_verification', views.pending_verification, name='pending_verification'),
    path('login', views.login, name='login_detail'),
    path('login_submit', views.login_submit, name='login_submit'),
    path('listings/<str:username>', views.listings, name='listings'),
    path('listing_detail/<int:listing_id>/<str:username>', views.listing_detail, name='listing_detail'),
    path('bid_submit', views.bid_submit, name='bid_submit'),
    path('bid_confirmed/<str:username>', views.bid_confirmed, name='bid_confirmed'),
    path('create_listing/<str:username>', views.create_listing, name='create_listing'),
    path('listing_submit', views.create_listing_submit, name='listing_submit'),
    path('user_account/<str:username>', views.user_account, name='user_account'),
    path('user_account_submit', views.user_account_submit, name='user_account_submit'),
]