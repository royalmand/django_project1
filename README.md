# Django Trial 1 - Tennis Club Website

## How to Use Django - VS Code Terminal🌟
To create a website using Django:

1. Buat repository baru
   ```bash
   mkdir django_project1
   ```
3. **cd django_project1**: Untuk akses data di directory tertuju
4. **py -m venv myworld**: Untuk buat v environment name myworld
5. **. myworld\Scripts\activate.ps1**: Activate venv
6. **py -m pip install --upgrade pip**: Cek version pip buat install Django di venv
7. **django-admin startproject my_tennis_club**: Create project
8. **Pop-up Management**: Modal pop-ups are closed automatically, keeping your screen clear.
9. Pindah cd ke **project my_tennis_club**, file yg ada manage.py nya
10. **py manage.py runserver**: run server di localhost
11. **Ctrl + C atau ctrl + break**: buat end run server
12. **py manage.py startapp members**: buat applikasi di web (ex: homepage, contact, member database)
13. jangan lupa di project > settings.py, tambah "members" atau "namaapp" di installed app
14. **py manage.py migrate**
15. buat model dulu di models.py terus migrate => **py manage.py makemigrations members**
16. **py manage.py migrate**


## Alur website berjalan 📖
1. views.py project where we define function of app
2. urls.py app dimana kita jelasin kalo path kita /app maka akan didirect ke views.app atau jalanin function di views.py
3. ini baru disetting di app, karena kita mengoperasikan app ini di dalam project maka setting jg di project
4. Ketika kita reach alamat tertentu, kita akan melibatkan app.urls sebagai opsi / selanjutnya. example website.com/ setelah / itu app kita, missal ada app contact, profile dll. jadi ini dijadikan opsi oleh Django


## Add User for ADMIN 🤝
1. Create an superuser
   ```bash
   py manage.py createsuperuser
   ```
3. Create username
   ```bash
   username: royalmand
   email: royalmandd@gmail.com
   pw: cek note internal laptop
   ```

## Add Records 📋
1. We will use the Python interpreter (Python shell) to add some members to it.
   ```bash
   py manage.py shell cara exit : exit()
   ```

   Cara exit
   ```bash
   exit()
   ```
   
3. Import class Member yang udah dibuat di app
   ```bash
   from members.models import Member
   ```
   
5. Copy paste ini untuk liat content di empty table Membernya. A QuerySet is a collection of data from a database.
   ```bash
   Member.objects.all()
   ```
   
7. Cara isi tabelnya
   ```bash
   member = Member(firstname='Emil', lastname='Refsnes')
   member.save()
   ```
   
5. cek isi ditabel
   ```bash
   Member.objects.all().values()
   ```
   
8. add beberapa data member dan pake for loop untuk save setiap looping nya 

9. cara add data lengkap
    ```bash
   from members.models import Member
   x = Member.objects.all()[0]
   x.phone = 5551234
   x.joined_date = '2022-01-05'
   x.save()
   Member.objects.all().values()
   ```
   

