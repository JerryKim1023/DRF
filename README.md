# DRF
DRF study and try!
### ai / (각 앱이 어떤 역할을 하는지, 그 안에는 뭐가 있는지)
 - AI
    - 프로젝트 이름 및 settings.py가 있는 핵심 패키지폴더
 - api(app)
    - DRF 공식문서 보고 연습해 봄. / rest_framework의 decorators 활용해서 api_view GET,POST,DELETE 통신 및 serializer 간단하게 사용
 - blog(app)
    - 카테고리, 게시물, 코멘트 기능 구현 
 - product(app)
    - event모델을 통해 상품, 리뷰 구현
 - user(app)
    - user에 관한 앱으로 auth기능을 담아 user를 커스텀하였음.
    - rest_framework.exceptions의 APIException을 활용해서 로그인하지 않은 사용자에 대한 제재를 추가함.(로그인 한 유저,관리자만 권한을 return True를 반환하게함)
    -  / serializer 활용하여 추가 기능구현 계획 중

## 6/17 과제

1. product 앱에서 <작성자, 썸네일, 상품 설명, 등록일자, 노출 종료 일자, 가격, 수정 일자, 활성화 여부>가 포함된 product 테이블을 생성해주세요
-> product.models.py
2. django serializer를 사용해 validate / create / update 하는 기능을 구현해주세요
    1. custom validation 기능을 사용해 노출 종료 일자가 현재보다 더 이전 시점이라면 상품을 등록할 수 없도록 해주세요
    -> eventserializer의 값을 어떻게 담아서 노출종료 일자를 담아야할지 모르겟음.. 계속 빈 쿼리셋값만 담김.
    2. custom creator 기능을 사용해 상품 설명의 마지막에 “<등록 일자>에 등록된 상품입니다.” 라는 문구를 추가해주세요
    -> 상품설명 커스텀을 잘 모르겟음...
    3. custom update 기능을 사용해 상품이 update 됐을 때 상품 설명의 가장 첫줄에 “<수정 일자>에 수정되었습니다.” 라는 문구를 추가해주세요
    -> 상품 설명으로 진입을 어떻게 함?? 2번이랑 같은 맥락인데.. 
3. product 앱에서 <작성자, 상품, 내용, 평점, 작성일>을 담고 있는 review 테이블을 만들어주세요
-> product = models.ForeignKey("상품", Event, on_delete=models.CASCADE)
TypeError: __init__() got multiple values for argument 'on_delete' ??
모델 설정부터.. 잘 모르겠음;;
4. 현재 날짜를 기준으로, 노출 종료 날짜가 지나지 않았고 활성화 여부가 True이거나 로그인 한 사용자가 등록 한 상품들의 정보를 serializer를 사용해 리턴해주세요
-> 시리얼라이저를 활용해 리턴?? Q를 view가 아닌 시리얼라이저 어느 위치에 써야함??
5. 4번 상품 정보를 리턴 할 때 상품에 달린 review와 평균 점수를 함께 리턴해주세요
    1. 평균 점수는 (리뷰 평점의 합/리뷰 갯수)로 구해주세요
    -> values로 가져오려는데 review모델 생성이 에러떠서 가져오는 게 안 되서 값을 못 찍어봐서... 못하겠음;;
    2. 작성 된 리뷰는 모두 return하는 것이 아닌, 가장 최근 리뷰 1개만 리턴해주세요
    -> ?? 기본기부터 다시 봐야할듯... 정리가 안됨..
6. 로그인 하지 않은 사용자는 상품 조회만 가능하고, 회원가입 이후 3일 이상 지난 사용자만 상품을 등록 할 수 있도록 권한을 설정해주세요
-> permission class 설정

## 6/15 과제

1. product라는 앱을 새로 생성해주세요
-> 생성 후 등록완료
2. product 앱에서 <제목, 썸네일, 설명, 등록일자, 노출 시작 일, 노출 종료일, 활성화 여부>가 포함된 event 테이블을 생성해주세요
-> models.py에서 생성 완료
3. django serializer에서 기본적으로 제공하는 validate / create / update 기능을 사용해 event 테이블의 생성/수정 기능을 구현해주세요
    1. 전달 받은 데이터는 **kwargs를 사용해 입력해주세요
    -> 필요없는 사항이라고 전달 받음. 그래도 **kwargs는 따로 공부하기!
    2. postman으로 파일을 업로드 할 때는 raw 대신 form-data를 사용하고, Key type을 File로 설정해주세요
    -> 설정 완료
4. 등록된 이벤트 중 현재 시간이 노출 시작 일과 노출 종료 일의 사이에 있고, 활성화 여부가 True인 event 쿼리셋을 직렬화 해서 리턴해주는 serializer를 만들어주세요
-> serializer를 만들어주세요 인데 뷰에서 처리하는 게 맞음?? serializer에서 뭔가 처리하란 소리 아니었음??

