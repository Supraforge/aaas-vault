#!/bin/bash
# Health check for database-schema-validator skill

echo "🔍 Validating database-schema-validator..."

# Check 1: Python availability
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed or not in PATH"
    exit 1
else
    echo "✅ Python3 is available"
fi

# Check 2: Validate script exists
if [ ! -f "scripts/validate_schema.py" ]; then
    echo "❌ validate_schema.py script not found"
    exit 1
else
    echo "✅ validate_schema.py script found"
fi

# Check 3: Script is executable
if [ -x "scripts/validate_schema.py" ]; then
    echo "✅ validate_schema.py is executable"
else
    echo "⚠️  validate_schema.py is not executable, making it executable"
    chmod +x scripts/validate_schema.py
fi

# Check 4: Test with a simple valid schema
cat > /tmp/test_valid_schema.sql << 'SQL_EOF'
CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100)
);
SQL_EOF

python3 scripts/validate_schema.py /tmp/test_valid_schema.sql
if [ $? -eq 0 ]; then
    echo "✅ Validation script works correctly"
else
    echo "❌ Validation script failed on valid schema"
    exit 1
fi

# Check 5: Test with invalid schema (DROP TABLE)
cat > /tmp/test_invalid_schema.sql << 'SQL_EOF'
DROP TABLE users;
CREATE TABLE Users (
    id INT PRIMARY KEY,
    username VARCHAR(50)
);
SQL_EOF

python3 scripts/validate_schema.py /tmp/test_invalid_schema.sql
if [ $? -eq 1 ]; then
    echo "✅ Validation script correctly rejects invalid schema"
else
    echo "❌ Validation script should reject invalid schema"
    exit 1
fi

# Cleanup
rm -f /tmp/test_valid_schema.sql /tmp/test_invalid_schema.sql

echo "🚀 database-schema-validator is ready."
exit 0
