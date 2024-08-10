# Django Trial 1 - Tennis Club Website

## How to Use Django - VS Code Terminal🌟
To create a website using Django:

1. **mkdir django_project1**: Untuk buat repository baru
2. **cd django_project1**: Untuk akses data di directory tertuju
3. **py -m venv myworld**: Untuk buat v environment name myworld
4. **. myworld\Scripts\activate.ps1**: Activate venv
5. **py -m pip install --upgrade pip**: Cek version pip buat install Django di venv
6. **django-admin startproject my_tennis_club**: Create project
7. **Pop-up Management**: Modal pop-ups are closed automatically, keeping your screen clear.
8. Pindah cd ke **project my_tennis_club**, file yg ada manage.py nya
9. **py manage.py runserver**: run server di localhost
10. **Ctrl + C atau ctrl + break**: buat end run server
11. **py manage.py startapp members**: buat applikasi di web (ex: homepage, contact, member database)
12. jangan lupa di project > settings.py, tambah "members" atau "namaapp" di installed app
13. **py manage.py migrate**
14. buat model dulu di models.py terus migrate => **py manage.py makemigrations members**
15. **py manage.py migrate**


## Alur website berjalan 📖
1. views.py project where we define function of app
2. urls.py app dimana kita jelasin kalo path kita /app maka akan didirect ke views.app atau jalanin function di views.py
3. ini baru disetting di app, karena kita mengoperasikan app ini di dalam project maka setting jg di project
4. Ketika kita reach alamat tertentu, kita akan melibatkan app.urls sebagai opsi / selanjutnya. example website.com/ setelah / itu app kita, missal ada app contact, profile dll. jadi ini dijadikan opsi oleh Django


## Add User for ADMIN 🤝
1. py manage.py createsuperuser 
2. un royalmand royalmandd@gmail.com pw cek note internal laptop

## Add Records 📋
1. We will use the Python interpreter (Python shell) to add some members to it. => py manage.py shell => cara exit : exit()
2. from members.models import Member
3. Member.objects.all() untuk liat empty table Membernya. A QuerySet is a collection of data from a database.
4. isi tabelnya 
>>> member = Member(firstname='Emil', lastname='Refsnes')
>>> member.save()
5. cek isi ditabel 
>>> Member.objects.all().values()
6. add beberapa data member dan pake for loop untuk save setiap looping nya 

7. cara add data lengkap 
>>> from members.models import Member
>>> x = Member.objects.all()[0]
>>> x.phone = 5551234
>>> x.joined_date = '2022-01-05'
>>> x.save()
>>> Member.objects.all().values()

