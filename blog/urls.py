from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # 글 목록 조회
    path("", views.Index.as_view(), name='list'),
    # 글 상세 조회
    path("<int:pk>/", views.DetailView.as_view(), name='detail'),
    # 글 작성
    path("write/", views.Write.as_view(), name='write'),
    # 글 수정
    path("edit/<int:pk>/", views.Update.as_view(), name='edit'),
    # 글 삭제
    path("delete/<int:pk>/", views.Delete.as_view(), name='delete'),
    # 검색
    path("search/<str:tag>/", views.Search.as_view(), name='search'),
]