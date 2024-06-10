
from django.contrib import admin
from django.urls import path
from config.views import main, burger_list, burger_search

urlpatterns = [
    path("admin/", admin.site.urls),
    # 경로를 지정하지 않으면 main 직원을 호출한다.
    path("", main),
    # 'burgers'경로로 접근하면 burger_list라는 직원을 호출한다.
    path("burgers/", burger_list),
    path("search/", burger_search),
]
