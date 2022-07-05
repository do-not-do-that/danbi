from django.db import models
# from multiselectfield import MultiSelectField
from accounts.models import CustomUser


class Routine(models.Model):
    class Meta:
        db_table = 'routine'
    
    MIRACLE = 'MI'
    HOMEWORK = 'HOMEWORK'

    CATEGORY_CHOICES = [
        (MIRACLE, 'MIRACLE'),
        (HOMEWORK, 'HOMEWORK'),
    ]

    account = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(
        max_length=8,
        choices=CATEGORY_CHOICES,
        default=MIRACLE
    )
    goal = models.CharField(max_length=500, null=True, blank=True)
    is_alarm = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class RoutineResult(models.Model):
    class Meta:
        db_table = 'routine_result'

    NOT = 'N'
    TRY = 'T'
    DONE = 'D'

    RESULT_CHOICES = [
        (NOT, 'NOT'),
        (TRY, 'TRY'),
        (DONE, 'DONE'),
    ]

    routine = models.ForeignKey(Routine, on_delete=models.CASCADE)
    result = models.CharField(
        max_length=4,
        choices=RESULT_CHOICES,
        default=NOT
    )
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class RoutineDay(models.Model):
    class Meta:
        db_table = 'routine_day'

    day = models.DateField()
    routine = models.ForeignKey(Routine, on_delete=models.CASCADE, related_name='days')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
