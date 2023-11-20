from django.urls import path
from .views import PostsList, PostDetail, SearchPostList, PostCreate, PostUpdate, PostDelete, ArticleCreate, \
   ArticleUpdate, ArticleDelete

urlpatterns = [
   path('news/', PostsList.as_view(), name='news'),
   path('news/<int:pk>', PostDetail.as_view(), name='new'),
   path('news/search', SearchPostList.as_view(), name='news_search'),
   path('news/create', PostCreate.as_view(), name='news_create'),
   path('news/<int:pk>/update', PostUpdate.as_view(), name='news_update'),
   path('news/<int:pk>/delete', PostDelete.as_view(), name='news_delete'),
   path('article/create', ArticleCreate.as_view(), name='article_create'),
   path('article/<int:pk>/update', ArticleUpdate.as_view(), name='article_update'),
   path('article/<int:pk>/delete', ArticleDelete.as_view(), name='article_delete')
]