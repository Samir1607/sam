from rest_framework.views import APIView
from .models import Students
from .serializers import StudentsSerializers
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from django.shortcuts import render


class StudentsView(APIView):
    def get(self, request):
        st = Students.objects.all()
        ss = StudentsSerializers(st, many=True)
        return Response(ss.data, status=status.HTTP_200_OK)

    def post(self, request):
        ss = StudentsSerializers(data=request.data)
        if ss.is_valid():
            ss.save()
            return Response(ss.data, status=status.HTTP_201_CREATED)
        return Response(ss.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentView(APIView):
    def get_by_pk(self, pk):
        try:
            return Students.objects.get(pk=pk)
        except Students.DoesNotExist :
            raise Http404

    def get(self, request, pk):
        st = self.get_by_pk(pk)
        ss = StudentsSerializers(st)
        return Response(ss.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        st = self.get_by_pk(pk)
        ss = StudentsSerializers(st, data=request.data)
        if ss.is_valid():
            ss.save()
            return Response(ss.data, status=status.HTTP_200_OK)
        return Response(ss.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        st = self.get_by_pk(pk)
        ss = StudentsSerializers(st, data=request.data, partial=True)
        if ss.is_valid():
            ss.save()
            return Response(ss.data, status=status.HTTP_200_OK)
        return Response(ss.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        st = self.get_by_pk(pk)
        st.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
