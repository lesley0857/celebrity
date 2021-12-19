from django import template
from celebrityapp.views import *

register = template.Library()

@register.filter
def commentss(value):
    print(value)
    c = Comments.objects.filter(posts_id=value)
    print(dir(c))
    return c

@register.filter
def no_commentss(value):
    print(value)
    c = Comments.objects.filter(posts_id=value)
    print('c',c.count())
    return c.count()

@register.filter
def replyy(value):
    print(value)
    c = Replies.objects.filter(comments_id=value)
    print(c)
    return c

@register.filter
def no_reply(value):
    print(value)
    c = Replies.objects.filter(comments_id=value)
    print('c',c.count())
    return c.count()