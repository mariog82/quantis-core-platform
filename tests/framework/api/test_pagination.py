from framework.api import Page, Pagination


def test_pagination_offset():
    pagination = Pagination(page=3, size=10)

    assert pagination.offset == 20


def test_page_model():
    page = Page(items=[1, 2], pagination=Pagination(page=1, size=2, total=2))

    assert page.items == [1, 2]
    assert page.pagination.total == 2
