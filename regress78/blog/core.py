from django.core.paginator import Paginator
from django.conf import settings
from blog.models import TopMenu


def fetch_menu():
    return TopMenu.objects.filter(parent__isnull=True).order_by('order')


def paged(prepared_data, c_page):
    """
    :param prepared_data: data to paginate
    :param c_page: current page number
    :return: django.core.paginator.Paginator
    """
    p = Paginator(prepared_data, settings.BLOG_TOPICS_PER_PAGE)
    return p.page(c_page), p

