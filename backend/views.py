from django.shortcuts import render
from django.http import JsonResponse
from .models import Donation
from .serializers import DonationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def donation_list(request):
    if request.method == 'GET':
        donations = Donation.objects.all()
        serializer = DonationSerializer(donations, many=True)
        return Response({"donations": serializer.data})

    if request.method == 'POST':
        serializer = DonationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def donation_detail(request, id):
    try:
        donation = Donation.objects.get(pk=id)
    except Donation.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DonationSerializer(donation)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DonationSerializer(donation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        donation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
