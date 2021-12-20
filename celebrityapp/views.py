from django.shortcuts import render,redirect
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from allauth.account.adapter import DefaultAccountAdapter
from django.core.mail import EmailMessage,send_mail
from django.views.generic import View
from django.utils import timezone
from django.contrib import messages
from.form import  *

from django.views.decorators import gzip
from django.http import StreamingHttpResponse
#import cv2
import threading

# Create your views here.

from allauth.account.views import SignupView
from django.db.models.signals import post_save

class CustomAllauthAdapter(DefaultAccountAdapter):
    def send_mail(self,template_prefix,email,context):
        account_confirm_email = 'accounts/confirm-email/'
        context['activate_url'] = (
            settings.BASE_URL + account_confirm_email + context['key']
        )
        msg = self.render_mail(template_prefix,email,context)
        msg.send()

class AccountSignupView(SignupView):
    # Signup View extended
    success_url = 'celebrityapp:accounts_login'
    # change template's name and path
    template_name = "account/login.html"


 # django Signal
    def create_customer(sender,instance, created, **kwargs):

        if created:
            if kwargs:
                print(kwargs)


            c = Customer.objects.create(user=instance,name=instance.username)
            print('customer created')


    post_save.connect(create_customer, sender=User)



account_signup_view = AccountSignupView



def error_404_view(request,exception):
    context = {}
    return render(request,'account/404.html',context)



def home_view(request):
    image = Images.objects.all()
    teams = Team.objects.all()
    context = {'image':image,
               'teams':teams,
               }
    return render(request, 'account/base.html', context)


class jview(View):
    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('account_login')
        posts = Posts.objects.all()
        comments = Comments.objects.all()
        form = create_post(request.POST,request.FILES)
        context = {'form':form,'posts':posts,'comments':comments}
        return render(request, 'bbbootstrap-snippett.html' , context)

    def post(self,request,*args,**kwargs):

        if not self.request.user.is_authenticated:
            return redirect('account_login')
        posts = Posts.objects.all()
        comments = Comments.objects.all()
        t = request.POST.get('details')
        post_id = request.POST.get('idd')
        file_field =  request.FILES.getlist('filefield')
        print('filefield',file_field)
        print(t)
        print("lll",post_id)
        print(request.FILES)
        #for i in file_field:
        create_comment = Comments.objects.create(comment_text=t,
                                                 customer_id=request.user.customer.id,
                                                 posts_id=post_id,
                                                 filefield=file_field)

        create_reply = Replies.objects.create()

        #comments_for_reply = Comments.objects.filter(posts_id=post_id.id)
        #print(comments_for_reply[0].filefield.url)
        #reply = Replies.objects.filter(comments_id=comments_for_reply.id)
#        #print(reply)
        form = create_post(request.POST,request.FILES)

        context = {'form': form, 'posts': posts, 'comments': comments}

        return render(request, 'bbbootstrap-snippett.html', context)
