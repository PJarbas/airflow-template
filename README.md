## Runing apache airflow

* pip install apache-airflow
* airflow db init
* airflow users create --username admin --password admin --firstname Anonymous --lastname Admin --role Admin --email admin@example.org
* cp my_scripts_pipeline.py ~/airflow/dags/

Run in separate terminals
* airflow webserver
* airflow scheduler

*  http:/ /localhost:8080
