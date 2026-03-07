#!/bin/bash
# Installation script for backend-scaffolding skill

echo "🚀 Installing dependencies for backend-scaffolding skill..."

# Function to check if a command exists
command_exists() {
    command -v "$1" &> /dev/null
}

# Function to install with apt-get
install_apt() {
    if command_exists apt-get; then
        echo "📦 Installing $1 via apt-get..."
        apt-get update && apt-get install -y "$1"
    else
        echo "⚠️  apt-get not available, cannot install $1"
        return 1
    fi
}

# Function to install with pip
install_pip() {
    if command_exists pip3; then
        echo "📦 Installing $1 via pip3..."
        pip3 install "$1"
    elif command_exists pip; then
        echo "📦 Installing $1 via pip..."
        pip install "$1"
    else
        echo "⚠️  pip not available, cannot install $1"
        return 1
    fi
}

# Check and install Python 3
if ! command_exists python3; then
    echo "❌ Python3 not found"
    install_apt python3
fi

# Check and install pip
if ! command_exists pip3 && ! command_exists pip; then
    echo "📦 Installing pip..."
    if command_exists python3; then
        python3 -m ensurepip --upgrade
    fi
fi

# Check and install UV (recommended Python package manager)
if ! command_exists uv; then
    echo "📦 Installing UV package manager..."
    if command_exists curl; then
        curl -LsSf https://astral.sh/uv/install.sh | sh
        echo "✅ UV installed. Please restart your shell or run: source ~/.bashrc"
    else
        echo "⚠️  curl not available, installing via pip..."
        install_pip uv
    fi
else
    echo "✅ UV already installed"
fi

# Check and install Git
if ! command_exists git; then
    echo "📦 Installing Git..."
    install_apt git
else
    echo "✅ Git already installed"
fi

# Check and install Docker
if ! command_exists docker; then
    echo "📦 Installing Docker..."
    echo "⚠️  Docker installation requires manual steps on some systems"
    echo "   Please visit: https://docs.docker.com/engine/install/"
    echo "   Or run the convenience script:"
    echo "   curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh"
else
    echo "✅ Docker already installed"
fi

# Check and install Docker Compose
if ! command_exists docker-compose; then
    echo "📦 Installing Docker Compose..."
    if command_exists docker; then
        # Try to install via pip first
        if install_pip docker-compose; then
            echo "✅ Docker Compose installed via pip"
        else
            echo "⚠️  Could not install Docker Compose via pip"
            echo "   Please install manually: https://docs.docker.com/compose/install/"
        fi
    else
        echo "⚠️  Docker not installed, skipping Docker Compose"
    fi
else
    echo "✅ Docker Compose already installed"
fi

# Install common Python packages for backend development
echo "\n📦 Installing common Python packages..."
if command_exists uv; then
    echo "Installing with UV..."
    uv pip install fastapi uvicorn pydantic sqlalchemy alembic django djangorestframework strawberry graphene
elif command_exists pip3; then
    echo "Installing with pip3..."
    pip3 install fastapi uvicorn pydantic sqlalchemy alembic django djangorestframework strawberry graphene
elif command_exists pip; then
    echo "Installing with pip..."
    pip install fastapi uvicorn pydantic sqlalchemy alembic django djangorestframework strawberry graphene
else
    echo "⚠️  No Python package manager found, skipping package installation"
fi

# Create template directories if they don't exist
echo "\n📁 Setting up directory structure..."
mkdir -p templates scripts

# Create a basic FastAPI template if templates directory is empty
if [ ! -f "templates/fastapi-basic.py" ]; then
    cat > templates/fastapi-basic.py << 'TEMPLATE_EOF'
"""Basic FastAPI template for quick starts"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="FastAPI Project", version="1.0.0")

class HealthResponse(BaseModel):
    status: str
    version: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health() -> HealthResponse:
    return HealthResponse(status="healthy", version="1.0.0")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
TEMPLATE_EOF
    echo "✅ Created basic FastAPI template"
fi

# Create a basic Django project setup script
if [ ! -f "scripts/setup-django.sh" ]; then
    cat > scripts/setup-django.sh << 'SCRIPT_EOF'
#!/bin/bash
# Django project setup script

PROJECT_NAME="${1:-myproject}"

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Django
pip install django djangorestframework django-cors-headers

# Create Django project
django-admin startproject "$PROJECT_NAME" .

# Create requirements.txt
pip freeze > requirements.txt

echo "✅ Django project '$PROJECT_NAME' created"
echo "📋 Next steps:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Run migrations: python manage.py migrate"
echo "3. Start development server: python manage.py runserver"
SCRIPT_EOF
    chmod +x scripts/setup-django.sh
    echo "✅ Created Django setup script"
fi

echo "\n🎉 Installation complete!"
echo "\n📋 To verify installation, run:"
echo "   bash test.sh"
echo "\n🚀 To use the skill:"
echo "1. Review SKILL.md for framework options"
echo "2. Use the setup scripts in scripts/ directory"
echo "3. Customize templates for your specific needs"

