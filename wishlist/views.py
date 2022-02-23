from django.shortcuts import render, redirect
from .models import Profile, Wish
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import WishForm
from .models import Wish, Commitment 

# Create your views here.

def home(request):
	return render(request, "wishlist/home.html")


def commitments(request):
	return render(request, "wishlist/commitments.html")


def user_list(request):
	users = Profile.objects.all() # exclude(user=request.user)
	return render(request, "wishlist/user_list.html", {"user_list": users})


def user(request, pk):
	usr = Profile.objects.get(pk=pk)
	return render(request, "wishlist/user.html", {"usr": usr})


def follow(request, pk):
	print(pk)
	f_profile = Profile.objects.get(pk=pk)
	cur_profile = request.user.profile
	print(cur_profile)
	cur_profile.follows.add(f_profile)
	cur_profile.save()
	return render(request, "wishlist/user.html", {"usr": f_profile})


def unfollow(request, pk):
	unf_profile = Profile.objects.get(pk=pk)
	cur_profile = request.user.profile
	cur_profile.follows.remove(unf_profile)
	cur_profile.save()
	return render(request, "wishlist/user.html", {"usr": unf_profile})


def delete_wish(request, pk):
	wish = Wish.objects.get(pk=pk)
	wish.delete()
	return HttpResponseRedirect(reverse("wishlist:home"))


def edit_wish(request, pk):
	messages.info(request, 'Wish has been edited?')
	return HttpResponseRedirect(reverse("wishlist:home"))


def add_wish(request):
	if request.method == "POST":
		wish = Wish(user=request.user)
		form = WishForm(request.POST, instance=wish)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/home/")
	else:
		form = WishForm()

	return render(request, "wishlist/form.html", {"form": form})


def change_wish_status(request, pk):
	wish = Wish.objects.get(pk=pk)
	commitment = Commitment.objects.get(wish=wish)
	print(commitment)
	wish.has_commitment = False
	wish.save()
	commitment.delete()
	return HttpResponseRedirect(reverse("wishlist:commitments"))


def add_commitments(request, pk):
	wish = Wish.objects.get(pk=pk)
	commitment = Commitment(user=request.user, wish=wish)
	commitment.save()
	wish.has_commitment = True
	wish.save()
	return HttpResponseRedirect(reverse("wishlist:commitments"))