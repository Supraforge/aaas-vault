# Enhancement Patterns

Common scenarios and enhancement strategies for different types of development requests.

## Feature Addition Patterns

### New UI Component

**Original:** "버튼 컴포넌트 만들어줘"

**Enhancement checklist:**
- Check existing component library (shadcn/ui, MUI, custom)
- Review existing button variants in codebase
- Identify styling system (CSS modules, Tailwind, styled-components)
- Check TypeScript prop patterns
- Find testing approach for components

**Enhanced structure:**
```
Create a Button component following project patterns:
- Location: /components/ui/Button.tsx
- Props: Match existing component prop patterns
- Variants: [list existing button types in project]
- Styling: [styling approach used]
- Accessibility: Match existing ARIA patterns
- Testing: Add tests in __tests__/components/
```

### API Endpoint

**Original:** "사용자 목록 API 만들어줘"

**Enhancement checklist:**
- Identify API framework (Express, FastAPI, Next.js API routes)
- Check existing endpoint patterns
- Review authentication/authorization approach
- Find database/ORM patterns
- Check error handling conventions
- Identify response format standards

**Enhanced structure:**
```
Create user list API endpoint:
- Route: [follow existing route structure]
- Method: GET
- Auth: [existing auth middleware]
- Query params: pagination, filters (match existing patterns)
- Response format: [existing JSON structure]
- Error handling: [existing error response format]
- Database: [ORM/query pattern used]
```

### State Management

**Original:** "장바구니 상태 관리 추가해줘"

**Enhancement checklist:**
- Identify state management library (Redux, Zustand, Context, Jotai)
- Review existing store structure
- Check action/reducer patterns
- Find persistence approach (localStorage, sessionStorage)
- Identify type definitions location

**Enhanced structure:**
```
Add cart state management:
- Store: [library being used]
- Location: [existing store directory]
- State shape: Match existing entity patterns
- Actions: [naming convention used]
- Selectors: [existing selector patterns]
- Persistence: [current persistence strategy]
- Types: [type definition location]
```

## Bug Fix Patterns

### Runtime Error

**Original:** "이 에러 고쳐줘"

**Enhancement checklist:**
- Identify error source file and line
- Check related dependencies
- Review error handling patterns in similar code
- Find test coverage for affected code
- Check recent changes to related files

**Enhanced structure:**
```
Fix [error type] in [file]:
- Error location: [file:line]
- Related files: [list dependencies]
- Current behavior: [describe issue]
- Expected behavior: [describe fix]
- Error handling: Match existing try-catch patterns
- Testing: Add regression test in [test location]
```

### Logic Error

**Original:** "계산이 잘못됐어"

**Enhancement checklist:**
- Identify calculation logic location
- Check input/output types
- Review similar calculations in codebase
- Find existing validation patterns
- Check edge cases handling

## Refactoring Patterns

### Code Organization

**Original:** "이 파일 리팩토링해줘"

**Enhancement checklist:**
- Understand current file structure
- Identify separation concerns
- Check existing module patterns
- Review import conventions
- Find related files to update

**Enhanced structure:**
```
Refactor [file] following project patterns:
- Split into: [component structure used in project]
- Extract utilities to: [utility directory location]
- Update imports: [existing import style]
- Maintain: [critical dependencies]
- Update tests: [test locations to modify]
```

### Performance Optimization

**Original:** "이 코드 최적화해줘"

**Enhancement checklist:**
- Profile current performance
- Identify optimization approach used in project (memoization, lazy loading)
- Check bundler/build tool capabilities
- Review caching strategies in use
- Find monitoring/metrics approach

## Database/Data Patterns

### Schema Changes

**Original:** "데이터베이스에 필드 추가해줘"

**Enhancement checklist:**
- Identify ORM/migration tool
- Check existing migration patterns
- Review schema conventions
- Find related model/type definitions
- Check seed data approach

**Enhanced structure:**
```
Add field to [table]:
- Migration: [migration tool and location]
- Field definition: [follow existing field patterns]
- Model update: [ORM model location]
- Type update: [TypeScript interface location]
- Seed data: [seed file to update]
```

### Query Optimization

**Original:** "쿼리 최적화해줘"

**Enhancement checklist:**
- Identify query builder/ORM
- Check existing index patterns
- Review join strategies used
- Find caching approach
- Check query logging setup

## Testing Patterns

### Unit Tests

**Original:** "테스트 작성해줘"

**Enhancement checklist:**
- Identify test framework (Jest, Vitest, PyTest)
- Review existing test file structure
- Check mocking patterns
- Find test data/fixtures approach
- Review assertion style

**Enhanced structure:**
```
Add tests for [component/function]:
- Test file: [location following convention]
- Framework: [test framework in use]
- Mocking: [existing mock patterns]
- Test data: [fixture/factory location]
- Coverage: [minimum coverage requirement]
```

### Flutter Widget Tests

**Original:** "위젯 테스트 작성해줘"

**Enhancement checklist:**
- Check test file location (test/ directory)
- Review existing widget test patterns
- Identify mock patterns (mockito, mocktail)
- Check provider/bloc testing approach
- Find golden test usage

