from django.db import models

# Create your models here.
class Event(models.Model):
    class Meta:
        db_table = "event"
    # <제목, 썸네일, 설명, 등록일자, 노출 시작 일, 노출 종료일, 활성화 여부>
    title = models.CharField("제목", max_length=50) # 제목
    thumbnail = models.ImageField("썸네일", upload_to="product/thumbnail", height_field='500') # 썸네일
    desc = models.TextField("설명", blank=True, null=True) # 설명
    created_at = models.DateTimeField("등록일자", auto_now_add=True) # 등록일자
    show_date = models.DateField("노출 시작일", auto_now=True) # 노출 시작 일
    show_expired_date = models.DateField("노출 종료일", (""),auto_now=False, auto_now_add=False) # 노출 종료일

    is_active = models.BooleanField(default=True)  # 활성화 여부

    def __str__(self):
        return self.title

    #   django serializer에서 기본적으로 제공하는 
    #   validate / create / update 기능을 사용해 event 테이블의 생성/수정 기능을 구현해주세요
    #1. 전달 받은 데이터는 **kwargs를 사용해 입력해주세요
    #2. postman으로 파일을 업로드 할 때는 raw 대신 form-data를 사용하고, Key type을 File로 설정해주세요
    #4. 등록된 이벤트 중 현재 시간이 노출 시작 일과 노출 종료 일의 사이에 있고, 
    #활성화 여부가 True인 event 쿼리셋을 직렬화 해서 리턴해주는 serializer를 만들어주세요