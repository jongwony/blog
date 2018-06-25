date: 2017-12-04 02:22:00
layout: post
title: Nginx uWSGI Django
tags: ['nginx','uwsgi','django']


기존의 프로젝트를 Django로 옮기는 데에 성공했고 uWSGI와 Nginx를 함께 사용하는 과정이 필요했습니다.

[페이지의 속도를 측정](//developers.google.com/speed/pagespeed/insights/)하는 도구로 확인해보니 `브라우저 캐싱`이 없었고 웹 서버에서 처리하는 것이 필요했기 때문입니다.

그동안 여러번 설치를 하면서 php-fpm nginx oracle도 연결해 보았고, nginx uwsgi flask도 연결해 보았습니다. 그래서 nginx uwsgi django 자체를 연결하는 데에는 [NGINX 및 UWSGI 연동](//wikidocs.net/7387) 페이지를 차근차근 따라가면서 해도 큰 문제가 없었습니다.

하지만 static 경로를 잡지 못하는 경우가 많았습니다. DEBUG 옵션을 `False`로 했을 때도 `STATIC_ROOT` 경로에 영향을 미치는 경우가 있었고 `nginx` 설정의 `root`와 `alias`의 차이도 있었습니다. [stackoverflow](//stackoverflow.com/questions/10631933/nginx-static-file-serving-confusion-with-root-alias)에 차이가 나와 있지만 그래도 에러가 발생하는 경우가 있어 `location` 외부에 root를 사용하여 해결하였습니다.

브라우저 캐싱 기능은 [https://stackoverflow.com/questions/20147587/how-to-leverage-browser-caching-in-django](//stackoverflow.com/questions/20147587/how-to-leverage-browser-caching-in-django) 문서를 참고하였습니다.

글을 쓰고나서 다시 보니 `views.py`에 `@cache_control`만 달아도 해결되는 문제였군요...

```python
from django.views.decorators.cache import cache_control

@cache_control(private=True)
def my_view(request):
    ...
```