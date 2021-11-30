from django.shortcuts import redirect, render
from django.http import HttpResponse, response, StreamingHttpResponse
from django.core.mail import send_mail
from django.conf import settings
from wsgiref.util import FileWrapper
from .models import Services,Post,Tag, Project
from .utils import searchProjects
import mimetypes
import os

# Create your views here.
def home(request):
    services = Services.objects.all()
    context = {'services':services}
    return render(request,'base/index.html',context)

def portfolio(request):
    projects = searchProjects(request)
    tags = Tag.objects.all()
    context={'projects':projects,'tags':tags}
    return render(request, 'base/portfolio.html', context)

def about(request):
    context = {}
    return render(request,'base/about.html', context)

def contact(request):

    if request.method == 'POST':
        print('The request is a post')
        subject = 'PERSONAL SITE INQUIRY'
        body = {
            'name': request.POST['name'],
            'email': request.POST['from_email'],
            'message': request.POST['message'],
        }
        message = "\n".join(body.values())
        try:
            print('Trying sending')
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                ['mufasadev@zohomail.com'],
                fail_silently=False,
            )
        except response.BadHeaderError:
            return HttpResponse('Invalid Header Found!')
        return redirect('contact')

    return render(request,'base/contact.html',{})
   

def services(request,pk):
    # url can be used to for both services and Projects hence the try catch block
    try:
        service = Services.objects.get(slug=pk)
        context = {'service':service}
    except:
        project = Project.objects.get(slug=pk)
        context = {'project':project}
    return render(request,'base/services.html', context)

def downloadfile(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'TyroneZekaCV.pdf'
    filepath = base_dir + '/static/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile,'rb'),chunk_size),content_type=mimetypes.guess_type(thefile)[0])
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "Attachment;filename=%s" % filename

    return response

def blog(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'base/blog.html',context)

def blogpost(request,slug):
    post = Post.objects.get(slug=slug)
    tags = Tag.objects.all()
    context = {'post':post,'tags':tags}
    return render(request,'base/post.html',context)