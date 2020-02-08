from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from campgrounds.models import Campground
from django.contrib.auth.models import User
from .models import Comment
from django.contrib.contenttypes.models import ContentType
from .forms import CommentForm


def new_comment(request,camp_id):
    camp = get_object_or_404(Campground, id=camp_id)
    context = {
        'camp':camp,
        'title':'Comment'
    }
    return render(request, 'comments/new.html',context)

def edit_comment(request):
    return render(request, 'comments/edit.html')