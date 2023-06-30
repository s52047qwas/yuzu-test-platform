from django.shortcuts import render
import base64
from rest_framework.decorators import api_view
from .serializers import SingleRequestSerializer
from rest_framework.response import Response
import requests

# Create your views here.


@api_view(http_method_names=['POST'])
def request_view(request, format=None):
    # 1、接收请求数据并校验
    serializer =SingleRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    # 2、发送请求
    data = serializer.validated_data
    res = requests.request(method=data['method'], url=data['url'], **data['request'])

    # 3、组织响应数据并返回
    res_data = {
        'status_code': res.status_code,
        'headers': dict(res.headers),
        'cookies': dict(res.cookies)
    }

    content_type = res_data['headers'].get('Content-Type')
    if content_type:
        if 'html' in content_type:
            res_data['text'] = res.text
        elif 'json' in content_type:
            res_data['json'] = res.json()
        else:
            res_data['content'] = base64.b64decode(res.content).decode()
    else:
        res_data['content'] = base64.b64decode(res.content).decode()

    return Response(res_data, status=200)

