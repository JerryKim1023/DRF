from rest_framework import serializers
from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel

class HobbySerializer(serializers.ModelSerializer):
    same_hobby_users = serializers.SerializerMethodField()
    def get_same_hobby_users(self, obj):
        # print(f"{obj} / {type(obj)}")
        user_list = []
        # print(dir(obj))
        # print(obj.userprofile_set.all())
        for userprofile in obj.userprofile_set.all():
            user_list.append(userprofile.user.fullname)


        return user_list
    class Meta:
        model = HobbyModel
        fields = ["name", "same_hobby_users"]
        # fields = "__all__"

class UserProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True)
    class Meta:
        model = UserProfileModel
        fields = ["introduction", "birthday", "age", "hobby"]
        # fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()

    class Meta:
        # serializer에 사용될 model, field지정
        model = UserModel
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ["username", "fullname", "email", "password", "join_date", "userprofile"]  
        exrta_kwargs = {
            'password': {'write_only': True},
        } # password를 write_only 로 설정하면 data 안에 password는 남아있지만 정보를 누군가 보는 행위는 못함.
