from django.db import models
# 모델 = 테이블
# 모델의 필드 = 테이블의 컬럼
# 인스턴스 : 테이블의 레코드
# 모델을 구성했다 ==> 데이타베이스에 어떤 데이타를 어떤 형태로 넣을 지 결정했음!!
# migration: 모델 구성 후 데이타베이스에 반영

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=200)
    url = models.URLField('Site URL')

    def __str__(self):
        return self.site_name + "(" + self.url + ")"
