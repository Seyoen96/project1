from django.db import models

# Create your models here.

# class 생성
class Notice(models.Model):
    # 클래스 변수
    num = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=200)
    contents = models.TextField(null=True)
    createDate = models.DateTimeField(auto_now_add=True)
    hit = models.IntegerField(default="0")
