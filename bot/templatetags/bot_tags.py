from django import template
from ..models import BotUser, MessageContent

register = template.Library()


@register.simple_tag
def get_total_member():
    return BotUser.objects.count()

@register.simple_tag
def get_total_message():
    return MessageContent.objects.count()
