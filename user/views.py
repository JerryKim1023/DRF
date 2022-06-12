from django.shortcuts import get_object_or_404, render

# Create your views here.
# views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status

from user.models import Hobby, User
from django.contrib.auth import authenticate, login
from django.db.models import F
class UserApiView(APIView):
    # 로그인
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)

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

    def get_same_hobby(self, request):
        user = request.user
        # user = User.objects.get(id=1)
        # print(user)


        hobbys = user.userprofile.hobby.all()
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