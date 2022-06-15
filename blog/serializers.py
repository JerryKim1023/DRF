from rest_framework import serializers
from blog.models import Article as ArticleModel
from blog.models import Category as CategoryModel
from blog.models import Comment as CommentModel

class AticleSerializer(serializers.ModelSerializer):
    class Meta:
        # serializer에 사용될 model, field지정
        model = ArticleModel
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        # serializer에 사용될 model, field지정
        model = CategoryModel
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        # serializer에 사용될 model, field지정
        model = CommentModel
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        fields = "__all__"
