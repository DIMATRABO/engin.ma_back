sleep 5
#alembic downgrade base
alembic upgrade 190720252148 #initial migration
#alembic downgrade b0c7ba5d9a9f
alembic upgrade head
gunicorn -w 4 -b 0.0.0.0:${APP_PORT} app:app --timeout 120 --worker-class gevent --log-level debug 
