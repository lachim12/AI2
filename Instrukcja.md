Instalacja Python --> python-3.4.3.amd64.msi 
 Podczas instalacji zaznaczyć wszystkie opcje (jedna jest odznaczona, trzeba ja zaznaczyć)
 Pozniej w CMD wpisujemy: 	pip install django==1.9
				easy_install Pillow
w cmd wchodzisz do BLOG, tam gdzie jest manage.py i wpisujesz:
				python manage.py makemigrations
				python manage.py migrate
				python manage.py createsuperuser     --> Tutaj poprosi cie o wpisanie loginu emaila i hasła admina

i odpalasz serwer: python manage.py runserver
Pojawi się link, najprawdopodobniej taki:  http://127.0.0.1:8000/ 


http://www.python.rk.edu.pl/w/p/wprowadzenie-do-django-10/

				
