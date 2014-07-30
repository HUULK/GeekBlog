# -*- coding: utf-8 -*-
import logging
from django.contrib.auth.models import User, Group

from blog.models import *
from utils import json_response
from blogcore.utils.verify_code import Code

logger = logging.getLogger('geekblog')


@json_response
def get_related_lookup_info(request):
    request_get = request.GET
    lookup_cls = request_get.get('cls_name', '')
    lookup_value = request_get.get('v', '')
    if not lookup_cls or not lookup_value:
        logger.exception('Invaild params, url: %s, field: %s, value: %s' % (lookup_cls, lookup_value))
        return ''

    try:
        obj = eval(lookup_cls).objects.get(pk__exact=lookup_value)
    except Exception:
        obj = None
    return str(obj) if obj else ''


def generate_verify_code(request):
    return Code(request).display()