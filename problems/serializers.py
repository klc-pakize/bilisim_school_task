from rest_framework import serializers

from .models import Problem

class ProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        fields = (
            'id',
            'title',
            'problem',
            'point',
            'level',
            'language',
            'input',
            'expected_output',
        )


    