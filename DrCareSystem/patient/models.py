from django.db import models

class HealthManager(models.Manager):

    def __str__(self):
        return self.title



class HealthParameters(models.Model):
    title        = models.CharField(max_length=100, default ='Health Parameters')
    WBC          = models.IntegerField(default=0)
    NEUT         = models.FloatField(default=0)
    LYMPH        = models.FloatField(default=0)
    RBC          = models.FloatField(default=0)
    HCT          = models.FloatField(default=0)
    UREA         = models.IntegerField(default=0)
    HB           = models.IntegerField(default=0)
    CREATININE   = models.FloatField(default=0)
    IRON         = models.IntegerField(default=0)
    HDL          = models.IntegerField(default=0)
    ALKALINE     = models.IntegerField(default=0)
    objects      = HealthManager()
    def __str__(self):
        return self.title
    
class QuestionnaireManager(models.Manager):

    def __str__(self):
        return self.title



class Questionnaire(models.Model):
    title               = models.CharField(max_length=100, default ='Medical Questionnaire')
    isSmoking           = models.BooleanField(default=False)
    isOriental          = models.BooleanField(default=False)
    isDrugsSensitive    = models.BooleanField(default=False)
    hasChronicalDisease = models.BooleanField(default=False)  
    isNeedsDiet         = models.BooleanField(default=False)
    isEatingToMuchMeat  = models.BooleanField(default=False)
    isMalnourished      = models.BooleanField(default=False)
    objects             = QuestionnaireManager()

    def __str__(self):
        return self.title









class PatientManager(models.Manager):

    def __str__(self):
        return self.fullName



class Patient(models.Model):
    fullName        = models.CharField(max_length=100, default ='Mendy')
    personID        = models.CharField(max_length=9, unique=True)
    tel             = models.CharField(max_length=10, default ='')
    gender          = models.CharField(max_length=1, default ='M')
    age             = models.IntegerField()
    health_param    = models.OneToOneField(HealthParameters, models.SET_NULL,blank= True, null= True)
    questionnaire   = models.OneToOneField(Questionnaire, models.SET_NULL,blank= True, null= True)
    objects         = PatientManager()
    def __str__(self):
        return self.fullName

class VisitManager(models.Manager):

    def __str__(self):
        return self.date



class Visit(models.Model):
    date            = models.DateField(auto_now=True)
    patient         = models.ForeignKey(Patient,null= True,blank = True, default= None, on_delete=models.CASCADE)
    description     = models.TextField()
    autoRec         = models.TextField()
    objects         = VisitManager()
    def __str__(self):
        return self.date.__str__()