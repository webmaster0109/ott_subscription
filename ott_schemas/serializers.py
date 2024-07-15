from rest_framework import serializers
from .models import User, Subscription, Plan, Payment, Content, UserContent, Notification, Setting

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'profile_picture_url', 'is_active']

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'user', 'plan', 'start_date', 'end_date', 'status', 'renewal_date', 'created_at', 'updated_at']

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'name', 'description', 'price', 'billing_cycle', 'features', 'created_at', 'updated_at']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user', 'subscription', 'amount', 'currency', 'payment_method', 'payment_status', 'transaction_id', 'payment_date', 'created_at', 'updated_at']

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'title', 'description', 'content_type', 'url', 'thumbnail_url', 'created_at', 'updated_at', 'is_premium']

class UserContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContent
        fields = ['id', 'user', 'content', 'watched', 'progress', 'rating', 'review', 'created_at', 'updated_at']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'is_read', 'created_at', 'updated_at']

class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = ['id', 'key', 'value', 'created_at', 'updated_at']
