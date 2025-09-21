from django.db import models
from django.contrib.auth.models import User


class ProjectType(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ProjectStatus(models.Model):
    status_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.status_name


class Team(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    members = models.ManyToManyField(User, related_name='teams', blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    project_type = models.ForeignKey(
        ProjectType, on_delete=models.CASCADE, related_name='projects', null=True, blank=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name='projects', null=True, blank=True)
    status = models.ForeignKey(
        ProjectStatus, on_delete=models.SET_NULL, null=True, blank=True, related_name='projects')
    team = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='projects')
    percentage = models.DecimalField(
        max_digits=5, decimal_places=2, help_text="Progress percentage", null=True, blank=True)

    def __str__(self):
        return self.title
