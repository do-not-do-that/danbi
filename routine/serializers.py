from rest_framework import serializers
from datetime import date, datetime, timedelta
from .models import Routine, RoutineDay, RoutineResult


class RoutineDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RoutineDay
        fields = ['day',]


class RoutineSerializer(serializers.ModelSerializer):
    days = RoutineDaySerializer(many=True, read_only=True)

    class Meta:
        model = Routine
        fields = ['id', 'title', 'days', 'goal', 'category', 'is_alarm']
        depth = 1

    def create(self, validated_data):
        DAY_TABLE = {
            "MON": 0,
            'TUE': 1,
            'WED': 2,
            'THU': 3,
            'FRI': 4,
            'SAT': 5,
            'SUN': 6
        }
        
        root_day = datetime.today()
        week_day  = root_day.weekday() # 오늘 요일
        days = self.context['request'].data['days']

        validated_data['account_id'] = self.context['request'].user.id
        routine = Routine.objects.create(**validated_data)
        
        for day in days:
            target_day = root_day + timedelta(days = (-week_day+DAY_TABLE[day]))
            RoutineDay.objects.create(day=target_day,routine_id=routine.id)

        return routine

    


