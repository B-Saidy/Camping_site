from django.shortcuts import render,redirect
from .models import Campground
from django.shortcuts import get_object_or_404
from .forms import UpdateForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType 
from comments.forms import CommentForm
from django.core.paginator import Paginator


def home(request):
    campgrounds = Campground.objects.order_by("-id")
    paginator = Paginator(campgrounds, 6)
    
    page = request.GET.get('page')
    
    camps = paginator.get_page(page)
    context = {
        'camps':camps,
    }    
    return render(request,'campgrounds/index.html', context)
def landing(request):
    return render(request, 'campgrounds/landing.html' )
@login_required
def show(request,camp_id):
    camp = get_object_or_404(Campground, id = camp_id)
    comments = camp.comments  # Comment.objects.filter_by_instance(camp)
    initial_data = {
            'object_id':camp.id,
            'content_type':camp.get_content_type,
            'author': request.user
        }
    form = CommentForm(request.POST or None, initial = initial_data)
    if request.method == "POST":
        if form.is_valid():
            ctype = form.cleaned_data['content_type']
            content_type = ContentType.objects.get(model=ctype)
            object_id = form.cleaned_data['object_id']
            author = form.cleaned_data['author']
            text = form.cleaned_data['text']
            comment=Comment.objects.create(author=author, text = text, object_id = object_id, content_type=content_type) 
            comment.save()
            return redirect('show', camp.id)
        else:
            context = {
            'camp':camp,
            'form':form,
            'comments':comments
            }    
            return render(request,'campgrounds/show.html', context)
    else: 
        context = {
        'camp':camp,
        'form':form,
        'comments':comments
        }    
        return render(request,'campgrounds/show.html', context)
@login_required
def edit(request, camp_id):
    camp = get_object_or_404(Campground, id = camp_id)
    print(request.user, camp.author)
    if str(request.user) == str(camp.author):
        print(request.user, camp.author)
        if request.method =='POST':
            camp = get_object_or_404(Campground, id = camp_id) 
            form = UpdateForm(request.POST, instance=camp)
            if form.is_valid():
                form.save() 
                context = {
                    'camp':camp
                } 
                return redirect('show', camp.id)
        else:
            camp = get_object_or_404(Campground, id = camp_id)
            form = UpdateForm()
            context = {
                'camp':camp,
                'form':form
            }
            return render (request,'campgrounds/edit.html', context)
    else:
        return redirect('show', camp.id)
@login_required
def new(request):
    if request.method=='POST':      
        name = request.POST['name']
        image = request.FILES['image']
        description = request.POST['description']
        price = request.POST['price']
        author = request.POST['author']
        fs=FileSystemStorage()
        fs.save(image.name,image)
        if request.user.is_authenticated:
            author = request.user.username
        camp = Campground.objects.create(name=name,image=image, description=description,price=price, author=author)
        camp.save()
        return redirect('index')
    return render(request, 'campgrounds/new.html')
def delete_comment(request, camp_id):   
    camp = get_object_or_404(Campground, id=camp_id) 
    comments = camp.comments
    if request.method == 'POST':
        comments.filter(author=request.user).delete()
        return redirect('show',camp.id)
            