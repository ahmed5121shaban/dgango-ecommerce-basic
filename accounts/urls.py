from django.urls import path


from .views import signup,user_activate,profile,task_celery

app_name = 'accounts'

urlpatterns = [
    path('task_celery',task_celery),
    path('signup',signup,name='signup'),
    path('<str:username>/activate',user_activate,name='user_activate'),
    path('profile',profile,name='profile'),
]