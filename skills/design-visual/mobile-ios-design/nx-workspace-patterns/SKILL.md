---
name: nx-workspace-patterns
description: Configure and optimize Nx monorepo workspaces. Use when setting up Nx, configuring project boundaries, optimizing build caching, or implementing affected commands.
version: 1.0.0
dependencies: ["nodejs", "nx"]
---

# Nx Workspace Patterns

Production patterns for Nx monorepo management.

## When to Use This Skill

- Setting up new Nx workspaces
- Configuring project boundaries
- Optimizing CI with affected commands
- Implementing remote caching
- Managing dependencies between projects
- Migrating to Nx

## Core Concepts

### 1. Nx Architecture

```
workspace/
├── apps/              # Deployable applications
│   ├── web/
│   └── api/
├── libs/              # Shared libraries
│   ├── shared/
│   │   ├── ui/
│   │   └── utils/
│   └── feature/
│       ├── auth/
│       └── dashboard/
├── tools/             # Custom executors/generators
├── nx.json            # Nx configuration
└── workspace.json     # Project configuration
```

### 2. Library Types

| Type | Purpose | Example |
|------|---------|---------|
| **feature** | Smart components, business logic | `feature-auth` |
| **ui** | Presentational components | `ui-buttons` |
| **data-access** | API calls, state management | `data-access-api` |
| **utils** | Helper functions | `utils-formatting` |
| **types** | TypeScript definitions | `types-shared` |

### 3. Module Boundaries

```json
// nx.json
{
  "affected": {
    "defaultBase": "main"
  },
  "tasksRunnerOptions": {
    "default": {
      "runner": "nx/tasks-runners/default",
      "options": {
        "cacheableOperations": ["build", "test", "lint"]
      }
    }
  },
  "targetDefaults": {
    "build": {
      "dependsOn": ["^build"]
    }
  },
  "workspaceLayout": {
    "appsDir": "apps",
    "libsDir": "libs"
  }
}
```

## Templates

### Template 1: Nx Configuration

```json
// nx.json
{
  "$schema": "./node_modules/nx/schemas/nx-schema.json",
  "affected": {
    "defaultBase": "main"
  },
  "tasksRunnerOptions": {
    "default": {
      "runner": "nx/tasks-runners/default",
      "options": {
        "cacheableOperations": ["build", "test", "lint", "e2e"]
      }
    },
    "cloud": {
      "runner": "nx-cloud",
      "options": {
        "cacheableOperations": ["build", "test", "lint"],
        "accessToken": "NX_CLOUD_ACCESS_TOKEN",
        "parallel": 3
      }
    }
  },
  "targetDefaults": {
    "build": {
      "dependsOn": ["^build"],
      "inputs": ["production", "^production"]
    },
    "test": {
      "inputs": ["default", "^production", "{workspaceRoot}/jest.config.ts"]
    },
    "lint": {
      "inputs": [
        "default",
        "{workspaceRoot}/.eslintrc.json",
        "{workspaceRoot}/.eslintignore"
      ]
    }
  },
  "namedInputs": {
    "default": ["{projectRoot}/**/*", "sharedGlobals"],
    "sharedGlobals": ["{workspaceRoot}/babel.config.json"],
    "production": [
      "default",
      "!{projectRoot}/**/*.spec.ts",
      "!{projectRoot}/**/*.test.ts",
      "!{projectRoot}/**/*.stories.ts",
      "!{projectRoot}/**/*.md",
      "!{projectRoot}/.eslintrc.json",
      "!{projectRoot}/jest.config.ts"
    ]
  },
  "generators": {
    "@nx/react": {
      "application": {
        "style": "css",
        "linter": "eslint",
        "bundler": "webpack"
      },
      "library": {
        "style": "css",
        "linter": "eslint"
      },
      "component": {
        "style": "css"
      }
    }
  }
}
```

### Template 2: Project Configuration

