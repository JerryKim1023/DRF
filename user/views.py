from django.shortcuts import get_object_or_404, render

# Create your views here.
# views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from user.models import User

class MyGoodPermission(permissions.BasePermission):
    """
    Allow any access.
    This isn't strictly required, since you could use an empty
    permission_classes list, but it's useful because it makes the intention
    more explicit.
    """

    def has_permission(self, request, view):
        user = request.user
        result = bool(user and user.is_authenticated and user.permission_rank >= 5)
        return 

class UserView(APIView): # CBV 방식
    permission_classes = [MyGoodPermission]
    # permission_classes = [permissions.AllowAny] # 누구나 view 조회 가능
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능

    def get(self, request):
        return Response({'message': 'get method!!'})
        
    def post(self, request):
        return Response({'message': 'post method!!'})

    def put(self, request):
        return Response({'message': 'put method!!'})

    def delete(self, request):
        return Response({'message': 'delete method!!'})


class ListUsers(APIView):

    permission_classes = [permissions.IsAdminUser]

    # def get(self, request):  # 리소스 조회, 세부 정보 열람
    #     return Response({'message': f'{usernames} 님의 조회가 완료되었습니다.'})
    def get_list_users(self, request, format=None): #  format=None과, urls의 format_suffix_patterns
        # 모든 사용자 리스트 반환
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)


        

    
    def post(self, request): # 리소스 생성
        return # Response({'message': f'{usernames} 님이 생성되었습니다.'})
    # def create_user(self, request, format=None): #  format=None과, urls의 format_suffix_patterns
    #     # 모든 사용자 리스트 반환
    #     User.objects.create(
    #         username = request.POST.get('username')
    #         email = request.POST.get('email')
    #         phone_number = request.POST.get('phone_number')
    #         password =  request.POST.get('password')
    #         fullname = request.POST.get('fullname')
    #     )
    #     return # redirect('/login') 로그인 창으로 간다던가 아니면 관리자가 억지로 만드는 거니까 그냥 둬도 될듯


    def put(self, request): # 해당 리소스 수정
        return # Response({'message': f'{usernames} 님이 수정되었습니다.'})
    

    def delete(self, request): # 해당 리소스 삭제
        return # Response({'message': f'{usernames} 님이 삭제되었습니다.'})