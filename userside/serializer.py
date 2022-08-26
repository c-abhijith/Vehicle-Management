from .models import UserDetails
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        

        # ...
        return token

class RegisterSerializer(serializers.ModelSerializer):
    
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserDetails
        fields = ('username','password', 'password2','usertype')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        if UserDetails.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError(
                {"username": "username already exits."})             

        return attrs

    def create(self, validated_data):
        user = UserDetails.objects.create(
            username=validated_data['username'],usertype=validated_data['usertype']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user