from rest_framework import serializers
from user.models import User as UserModel
from user.models import UserProfile as UserProfileModel
from user.models import Hobby as HobbyModel

class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = HobbyModel
        fields = "__all__"
        # fields = "__all__"

class UserProfileSerializer(serializers.ModelSerializer):
    hobby = HobbySerializer(many=True, required=False, read_only=True)
    get_hobbys = serializers.ListField(required=False) # 리스트 필드로 지정해서 리스트 포맷으로 받을 수 있게 됨.
    class Meta:
        model = UserProfileModel
        fields = ["introduction", "birthday", "age", "hobby", "get_hobbys"]
        # fields = "__all__"

# 내가 나를 볼 때는 UserSerializer 쓰고 남을 볼 때는 UserSimpleSerializer를 보게 하는 활용도 가능
class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["username", "fullname", "email"]

class UserSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()

    class Meta:
        # serializer에 사용될 model, field지정
        model = UserModel
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ["username", "fullname", "email", "phone_number", "password", "join_date", "userprofile"]  
        # 각 필드에 해당하는 다양한 옵션 지정
        extra_kwargs = {
            # write_only : 해당 필드를 쓰기 전용으로 만들어 준다.
            # 쓰기 전용으로 설정 된 필드는 직렬화 된 데이터에서 보여지지 않는다.
             # password를 write_only 로 설정하면 data 안에 password는 남아있지만 정보를 누군가 보는 행위는 못함.
            'password': {'write_only': True}, # default : False
            'email': {
                # error_messages : 에러 메세지를 자유롭게 설정 할 수 있다.
                'error_messages': {
                    # required : 값이 입력되지 않았을 때 보여지는 메세지
                    'required': '이메일을 입력해주세요.',
                    # invalid : 값의 포맷이 맞지 않을 때 보여지는 메세지
                    'invalid': '알맞은 형식의 이메일을 입력해주세요.'
                    },
                    # required : validator에서 해당 값의 필요 여부를 판단한다.
                    'required': True # default : True
                    },
            }

     # validate 함수 선언 시 serializer에서 자동으로 해당 함수의 validation을 해줌
    def validate(self, data):
        # custom validation pattern
        if data.get("userprofile", {}).get("age", 0) < 12:
            # validation에 통과하지 못할 경우 ValidationError class 호출
            raise serializers.ValidationError(
                    # custom validation error message
                    detail={"error": "12세 이상만 가입할 수 있습니다."},
                )

        # validation에 문제가 없을 경우 data return
        return data

    def create(self, validated_data):
        # object를 생성할때 다른 데이터가 입력되는 것을 방지하기 위해 미리 pop 해준다.
        user_profile = validated_data.pop('userprofile')
        get_hobbys = user_profile.pop("get_hobbys", []) # 앞의 값 가져와서 없으면 [] 로 넘겨줌.

        # User object 생성
        user = UserModel(**validated_data)
        user.save()

        # UserProfile object 생성
        user_profile = UserProfileModel.objects.create(user=user, **user_profile)
        
        # hobby 등록
        user_profile.hobby.add(*get_hobbys) # M2M 관계여서 .add 가 가능
        user_profile.save()

        return user

    def update(self, instance, validated_data):
        
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
                # continue
            setattr(instance, key, value)
        instance.save()

        return instance
    

# sample request data
'''
{
    "username": "user_name",
    "password": "H0t$ix",
    "fullname": "이름",
    "email": "sample@email.com",
    "userprofile": {
        "introduction": "자기소개입니다.",
        "birthday": "2000-1-01",
        "age": 13,
        "get_hobbys": [3,4,5,6],
    },
}
'''