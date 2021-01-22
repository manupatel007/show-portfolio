from .models import NotificationsField

def notification_processor(request):
    if request.user.is_authenticated:
        notifications = NotificationsField.objects.filter(person__username__contains=request.user.username)
    else:
        notifications = ''
    return {
        'notifications' : notifications,
    }