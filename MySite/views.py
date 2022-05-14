from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .models import Person, Appoint, Doctor, Patient, docprofile
from .forms import RegisterForm, LoginForm
from datetime import datetime
import logging
from django.db.utils import IntegrityError

logger = logging.getLogger(__name__)

# 1 логин
def login3(request):
    if request.method == "POST":
        usr = Person.objects.all()
        login = request.POST.get("login")
        password = request.POST.get("password")
        loginform = LoginForm()
        data = {"wrong": "Ошибка! Неправильный логин или пароль.", "form": loginform}
        data2 = {"wrong": "Ошибка! Введите логин или пароль.", "form": loginform}
        sessid = request.session.get("person_id")

        for p in usr:
            if(login == p.login and password == p.password):
                if (sessid == None):
                    if (p.id == 1):
                        logger.info("Admin Logged in")
                        request.session['person_id'] = p.id
                        #p.save()
                        return HttpResponseRedirect("adm/")
                    elif(p.usertype == False):
                        logger.info("{0} Logged in".format(p.name))
                        request.session['person_id'] = p.id
                       # p.save()
                        return HttpResponseRedirect("id{0}".format(p.id))
                    else:
                        logger.info("{0} doctor Logged in".format(p.name))
                        request.session['person_id'] = p.id
                       # p.save()
                        return HttpResponseRedirect("id{0}".format(p.id))
        else:
            return render(request, "auth.html", context=data)

# 2 страница авторизация
def auth(request):
    sessid = request.session.get("person_id")
    loginform = LoginForm()
    #sessid=None
    print(sessid)
    if (sessid == None):
        return render(request, "auth.html", context={"form": loginform})
    else:
        if (sessid == 1):
            return HttpResponseRedirect("adm/")
        else:
            return HttpResponseRedirect("id{0}".format(sessid))

    def __str__(self):
        return f"{self.auth}"

# 3 выход
def logout(request):
    sessid = request.session.get("person_id")
    person = Person.objects.get(id=sessid)
    if (sessid == 1):
        logger.info("Admin Logged out")
        del request.session['person_id']

        return HttpResponseRedirect("/")
    else:
        logger.info("{0}(id{1}) Logged out".format(person.name, person.id))
        del request.session['person_id']

        return HttpResponseRedirect("/")

# 4 основная пользовательская страница
def user(request, id, id2='1'):
    usr = Person.objects.all()
    person = Person.objects.get(id=id)
    today = datetime.date(datetime.now())
    today2 = datetime.time(datetime.now())
    app = Appoint.objects.all().order_by('appointdate', 'appointtime')
    prof = docprofile.objects.all()
    doc = Doctor.objects.all()
    print(Doctor.objects.get(id=1))
    #appointform = AppointForm()
    sessid = request.session.get("person_id")
    spec1 = request.POST.get("profile", 0)
    if (spec1 == ""):
        spec = None
    else:
        spec = int(spec1)
    if (sessid == person.id and person.usertype == False):
        app = Appoint.objects.filter(patient__user__id=person.id, appointdate__gte = today).order_by('appointdate', 'appointtime')
        pat = Patient.objects.get(user=id)
        output = "Здравствуйте, {0}".format(person.name)
        patient = pat.id
        data = {"output": output, "app": app, "usr": usr, "patient": patient, "today": today, "today2": today2, "prof": prof, "doc": doc, "spec": spec}
        return render(request, "appointment.html", context=data)
    elif (sessid == person.id and person.usertype == True):
        app = Appoint.objects.filter(doctor__user__id=person.id, appointdate__gte = today).order_by('appointdate', 'appointtime')
        doc = Doctor.objects.get(user=id)
        output = "Hello, {0}".format(person.name)
        doctor = doc.id
        data2 = {"app": app, "output": output, "doctor": doctor, "today": today, "today2": today2}
        return render(request, "doctor.html", context=data2)
    else:
        return HttpResponse("Forbidden")

def apptest(request):
    # usr = Person.objects.all()
    # person = Person.objects.get(id=1)
    # today = datetime.date(datetime.now())
    # today2 = datetime.time(datetime.now())
    # app = Appoint.objects.all().order_by('appointdate', 'appointtime')
    # prof = docprofile.objects.all()
    # doc = Doctor.objects.all()
    # print(Doctor.objects.get(id=1))
    # # appointform = AppointForm()
    # sessid = request.session.get("person_id")
    # spec1 = request.POST.get("profile", 0)
    # if (spec1 == ""):
    #     spec = None
    # else:
    #     spec = int(spec1)
    # data = {"app": app, "usr": usr, "today": today, "today2": today2,
    #         "prof": prof, "doc": doc, "spec": spec}
    return render(request, "apptest.html")

