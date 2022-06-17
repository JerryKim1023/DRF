from rest_framework import serializers

from product.models import Event as EventModel

class EventSerializer(serializers.ModelSerializer):
    # userprofile = UserProfileSerializer()

    def create(self, validated_data):
        # object를 생성할때 다른 데이터가 입력되는 것을 방지하기 위해 미리 pop 해준다.
        user_profile = validated_data.pop('userprofile')
        get_hobbys = user_profile.pop("get_hobbys", [])

        # User object 생성
        user = UserModel(**validated_data)
        user.save()

        # UserProfile object 생성
        user_profile = UserProfileModel.objects.create(user=user, **user_profile)
        
        # hobby 등록
        user_profile.hobby.add(*get_hobbys)
        user_profile.save()


    def update(self, instance, validated_data):
        
        for key, value in validated_data.items():
            print(f"key : {key}, valuer : {value}")
            setattr(instance, key, value)

        instance.save()

        return instance

    # def update(self, instance, validated_data): # 기본 업데이트 함수 구현해서 위로 커스텀
        
    #     for key, value in validated_data.items():
    #         if key == "password":
    #             instance.set_password(value)
    #             continue

    #             serattr(instance, key, value)
    #         return

    class Meta:
        # serializer에 사용될 model, field지정
        model = EventModel
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = "__all__" 
        # exrta_kwargs = {
        #     'password': {'write_only': True},
        # } # password를 write_only 로 설정하면 data 안에 password는 남아있지만 정보를 누군가 보는 행위는 못함.