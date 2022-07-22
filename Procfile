web: gunicorn wsgi -w 1 -b :$PORT -k gthread --threads 3 --timeout 600 --max-requests 500 --max-requests-jitter 100 --access-logfile - --error-logfile - --access-logformat '[%(h)s] %({request_id}i)s %(u)s %(t)s "%(r)s" %(s)s %(D)s %(b)s "%(f)s" "%(a)s"'

pworker: python manage.py celery worker -n prefork@%h -P threads -c 4 -l info -O fair --maxtasksperchild=100
gworker: python manage.py celery worker -P gevent -n gevent@%h -c 4 -l info --maxtasksperchild=100
beat: python manage.py celery beat -l info
