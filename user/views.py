from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import User  # 모델 안에 있는 Fcuser 클래스르 가지고 옴
# 장고에서 자동 비밀번호 암호화 제공해줌
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

# html 파일을 장고연결 하고 보여주기 위함
# render(request, templateName, 사전형 객체(템플릿에서 사용할 변수들)):
# 해당 .html를 불러오고 여기에 미리 만들어둔 것을 변수를 이용해 전달한다.


def home(request):
    user_id = request.session.get('user')

    if user_id:
        user = User.objects.get(pk=user_id)
        return HttpResponse(user.username)

    return HttpResponse('home!!!!!!')


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        res_data = {}
        # 입력되지 않은 값이 있다면
        if not(username and password):
            res_data['error'] = "모든 값을 입력해야 합니다."
        # 비밀번호가 일치하지 않다면
        user = User.objects.get(username=username)
        if check_password(password, user.password):
            # 비밀번호 일치
            # return redirect('http://www.naver.com')
            request.session['user'] = user.id  # 쿠키에 저장
            return redirect('/')  # 홈으로 이동
        else:
            res_data['error'] = "비밀번호가 틀렸습니다."
        return render(request, 'login.html', res_data)


def register(request):
    # 등록 버튼을 눌러서 들어오는 경우
    if request.method == 'GET':
        return render(request, 'register.html')  # 페이지로 전달
    # 주소를 입력해서 들어오는 경우
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)
        userEmail = request.POST.get('userEmail', None)

        res_data = {}

        if not (username and password and re_password and userEmail):
            res_data['error'] = '모든 값을 입력해야합니다.'

        if password != re_password:
            res_data['error'] = "비밀번호가 다릅니다."
            # return HttpResponse("비밀번호가 다릅니다.")

        user = User(username=username, password=make_password(
            password), userEmail=userEmail)
        user.save()

        return render(request, 'register.html', res_data)
