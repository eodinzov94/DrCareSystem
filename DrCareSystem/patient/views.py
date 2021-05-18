from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
@login_required
def patients (request):
    patients = Patient.objects.all()
    return render(request, 'patients.html', {'patients': patients})

@login_required
def getVisits (request):
    if request.method == 'POST':
        id      = request.POST['id']
        patient = Patient.objects.get(id=id)
        visits  = Visit.objects.filter(patient=patient)
        return render(request, 'patientinfo.html', {'visits': visits,'patient':patient})
    else:
        return redirect('patients')

@login_required
def newVisit (request):
    if request.method == 'POST':
        id      = request.POST['id']
        patient = Patient.objects.get(id=id)
        results = patient.health_param
        quest   = patient.questionnaire
        return render(request, 'newVisit.html', {'patient':patient,'results': results,'quest': quest})
        

@login_required
def getInfo(request):
    if request.method == 'POST':
        id      = request.POST['id']
        patient = Patient.objects.get(id=id)
        results = patient.health_param
        quest   = patient.questionnaire
        return render(request, 'medinfo.html', {'results': results,'quest': quest})
    else:
        return redirect('patients')

@login_required
def newPatient(request): #TODO: make error appear on screen.
    if request.method == 'POST':
        fullName = request.POST.get('fullname')
        personID = request.POST.get('personid')
        tel = request.POST.get('tel')
        gender = request.POST.get('gender')
        age = int(request.POST.get('age'))

        if len(fullName) < 4:
            messages.info(request, 'Name too short!')
            return redirect('newPatient')
        if len(personID) != 9:
            messages.info(request, 'ID Must be 9 digits long!')
            return redirect('newPatient')
        if len(tel) != 10:
            messages.info(request, 'Phone must be 10 digits long!')
            return redirect('newPatient')
        if age < 0 or age > 140:
            messages.info(request, 'Illegal age!')
            return redirect('newPatient')        

        newP = Patient(
            fullName=fullName,
            personID=personID,
            tel=tel,
            gender=gender,
            age=age,
        )

        newP.save()
        return redirect('patients')
    else:
        return render(request, 'newPatient.html')

@login_required
def updateQuest(request):
    if request.method == 'POST':
        id                  = request.POST.get('patient_db_id')
        isSmoking           = bool(request.POST.get('isSmoking'))
        isOriental          = bool(request.POST.get('isOriental'))
        isDrugsSensitive    = bool(request.POST.get('isDrugsSensitive'))
        hasChronicalDisease = bool(request.POST.get('hasChronicalDisease'))
        isNeedsDiet         = bool(request.POST.get('isNeedsDiet'))
        isEatingToMuchMeat  = bool(request.POST.get('isEatingToMuchMeat'))
        isMalnourished      = bool(request.POST.get('isMalnourished'))
        patient = Patient.objects.get(id=id)
        quest = patient.questionnaire
        results = patient.health_param
        if quest is None:
            quest = Questionnaire(
                isSmoking              =  isSmoking ,
                isOriental             =  isOriental, 
                isDrugsSensitive       =  isDrugsSensitive ,
                hasChronicalDisease    =  hasChronicalDisease ,
                isNeedsDiet            =  isNeedsDiet ,
                isEatingToMuchMeat     =  isEatingToMuchMeat ,
                isMalnourished         =  isMalnourished 
            )
            quest.save()
            patient.questionnaire = quest
            patient.save()
        else:
            quest   = Questionnaire.objects.get(id =  patient.questionnaire.id)
            quest.isSmoking              =  isSmoking 
            quest.isOriental             =  isOriental
            quest.isDrugsSensitive       =  isDrugsSensitive
            quest.hasChronicalDisease    =  hasChronicalDisease
            quest.isNeedsDiet            =  isNeedsDiet
            quest.isEatingToMuchMeat     =  isEatingToMuchMeat
            quest.isMalnourished         =  isMalnourished 
            quest.save()
        return render(request, 'newVisit.html', {'patient':patient,'results': results,'quest': quest})

