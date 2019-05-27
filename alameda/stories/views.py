from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from rest_framework import viewsets

from .models import Epic, Story, Task
from .serializers import EpicSerializer, StorySerializer, TaskSerializer
from alameda.sprints.views import BaseListView, BaseView


class EpicViewSet(viewsets.ModelViewSet):
    serializer_class = EpicSerializer
    queryset = Epic.objects.all()


class StoryViewSet(viewsets.ModelViewSet):
    serializer_class = StorySerializer
    queryset = Story.objects.all()


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class StoryBaseView(BaseView):
    model = Story
    fields = [
        'title', 'description',
        'epic', 'sprint',
        'owner', 'assignee',
        'priority', 'points',
        'state', 'tags',
    ]
    success_url = reverse_lazy('stories:story-list')


class StoryCreateView(StoryBaseView, CreateView):

    def _get_success_message(self):
        return 'Story successfully created!'

    def get_initial(self):
        return dict(owner=self.request.user.id, state='pl')


class StoryUpdateView(StoryBaseView, UpdateView):

    def _get_success_message(self):
        return 'Story successfully updated!'


class EpicBaseView(BaseView):
    model = Epic
    fields = [
        'title', 'description',
        'owner', 'priority',
        'state', 'tags',
    ]
    success_url = reverse_lazy('stories:epic-list')


class EpicCreateView(EpicBaseView, CreateView):

    def _get_success_message(self):
        return 'Epic successfully created!'

    def get_initial(self):
        return dict(owner=self.request.user.id, state='pl')


class EpicUpdateView(EpicBaseView, UpdateView):

    def _get_success_message(self):
        return 'Epic successfully updated!'


class EpicList(BaseListView):
    model = Epic

    filter_fields = dict(
        owner='owner__username',
        state='state__name__iexact',
        label='tags__name__iexact'
    )

    select_related = ['owner', 'state']
    prefetch_related = ['tags']


class StoryList(BaseListView):
    model = Story

    filter_fields = dict(
        owner='owner__username',
        assignee='assignee__username',
        state='state__name__iexact',
        label='tags__name__iexact',
        sprint='sprint__title__iexact'
    )

    select_related = ['owner', 'assignee', 'state', 'sprint']
    prefetch_related = ['tags']
