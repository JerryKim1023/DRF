from rest_framework import serializers

from django.db.models import F, Q, Avg, Max

from product.models import Event as EventModel
from product.models import Product as ProductModel
from product.models import Review as ReviewModel

from datetime import datetime, timedelta
from django.utils import timezone

class EventSerializer(serializers.ModelSerializer):
    # validate 함수 선언 시 serializer에서 자동으로 해당 함수의 validation을 해줌
    def validate(self, data):
        # custom validation pattern
        today = timezone.now().date() # datetime.now().date()
        print(today)
        show_expired_date = data.get("EventSerializer()", {}).get("show_expired_date", 0)
        print(show_expired_date)
        # show_date = data.get("EventSerializer()", {}).get("show_date", 0)
        if Q(show_expired_date__lt=today):
            # validation에 문제가 없을 경우 data return
            return data
        # validation에 통과하지 못할 경우 ValidationError class 호출
        raise serializers.ValidationError(
                # custom validation error message
                detail={"error": "기한이 만료되어 등록이 불가합니다."},
            )
        
    def create(self, validated_data):

        # product object 생성
        product = EventModel(**validated_data)
        product.save()

        return product
        
    def update(self, instance, validated_data): # 기본 업데이트 함수 구현해서 위로 커스텀
        # 인스턴스에는 입력된 오브젝트가 담긴다.
        print(instance)
        print(validated_data)
        for key, value in validated_data.items():
            setattr(instance, key, value) # instance.key = value 이렇게 매핑 시켜주는 로직
        instance.save()
        return instance

        # partial 에서 데이터가 없으면 처리?? 어떻게?? try except?

    class Meta:
        # serializer에 사용될 model, field지정
        model = EventModel
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = "__all__" 
        # exrta_kwargs = {
        #     'password': {'write_only': True},
        # } # password를 write_only 로 설정하면 data 안에 password는 남아있지만 정보를 누군가 보는 행위는 못함.

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.fullname

    class Meta:
        # serializer에 사용될 model, field지정
        model = ReviewModel
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ["user", "content", "created", "rating", ]

class ProductSerializer(serializers.ModelSerializer):
    review = serializers.SerializerMethodField()
    def get_review(self, obj):
        reviews = obj.review_set
        return {
            "last_review": ReviewSerializer(reviews.last()).data,
            "average_rating": reviews.aggregate(avg=Avg("rating"))["avg"]
        }

    def validate(self, data):
        show_expired_date = data.get("show_expired_date", "")
        if show_expired_date and show_expired_date < datetime.now().date():
            raise serializers.ValidationError(
                detail={"error": "유효하지 않은 노출 종료 날짜입니다."},
            )
        return data

    def create(self, validated_data):
        product = ProductModel(**validated_data)
        product.user = self.context['request'].user
        product.save()
        product.desc += f"\n\n{product.created.replace(microsecond=0, tzinfo=None)}에 등록된 상품입니다."
        product.save()

        return product

    def update(self, instance, validated_data): # 기본 업데이트 함수 구현해서 위로 커스텀
        # 인스턴스에는 입력된 오브젝트가 담긴다.
        print(instance)
        print(validated_data)
        for key, value in validated_data.items():
            if key == "desc":
                created = getattr(instance, key).split("\n")[-1]
                value += f"\n\n{created}"
            setattr(instance, key, value) # instance.key = value 이렇게 매핑 시켜주는 로직

        instance.desc = f"{instance.modified.replace(microsecond=0, tzinfo=None)}에 수정되었습니다.\n\n"\
                                  + instance.desc

        instance.save()
        return instance

    class Meta:
        # serializer에 사용될 model, field지정
        model = ProductModel
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = ["user", "thumbnail", "desc", "created", 
                  "modified", "show_date_expired", "is_active", "price", "review"]
