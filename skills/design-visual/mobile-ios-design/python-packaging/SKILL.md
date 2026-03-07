---
name: python-packaging
description: Create distributable Python packages with proper project structure, setup.py/pyproject.toml, and publishing to PyPI. Use when packaging Python libraries, creating CLI tools, or distributing Python code.
version: 1.0.0
dependencies: ["python3", "pip", "build", "twine", "setuptools", "wheel"]
---

# Python Packaging

Comprehensive guide to creating, structuring, and distributing Python packages using modern packaging tools, pyproject.toml, and publishing to PyPI.

## When to Use This Skill

- Creating Python libraries for distribution
- Building command-line tools with entry points
- Publishing packages to PyPI or private repositories
- Setting up Python project structure
- Creating installable packages with dependencies
- Building wheels and source distributions
- Versioning and releasing Python packages
- Creating namespace packages
- Implementing package metadata and classifiers

## Core Concepts

### 1. Package Structure
- **Source layout**: `src/package_name/` (recommended)
- **Flat layout**: `package_name/` (simpler but less flexible)
- **Package metadata**: pyproject.toml, setup.py, or setup.cfg
- **Distribution formats**: wheel (.whl) and source distribution (.tar.gz)
- **Entry points**: console_scripts for CLI tools
- **Package data**: non-Python files included in distributions

### 2. Modern Packaging (pyproject.toml)

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "my-package"
version = "0.1.0"
description = "My awesome package"
readme = "README.md"
authors = [{name = "Your Name", email = "you@example.com"}]
license = {text = "MIT"}
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

[project.urls]
Homepage = "https://github.com/username/my-package"
Documentation = "https://github.com/username/my-package#readme"
Repository = "https://github.com/username/my-package.git"

[project.optional-dependencies]
dev = ["pytest>=7.0", "black", "mypy"]
test = ["pytest>=7.0"]

[tool.setuptools]
package-dir = { "" = "src" }

[tool.setuptools.packages.find]
where = ["src"]
```

### 3. Traditional Packaging (setup.py)

```python
from setuptools import setup, find_packages

setup(
    name="my-package",
    version="0.1.0",
    description="My awesome package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="you@example.com",
    url="https://github.com/username/my-package",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0",
        "pandas>=1.5.0",
    ],
    extras_require={
        "dev": ["pytest>=7.0", "black", "mypy"],
        "test": ["pytest>=7.0"],
    },
    entry_points={
        "console_scripts": [
            "my-cli=my_package.cli:main",
        ],
    },
    include_package_data=True,
)
```

### 4. Building and Distributing

```bash
# Install build tools
pip install build twine

# Build distributions
python -m build

# Check distributions
twine check dist/*

# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*
```

### 5. Versioning Strategies

- **Semantic Versioning** (SemVer): MAJOR.MINOR.PATCH
- **Calendar Versioning** (CalVer): YYYY.MM.MICRO
- **Pre-release versions**: 1.0.0a1 (alpha), 1.0.0b1 (beta), 1.0.0rc1 (release candidate)
- **Post-release versions**: 1.0.0.post1 (post-release)
- **Development versions**: 1.0.0.dev1 (development)

### 6. Private Package Indexes

```bash
pip install my-package --index-url https://private.pypi.org/simple/

# Or add to pip.conf
[global]
index-url = https://private.pypi.org/simple/
extra-index-url = https://pypi.org/simple/

# Upload to private index
twine upload --repository-url https://private.pypi.org/ dist/*
```

## File Templates

### .gitignore for Python Packages

```gitignore
# Build artifacts
build/
dist/
*.egg-info/
*.egg
.eggs/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so

# Virtual environments
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp

# Testing
.pytest_cache/
.coverage
htmlcov/

# Distribution
*.whl
*.tar.gz
```

### MANIFEST.in

```
# MANIFEST.in
include README.md
include LICENSE
include pyproject.toml

recursive-include src/my_package/data *.json
recursive-include src/my_package/templates *.html
recursive-exclude * __pycache__
recursive-exclude * *.py[co]
```

## Checklist for Publishing

- [ ] Code is tested (pytest passing)
- [ ] Documentation is complete (README, docstrings)
- [ ] Version number updated
- [ ] CHANGELOG.md updated
- [ ] License file included
- [ ] pyproject.toml is complete
- [ ] Package builds without errors
- [ ] Installation tested in clean environment
- [ ] CLI tools work (if applicable)
- [ ] PyPI metadata is correct (classifiers, keywords)
- [ ] GitHub repository linked
- [ ] Tested on TestPyPI first
- [ ] Git tag created for release

## Resources

- **Python Packaging Guide**: https://packaging.python.org/
- **PyPI**: https://pypi.org/
- **TestPyPI**: https://test.pypi.org/
- **setuptools documentation**: https://setuptools.pypa.io/
- **build**: https://pypa-build.readthedocs.io/
- **twine**: https://twine.readthedocs.io/

## Best Practices Summary

1. **Use src/ layout** for cleaner package structure
2. **Use pyproject.toml** for modern packaging
3. **Pin build dependencies** in build-system.requires
4. **Version appropriately** with semantic versioning
5. **Include all metadata** (classifiers, URLs, etc.)
6. **Test installation** in clean environments
7. **Use TestPyPI** before publishing to PyPI
8. **Document thoroughly** with README and docstrings
9. **Include LICENSE** file
10. **Automate publishing** with CI/CD
