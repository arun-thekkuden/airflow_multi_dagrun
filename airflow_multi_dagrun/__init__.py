from airflow.plugins_manager import AirflowPlugin

from . import operators
from . import sensors


class MultiDagRunPlugin(AirflowPlugin):
    name = 'multi_dagrun'
    operators = [
        operators.TriggerMultiDagRunOperator,
        sensors.ExternalDagsSensor,
        sensors.MultiDagRunSensor,
    ]
