
from django.core.management import BaseCommand
from blogapp.models import Article


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Start add articles")
        info = []
        for i in range(3000):
            info.append(f'Article_{i}')

        articles = [
            Article(title=title, content='Статья...', category_id=1, author_id=1, pub_date='2020-04-23 12:30:30')
            for title in info
        ]
        Article.objects.bulk_create(articles)

        self.stdout.write("Done")
