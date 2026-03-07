# Framework-Specific Guides

Quick reference for enhancing prompts in popular frameworks.

## Frontend Frameworks

### Next.js

**Key context to gather:**
- App Router vs Pages Router
- TypeScript usage
- API route patterns
- Server/Client component split
- State management approach
- CSS solution (Tailwind, CSS Modules, styled-components)

**Enhancement focus:**
```
- Route structure: app/[route]/page.tsx or pages/[route].tsx
- Server components: Default in App Router
- Client components: 'use client' directive
- Data fetching: async components, fetch, SWR, React Query
- Metadata: generateMetadata for SEO
- API routes: app/api/[route]/route.ts or pages/api/[route].ts
```

### React (Create React App / Vite)

**Key context to gather:**
- State management (Context, Redux, Zustand)
- Routing library (React Router)
- Component patterns (functional vs class)
- Build tool (Webpack, Vite)
- CSS approach

**Enhancement focus:**
```
- Component location: src/components/
- Hooks usage: useState, useEffect, custom hooks
- Route definitions: React Router configuration
- State structure: Global vs local state
- Build configuration: vite.config.ts or webpack config
```

### Vue.js

**Key context to gather:**
- Vue 2 vs Vue 3
- Composition API vs Options API
- State management (Vuex, Pinia)
- TypeScript integration
- Component style (SFC structure)

**Enhancement focus:**
```
- Component structure: <template>, <script>, <style>
- Composition API: setup(), ref, reactive
- Store: Vuex modules or Pinia stores
- Router: vue-router configuration
- Props and emits: defineProps, defineEmits
```

### Angular

**Key context to gather:**
- Angular version
- Module structure
- Component/Service patterns
- RxJS usage
- TypeScript strict mode

**Enhancement focus:**
```
- Module organization: feature modules
- Component structure: @Component decorator
- Services: @Injectable and dependency injection
- Observables: RxJS operators
- Forms: Reactive vs template-driven
```

## Backend Frameworks

### Express.js

**Key context to gather:**
- Middleware patterns
- Route organization
- Database/ORM (Prisma, TypeORM, Sequelize)
- Authentication approach
- TypeScript usage

**Enhancement focus:**
```
- Route structure: /routes directory
- Middleware: auth, validation, error handling
- Controllers: separation of concerns
- Database: ORM models and migrations
- Error handling: centralized error middleware
```

### FastAPI (Python)

**Key context to gather:**
- Router organization
- Pydantic models
- Database/ORM (SQLAlchemy, Tortoise)
- Authentication (OAuth2, JWT)
- Async patterns

**Enhancement focus:**
```
- Routers: APIRouter organization
- Models: Pydantic schemas vs SQLAlchemy models
- Dependencies: Depends() for injection
- Async routes: async def endpoints
- Documentation: automatic OpenAPI docs
```

### Django

**Key context to gather:**
- Django version
- App structure
- ORM usage
- Django REST Framework (if API)
- Template vs API approach

**Enhancement focus:**
```
- Apps: Django app organization
- Models: ORM model definitions
- Views: function-based vs class-based
- URLs: url patterns
- Migrations: makemigrations workflow
```

### Spring Boot (Java)

**Key context to gather:**
- Spring Boot version
- Maven vs Gradle
- JPA/Hibernate usage
- Controller patterns
- Service layer structure

**Enhancement focus:**
```
- Controllers: @RestController patterns
- Services: @Service and business logic
- Repositories: JPA repositories
- Configuration: application.properties/yml
- DTOs: data transfer objects
```

## Full-Stack Frameworks

### Ruby on Rails

**Key context to gather:**
- Rails version
- MVC structure
- ActiveRecord patterns
- Asset pipeline vs Webpacker
- Testing framework (RSpec, Minitest)

**Enhancement focus:**
```
- Models: ActiveRecord associations
- Controllers: RESTful actions
- Views: ERB templates or API mode
- Routes: config/routes.rb
- Migrations: db/migrate/
```

### Laravel (PHP)

