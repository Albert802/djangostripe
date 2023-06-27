from django.urls import path
from . import views

app_name='subscriptions'

urlpatterns = [
    path('sub_home/', views.home, name='subscriptions-home'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.success),
    path('cancel/', views.cancel,name='cancel'),
    path('webhook/', views.stripe_webhook),

]
