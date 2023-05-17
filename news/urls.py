from django.urls import path
from pages.views import home_view,PostCreate,PostDelete,PostDetail,PostList,PostUpdate,UserPostList

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('user/<str:username>/', UserPostList.as_view(), name='user-post-list'),
    path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post-update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post-delete'),
    path('create/', PostCreate.as_view(), name= 'post-create'),
    ]