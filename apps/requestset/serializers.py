from rest_framework import serializers


class SingleRequestSerializer(serializers.Serializer):
    method_choices = [
        ('get', 'get'),
        ('post', 'post'),
        ('delete', 'delete'),
        ('put', 'put'),
        ('patch', 'patch')
    ]

    url = serializers.CharField(help_text='url', label='url')
    method = serializers.ChoiceField(choices=method_choices,help_text='请求方法', label='请求方法')
    request = serializers.JSONField(help_text='请求参数', required=False, label='请求参数', default={})

    def validate_request(self, value):
        """解决json数据为空的问题"""
        if value.get('json') == {}:
            value.pop('json')

        return value
