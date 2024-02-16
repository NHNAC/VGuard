from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Camera(models.Model):
    name = models.CharField(max_length=50)
    notes = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=255, null=True)
    latitude = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)], null=True)
    longitude = models.FloatField(validators=[MinValueValidator(-180) , MaxValueValidator(180)], null=True)

    def __str__(self):
        return self.name


class FireSmokeWeaponDetection(Base):
    FIRE = "fire"
    SMOKE = "smoke"
    WEAPON = "weapon"

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

    NEED_HANDLING = "need handling"
    HANDLED = "handled"
    IN_PROGRESS = "in progress"
    RESOLVED = "resolved"


    ALARM_TITLE_CHOICES = [
        (FIRE, 'fire'),
        (SMOKE, 'smoke'),
        (WEAPON, 'weapon')
    ]


    SEVERITY_CHOICES = [
        (LOW, 'low'),
        (MEDIUM, 'medium'),
        (HIGH, 'high'),
        (CRITICAL, 'critical')
    ]


    STATUS_CHOICES = [
        (NEED_HANDLING, 'need handling'),
        (HANDLED, 'handled'),
        (IN_PROGRESS, 'in progress'),
        (RESOLVED, 'resolved')
    ]

    camera = models.ForeignKey(Camera, on_delete=models.PROTECT, related_name="detection")
    alarm_title = models.CharField(max_length=15, choices=ALARM_TITLE_CHOICES)
    severity = models.CharField(max_length=15, choices=SEVERITY_CHOICES)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)

    def __str__(self):
        return self.alarm_title


class AgeGender(models.Model):
    male_kids = models.IntegerField(default=0)
    female_kids = models.IntegerField(default=0)
    male_teens = models.IntegerField(default=0)
    female_teens = models.IntegerField(default=0)
    male_adults = models.IntegerField(default=0)
    female_adults = models.IntegerField(default=0)
    male_old = models.IntegerField(default=0)
    female_old = models.IntegerField(default=0)
    camera = models.ForeignKey(Camera, on_delete=models.PROTECT, related_name="agegender")

    def __str__(self):
        sum = self.male_adults + self.male_teens + self.male_adults + self.male_old\
            + self.female_kids + self.female_teens + self.female_adults + self.female_old 
        return f"Sum of all types - {sum}"


class FaceRecognition(Base):
    camera = models.ForeignKey(Camera, on_delete=models.PROTECT, related_name="face")
    image = models.ImageField()

    def __str__(self):
        return f"Face - {self.id}"


class LicensePlateRecognition(Base):
    camera = models.ForeignKey(Camera, on_delete=models.PROTECT, related_name="plate")
    plate_number = models.CharField(max_length=10)

    def __str__(self):
        return f"Plate - {self.plate_number}"
    



