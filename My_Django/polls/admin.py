from django.contrib import admin
from .models import Question, Choice


# Register your models here.


# class ChoiceInline(admin.TabularInline):
class ChoiceInline(admin.StackedInline):
    model = Choice  # inline에 표시할 외래키로 연결된 데이터
    extra = 0  # 빈값의 칸 표시 수 default 값은 1


class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date", "question_text"]  # admin 데이터 추가 순서
    fieldsets = [
        ("Question Statement", {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["pub_date"]}),
    ]  # admin 데이터 추가 화면 커스텀
    inlines = [ChoiceInline]  # 외래키로 연결된 다른 데이터의 정보를 같이 보여줌
    list_display = ("question_text", "pub_date")  # 각 데이터에 표시할 목록(0번인덱스 값으로 detail로 들어감)
    list_filter = ["pub_date"]  # 데이터의 값에 맞는 필터링 생성
    search_fields = ["question_text"]  # 검색내용을 찾을 위치


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
