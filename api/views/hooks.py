import pytz
utc = pytz.UTC
from datetime import datetime, timedelta
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from django.db.models import F, Func

from api.models import Employee, Shift, ShiftInvite, ShiftApplication, Clockin, Employer, AvailabilityBlock, FavoriteList, Venue, JobCoreInvite, Rate, FCMDevice, Notification, PayrollPeriod, PayrollPeriodPayment, Profile
from django.contrib.auth.models import User
from api.actions import employee_actions
from api.serializers import clockin_serializer

from rest_framework import serializers

class ShiftInviteGetSmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftInvite
        exclude = ()


class DefaultAvailabilityHook(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        employees = Employee.objects.all()
        for emp in employees:
            employee_actions.create_default_availablity(emp)

        return Response({"status": "ok"}, status=status.HTTP_200_OK)


class DeleteAllShifts(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        ShiftInvite.objects.all().delete()
        ShiftApplication.objects.all().delete()
        Shift.objects.all().delete()

        return Response({"status": "ok"}, status=status.HTTP_200_OK)


class DeleteAllData(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        log = []

        log.insert(0, "Deleting ShiftInvites...")
        ShiftInvite.objects.all().delete()

        log.insert(0, "Deleting ShiftApplication...")
        ShiftApplication.objects.all().delete()

        log.insert(0, "Deleting Shifts...")
        Shift.objects.all().delete()

        log.insert(0, "Deleting Employees...")
        Employee.objects.all().delete()

        log.insert(0, "Deleting Employers...")
        Employer.objects.all().delete()
        log.insert(0, "Deleting Profiles and Users...")
        Profile.objects.all().delete()
        User.objects.all().delete()

        log.insert(0, "Deleting Clockins...")
        Clockin.objects.all().delete()

        log.insert(0, "Deleting AvailabilityBlocks...")
        AvailabilityBlock.objects.all().delete()

        log.insert(0, "Deleting FavoriteLists...")
        FavoriteList.objects.all().delete()

        log.insert(0, "Deleting Venues...")
        Venue.objects.all().delete()

        log.insert(0, "Deleting JobCoreInvites...")
        JobCoreInvite.objects.all().delete()

        log.insert(0, "Deleting Ratings...")
        Rate.objects.all().delete()

        log.insert(0, "Deleting FCM Devices...")
        FCMDevice.objects.all().delete()

        log.insert(0, "Deleting Notification...")
        Notification.objects.all().delete()

        log.insert(0, "Deleting PayrollPeriods...")
        PayrollPeriod.objects.all().delete()

        log.insert(0, "Deleting PayrollPeriodPayments...")
        PayrollPeriodPayment.objects.all().delete()

        return Response({"status": "ok", "log": log }, status=status.HTTP_200_OK)

class ClockOutExpiredShifts(APIView):
    permission_classes = [AllowAny]

    def get(self, request):

        NOW = utc.localize(datetime.now())
        # if now > shift.ending_at + delta:
        clockins = Clockin.objects.filter(ended_at__isnull=True, shift__ending_at__lte= NOW + (timedelta(minutes=1) * F('shift__maximum_clockout_delay_minutes'))).select_related('shift')
        for clockin in clockins:
            clockin.ended_at = clockin.shift.ending_at + timedelta(minutes=clockin.shift.maximum_clockout_delay_minutes)
            clockin.save()

        serializer = clockin_serializer.ClockinGetSerializer(clockins, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

# Expire invitations that its shifts have already started.
class ExpireOldInvites(APIView):
    permission_classes = [AllowAny]

    def get(self, request):

        NOW = utc.localize(datetime.now())
        invites = ShiftInvite.objects.filter(shift__starting_at__lte= NOW + (timedelta(minutes=1) * F('shift__maximum_clockout_delay_minutes'))).select_related('shift')
        for invite in invites:
            invite.status = 'EXPIRED'
            invite.save()

        serializer = ShiftInviteGetSmallSerializer(invites, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
