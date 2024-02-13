DJANGO_MANAGE = python3 routerflow/manage.py

migrations:
	$(DJANGO_MANAGE) makemigrations
	$(DJANGO_MANAGE) migrate

runserver:
	$(DJANGO_MANAGE) runserver

watch:
	npx tailwindcss -i ./routerflow/static/tw/input.css -o ./local-cdn/static/tw/output.css --watch