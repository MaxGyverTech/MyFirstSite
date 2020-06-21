from django.shortcuts import render
# Create your views here.
from .forms import PostForm
from .models import Post,Curse,CurseBuy,Lesson,Nofication,Comment,CommentReply,CurseLandingAsk,CurseLanding
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required



def haveCursePerm(requests,curse_id):
    my_curses_buys = CurseBuy.objects.filter(buyer=requests.user)
    my_curses = []
    for i in range(len(my_curses_buys) - 1):
        my_curses.append(my_curses_buys[i].parent)
    my_curses_ids = []
    for i in my_curses:
        my_curses_ids.append(i.curse_id)
    if curse_id in my_curses_ids:
        return True
    else:
        return False

def nofication(requests,text):
    user = requests.user
    #nof = Nofication(nof_user=requests.user,nof_date=timezone.now(),nof_email=user.email,nof_username=user.username,nof_text=text)
    nof = Nofication(nof_user=requests.user, nof_date=timezone.now(), nof_text=text)
    print(nof)
    nof.save()

def returnid():
    try:
        id = Comment.objects.order_by('comment_id')[(len(Comment.objects.all()) - 1)].id
    except IndexError:
        return 0
    except AssertionError:
        return 0
    else:
        return id

def index(requests):
    posts = Post.objects.all()
    return render(requests, 'posts/index.html', {'posts':posts})

def send(requests):
    posts = Post.objects.all()
    if requests.method == 'POST':
        print(requests.POST)
        a = Post(post_name=requests.POST['post_name'],post_text=requests.POST['post_text'],post_pubdate=timezone.now())
        a.save()
    return HttpResponseRedirect(reverse('index'))

def singup(requests):
    iserr = int(requests.GET.get('err',0))
    return render(requests, 'registration/registration.html',{'err':iserr})


def saveuser(requests):
    if requests.method == 'POST':
        if len(requests.POST['password']) >= 8:
            print(requests.POST)
            newuser = User(username=requests.POST['username'], email=requests.POST['email'],password=requests.POST['password'])
            newuser.save()
            login(requests, newuser)
            nofication(requests,'Зарегистрировался')
            return HttpResponseRedirect(reverse('index'))
        else:
            link = '/singup?err=1'
            return HttpResponseRedirect(link)

def test(requests):
    return HttpResponse(requests.META['HTTP_USER_AGENT'])

def shop(requests):
    curses = Curse.objects.all()
    return render(requests,'posts/shop.html',{'curses':curses})

def curselanding(requests,shop_id):
    curse = Curse.objects.filter(curse_id=shop_id)[0]
    landing = CurseLanding.objects.filter(parent=curse)[0]
    asks = CurseLandingAsk.objects.filter(parent=landing)[0]
    return render(requests, 'posts/landing.html', {'curse': curse,'landing':landing,'asks':asks})


@login_required
def shop_buy(requests,shop_id):
    print(Curse.objects.filter(curse_id=shop_id))
    a = CurseBuy(buyer=requests.user, parent=Curse.objects.filter(curse_id=shop_id)[0])
    a.save()
    nofication(requests, 'Кто то купил курс '+str(a.parent))
    return HttpResponseRedirect(reverse('profile'))

@login_required
def profile(requests):
    my_curses_buys = CurseBuy.objects.filter(buyer=requests.user)
    my_curses = []
    for i in range(len(my_curses_buys)-1):
        my_curses.append(my_curses_buys[i].parent)
    return render(requests,'posts/profile.html',{'my_curses':my_curses})

@login_required
def current_curse(requests,curse_id):
    if haveCursePerm(requests,curse_id):
        curse = Curse.objects.filter(curse_id=curse_id)[0]
        lessons = Lesson.objects.filter(curse=curse)
        return render(requests, 'posts/current_curse.html', {'curse': curse, 'lessons': lessons})
    else:
        return HttpResponse('У вас нет доступа к этой странице!\nУбедитесь что вы приобрели курс и/или вошли в нужный аккаунт')

@login_required
def current_lesson(requests,curse_id,les_id):
    if haveCursePerm(requests, curse_id):
        curse = Curse.objects.filter(curse_id=curse_id)[0]
        lesson = Lesson.objects.filter(les_id=les_id)[0]
        comments = Comment.objects.filter(lesson=lesson)
        commentsreplys = []
        for comment in comments:
             commentsreplys += CommentReply.objects.filter(pr_comment=comment)
        return render(requests, 'posts/current_lesson.html', {'curse': curse, 'lesson': lesson,'comments':comments,'replys':commentsreplys})
    else:
        return HttpResponse('У вас нет доступа к этой странице!\nУбедитесь что вы приобрели курс и/или вошли в нужный аккаунт')

@login_required
def new_comm(requests,curse_id,les_id):
    if haveCursePerm(requests, curse_id):
        prevCom = returnid()
        comm = Comment(commenter=requests.user, datetime=timezone.now(),com_text=requests.POST['com_txt'],lesson=Lesson.objects.filter(les_id=les_id)[0],comment_id=prevCom+1)
        comm.save()
        nofication(requests,'Новый комент!: '+ comm.commenter.username + ': '+ comm.com_text)
        return HttpResponseRedirect(reverse('current_lesson',args=(curse_id,les_id)))
    else:
        return HttpResponse('У вас нет доступа к этой странице!\nУбедитесь что вы приобрели курс и/или вошли в нужный аккаунт')

@login_required
def new_reply(requests,curse_id,les_id,com_id):
    if haveCursePerm(requests, curse_id):
        comm = CommentReply(commenter=requests.user, datetime=timezone.now(), com_text=requests.POST['reply_txt'],lesson=Lesson.objects.filter(les_id=les_id)[0], pr_comment=Comment.objects.filter(comment_id=com_id)[0])
        comm.save()
        nofication(requests, 'Новый ответ на комент! ' + comm.commenter.username + ': '+ comm.com_text)
        return HttpResponseRedirect(reverse('current_lesson', args=(curse_id, les_id)))
    else:
        return HttpResponse(
            'У вас нет доступа к этой странице!\nУбедитесь что вы приобрели курс и/или вошли в нужный аккаунт')



'''''
@login_required
def lol(requests,curse_id,les_id):
    if haveCursePerm(requests, curse_id):
        pass
    else:
        return HttpResponse('У вас нет доступа к этой странице!\nУбедитесь что вы приобрели курс и/или вошли в нужный аккаунт')
'''''

