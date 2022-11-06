import pendulum

from airflow.decorators import dag, task


@dag(
    schedule=None,
    start_date=pendulum.datetime(2022, 8, 1),
    catchup=False,
    tags=["k8s", "airflow", "docker", "helm"],
)
def hello_kubernetes():
    """
    Print out the contents of the Airflow Context.
    """

    @task
    def a_task(**context):
        for item in dict(context).items():
            print(f"{item[0]} --> {str(item[1])}")
            print(f"{item[0]} --> {repr(item[1])}")

    a_task()

hello_kubernetes()