@login_required
def genRecQuest(quest):
    rec = ""
    if quest.isSmoking:
        rec += "Patient smokes - Recommendation: Stop smoking\n"
    if quest.isNeedsDiet or quest.isEatingToMuchMeat or quest.isMalnourished:
        rec += "Patient has diet issues - Recommendation: Arrange meeting with Nutritionist\n"
    if quest.isDrugsSensitive:
        rec += "Patient has sensitivity to drugs - Recommendation: Arrange meeting with Family Doctor to check for effect overlap\n"
    if quest.hasChronicalDisease:
        rec += "Patient has chronical diseases - Recommendation: Arrange follow ups with Family Doctor\n"
    return rec

@login_required
def genRecHealth(quest, params, patient):
    rec = ""

    # WBC
    wbc_smaller ="WBC Levels point at a viral disease or possibly immunity system failure.\n Recommendation: Rest at home, Arrange follow up with Doctor if disease doesn't pass in 3 days.\n"
    wbc_bigger = "WBC Levels point at a probable infection, or rarely a blood disease.\n Recommendation: Check temperature, exceeding levels might point towards infection. in case of infection administer antibiotics\n If patient tests positive for blood disease, administer cyclophosphamide and corticosteroids\n"
    if 0<patient.age<=3:
        if params.WBC < 6000:
            rec += wbc_smaller

        elif params.wbc > 17500:
            rec += wbc_bigger
    elif 3<patient.age<=17:
        if params.WBC < 5500:
            rec += wbc_smaller

        elif params.wbc > 15500:
            rec += wbc_bigger
    else:
        if params.WBC < 4500:
            rec += wbc_smaller

        elif params.wbc > 11000:
            rec += wbc_bigger

    #Neut
    neut_smaller ="Neut levels hint at blood creation difficulties- possible infection.\n Recommendation: B12 treatment, 10mg/day for 30 days. Folic acid treatment, 5mg/day for 30 days.\nCheck temperature, exceeding levels might point towards infection. in case of infection administer antibiotics\n"
    neut_bigger = "Neut levels hint at probable infection.\nRecommendation: Check temperature, exceeding levels might point towards infection. in case of infection administer antibiotics\n"
    if params.NEUT < 28:
        rec += neut_smaller
    elif params.NEUT > 54:
        rec += neut_bigger

    #Lymph
    lymp_smaller ="Lymph levels hint at blood creation difficulties.\n Recommendation: B12 treatment, 10mg/day for 30 days. Folic acid treatment, 5mg/day for 30 days.\n"
    lymp_bigger = "Lymph levels hint at probable infection.\nRecommendation: Check temperature, exceeding levels might point towards infection. in case of infection administer antibiotics\n"
    if params.LYMPH < 36:
        rec += lymp_smaller
    elif params.LYMPH > 52:
        rec += lymp_bigger

    #RBC
    rbc_bigger ="RBC levels hint at blood creation difficulties.\n Recommendation: B12 treatment, 10mg/day for 30 days. Folic acid treatment, 5mg/day for 30 days.\n Check if the patient shows signs of lung disease, and schedule an XRay accordingly."
    rbc_smaller = "RBC levels hint at anemia or excessive bleeding.\nRecommendation: If patient shows signs of excessive bleeding- immediately transfer to a hospital.\n If patient shows signs of anemia, treat with 10mg B12 pills twice a day for 30 days."
    if params.RBC < 4.5:
        rec += rbc_smaller
    elif params.RBC > 6:
        rec += rbc_bigger

    #HCT
    hct_smaller ="HCT levels hint at anemia or excessive bleeding.\nRecommendation: If patient shows signs of excessive bleeding- immediately transfer to a hospital.\n If patient shows signs of anemia, treat with 10mg B12 pills twice a day for 30 days."
    hct_bigger = "HCT Levels point towards the probability that patient is a smoker. Recommendation: Stop smoking.\n"
    if patient.gender == 'Male':
        if params.HCT < 37:
            rec += hct_smaller

        elif params.HCT > 54:
            rec += hct_bigger
    else:
        if params.HCT < 33:
            rec += hct_smaller

        elif params.HCT > 47:
            rec += hct_bigger

    #Urea
    urea_smaller ="Urea levels hint towards dietery problems, possible malnourishment or lack of protein. Could also be a liver disease.\nRecommendation: Schedule appointment with Nutritionist, with emphasis on test for liver disease.\n"
    urea_bigger = "Urea Levels point towards the dehydration, protein-full diet or even kidney disease.\nRecommendation: Hydrate, rest horizontally. If current state continues, attempt to level the sugar levels in blood.\n"
    if quest.isOriental:
        if params.UREA < 17:
            rec += urea_smaller

        elif params.HCT > 47.3:
            rec += urea_bigger
    else:
        if params.HCT < 17:
            rec += urea_smaller

        elif params.HCT > 43:
            rec += urea_bigger
    
    #Hb
    hb_smaller= "Hb levels hint at anemia, possible bleeding and iron deficiency.\nRecommendation: If patient shows signs of anemia or iron deficiency, treat with 10mg B12 pills twice a day for 30 days.\nIf patient shows signs of excessive bleeding- immediately transfer to a hospital.\n"

    if patient.age<=17:
        if params.HB < 11.5:
            rec += hb_smaller

    else:
        if params.HB<12:
            rec += hb_smaller

    #CREATININE
    Creatinine_smaller = "Creatinine levels hint at possible malnourishment and/or lack of protein in diet.\nRecommendation: Schedule appointment with Nutritionist.\n"
    Creatinine_bigger =  "Excessive creatinine levels could be attributed to one of the following: Kidney problems and/or kidney diseases, muscle diseases or protein-filled diets.\nRecommendation: Schedule appointment with Nutritionist.\n"

    if patient.age <3:
        if params.CREATININE < 0.2:
            rec += Creatinine_smaller
        elif params.CREATININE > 0.5:
            rec += Creatinine_bigger
    elif patient.age< 18:
        if params.CREATININE < 0.5:
            rec += Creatinine_smaller
        if params.CREATININE > 1:
            rec += Creatinine_bigger
    elif patient.age < 60:
        if params.CREATININE < 0.6:
            rec += Creatinine_smaller
        if params.CREATININE > 1:
            rec += Creatinine_bigger
    else:
        if params.CREATININE < 0.6:
            rec += Creatinine_smaller
        if params.CREATININE > 1.2:
            rec += Creatinine_bigger

    #Iron
    iron_smaller ="Iron levels hint at either iron deficiency or blood loss.\nRecommendation: If the patient shows sign of blood loss, administer to a hospital.\nIf the patient shows lack of iron deficiency due to his diet, schedule appointment with Nutritionist.\n"
    iron_bigger ="Iron levels show iron poisoning.\nRecommendation: Admint to a hospital!\n"

    if patient.gender == 'Male':
        if params.IRON < 60:
            rec += iron_smaller
        elif params.IRON > 160:
            rec+= iron_bigger
    else:
        if params.IRON < 48:
            rec += iron_smaller
        elif params.IRON > 128:
            rec+= iron_bigger

    #HDL
    hdl_smaller="HDL levels hint at a possible case of adult diabetes, or a heart disease.\nRecommendation: If the patient shows signs of diabetes, assign an insulin syringe.\nIf the patient shows a possibility for heart disease, consult Nutritionist\nWARNING! Ethiopians have a 20 percent higher value range for HDL.\n"
    hdl_bigger="HDL levels show no major risk.\nRecommendation: Exercise more often.\n"

    if patient.gender == 'Male':
        if params.HDL < 29:
            rec += hdl_smaller
        elif params.HDL > 62:
            rec+= hdl_bigger
    else:
        if params.HDL < 34:
            rec += hdl_smaller
        elif params.HDL > 82:
            rec+= hdl_bigger

    #ALKALINE
    alk_smaller="Alkaline levels show lacking diet, probable B12 deficiency and/or protein, C, folic acid or B6 deficiencies.\nRecommendation: Refer patient to blood test to discern the possibile deficiencies."
    alk_bigger="Alkaline levels hint at one of the following: Liver diseases, Bile routes diseases, pregnancy, overactive thyroid gland or a mixture of different drugs.\nRecommendation: For bile route diseases, refer to surgery.\n For liver diseases, refer to specialist for analysis.\nFor an overactive thyroid gland, administer Propylthiouracil.\n"

    if quest.isOriental:
        if params.ALKALINE < 60:
            rec += alk_smaller

        elif params.ALKALINE > 120:
            rec += alk_bigger
    else:
        if params.ALKALINE < 30:
            rec += alk_smaller

        elif params.ALKALINE > 90:
            rec += alk_bigger

    return rec

    