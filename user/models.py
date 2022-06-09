from django.db import models

# Create your models here.
# models.py
class User(models.Model):
    username = models.CharField("사용자 계정", max_length=20, unique=True)
    email = models.EmailField("이메일 주소", max_length=100, unique=True)
    password = models.CharField("비밀번호", max_length=60)
    fullname = models.CharField("이름", max_length=20)
    join_date = models.DateTimeField("가입일", auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(to=User, verbose_name="사용자", on_delete=models.CASCADE)
    hobby = models.ManyToManyField(to="Hobby", verbose_name="취미")
    introduction = models.TextField("소개")
    birthday = models.DateField("생일")
    age = models.IntegerField("나이")

class Hobby(models.Model):
    name = models.CharField("취미", max_length=50)