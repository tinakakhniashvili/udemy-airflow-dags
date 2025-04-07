from airflow.decorators import task, dag
from datetime import datetime
from airflow.providers.docker.operators.docker import DockerOperator

@dag(start_date=datetime(2021, 1, 1), schedule_interval='@daily', catchup=False)
def docker_dag():

    @task()
    def t1():
        pass

    t2 = DockerOperator(
        task_id='t2',
        image='python:3.8-slim-buster',
        command='echo "command running in the docker container"',
        docker_url='unix://var/run/docker.sock',  # Docker socket URL
        network_mode='bridge',
        # extra_host=['/var/run/docker.sock:/var/run/docker.sock'],  # Correct way to mount the Docker socket
    )

    t1() >> t2

dag = docker_dag()
