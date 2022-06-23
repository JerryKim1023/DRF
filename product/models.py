from django.db import models

# Create your models here.
class Event(models.Model):
    class Meta:
        db_table = "event"
    # <제목, 썸네일, 설명, 등록일자, 노출 시작 일, 노출 종료일, 활성화 여부>
    title = models.CharField("제목", max_length=50)
    thumbnail = models.ImageField("썸네일", upload_to="product/thumbnail",  height_field=None, width_field=None, max_length=None)
    desc = models.TextField("설명", blank=True)
    created_at = models.DateTimeField("등록일자", auto_now_add=True)
    show_date = models.DateField("노출 시작일", auto_now=False) # 노출 시작 일
    show_expired_date = models.DateField("노출 종료일", (""),auto_now=False, auto_now_add=False) # 노출 종료일

    is_active = models.BooleanField("활성화 여부", default=True)  # 활성화 여부

    def __str__(self):
        return f"{self.title} 이벤트입니다"

    #   django serializer에서 기본적으로 제공하는 
    #   validate / create / update 기능을 사용해 event 테이블의 생성/수정 기능을 구현해주세요
    #1. 전달 받은 데이터는 **kwargs를 사용해 입력해주세요
    #2. postman으로 파일을 업로드 할 때는 raw 대신 form-data를 사용하고, Key type을 File로 설정해주세요
    #4. 등록된 이벤트 중 현재 시간이 노출 시작 일과 노출 종료 일의 사이에 있고, 
    #활성화 여부가 True인 event 쿼리셋을 직렬화 해서 리턴해주는 serializer를 만들어주세요

class Product(models.Model):
    class Meta:
        db_table = "product"
    # <제목, 썸네일, 설명, 등록일자, 노출 시작 일, 노출 종료일, 활성화 여부>
    user = models.ForeignKey("user.User", verbose_name="작성자", on_delete=models.SET_NULL, null=True)
    thumbnail = models.ImageField("썸네일", upload_to="product/thumbnail",  height_field=None, width_field=None, max_length=None)
    desc = models.TextField("설명", blank=True)
    created = models.DateTimeField("등록시간", auto_now_add=True)
    modified = models.DateTimeField("수정시간", auto_now=True)
    show_expired_date = models.DateField("노출 종료일", (""),auto_now=False, auto_now_add=False) # 노출 종료일

    is_active = models.BooleanField("활성화 여부", default=True)  # 활성화 여부
    price = models.IntegerField("가격")

    def __str__(self):
        return f"{self.title} 입니다"

class Review(models.Model):
    class Meta:
        db_table = "review"
    # <작성자, 상품, 내용, 평점, 작성일>
    user = models.ForeignKey("user.User", verbose_name="작성자", on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, verbose_name="상품", on_delete=models.SET_NULL, null=True)
    content = models.TextField("내용", blank=True)
    rating = models.IntegerField("평점", blank=True)
    created = models.DateTimeField("등록시간", auto_now_add=True)


    def __str__(self):
        return f"{self.product} {self.user} 댓글 : {self.content} 입니다"