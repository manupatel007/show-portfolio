from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('portfolio/', views.portfolio, name='portfolio'),
    path('addproject/<personp>', views.addproject, name='addproject'),
    path('addfields/<personp>', views.completeprofile, name='completeprofile'),
    path('project_detail/<int:pk>/<personp>', views.project_detail, name='project_detail'),
    path('project_home/', views.project_home, name='project_home'),
    path('project_describe/<int:pk>/', views.project_describe, name='project_describe'),
    path('followers/', views.followers, name='followers'),
    path('following/', views.following, name='following'),
    path('notifications/', views.notifications, name='notifications'),
    path('portfolio/ajax_notification/', views.NotificationCheck.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)