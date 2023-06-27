from django.urls import path
from . import views




app_name = 'thuto'

urlpatterns = [
    path('index/', views.home,name='home'),
    path('<str:pk>/grades/',views.GradePage,name='grade'),
    path('<str:pk>/lessons/',views.LessonPage,name='lesson'),
    path('quiz/<str:pk>',views.examonline,name='quiz'),
    path('news/',views.news,name='news'),
    path('contact/',views.contact,name='contact'),
    path('',views.visitor,name='visitor'),
    path('demo/',views.login_demo,name='login_demo'),
    path('demo_register/',views.register_demo)



  ]