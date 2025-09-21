from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import ProjectType, Company, ProjectStatus, Team, Project

from django.utils.html import format_html


@admin.register(ProjectType)
class ProjectTypeAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Company)
class CompanyAdmin(ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name',)


@admin.register(ProjectStatus)
class ProjectStatusAdmin(ModelAdmin):
    list_display = ('status_name',)
    search_fields = ('status_name',)


@admin.register(Team)
class TeamAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    filter_horizontal = ('members',)


@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ('title', 'company', 'project_type',
                    'status', 'team', 'percentage', 'progress_bar')
    list_filter = ('company', 'project_type', 'status', 'team')
    search_fields = ('title', 'description')

    def progress_bar(self, obj):
        return format_html(
            '''
            <div style="width: 100px; background-color: #eee; border-radius: 4px; overflow: hidden;">
                <div style="width: {}%; background-color: #4CAF50; height: 10px;"></div>
            </div>
            <small>{}%</small>
            ''',
            obj.percentage, obj.percentage
        )
    progress_bar.short_description = "Progress"
