from rest_framework import serializers
from .models import User, Subscription, Plan, Payment, Content, UserContent, Notification, Setting

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirmPassword = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'confirmPassword', 'first_name', 'last_name', 'phone_number', 'profile_picture_url', 'is_active']
    
    def validate(self, data):
        if data['password'] != data['confirmPassword']:
            raise serializers.ValidationError({"password": "Passwords do not match"})
        return data

    def create(self, validated_data):
        validated_data.pop('confirmPassword')
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        validated_data.pop('confirmPassword', None)
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

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
