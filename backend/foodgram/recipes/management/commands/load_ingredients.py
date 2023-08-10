import json

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Loading data from csv to database.'

    def handle(self, *args, **kwargs):
        try:
            with open(
                    'recipes/data/ingredients.json', 'r',
                    encoding='UTF-8'
            ) as ingredients:
                ingredient_data = json.loads(ingredients.read())
                for ingredients in ingredient_data:
                    Ingredient.objects.get_or_create(**ingredients)
            self.stdout.write(self.style.SUCCESS('Данные загружены'))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR('Файл не найден'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Произошла ошибка: {e}'))
