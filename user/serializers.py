from rest_framework import serializers
from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # serializer에 사용될 model, field지정
        model = UserModel
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ["username", "fullname", "email", "password", "join_date"]  
        exrta_kwargs = {
            'password': {'write_only': True},
        } # password를 write_only 로 설정하면 data 안에 password는 남아있지만 정보를 누군가 보는 행위는 못함.