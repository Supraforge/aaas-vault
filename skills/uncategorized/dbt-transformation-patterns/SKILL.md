---
name: dbt-transformation-patterns
description: >-
  Master dbt (data build tool) for analytics engineering with model
  organization, testing, documentation, and incremental strategies. Use when
  building data transformations, creating data models, or implementing analytics
  engineering best practices.
version: 1.0.0
dependencies:
  - python3
  - dbt
compatibility: 'agent-zero, claude-code, cursor'
---

# dbt Transformation Patterns

Production-ready patterns for dbt (data build tool) including model organization, testing strategies, documentation, and incremental processing.

## When to Use This Skill

- Building data transformation pipelines with dbt
- Organizing models into staging, intermediate, and marts layers
- Implementing data quality tests
- Creating incremental models for large datasets
- Documenting data models and lineage
- Setting up dbt project structure

## Core Concepts

### 1. Project Structure

Organize dbt projects with clear separation of concerns:

```yaml
# dbt_project.yml
name: my_project
version: '1.0.0'
profile: my_project

model-paths: ["models"]
test-paths: ["tests"]
analysis-paths: ["analyses"]
macro-paths: ["macros"]
seed-paths: ["data"]
docs-paths: ["docs"]
asset-paths: ["assets"]

target-path: "target"  # directory for compiled files
clean-targets:         # directories to be removed by `dbt clean`
  - "target"
  - "dbt_packages"
```

### 2. Model Layers

Follow a layered architecture for maintainability:

1. **Staging models** - Raw data transformations, basic cleaning
2. **Intermediate models** - Business logic, joins, aggregations
3. **Mart models** - Final business-facing tables

### 3. Testing Strategy

Implement comprehensive data quality checks:

```sql
-- models/staging/stg_customers.sql
{{ config(
    materialized='view',
    tags=['staging']
) }}

SELECT
    customer_id,
    customer_name,
    email,
    created_at
FROM {{ source('raw', 'customers') }}

-- Add tests in schema.yml
version: 2

models:
  - name: stg_customers
    description: "Staging model for customer data"
    columns:
      - name: customer_id
        description: "Primary key for customers"
        tests:
          - unique
          - not_null
      - name: email
        description: "Customer email address"
        tests:
          - not_null
          - accepted_values:
              values: ['@']  # Basic email validation
```

### 4. Incremental Models

Optimize large datasets with incremental processing:

```sql
-- models/marts/dim_customers.sql
{{ config(
    materialized='incremental',
    unique_key='customer_id',
    incremental_strategy='merge',
    merge_update_columns=['customer_name', 'email', 'updated_at']
) }}

WITH latest_customers AS (
    SELECT
        customer_id,
        customer_name,
        email,
        created_at,
        updated_at,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id 
            ORDER BY updated_at DESC
        ) as rn
    FROM {{ ref('stg_customers') }}
    {% if is_incremental() %}
    WHERE updated_at > (SELECT MAX(updated_at) FROM {{ this }})
    {% endif %}
)

SELECT
    customer_id,
    customer_name,
    email,
    created_at,
    updated_at
FROM latest_customers
WHERE rn = 1
```

### 5. Documentation

Create self-documenting data models:

```yaml
# models/schema.yml
version: 2

models:
  - name: dim_customers
    description: "Dimension table for customer information"
    columns:
      - name: customer_id
        description: "Primary key for customers"
      - name: customer_name
        description: "Full name of the customer"
      - name: email
        description: "Customer email address for communication"
      - name: created_at
        description: "Timestamp when the customer was first created"
      - name: updated_at
        description: "Timestamp of the last update to this record"

sources:
  - name: raw
    description: "Raw data from source systems"
    tables:
      - name: customers
        description: "Raw customer data from CRM system"
        columns:
          - name: customer_id
            description: "Customer identifier from source"
          - name: customer_name
            description: "Customer name from source"
```

