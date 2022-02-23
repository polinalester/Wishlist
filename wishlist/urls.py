from django.urls import path
from .views import home, user_list, user, follow, unfollow, delete_wish, edit_wish, \
add_wish, commitments, change_wish_status, add_commitments

app_name = "wishlist"

urlpatterns = [
	path("", home, name="home"),
	path("users/", user_list, name="user_list"),
	path("user/<int:pk>", user, name="user"),
	path("follow/<int:pk>", follow, name="follow"),
	path("unfollow/<int:pk>", unfollow, name="unfollow"),
	path("delete/<int:pk>", delete_wish, name="delete_wish"),
	path("edit/<int:pk>", edit_wish, name="edit_wish"),
	path("add/", add_wish, name="add_wish"),
	path("commitments/", commitments, name="commitments"),
	path("changestatus/<int:pk>", change_wish_status, name="change_wish_status"),
	path("addcommitments/<int:pk>", add_commitments, name="add_commitments")
]