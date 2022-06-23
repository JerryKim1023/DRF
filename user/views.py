from django.shortcuts import get_object_or_404, render

# Create your views here.
# views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, authentication
from rest_framework import status
from rest_framework.exceptions import APIException
from blog.models import Article

from user.models import Hobby, User
from django.contrib.auth import authenticate, login
from django.db.models import F

from datetime import datetime, timedelta, timezone

from user.serializers import UserSerializer
class UserApiView(APIView):
    
    #모든 사용자에 대해서 user 정보와 userpofile 정보를 가져오고
    # 같은 취미를 가진 사람들을 출력하기
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        # user = request.user
        user = User.objects.all().order_by('?').first()
        # serializer에 queryset을 인자로 줄 경우 many=True 옵션을 사용해야 한다.
        serialized_user_data = UserSerializer(user).data # 오브젝트를 넣어서 직렬화해주기
        return Response(serialized_user_data, status=status.HTTP_200_OK)

        # return data
        """
        {
            "username": "user",
            "password": "pbkdf2_sha256$320000$u5YnmKo9luab9csqWpzRsa$pKfqHnBiF5Rgdo1Mj9nxNOdhpAl9AhPVXFPXkbPz7Mg=",
            "fullname": "user's name",
            "email": "user@email.com"
        }
        """

    # 회원가입 / serializer로 쉽고 직관적으로 구현가능하다해서 우선 스킵
    def post(self, request):
        '''
        사용자 정보를 입력받아 create 하는 함수
        '''
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save() # 정상
        return Response(user_serializer.data, status=status.HTTP_200_OK)
        
        # is_valid 함수에서 raise_exeption=True를 주면 위처럼 코드 간소화 가능
        # if user_serializer.is_valid(): 
        #     user_serializer.save() # 정상
        #     return Response(user_serializer.data, status=status.HTTP_200_OK)

        # return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
    # 수정
    def put(self, request, obj_id):
        
        user_update = User.objects.get(id=obj_id)
        # 오브젝트, data , partial 넘기기
        user_serializer = UserSerializer(user_update, data=request.data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save() # 정상
        return Response(user_serializer.data, status=status.HTTP_200_OK)
        
        
        # is_valid 함수에서 raise_exeption=True를 주면 위처럼 코드 간소화 가능
        # if user_serializer.is_valid(): 
        #     user_serializer.save() # 정상
        #     return Response(user_serializer.data, status=status.HTTP_200_OK)

        # return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 삭제
    def delete(self, request, obj_id):
        
        try:
            user_delete = User.objects.get(obj_id)  
        except User.DoesNotExist:
         # some event						   status=400
            return Response({"message": "오브젝트가 존재하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)
        user_delete.delete()
        # 오브젝트, data , partial 넘기기
        return Response({"message": f"{User.username} 정보가 더 이상 존재하지 않습니다."}, status=status.HTTP_200_OK)

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
    # permission_classes = [MyGoodPermission]
    permission_classes = [permissions.AllowAny] # 누구나 view 조회 가능
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능

    
    def get(self, request): # 같은 취미의 유저를 구하는 로직
        user = request.user
        # user = User.objects.get(id=1)
        print(user)
        print(dir(user))

        hobbys = user.userprofile.hobby.all()
        print(dir(hobby))
        for hobby in hobbys:
            # exclde : 매칭 된 쿼리만 제외, filter와 반대
		    # annotate : 필드 이름을 변경해주기 위해 사용, 이외에도 원하는 필드를 추가하는 등 다양하게 활용 가능
		    # values / values_list : 지정한 필드만 리턴 할 수 있음. values는 dict로 return, values_list는 tuple로 ruturn
		    # F() : 객체에 해당되는 쿼리를 생성함
            hobby_members = hobby.userprofile_set.exclude(user=user).annotate(username=F('user__username')).values_list('username', flat=True)
            # hobby_members = list(hobby_members) # 리스트로 보려면 리스트화
            print(f"hobby : {hobby.name} / hobby members : {hobby_members}")
        return Response({})
# result print
"""
hobby : 산책 / hobby members : ['user1']
hobby : 음악감상 / hobby members : ['user1', 'user2']
hobby : 스쿠버다이빙 / hobby members : ['user2']
hobby : 여행 / hobby members : ['user2']
"""

    # def get(self, request):
    #     try:
    #         # hobby_list = Hobby.objects.all()
    #         hobby_list = Hobby.objects.filter(id__gt=5)[0]
    #         print(hobby_list)
    #     except:
    #         return Response({"message": "오브젝트가 존재하지 않습니다."},status=status.HTTP_400_BAD_REQUEST)

    #     return Response({'message': 'get method!!'})

    # def post(self, request):
    #     return Response({'message': 'post method!!'})

    # def put(self, request):
    #     return Response({'message': 'put method!!'})

    # def delete(self, request):
    #     return Response({'message': 'delete method!!'})


class ListUsers(APIView): # 유저리스트에 대한 API
    authentication_classes = [authentication.TokenAuthentication] # rest_framework에 토큰인증이 있어서 넣어봄.
    permission_classes = [permissions.AllowAny]

    # def get(self, request):  # 리소스 조회, 세부 정보 열람
    #     return Response({'message': f'{usernames} 님의 조회가 완료되었습니다.'})
    def get_login_list_users(self, request, format=None): #  format=None과, urls의 format_suffix_patterns
        # 모든 로그인한 사용자 리스트 반환
        users = User.objects.all()
        try:
            User.objects.filter(user=users)
            if users.is_authenticated:
                login_users = [user for user in users]
                print(login_users)
            return Response(login_users)
        except:
            return Response(f"{login_users.username}님 로그인 후에 조회가 가능합니다.")

    
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