### 6. Macros for Reusability

Create reusable SQL components:

```sql
-- macros/generate_surrogate_key.sql
{% macro generate_surrogate_key(field_list) -%}
    {{ return(adapter.dispatch('generate_surrogate_key', 'dbt')(field_list)) }}
{%- endmacro %}

{% macro default__generate_surrogate_key(field_list) -%}
    MD5(
        {%- for field in field_list -%}
            {% if not loop.first %} || '|' || {% endif %}
            COALESCE(CAST({{ field }} AS VARCHAR), '')
        {%- endfor -%}
    )
{%- endmacro %}

-- Usage in models
SELECT
    {{ generate_surrogate_key(['customer_id', 'order_date']) }} as order_key,
    customer_id,
    order_date,
    amount
FROM {{ ref('stg_orders') }}
```

## Workflow

1. **Analyze Requirements** - Understand source data and business needs
2. **Design Model Layers** - Plan staging, intermediate, and mart models
3. **Implement Staging Models** - Create initial data transformations
4. **Add Tests** - Implement data quality checks
5. **Build Business Logic** - Create intermediate and mart models
6. **Document** - Add descriptions and lineage
7. **Optimize** - Implement incremental models for large datasets
8. **Deploy** - Set up CI/CD for dbt runs

## Best Practices

1. **Version Control** - Keep all dbt code in Git
2. **Environment Separation** - Use different profiles for dev/staging/prod
3. **CI/CD Integration** - Run tests on every pull request
4. **Monitoring** - Track model run times and test failures
5. **Documentation First** - Write descriptions before implementing models
6. **Incremental Thinking** - Design for scalability from the start

## Common Patterns

### Pattern 1: Slowly Changing Dimensions (SCD)

```sql
-- Type 2 SCD implementation
{{ config(
    materialized='incremental',
    unique_key='customer_scd_key'
) }}

WITH scd_logic AS (
    SELECT
        customer_id,
        customer_name,
        email,
        effective_date,
        COALESCE(
            LEAD(effective_date) OVER (
                PARTITION BY customer_id 
                ORDER BY effective_date
            ) - INTERVAL '1 day',
            '9999-12-31'
        ) as end_date,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id 
            ORDER BY effective_date DESC
        ) = 1 as is_current
    FROM {{ ref('stg_customer_changes') }}
)

SELECT
    {{ generate_surrogate_key(['customer_id', 'effective_date']) }} as customer_scd_key,
    customer_id,
    customer_name,
    email,
    effective_date,
    end_date,
    is_current
FROM scd_logic
```

### Pattern 2: Data Vault Modeling

```sql
-- Hub table
{{ config(materialized='table') }}

SELECT
    MD5(customer_id) as customer_hkey,
    customer_id,
    LOAD_TIMESTAMP as load_date,
    'CRM' as record_source
FROM {{ source('raw', 'customers') }}

-- Satellite table
{{ config(materialized='table') }}

SELECT
    MD5(customer_id) as customer_hkey,
    customer_name,
    email,
    created_at,
    LOAD_TIMESTAMP as load_date,
    'CRM' as record_source
FROM {{ source('raw', 'customers') }}
```

## Troubleshooting

### Common Issues

1. **Connection Errors** - Check profiles.yml and database permissions
2. **Test Failures** - Review data quality and test logic
3. **Performance Issues** - Optimize with incremental models and indexes
4. **Documentation Gaps** - Ensure all models have descriptions

### Debugging Commands

```bash
# Test connection
dbt debug

# Run specific model
dbt run --models stg_customers

# Run tests
dbt test --models stg_customers

# Generate documentation
dbt docs generate

# Serve documentation
dbt docs serve
```

## Resources

- [dbt Documentation](https://docs.getdbt.com/)
- [dbt Discourse Community](https://discourse.getdbt.com/)
- [dbt Labs Blog](https://blog.getdbt.com/)
