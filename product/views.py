from datetime import date, datetime, timezone
from django.shortcuts import render

from django.db.models import Q

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status

from django.views.static import serve
from AI.permissions import IsRegisterdMoreThanThreeDaysOrReadOrReadOnly

from product.serializers import EventSerializer
from product.serializers import ProductSerializer

from product.models import Event as EventModel
from product.models import Product as ProductModel
from product.models import Review as ReviewModel


import os
# Create your views here.

class EventApiView(APIView):
    # 조회
    def get(self, request):
        today = datetime.now().date()
        products = EventModel.objects.filter(
            show_date__lte=today,
            show_expired_date__gte=today,
            is_active=True
        )
        return Response(EventSerializer(products, many=True), status=status.HTTP_200_OK)
    # 생성
    def post(self, request):
        '''
        이벤트 정보를 입력받아 create 하는 함수
        '''
        event_serializer = EventSerializer(data=request.data)
        event_serializer.is_valid(raise_exception=True)
        event_serializer.save() # 정상
        return Response(event_serializer.data, status=status.HTTP_200_OK) # {"message": f"{EventModel.created_at}에 등록된 상품입니다."}, 
        
        # is_valid 함수에서 raise_exeption=True를 주면 위처럼 코드 간소화 가능
        # if event_serializer.is_valid(): 
        #     event_serializer.save() # 정상
        #     return Response(event_serializer.data, status=status.HTTP_200_OK)

        # return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
    # 수정
    def put(self, request, obj_id):
        
        product = EventModel.objects.get(obj_id)
        # 오브젝트, data , partial 넘기기
        event_serializer = EventSerializer(product, data=request.data, partial=True)
        event_serializer.is_valid(raise_exception=True)
        event_serializer.save() # 정상
        time_now = timezone.now()
        return Response({"message": f"{time_now}에 수정되었습니다."}, event_serializer.data, status=status.HTTP_200_OK)
        
        # is_valid 함수에서 raise_exeption=True를 주면 위처럼 코드 간소화 가능
        # if event_serializer.is_valid(): 
        #     event_serializer.save() # 정상
        #     return Response(event_serializer.data, status=status.HTTP_200_OK)

        # return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 삭제
    def delete(self, request, obj_id):
        
        try:
            user_delete = EventModel.objects.get(obj_id)  
        except EventModel.DoesNotExist:
         # some event						   status=400
            return Response({"message": "오브젝트가 존재하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)
        user_delete.delete()
        return Response({"message": f"{EventModel.title} 정보가 더 이상 존재하지 않습니다."}, status=status.HTTP_200_OK)


class ProductThumbnailView(APIView):
    permission_classes = []

    def get(self, request, obj_id):
        product = EventModel.objects.get(id=obj_id)
        file_path = product.thumbnail.path
        return serve(request, os.path.basename(file_path), os.path.dirname(file_path))
            # 스태틱파일(이미지 파일 등등) 을 serve(보내준다)해준다.


class ProductView(APIView):
    permission_classes = [IsRegisterdMoreThanThreeDaysOrReadOrReadOnly]

    # 조회
    def get(self, request):
        today = datetime.now().date()
        products = ProductModel.objects.filter(
            Q(show_expired_date__gte=today, is_active=True) |
            Q(user=request.user)
        )

        return Response(ProductSerializer(products, many=True).data, status=status.HTTP_200_OK)
    # 생성
    def post(self, request):
        '''
        이벤트 정보를 입력받아 create 하는 함수
        '''
        product_serializer = ProductSerializer(data=request.data, context={"reuquest": request})
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save() # 정상
        return Response(product_serializer.data, status=status.HTTP_200_OK) # {"message": f"{EventModel.created_at}에 등록된 상품입니다."}, 
        
        # is_valid 함수에서 raise_exeption=True를 주면 위처럼 코드 간소화 가능
        # if event_serializer.is_valid(): 
        #     event_serializer.save() # 정상
        #     return Response(event_serializer.data, status=status.HTTP_200_OK)

        # return Response(event_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
    # 수정
    def put(self, request, obj_id):
        
        product = ProductModel.objects.get(id=obj_id)
        # 오브젝트, data , partial 넘기기
        product_serializer = ProductSerializer(product, data=request.data, partial=True)
        if product_serializer.is_valid:
            product_serializer.save() # 정상

            return Response(product_serializer.data, status=status.HTTP_200_OK)

        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)