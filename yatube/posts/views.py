from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def group_posts(request):
    return HttpResponse('Список постов')


def post_detail(request, pk):
    return HttpResponse(f'Пост номер {pk}')