**Enhanced structure:**
```
Add widget tests for [screen/widget]:
- Test file: test/presentation/[feature]/[widget]_test.dart
- Setup: testWidgets with WidgetTester
- Mocking: Mock repositories/providers
- State management testing:
  - Provider: ChangeNotifierProvider with mock
  - Bloc: BlocProvider with mock bloc
  - Riverpod: ProviderScope with overrides
- Finders: find.byType, find.text, find.byKey
- Interactions: tester.tap, tester.enterText
- Assertions: expect, findsOneWidget, findsNothing
- Pump: tester.pump(), tester.pumpAndSettle()
```

## Mobile App Patterns

### Flutter Screen/Feature

**Original:** "프로필 화면 만들어줘"

**Enhancement checklist:**
- Identify app architecture (Clean Architecture, MVVM)
- Check state management (Provider, Bloc, Riverpod, GetX)
- Review navigation approach
- Find existing screen patterns
- Check responsive design strategy
- Identify localization approach

**Enhanced structure:**
```
Create profile screen following project architecture:

1. Presentation Layer:
   - lib/presentation/profile/profile_screen.dart
   - Widget type: [StatefulWidget/ConsumerWidget/BlocConsumer]
   - Layout: Match existing screen structure
   - AppBar: Follow existing AppBar style
   - Responsive: Use MediaQuery if project uses it

2. State Management:
   [Based on project's approach]
   - Provider: profile_provider.dart with ChangeNotifier
   - Bloc: profile_bloc.dart, profile_event.dart, profile_state.dart
   - Riverpod: profile_provider.dart with StateNotifier
   - GetX: profile_controller.dart with GetxController

3. Data Layer:
   - Repository: lib/data/repositories/profile_repository.dart
   - Model: lib/data/models/profile_model.dart with fromJson/toJson
   - API: Use existing Dio/http client pattern

4. Domain Layer (if Clean Architecture):
   - Entity: lib/domain/entities/profile.dart
   - Use case: lib/domain/usecases/get_profile.dart

5. Navigation:
   - Route definition: [follow existing routing pattern]
   - Access from: [menu/drawer/bottom navigation]

6. UI Components:
   - Reuse existing widgets: [list existing components]
   - Form fields: Match existing input styling
   - Buttons: Use existing button widgets
   - Loading: CircularProgressIndicator with existing pattern
   - Error: SnackBar/Dialog matching project style

7. Assets:
   - Profile placeholder: assets/images/
   - Update pubspec.yaml if needed

8. Localization:
   - Add strings to: [existing l10n approach]
   - Use: AppLocalizations.of(context) or Get.find()

9. Testing:
   - Widget test: test/presentation/profile/profile_screen_test.dart
   - Repository test: test/data/repositories/profile_repository_test.dart
```

### Flutter API Integration

**Original:** "상품 목록 API 연결해줘"

**Enhancement checklist:**
- Identify HTTP client (Dio, http package)
- Check existing API client configuration
- Review error handling approach
- Find model serialization pattern (json_serializable, freezed)
- Check caching strategy

**Enhanced structure:**
```
Integrate product list API:

1. API Client:
   - Location: lib/data/datasources/remote/product_api.dart
   - Use existing Dio instance with interceptors
   - Endpoint: GET /api/products
   - Headers: Match existing auth/content-type

2. Model:
   - lib/data/models/product_model.dart
   - Serialization: [json_serializable/freezed/manual]
   - Fields: Match API response structure
   - fromJson/toJson methods

3. Repository:
   - lib/data/repositories/product_repository.dart
   - Interface: lib/domain/repositories/product_repository.dart
   - Methods: Future<List<Product>> getProducts()
   - Error handling: try-catch with Either/Result type

4. State Management:
   - Provider: ProductListProvider with loading/error states
   - Bloc: ProductListBloc with events (Load, Refresh)
   - Riverpod: FutureProvider or AsyncNotifier
   
5. UI Update:
   - Show loading: CircularProgressIndicator
   - Display list: ListView.builder with product items
   - Handle errors: Show retry option
   - Pull to refresh: RefreshIndicator

6. Caching (if needed):
   - Use existing cache approach (Hive, SharedPreferences)
   - Cache duration: [project standard]

7. Pagination (if applicable):
   - Infinite scroll with ScrollController
   - Load more indicator at bottom
```

## Documentation Patterns

### README Updates

**Original:** "문서 업데이트해줘"

**Enhancement checklist:**
- Review existing README structure
- Check documentation style
- Find related docs to update
- Review example format
- Check if auto-generated docs exist

**Enhanced structure:**
```
Update documentation:
- Main README: [section to update]
- API docs: [doc tool in use]
- Examples: [example format used]
- Changelog: [changelog location]
- Comments: [JSDoc/docstring style]
```

## Tips for Pattern Recognition

### Quick Context Gathering

1. **Project root files**: Check package.json, requirements.txt for dependencies
2. **Config files**: Review .eslintrc, tsconfig.json for conventions
3. **Directory structure**: Scan for organization patterns
4. **Recent commits**: Check git history for active patterns

### Common Warning Signs

- Multiple approaches for same task → clarify preferred pattern
- Outdated dependencies → mention version constraints
- Missing tests → emphasize test requirements
- Inconsistent naming → enforce existing convention
