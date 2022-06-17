from datetime import datetime
from itertools import product
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status

from product.serializers import EventSerializer

from product.models import Event as EventModel

# Create your views here.

class EventApiView(APIView):
    # 조회
    def get(self, request):
        today = datetime.now().date()
        products = EventModel.objects.filter(
            exposure_start_date__lte=today,
            exposure_end_date__gte=today,
            is_active=True
        )
        return Response(EventSerializer(products), status=status.HTTP_200_OK)
    # 생성
    def post(self, request):
        '''
        이벤트 정보를 입력받아 create 하는 함수
        '''
        event_serializer = EventSerializer(data=request.data)
        event_serializer.is_valid(raise_exception=True)
        event_serializer.save() # 정상
        return Response(event_serializer.data, status=status.HTTP_200_OK)
        
        # is_valid 함수에서 raise_exeption=True를 주면 위처럼 코드 간소화 가능
        # if user_serializer.is_valid(): 
        #     user_serializer.save() # 정상
        #     return Response(user_serializer.data, status=status.HTTP_200_OK)

        # return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
    # 수정
    def put(self, request, obj_id):
        
        update = product.objects.get(obj_id)
        # 오브젝트, data , partial 넘기기
        event_serializer = EventSerializer(product, data=request.data, partial=True)
        event_serializer.is_valid(raise_exception=True)
        event_serializer.save() # 정상
        return Response(event_serializer.data, status=status.HTTP_200_OK)
        
        
        # is_valid 함수에서 raise_exeption=True를 주면 위처럼 코드 간소화 가능
        # if user_serializer.is_valid(): 
        #     user_serializer.save() # 정상
        #     return Response(user_serializer.data, status=status.HTTP_200_OK)

        # return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductThumbnailView(APIView):
    permission_classes = []

    def get(self, request, obj_id):
        product = EventModel.objects.get(id=obj_id)
        file_path = product.objects.


class ProductView(APIView):
    permission_classes = [permissions.AllowAny]

def get(self, request):
    today = datetime.now().date()