DJANGO_MANAGE = python3 manage.py

migrations:
	$(DJANGO_MANAGE) makemigrations
	$(DJANGO_MANAGE) migrate

runserver:
	$(DJANGO_MANAGE) runserver

watch:
	npx tailwindcss -i ./static/tw/input.css -o ./static/tw/output.css --watch