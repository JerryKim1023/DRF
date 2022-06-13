from blog.models import Article


def create_article(title, user_id, content, category, img):
        return Article.objects.create(title=title, user=user_id, content=content, category=category, img=img)