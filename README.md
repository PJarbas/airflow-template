## Runing apache airflow

* pip install apache-airflow
* airflow db init
* airflow users create --username admin --password admin --firstname Anonymous --lastname Admin --role Admin --email admin@example.org
* cp my_scripts_pipeline.py ~/airflow/dags/
* airflow webserver
* airflow scheduler

*  http:/ /localhost:8080
