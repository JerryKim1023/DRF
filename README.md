# DRF
DRF study and try!

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
-->> ListUsers class에 로그인한 사용자만 조회하는 함수 생성 / user쪽에다 만들었는데 blog 쪽으로 수정해야함.
12. views.py에 <글 제목, 카테고리, 글 내용>을 입력받아 게시글을 작성해주는 기능을 만들어주세요
    - 게시글은 계정 생성 후 3일 이상 지난 사용자만 생성할 수 있도록 권한을 설정해주세요
    - 테스트 코드에서는 계정 생성 후 3분 이상 지난 사용자는 게시글을 작성할 수 있도록 해주세요
<br>
-->> 처음부터 못 하겠어서 보고서 붙여넣고 따라하면서 만든거라... 다시 복습을 열심히 하겠습니다.

## 6월8일
1. OneToOneField는 unique함을 가진다. CASCADE / ManyToManyField의 활용

2. FBV, CBV 요청응답을 받을 때 예를 들어  GET,POSTmPUT,DELETE 네가지의 요청이 있을 때 CBV는 class를 만들어서 한번에 대응이 가능한 장점이 있다. / CBV를 사용해 views.py 구성해보기

3. custom user psermission을 활용해 내가 원하는 대로 권한 바꿔보기

## 6월7일
DRF 설치 및 사용 / PostMan 사용해서 요청응답 받기 / 미션 : [mutable,immutable이란?](https://velog.io/@ecec1023/mutable-immutable) / [PostMan 사용해서 json으로 message : success 띄우기](https://velog.io/@ecec1023/DRF-%EC%84%A4%EC%B9%98%ED%95%98%EA%B3%A0-POST-MAN%EC%9C%BC%EB%A1%9C-JsonResponse-%EB%B0%9B%EA%B8%B0)
