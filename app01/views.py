from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import models
import utils
# Create your views here.



@login_required
def host(request):
    return render(request, 'host.html')

@login_required
def asset(request):
    return render(request, 'asset.html')

@login_required
def audit(request):
    return render(request, 'audit.html')


def acc_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('password')
        user = authenticate(username=username,password=passwd)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            return render(request,'login.html',{
                'login_err':"Wrong username or password"
            })
    else:
        return render(request, 'login.html')

@login_required
def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def index(request):
    article_list = models.Article.objects.all().order_by('-publish_date')
    paginator = Paginator(article_list, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    return render(request,'index.html',{
        'articles':articles
    })


def article(request, article_id):
    err_msg = ''
    try:
        article_obj = models.Article.objects.get(id=article_id)
        comments = utils.bulid_comments_tree(request)
    except ObjectDoesNotExist,e:
        err_msg = str(e)
    return render(request,'article.html',{
                    'article':article_obj,
                    'err_msg':err_msg,
                    'comments':comments
                  })

def create_article(request):
    if request.method == 'GET':
        return render(request,'create_article.html')
    elif request.method =='POST':
        print render(request,'create_article.html')
        bbs_generator = utils.ArticleGen(request)
        res = bbs_generator.create()
        html_ele = '''Your article <<a href="/article/%s/">%s</a> >
        has been created successfully'''%(res.id,res.title)
        return HttpResponse(html_ele)