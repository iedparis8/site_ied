from angular_plugins.models import Rules
from rest_framework import serializers


class RulesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rules
        fields = ('rule',)
