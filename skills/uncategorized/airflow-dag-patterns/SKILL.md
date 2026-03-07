---
name: airflow-dag-patterns
description: >-
  Build production Apache Airflow DAGs with best practices for operators,
  sensors, testing, and deployment. Use when creating data pipelines,
  orchestrating workflows, or scheduling batch jobs.
version: 1.0.0
dependencies:
  - python3
  - apache-airflow
compatibility: 'agent-zero, claude-code, cursor'
---

# Apache Airflow DAG Patterns

Production-ready patterns for Apache Airflow including DAG design, operators, sensors, testing, and deployment strategies.

## When to Use This Skill

- Creating data pipeline orchestration with Airflow
- Designing DAG structures and dependencies
- Implementing custom operators and sensors
- Testing Airflow DAGs locally
- Setting up Airflow in production
- Debugging failed DAG runs

## Core Concepts

### 1. DAG Design Principles

| Principle | Description |
|-----------|-------------|
| **Idempotent** | Running twice produces same result |
| **Atomic** | Tasks succeed or fail completely |
| **Incremental** | Process only new/changed data |
| **Observable** | Logs, metrics, alerts at every step |

### 2. Task Dependencies

```python
# Linear
task1 >> task2 >> task3

# Fan-out
task1 >> [task2, task3, task4]

# Fan-in
[task1, task2, task3] >> task4

# Complex
task1 >> task2 >> task4
task1 >> task3 >> task4
```

## Quick Start

```python
# dags/example_dag.py
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator

default_args = {
    'owner': 'data-team',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'retry_exponential_backoff': True,
    'max_retry_delay': timedelta(hours=1),
}

with DAG(
    dag_id='example_etl',
    default_args=default_args,
    description='Example ETL pipeline',
    schedule='0 6 * * *',  # Daily at 6 AM
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['etl', 'example'],
    max_active_runs=1,
) as dag:

    start = EmptyOperator(task_id='start')

    def extract_data(**context):
        execution_date = context['ds']
        # Extract logic here
        return {'records': 1000}

    extract = PythonOperator(
        task_id='extract',
        python_callable=extract_data,
    )

    end = EmptyOperator(task_id='end')

    start >> extract >> end
```

## Patterns

### Pattern 1: TaskFlow API (Airflow 2.0+)

```python
# dags/taskflow_example.py
from airflow.decorators import dag, task
from datetime import datetime

@dag(
    schedule='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['example'],
)
def taskflow_example():
    @task
    def extract():
        return {'data': [1, 2, 3]}

    @task
    def transform(data):
        return [x * 2 for x in data['data']]

    @task
    def load(transformed):
        print(f'Loaded: {transformed}')

    load(transform(extract()))

taskflow_example_dag = taskflow_example()
```

### Pattern 2: Custom Operators

```python
# plugins/custom_operator.py
from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataValidationOperator(BaseOperator):
    @apply_defaults
    def __init__(self, validation_rules, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validation_rules = validation_rules

    def execute(self, context):
        self.log.info(f'Validating with rules: {self.validation_rules}')
        # Validation logic here
        if not self.validate_data():
            raise ValueError('Data validation failed')
        return 'Validation passed'

    def validate_data(self):
        # Implement validation
        return True
```

### Pattern 3: Sensors

```python
# dags/sensor_example.py
from airflow.sensors.filesystem import FileSensor
from airflow.sensors.external_task import ExternalTaskSensor

# Wait for file
file_sensor = FileSensor(
    task_id='wait_for_file',
    filepath='/data/input.csv',
    mode='reschedule',  # Free up worker slot
    timeout=60 * 60 * 24,  # 24 hours
    poke_interval=60,  # Check every minute
)

# Wait for another DAG
external_sensor = ExternalTaskSensor(
    task_id='wait_for_upstream_dag',
    external_dag_id='upstream_dag',
    external_task_id='final_task',
    allowed_states=['success'],
    mode='poke',
)
```

## Testing

### Unit Testing DAGs

```python
# tests/test_dags.py
def test_dag_import():
    from dags.example_dag import dag
    assert dag.dag_id == 'example_etl'
    assert len(dag.tasks) == 3

def test_task_dependencies():
    from dags.example_dag import dag
    task_dict = {task.task_id: task for task in dag.tasks}
    assert task_dict['start'].downstream_task_ids == {'extract'}
    assert task_dict['extract'].downstream_task_ids == {'end'}
```

### Integration Testing

```bash
# Test DAG validation
airflow dags list
airflow dags test example_etl 2024-01-01

# Run specific task
airflow tasks test example_etl extract 2024-01-01
```

## Deployment

### Local Development

```bash
# Start Airflow locally
airflow standalone

# Initialize database
airflow db init

# Create user
airflow users create \
    --username admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com
```

### Production Considerations

- **Executor**: Use CeleryExecutor or KubernetesExecutor for scaling
- **Database**: PostgreSQL or MySQL (not SQLite)
- **Monitoring**: Metrics, logs, and alerting
- **Security**: RBAC, network policies, secrets management
- **CI/CD**: DAG deployment pipeline

## Project Structure

```
airflow-project/
├── dags/
│   ├── __init__.py
│   ├── example_dag.py
│   └── utils/
│       └── helpers.py
├── plugins/
│   ├── __init__.py
│   ├── operators/
│   │   ├── __init__.py
│   │   ├── data_validation.py
│   │   └── custom_transforms.py
│   ├── sensors/
│   │   ├── __init__.py
│   │   ├── custom_sensors.py
│   │   └── callbacks.py
│   └── hooks/
│       └── custom_hooks.py
├── tests/
│   ├── __init__.py
│   ├── test_dags.py
│   └── test_operators.py
├── docker-compose.yml
└── requirements.txt
```

## Best Practices

### Do's
- **Use TaskFlow API** - Cleaner code, automatic XCom
- **Set timeouts** - Prevent zombie tasks
- **Use `mode='reschedule'`** - For sensors, free up workers
- **Test DAGs** - Unit tests and integration tests
- **Idempotent tasks** - Safe to retry

### Don'ts
- **Don't use `depends_on_past=True`** - Creates bottlenecks
- **Don't hardcode dates** - Use `{{ ds }}` macros
- **Don't use global state** - Tasks should be stateless
- **Don't skip catchup blindly** - Understand implications
- **Don't put heavy logic in DAG file** - Import from modules

## Resources

- [Airflow Documentation](https://airflow.apache.org/docs/)
- [Astronomer Guides](https://docs.astronomer.io/learn)
- [TaskFlow API](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/taskflow.html)
