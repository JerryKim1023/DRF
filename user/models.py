from django.db import models
# from django.contrib.auth.models import UserManager
# Create your models here.
# models.py
class User(models.Model):
    username = models.CharField("사용자 계정", max_length=20, unique=True)
    email = models.EmailField("이메일 주소", max_length=100, unique=True)
    # phone_number = models.CharField("전화번호", max_length=30, unique=True) 
    # # 슈퍼유저를 폰넘버 만들기 전에 만들어서 makemigrations가 안 됨. 나중에 추가할 때 user 삭제 후 사용하기
    password = models.CharField("비밀번호", max_length=60)
    fullname = models.CharField("이름", max_length=20)
    join_date = models.DateTimeField("가입일", auto_now_add=True)
    permission_rank = models.IntegerField(default=0)
    
    # 사용자계정으로 email을 사용, 추후 넷플릭스처럼 이메일 or 핸드폰 로그인 추가예정
    # objects = UserManager() 
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.username} / {self.email}"

class UserProfile(models.Model):
    user = models.OneToOneField(to=User, verbose_name="사용자", on_delete=models.CASCADE, primary_key=True)
    hobby = models.ManyToManyField(to="Hobby", verbose_name="취미", through='UserProfileHobby')
    introduction = models.TextField("소개")
    birthday = models.DateField("생일")
    age = models.IntegerField("나이")

    def __str__(self) -> str:
        return f"{self.user.fullname}님의 프로필입니다."

class Hobby(models.Model):
    name = models.CharField("취미", max_length=50)
    def __str__(self):
        return self.name

class UserProfileHobby(models.Model):
    userprofile = models.ForeignKey(UserProfile, on_delete=models.CASCADE) # UserProfile 처럼 클래스 직접지정 or 스트링으로 테이블지정
    Hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE)