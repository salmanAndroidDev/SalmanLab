from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # path('', views.post_list, name='post_list'), #..... function-based view ref
    # Nice trick to make SEO-Friendly url
    # path('<int:day>/<int:month>/<int:year>/<slug:post>/',
    #      views.post_detail, name='post_detail'),
    path('', views.PostListView.as_view(),
         name='post_list'),  # class-based view ref
    path('<int:day>/<int:month>/<int:year>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    path('<int:post_id>/share/', views.post_share_by_email,
         name='post_share_by_email'),

]
