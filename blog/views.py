from django.shortcuts import render
from django.views import View

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status

from blog.models import Article
from blog.serializers import AticleSerializer
from blog.services import create_article
from user.models import User
from user.serializers import UserSerializer

# Create your views here.


class ArticleApiView(APIView):
    #해당 user의 정보를 가져옴 (나중에 user 변수를 가져다 쓰면 됨.)
    #유저의 글 정보를 가져옴.
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        user = request.user
        user_number2 = User.objects.get(id=2)
        user_article = Article.objects.filter(user=user_number2)
        print('@@@@@@@@@@@@@@@@@')
        print(type(user_number2)) # 오브젝트
        print(type(user_article)) # 쿼리셋
        print('@@@@@@@@@@@@@@@@@')
        
        # serializer에 queryset을 인자로 줄 경우 many=True 옵션을 사용해야 한다.
        serialized_article_data = AticleSerializer(user_article, many=True).data
        serialized_user_data = UserSerializer(user_number2).data
        return Response(serialized_user_data, serialized_article_data, status=status.HTTP_200_OK)

        # return data
        """
        {
            "username": "user",
            "password": "pbkdf2_sha256$320000$u5YnmKo9luab9csqWpzRsa$pKfqHnBiF5Rgdo1Mj9nxNOdhpAl9AhPVXFPXkbPz7Mg=",
            "fullname": "user's name",
            "email": "user@email.com"
        }
        """

class ArticleView(View):
    # def get(self, request, pk): #ListUser 쪽 거 옮겨와서 다시 만들기
    #     article_id = pk
    #     all_articles = read_all_article()[:8]
    #     recent_comments = read_all_comment()[:5]
    #     check_bookmark = bookmark_check(request.user.id, article_id)

    #     like_cnt = Article.objects.get(pk=article_id)

    #     try:
    #         ip = get_client_ip(request)

    #         target_article = hit_article(ip, pk)
    #         best_comment = read_best_comment()


    #         target_comment = read_target_article_comment(article_id)

    #         try:
    #             like_article = ArticleLikes.objects.filter(article=article_id, user=request.user.id).get()


    #             return render(request, 'articleapp/article_detail.html',
    #                           {'target_article': target_article,
    #                            'target_comment': target_comment, 'best_comment': best_comment,
    #                            'left_content_articles': all_articles, 'left_content_recent_comments': recent_comments,
    #                            'like_article': like_article, 'check_bookmark': check_bookmark, 'like_cnt': like_cnt},
    #                           status=200)
    #         # 좋아요가 없을 때
    #         except ObjectDoesNotExist:

    #             return render(request, 'articleapp/article_detail.html',
    #                           {'target_article': target_article,
    #                            'left_content_articles': all_articles, 'left_content_recent_comments': recent_comments,
    #                            'best_comment': best_comment,
    #                            'target_comment': target_comment, 'check_bookmark': check_bookmark,
    #                            'like_cnt': like_cnt}, status=200)

    #     except ObjectDoesNotExist:
    #         return JsonResponse({'msg': "게시글이 존재하지 않습니다."}, status=404)
    permissions = [
            ('signup_three_days_permission')
        ]

    def post(self, request):
        try:
            create_article(title=request.POST.get('title'),
                           user_id=request.user,
                           content=request.POST.get('content'),
                           category=request.POST.get('category') )
                           #    img=request.POST.get('img', '')                       
            return Response({'result': '게시글이 생성 되었습니다.'}, status=status.HTTP_200_OK)

        except TypeError:
            return Response({'msg': "항목을 다시 확인 해 주세요."}, status=status.HTTP_404_NOT_FOUND)

    # def patch(self, request, article_id):
    #     target_article = read_target_article(article_id)
    #     if request.user == target_article.user:
    #         try:
    #             update_article(request.PATCH.get('content'))
    #             return JsonResponse({'result': '게시글이 수정 되었습니다.'}, status=200)
    #         except ObjectDoesNotExist:
    #             return JsonResponse({'result': '게시글이 존재하지 않습니다.'}, status=404)

    # def delete(self, request, pk):
    #     try:
    #         delete_article(pk)
    #         return JsonResponse({'result': '게시글이 삭제되었습니다.'}, status=200)

    #     except ObjectDoesNotExist:
    #         return JsonResponse({'result': '게시글이 존재하지 않습니다.'}, status=404)