from django.contrib import admin
from .models import User
# Register your models here.
# 관리자에 쓸 정보들을 기입함


# 자신이 만든 모델을 관리자 페이지에서 확인 or 기능 추가 -> admin.py에 작성해 주면 됨.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')  # 관리자 화면에 클릭안하고도 정보를 보여지게 하는 법


# 등록
admin.site.register(User, UserAdmin)
