from django.db import models

# Create your models here.

# 장고의 모델은 [models.Model]을 상속받아 만든다.
# 클래스 이름: Table name
# 클래스 속성: Column

# CharField(): 문자열 타입
# DateTimeFIeld(): 날짜와 시간 형태

# 모델을 완성하면 데이터 베이스에 적용해야 한다. 이때 사용하는 명령이 migrate명령들인데 이 명령을 사용하려면 앱이 현재 프로젝트에 설치되어 있다고 알려줘야 한다.
# setting.py -> [INSTALLED_APP]변수 제일 윗줄에 User 앱을 추가한다.


class User(models.Model):
    username = models.CharField(
        max_length=32, verbose_name='사용자명')  # 문자열을 담을 수 있는 필드

    userEmail = models.EmailField(max_length=128, verbose_name="사용자 이메일")
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')  # 데이트 타임 필드2

# 관리자 화면이나 쉘에서 객체를 출력할 때 나타날 내용을 결정하는 메소드
    def __str__(self):
        return self.username

    class Meta:
        db_table = '유저 정보 테이블'
        verbose_name = '유저 정보'  # Fcuser를 한국말로 변경
        verbose_name_plural = "유저 정보"  # 복수형으로 쓰게 되어있는 부분 설정

# 실제로 테이블로 어떻게 보여지는지 확인방법
# python3 manage.py makemigrations  # 만든 모델을 가지고 데이터 베이스가 생성 및 수정(0001_initial.py)
# python3 manage.py migrate # 적용

# 데이터 베이스가 잘 존재하는지 확인 하려면,
# sqlite3 db.sqlite3
# .tables
# .schema fastcampus_fcuser
# .q   # 나오기
