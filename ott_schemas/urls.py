from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, SubscriptionViewSet, PlanViewSet, PaymentViewSet, ContentViewSet, UserContentViewSet, NotificationViewSet, SettingViewSet, ProtectedView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'plans', PlanViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'contents', ContentViewSet)
router.register(r'usercontents', UserContentViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'settings', SettingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('protected/', ProtectedView.as_view(), name='protected-view'),
]
