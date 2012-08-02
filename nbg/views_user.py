# -*- coding: utf-8 -*-

from django.contrib import auth
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from nbg.models import UserProfile
from nbg.helpers import json_response, auth_required

@require_http_methods(['POST'])
@json_response
def login_email(request):
    username = request.POST.get('email', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            auth.login(request, user)
            response = {
                'id': user.pk,
                'nickname': user.get_profile().nickname,
                'university': None,
            }
            university = user.get_profile().university
            if university:
                response['university'] = {
                    'id': university.pk,
                    'name': university.name,
                }
        else:
            response = {
                'error': "用户已被吊销。",
            }, 401
    else:
        response = {
            'error': "Email 或密码错误。",
        }, 401

    return response

@require_http_methods(['POST'])
@json_response
def reg_email(request):
    email = request.POST.get('email', None)
    nickname = request.POST.get('nickname', None)
    password = request.POST.get('password', None)

    if email and nickname and password:
        try:
            validate_email(email)
        except ValidationError:
            return {'error': 'Email 格式不正确。'}, 400

        try:
            user = User.objects.create_user(username=email, email=email, password=password)
        except IntegrityError:
            return {'error': 'Email 已被使用。'}, 403
        UserProfile.objects.create(user=user, nickname=nickname)

        user = auth.authenticate(username=email, password=password)
        auth.login(request, user)

        return {'id': user.pk}
    else:
        return {'error': '缺少必要的参数。'}, 400

@require_http_methods(['POST'])
@auth_required
@json_response
def logout(request):
    auth.logout(request)
    return 0

@require_http_methods(['POST'])
@auth_required
@json_response
def deactive(request):
    request.user.is_active = False
    request.user.save()
    auth.logout(request)
    return 0
