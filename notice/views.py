from django.shortcuts import render, redirect
# class를 불러올 때 편의 상
from .models import Notice
from django.core.paginator import Paginator
from .customPager import CustomPager

# Create your views here.
def delete(request, num) :
    notice = Notice(num=num)
    notice.delete()
    return redirect("notice:list")

def update(request, num) :
    if request.method=='POST':
        notice = Notice.objects.get(pk=num)
        notice.title=request.POST['title']
        notice.contents=request.POST['contents']
        notice.save()
        return redirect("notice:list")
    else :
        notice = Notice.objects.get(pk=num)
        context = {"vo":notice, "board":"NoticeUpdate"}
        return render(request, 'notice/write.html', context)

def select(request, num=1) :
    notice = Notice.objects.get(pk=num)
    context = {"vo":notice,"board":"NoticeSelect",}
    return render(request, 'notice/select.html',context)

def write(request) :
    if request.method=='POST':
        #                                       POST로 title이라는 변수를 받아온다
        notice =  Notice(title=request.POST['title'], writer=request.POST['writer'], contents=request.POST['contents'])
        notice.save()
        return redirect("/notice/noticeList")
    else :
        print("Write Form")
        return render(request, 'notice/write.html', {"board":"NoticeWrite"})


#                               default=1로 설정
def list(request, page=1, kind="title", search="") :
    # QuerySet
    # select * from notice_notice
    # notice = Notice.objects.all()
    # select * from notice_notice order by num desc
    # notice = Notice.objects.order_by("-num")

    # slicing ------------------------------------------------------------------
    # start = (page-1)*2
    # last = (page)*2
    # select * from notice_notice order by num desc index 0번 부터 2번 전까지 가져오기
    # notice = Notice.objects.order_by("-num")[start:last]

    # Paginator --------------------------------------------------------------
    # notice = Notice.objects.order_by("-num")
    # Paginator(QuerySet, 가져올 페이지 수)
    # notice = Paginator(notice, 2)
    # 실제 조회
    # notice = notice.get_page(page)

    # CustomPager ----------------------------------------------------------
    customPager = CustomPager(page, kind, search) 

    notice = Notice.objects.order_by("-num")
    notice = Paginator(notice, 2)
    
    customPager.makePage(notice.num_pages)

    notice = notice.get_page(customPager.page)

    context = {"board":"NoticeList", "list":notice,"pager":customPager,}
    return render(request, 'notice/list.html',context)