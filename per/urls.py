from django.urls import path
from per import views
urlpatterns = [
    path('', views.home, name="home"),
    path('blogs', views.blogs, name="blogs"),
    path('add_post', views.add_post, name="add_post"),
    path('show_post/<post_id>', views.show_post, name="show_post"),
    path('update_post/<post_id>', views.update_post, name="update_post"),
    path('edit_about', views.edit_about, name="edit_about"),
    path('delete_post/<post_id>', views.delete_post, name="delete_post"),
]
