"""refugee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import get_list_or_404
from .models.refugee import Refugee
from .models.story import Story
from .models.location import Location
from .models.qa import Qa

from rest_framework import routers, serializers, viewsets

class RefugeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refugee
        fields = ('name', 'location_id')

class RefugeeViewSet(viewsets.ModelViewSet):
    queryset = Refugee.objects.all()
    serializer_class = RefugeeSerializer

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('message', 'is_from_refugee', 'image_url', 'refugee_id')

class StoryViewSet(viewsets.ModelViewSet):
    serializer_class = StorySerializer
    def get_queryset(self):
        refugee_id = self.kwargs['refugee_id']
        return get_list_or_404(Story, refugee_id=refugee_id)

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'description', 'url',)

class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return get_list_or_404(Location, id=id)

class QaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qa
        fields = ('correct_answer_image', 'wrong_answer_image', 'story',)

class QaViewSet(viewsets.ModelViewSet):
    serializer_class = QaSerializer

    def get_queryset(self):
        message_id = self.kwargs['message_id']
        return get_list_or_404(Qa, story_id=message_id)

router = routers.DefaultRouter()
router.register(r'refugee', RefugeeViewSet)
router.register(r'story/(?P<refugee_id>.+)', StoryViewSet, base_name='Story')
router.register(r'location/(?P<id>.+)', LocationViewSet, base_name='Location')
router.register(r'qa/(?P<message_id>.+)', QaViewSet, base_name='Qa')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