**Key context to gather:**
- Laravel version
- Eloquent ORM usage
- Blade templates
- API vs full-stack
- Testing approach

**Enhancement focus:**
```
- Models: Eloquent model patterns
- Controllers: resource controllers
- Routes: web.php vs api.php
- Migrations: database/migrations/
- Middleware: app/Http/Middleware/
```

## Mobile Frameworks

### React Native

**Key context to gather:**
- Expo vs bare workflow
- Navigation library (React Navigation)
- State management
- Native modules usage
- Platform-specific code

**Enhancement focus:**
```
- Components: React Native primitives
- Navigation: stack, tab, drawer navigators
- Platform code: Platform.select()
- Native modules: linking and configuration
- Styling: StyleSheet API
```

### Flutter

**Key context to gather:**
- Flutter version (2.x vs 3.x+)
- State management (Provider, Riverpod, Bloc, GetX, MobX)
- Null safety enabled
- Package dependencies (pubspec.yaml)
- Platform-specific code (iOS/Android)
- Architecture pattern (Clean Architecture, MVVM, MVC)
- Routing approach (Navigator 1.0, Navigator 2.0, go_router, auto_route)
- Network layer (Dio, http package)
- Local storage (Hive, SharedPreferences, SQLite)

**Enhancement focus:**
```
- Widgets: StatelessWidget vs StatefulWidget
  - Prefer StatelessWidget for UI-only components
  - Use StatefulWidget only when managing local state
  - Consider using Hooks (flutter_hooks) if in use

- State Management Pattern:
  - Provider: ChangeNotifier, Consumer, Provider.of
  - Riverpod: StateProvider, StateNotifierProvider, ConsumerWidget
  - Bloc: BlocProvider, BlocBuilder, BlocListener, BlocConsumer
  - GetX: GetxController, Obx, GetBuilder

- Navigation:
  - Navigator 1.0: Named routes in MaterialApp
  - Navigator 2.0: Router, RouterDelegate, RouteInformationParser
  - go_router: GoRoute configuration, nested routes
  - auto_route: @AutoRoute annotations, generated routing

- Project Structure:
  lib/
  ├── core/          (constants, themes, utils)
  ├── data/          (repositories, data sources, models)
  ├── domain/        (entities, use cases)
  ├── presentation/  (screens, widgets, state management)
  └── main.dart

- UI Components:
  - Material vs Cupertino widgets
  - Custom themes: ThemeData configuration
  - Responsive design: MediaQuery, LayoutBuilder
  - Custom widgets: reusable component patterns

- Data Layer:
  - Models: fromJson/toJson serialization
  - Repositories: abstraction layer
  - API clients: Dio interceptors, error handling
  - Local storage: async data persistence

- Platform Channels:
  - MethodChannel for platform-specific code
  - EventChannel for streaming data
  - Platform-specific implementations (iOS/Android)

- Assets and Resources:
  - pubspec.yaml: asset declarations
  - Image loading: AssetImage, NetworkImage, CachedNetworkImage
  - Fonts: custom font configuration
  - Localization: intl package, arb files
```

**Common Flutter Enhancement Patterns:**

**Example 1 - Feature Addition:**
```
Original: "로그인 화면 만들어줘"

Enhanced:
Create login screen following project architecture:

1. UI Layer (lib/presentation/auth/):
   - login_screen.dart: StatefulWidget with form
   - Use existing TextFormField styling from theme
   - Apply validation matching existing patterns
   - Follow project's responsive design approach

2. State Management (based on project):
   - Provider: Create AuthProvider with login method
   - Bloc: Create LoginBloc with LoginEvent and LoginState
   - Riverpod: Create loginProvider with StateNotifier
   - GetX: Create LoginController with login method

3. Data Layer (lib/data/):
   - auth_repository.dart: login API call
   - Use existing Dio instance and interceptors
   - Follow error handling pattern (try-catch, Either type)
   - user_model.dart: Add/update user model with serialization

4. Navigation:
   - After successful login, navigate to home
   - Use existing navigation pattern (context.go, Navigator.push)
   - Handle back button with WillPopScope if needed

5. Validation:
   - Email validator: match existing validation utils
   - Password strength: follow existing requirements
   - Form key: GlobalKey<FormState>

6. Error Handling:
   - Show SnackBar for errors (match existing UI feedback)
   - Loading state: CircularProgressIndicator
   - Disable button during loading

7. Testing:
   - Widget tests: test/presentation/auth/login_screen_test.dart
   - Unit tests: test/data/auth_repository_test.dart
   - Follow existing test patterns (mockito, mocktail)
```

