from .models import Students
from rest_framework import serializers


class StudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"
