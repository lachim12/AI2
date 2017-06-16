Instalacja Python --> python-3.4.3.amd64.msi <br />
Podczas instalacji zaznaczyć wszystkie opcje (jedna jest odznaczona, trzeba ja zaznaczyć)<br />
potem w CMD wpisujemy: 	pip install django==1.9<br />
			easy_install Pillow<br /><br />
Następnie w cmd wchodzimy do folderu BLOG, tam gdzie jest manage.py i wpisujemy po kolei:<br />
			python manage.py makemigrations<br />
			python manage.py migrate<br />
			python manage.py createsuperuser     --> Tutaj prosi nas o podanie emailu admina oraz hasła<br /><br />

I odpalamy serwer komendą: python manage.py runserver<br />
Pojawi się link, najprawdopodobniej taki:  http://127.0.0.1:8000/ który wpisujemy w przeglądarke.<br /><br />


http://www.python.rk.edu.pl/w/p/wprowadzenie-do-django-10/

				