# 5 административная страница
def adm(request):
    sessid = request.session.get("person_id")
    #sessid = 1
    person = Person.objects.get(id=sessid)
    today = datetime.date(datetime.now())
    today2 = datetime.time(datetime.now())
    if (sessid == 1):
        personform = RegisterForm()
        doctor = Doctor.objects.all()
        patient = Patient.objects.all()
        usr = Person.objects.all()
        prof = docprofile.objects.all()
        app = Appoint.objects.all().order_by('appointdate', 'appointtime')
        app2 = app.order_by('-appointdate', '-appointtime')

        return render(request, "adm.html", {"doctor": doctor, "patient": patient, "usr": usr, "app": app, "today": today, "today2": today2, "app2": app2, "prof": prof, "form": personform})
    else:
        return HttpResponse("Forbidden")

# 6 создание пользователя
def usercreate(request):
    if request.method == "POST":
        personform = RegisterForm()
        pers = Person()
        pers.name = request.POST.get("name")
        pers.login = request.POST.get("login")
        pers.password = request.POST.get("password")
        pers.usertype = request.POST.get("radiobutton")
        pers.registered = datetime.now()

        try:
            pers.save()
        except IntegrityError:
            data = {"wrong": "Ошибка. Выберите другой логин или пароль!", "form": personform}
            return render(request, "register.html", context=data)

        if request.POST.get("radiobutton") == "False":
            pat = Patient()
            pat.user = Person.objects.get(id=pers.id)

            try:
                pat.save()
            except IntegrityError:
                data = {"wrong": "Ошибка. Выберите другой логин или пароль!", "form": personform}
                return render(request, "register.html", context=data)

        elif request.POST.get("radiobutton") == "True":
            doc = Doctor()
            doc.profile = docprofile.objects.get(id=request.POST.get("docprof", "patient"))
            doc.user = Person.objects.get(id=pers.id)

            try:
                doc.save()
            except IntegrityError:
                data = {"wrong": "Ошибка. Выберите другой логин или пароль!", "form": personform}
                return render(request, "register.html", context=data)
    return HttpResponseRedirect("/")

# 7 Страница регистрации
def register(request):
    personform = RegisterForm()
    return render(request, "register.html", {"form": personform})

# 8 удаление данных пользователей из бд
def userdelete(request, id):
    try:
        person = Person.objects.get(id=id)
        adm = Person.objects.get(id=1)
        person.delete()
        return HttpResponseRedirect("/adm/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

# 9 удаление встречи/записи
def appdelete(request, id):
    try:
        appoint = Appoint.objects.get(id=id)
        adm = Person.objects.get(id=1)
        appoint.delete()
        return HttpResponseRedirect("/adm/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Appointment not found</h2>")

# 10 создание записи к врачу
def makeappoint(request, id):
    person = Person.objects.get(id=id)
    usr = Person.objects.all()
    if request.method == "POST":
        app = Appoint()
        app.patient = Patient.objects.get(user=id)
        app.doctor = Doctor.objects.get(id=request.POST.get("specialist"))
        app.appointdate = request.POST["calendar"]
        app.appointtime = request.POST["apptime"]
        app.appointreg = datetime.now()
        logger.info("{0}(id{1}) ask an appointment for {2} ({3}, {4})".format(person.name, person.id, app.doctor, app.appointdate, app.appointtime))
        try:
            app.save()
        except IntegrityError:
            print("Unhandled integrity error:")
            app = Appoint.objects.all().order_by('appointdate', 'appointtime')
            output = "Hello, {0}".format(person.name)
            today = datetime.date(datetime.now())
            today2 = datetime.time(datetime.now())
            patient = "{0}".format(person.name)
            error = "Ошибка, данное время уже занято!"
            data = {"output": output, "app": app, "usr": usr, "patient": patient, "today": today, "today2": today2, "error": error}
            data2 = {"wrong": "Ошибка. Выберите другую дату или время!"}
            return render(request, 'appointment.html', context=data2)
    return HttpResponseRedirect("/id{0}".format(id))

# 11 контакты
def about(request):
    return render(request, "about.html")

# 12 о сервисе
def abouts(request):
    return render(request, "abouts.html")