**Example 2 - State Management Integration:**
```
Original: "장바구니 기능 추가해줘"

Enhanced based on Riverpod project:

1. State (lib/presentation/cart/):
   - cart_state.dart: CartState class (items, total, loading)
   - cart_notifier.dart: StateNotifier<CartState>
   - cart_provider.dart: StateNotifierProvider definition

2. UI (lib/presentation/cart/):
   - cart_screen.dart: ConsumerWidget
   - Use ref.watch(cartProvider) for state
   - Use ref.read(cartProvider.notifier) for actions
   - cart_item_widget.dart: reusable cart item component

3. Models (lib/domain/):
   - cart_item.dart: CartItem entity with Freezed
   - Follow existing entity patterns
   - Include copyWith, toJson, fromJson

4. Repository (lib/data/):
   - cart_repository.dart: local storage operations
   - Use existing Hive box or SharedPreferences approach
   - Implement caching strategy

5. Actions:
   - addToCart(Product product)
   - removeFromCart(String productId)
   - updateQuantity(String productId, int quantity)
   - clearCart()
   - Match existing method naming conventions

6. UI Integration:
   - Add cart icon to AppBar with badge (item count)
   - Use existing badge widget if available
   - Navigate to cart on tap
```

**Flutter-Specific Considerations:**

- **Null Safety**: Use sound null safety (required, ?, !)
- **Async Operations**: FutureBuilder, StreamBuilder, or state management
- **Immutability**: Consider using Freezed for immutable models
- **Performance**: 
  - Use const constructors where possible
  - Implement shouldRepaint for CustomPainters
  - ListView.builder for long lists
- **Testing**:
  - Widget tests: testWidgets, find, expect
  - Golden tests: matchesGoldenFile
  - Integration tests: flutter_driver or integration_test

## Enhancement Strategies by Framework

### For Component-Based Frameworks (React, Vue, Angular)

1. Check existing component structure
2. Identify state management pattern
3. Review prop/event patterns
4. Check testing approach (component tests)
5. Verify styling solution

### For MVC Frameworks (Rails, Django, Laravel)

1. Understand model relationships
2. Check controller patterns
3. Review route organization
4. Identify view/template approach
5. Verify migration patterns

### For API Frameworks (Express, FastAPI)

1. Check route organization
2. Review middleware patterns
3. Identify validation approach
4. Check authentication/authorization
5. Verify error handling strategy

## Quick Detection Commands

```bash
# Next.js
ls app/ pages/ next.config.js

# React
ls src/App.tsx package.json vite.config.ts

# Vue
ls src/main.ts vue.config.js

# Angular  
ls angular.json src/app/app.module.ts

# Express
ls index.js routes/ middleware/

# FastAPI
ls main.py routers/ models/

# Django
ls manage.py settings.py

# Rails
ls config/routes.rb app/models/

# React Native
ls App.tsx app.json

# Flutter
ls pubspec.yaml lib/main.dart
```

## Framework Version Considerations

### Breaking Changes to Note

- **Next.js 13+**: App Router vs Pages Router
- **React 18+**: Concurrent features, automatic batching
- **Vue 3**: Composition API, Teleport
- **Angular 14+**: Standalone components
- **Django 3.2+**: Async views support
- **Rails 7+**: Hotwire/Turbo
- **Spring Boot 3+**: Jakarta EE namespace

When enhancing prompts, always note the framework version if it affects implementation patterns.