```json
// apps/web/project.json
{
  "name": "web",
  "$schema": "../../node_modules/nx/schemas/project-schema.json",
  "sourceRoot": "apps/web/src",
  "projectType": "application",
  "tags": ["type:app", "scope:web"],
  "targets": {
    "build": {
      "executor": "@nx/webpack:webpack",
      "outputs": ["{options.outputPath}"],
      "defaultConfiguration": "production",
      "options": {
        "compiler": "babel",
        "outputPath": "dist/apps/web",
        "index": "apps/web/src/index.html",
        "main": "apps/web/src/main.tsx",
        "tsConfig": "apps/web/tsconfig.app.json",
        "assets": ["apps/web/src/assets"],
        "styles": ["apps/web/src/styles.css"]
      },
      "configurations": {
        "development": {
          "extractLicenses": false,
          "optimization": false,
          "sourceMap": true,
          "vendorChunk": true
        },
        "production": {
          "fileReplacements": [
            {
              "replace": "apps/web/src/environments/environment.ts",
              "with": "apps/web/src/environments/environment.prod.ts"
            }
          ],
          "optimization": true,
          "outputHashing": "all",
          "sourceMap": false,
          "namedChunks": false,
          "extractLicenses": true,
          "vendorChunk": false
        }
      }
    },
    "serve": {
      "executor": "@nx/webpack:dev-server",
      "options": {
        "buildTarget": "web:build",
        "hmr": true
      },
      "configurations": {
        "production": {
          "buildTarget": "web:build:production",
          "hmr": false
        }
      }
    },
    "lint": {
      "executor": "@nx/eslint:lint",
      "outputs": ["{options.outputFile}"],
      "options": {
        "lintFilePatterns": ["apps/web/**/*.{ts,tsx,js,jsx}"]
      }
    },
    "test": {
      "executor": "@nx/jest:jest",
      "outputs": ["{workspaceRoot}/coverage/apps/web"],
      "options": {
        "jestConfig": "apps/web/jest.config.ts",
        "passWithNoTests": true
      }
    }
  }
}
```

### Template 3: Module Boundary Rules

```json
// .eslintrc.json
{
  "root": true,
  "ignorePatterns": ["**/*"],
  "plugins": ["@nx"],
  "overrides": [
    {
      "files": ["*.ts", "*.tsx", "*.js", "*.jsx"],
      "rules": {
        "@nx/enforce-module-boundaries": [
          "error",
          {
            "enforceBuildableLibDependency": true,
            "allow": [],
            "depConstraints": [
              {
                "sourceTag": "scope:web",
                "onlyDependOnLibsWithTags": ["scope:web", "scope:shared"]
              },
              {
                "sourceTag": "scope:api",
                "onlyDependOnLibsWithTags": ["scope:api", "scope:shared"]
              },
              {
                "sourceTag": "scope:shared",
                "onlyDependOnLibsWithTags": ["scope:shared"]
              },
              {
                "sourceTag": "type:feature",
                "onlyDependOnLibsWithTags": ["type:ui", "type:data-access", "type:utils", "type:types"]
              },
              {
                "sourceTag": "type:ui",
                "onlyDependOnLibsWithTags": ["type:utils", "type:types"]
              },
              {
                "sourceTag": "type:data-access",
                "onlyDependOnLibsWithTags": ["type:utils", "type:types"]
              }
            ]
          }
        ]
      }
    }
  ]
}
```

### Template 4: Remote Cache Configuration

```json
// nx-cloud.json
{
  "nxCloudId": "your-cloud-id",
  "cacheDirectory": "./node_modules/.cache/nx",
  "tasksRunnerOptions": {
    "default": {
      "runner": "nx-cloud",
      "options": {
        "cacheableOperations": ["build", "test", "lint"],
        "accessToken": "NX_CLOUD_ACCESS_TOKEN",
        "parallel": 3,
        "encryptionKey": "NX_CLOUD_ENCRYPTION_KEY",
        "url": "https://nx.app"
      }
    }
  }
}
```

### Template 5: AWS S3 Remote Cache

```json
// nx.json (S3 cache)
{
  "tasksRunnerOptions": {
    "default": {
      "runner": "nx/tasks-runners/default",
      "options": {
        "cacheableOperations": ["build", "test", "lint"],
        "remoteCache": {
          "storage": "s3",
          "bucket": "your-nx-cache-bucket",
          "awsProfile": "default"
        }
      }
    }
  }
}
```

## Common Commands

```bash
# Generate new library
nx g @nx/react:lib feature-auth --directory=libs/web --tags=type:feature,scope:web

# Run affected tests
nx affected -t test --base=main

# View dependency graph
nx graph

# Run specific project
nx build web --configuration=production

# Reset cache
nx reset

# Run migrations
nx migrate latest
nx migrate --run-migrations
```

## Best Practices

### Do's
- **Use tags consistently** - Enforce with module boundaries
- **Enable caching early** - Significant CI savings
- **Keep libs focused** - Single responsibility
- **Use generators** - Ensure consistency
- **Document boundaries** - Help new developers

### Don'ts
- **Don't create circular deps** - Graph should be acyclic
- **Don't skip affected** - Test only what changed
- **Don't ignore boundaries** - Tech debt accumulates
- **Don't over-granularize** - Balance lib count

## Resources

- [Nx Documentation](https://nx.dev/getting-started/intro)
- [Module Boundaries](https://nx.dev/core-features/enforce-module-boundaries)
- [Nx Cloud](https://nx.app/)
