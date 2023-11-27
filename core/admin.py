from django.contrib import admin
from django.utils.html import format_html
from import_export import resources
from import_export.admin import ExportMixin
from rest_framework.reverse import reverse
from simple_history.admin import SimpleHistoryAdmin

from .models import Category, Question, Answer, QuestionRating, AnswerRating

# Resources start

class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question

class QuestionRatingResource(resources.ModelResource):
    class Meta:
        model = QuestionRating


class AnswerResource(resources.ModelResource):
    class Meta:
        model = Answer

class AnswerRatingResource(resources.ModelResource):
    class Meta:
        model = AnswerRating


# Resources end

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 1
    readonly_fields = ('created_at',)

class QuestionAdmin(ExportMixin,SimpleHistoryAdmin):
    list_display = ('title', 'category_link', 'created_at', 'get_rating_average')
    list_filter = ('category',)
    date_hierarchy = 'created_at'
    search_fields = ('title', 'content')
    readonly_fields = ('created_at',)
    resource_class = QuestionResource
    inlines = [AnswerInline]

    def category_link(self, obj):
        if obj.category:
            url = reverse('admin:core_category_change', args=[obj.category.id])
            return format_html('<a href="{}">{}</a>', url, obj.category.name)
        return None

    category_link.short_description = 'Category'


    
    def get_rating_average(self, obj):
        ratings = obj.questionrating_set.all()
        if ratings:
            average = sum(rating.rating for rating in ratings) / len(ratings)
            return average
        return None
    get_rating_average.short_description = 'Rating Average'

class AnswerAdmin(ExportMixin, SimpleHistoryAdmin):
    list_display = ('content', 'question', 'created_at')
    list_filter = ('question__category',)
    search_fields = ('content',)
    resource_class = AnswerResource
class QuestionRatingAdmin(ExportMixin, SimpleHistoryAdmin):
    list_display = ('question', 'user', 'rating', 'created_at')
    resource_class = QuestionRatingResource

class AnswerRatingAdmin(ExportMixin, SimpleHistoryAdmin):
    list_display = ('answer', 'user', 'rating', 'created_at')
    resource_class = AnswerRatingResource

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1
    readonly_fields = ('created_at',)
class CategoryAdmin(SimpleHistoryAdmin):
    fieldsets = [
        ('Main Information', {'fields': ['name', 'description']}),
    ]
    inlines = [QuestionInline]


admin.site.register(Category,CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(QuestionRating, QuestionRatingAdmin)
admin.site.register(AnswerRating, AnswerRatingAdmin)
