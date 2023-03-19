from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id','username','email','phone','car','password')


    def validate_password(self,value):
        validate_password(value)
        return value


    def create(self, validated_data):
        user = User.objects.create (
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            car=validated_data['car'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user