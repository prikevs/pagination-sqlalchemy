from .paginator import Paginator
from .paginate import Pagination

def pager(query, page, per_page):
    paginator = Paginator(query, per_page)
    return Pagination(paginator, page, per_page, paginator.total_pages, paginator.page(page).object_list)

