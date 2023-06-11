from django.db import models


class Gangnam(models.Model):
    본부 = models.TextField(blank=True, null=True)
    팀 = models.TextField(blank=True, null=True)
    시설코드 = models.TextField(blank=True, null=True)
    장비유형 = models.TextField(blank=True, null=True)
    국소등급 = models.TextField(blank=True, null=True)
    국소명 = models.TextField(blank=True, null=True)
    사용여부 = models.TextField(blank=True, null=True)
    세부사업구분 = models.TextField(blank=True, null=True)
    주소 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gangnam'