## 6/13 과제

1. blog 앱에 <게시글, 작성자, 작성 시간, 내용>이 포함된 comment라는 테이블을 추가해주세요
    1. 게시글과 작성자는 fk 필드로 생성해주셔야 해요
   -> blog 앱의 models.py에 추가
2. Django Serializer 기능을 사용해 로그인 한 사용자의 기본 정보들을 response data에 넣어서 return 해주세요
   -> user 앱의 views.py에 class UserApiView(APIView)
3. 사용자가 작성 한 게시글을 로그인 한 (2번)User의 serializer data에 포함시켜서 같이 return해주세요
   -> blog 앱의 views.py에 class ArticleApiView(APIView)

## 6월10일 / *참고* 아래 과제는 CBV 기반으로 수행

1. Django 프로젝트를 생성하고, user 라는 앱을 만들어서 settings.py 에 등록해보세요.<br>
-->> 앱 생성 후 INSTALLED_APPS에 추가
2. user/models.py에 `Custom user model`을 생성한 후 django에서 user table을 생성 한 모델로 사용할 수 있도록 설정해주세요<br>
-->> AbstractBaseUser 상속 받아서 User 사용
3. user/models.py에 사용자의 상세 정보를 저장할 수 있는 `UserProfile` 이라는 모델을 생성해주세요<br>
-->> User 와 OneToOneField 로 생성
4. blog라는 앱을 만든 후 settings.py에 등록해주세요
-->> 앱 생성 후 INSTALLED_APPS에 추가
5. blog/models.py에 <카테고리 이름, 설명>이 들어갈 수 있는 `Category`라는 모델을 만들어보세요.<br>
-->> <span style='background-color:yellow'>name, description 필드 두개 넣어서 생성</span>
6. blog/models.py에 <글 작성자, 글 제목, 카테고리, 글 내용>이 들어갈 수 있는 `Article` 이라는 모델을 만들어보세요.(카테고리는 2개 이상 선택할 수 있어야 해요)<br>
-->> <span style='background-color:orange'>카테고리는 2개이상선택? 이랑 매니투매니필드 활용 시 through 활용해서 쓰는 게 헷갈림.</span>
7. Article 모델에서 외래 키를 활용해서 작성자와 카테고리의 관계를 맺어주세요<br>
-->> User를 포린키로 걸음
8. admin.py에 만들었던 모델들을 추가해 사용자와 게시글을 자유롭게 생성, 수정 할 수 있도록 설정해주세요<br>
-->> 추가는 했는데 migrate 후에 체크해봐야함.
9. admin 페이지에서 사용자, 카테고리, 게시글을 자유롭게 추가해주세요<br>
-->> migrate 후 체크 요망
10. views.py에 username, password를 받아 로그인 할 수 있는 기능을 만들어주세요
    - 로그인 기능 구현이 처음이시라면 3일차 강의자료 5번 항목을 확인해주세요<br>
-->> 로그인 기능에 임시로 class view에 signup도 껴놓음. / login은 post로 받고 sign up은 get 요청으로 받고 싶은데 APIView에서 어떻게 구분??
11. views.py에 로그인 한 사용자의 정보, 게시글을 보여주는 기능을 만들어주세요<br>
-->> class UserApiView(APIView) 에 get 함수로 구현해놓음
12. views.py에 <글 제목, 카테고리, 글 내용>을 입력받아 게시글을 작성해주는 기능을 만들어주세요
    - 게시글은 계정 생성 후 3일 이상 지난 사용자만 생성할 수 있도록 권한을 설정해주세요
    - 테스트 코드에서는 계정 생성 후 3분 이상 지난 사용자는 게시글을 작성할 수 있도록 해주세요
<br>
-->> blog views.py 에서 permission classes 생성

## 6월8일
1. OneToOneField는 unique함을 가진다. CASCADE / ManyToManyField의 활용

2. FBV, CBV 요청응답을 받을 때 예를 들어  GET,POSTmPUT,DELETE 네가지의 요청이 있을 때 CBV는 class를 만들어서 한번에 대응이 가능한 장점이 있다. / CBV를 사용해 views.py 구성해보기

3. custom user psermission을 활용해 내가 원하는 대로 권한 바꿔보기

## 6월7일
DRF 설치 및 사용 / PostMan 사용해서 요청응답 받기 / 미션 : [mutable,immutable이란?](https://velog.io/@ecec1023/mutable-immutable) / [PostMan 사용해서 json으로 message : success 띄우기](https://velog.io/@ecec1023/DRF-%EC%84%A4%EC%B9%98%ED%95%98%EA%B3%A0-POST-MAN%EC%9C%BC%EB%A1%9C-JsonResponse-%EB%B0%9B%EA%B8%B0)
