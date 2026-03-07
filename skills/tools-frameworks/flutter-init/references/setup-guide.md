# Flutter Init 상세 가이드

## 전체 Setup 프로세스

### 1. 프로젝트 생성

**중요**: Android(Kotlin), iOS(Swift)만 포함하고 웹, 윈도우, 리눅스는 제외합니다.

```bash
flutter create --platforms android,ios --android-language kotlin --org com.example my_app
cd my_app
```

**언어 설정**:
- Android: Kotlin (명시적으로 지정)
- iOS: Swift (기본값)

### 1-1. Gradle Kotlin DSL 변환

기본 생성된 Gradle 파일(Groovy)을 Kotlin DSL로 변환합니다.

#### settings.gradle → settings.gradle.kts

**android/settings.gradle 삭제 후** `android/settings.gradle.kts` 생성:

```kotlin
pluginManagement {
    val flutterSdkPath = run {
        val properties = java.util.Properties()
        file("local.properties").inputStream().use { properties.load(it) }
        val flutterSdkPath = properties.getProperty("flutter.sdk")
        require(flutterSdkPath != null) { "flutter.sdk not set in local.properties" }
        flutterSdkPath
    }

    includeBuild("$flutterSdkPath/packages/flutter_tools/gradle")

    repositories {
        google()
        mavenCentral()
        gradlePluginPortal()
    }
}

plugins {
    id("dev.flutter.flutter-plugin-loader") version "1.0.0"
    id("com.android.application") version "8.1.0" apply false
    id("org.jetbrains.kotlin.android") version "1.9.10" apply false
}

include(":app")
```

#### build.gradle → build.gradle.kts (Project level)

**android/build.gradle 삭제 후** `android/build.gradle.kts` 생성:

```kotlin
buildscript {
    repositories {
        google()
        mavenCentral()
    }

    dependencies {
        // Flutter Gradle Plugin이 자동으로 관리
    }
}

allprojects {
    repositories {
        google()
        mavenCentral()
    }
}

rootProject.buildDir = file("../build")

subprojects {
    project.buildDir = file("${rootProject.buildDir}/${project.name}")
}

subprojects {
    project.evaluationDependsOn(":app")
}

tasks.register<Delete>("clean") {
    delete(rootProject.buildDir)
}
```

#### app/build.gradle → app/build.gradle.kts

**android/app/build.gradle 삭제 후** `android/app/build.gradle.kts` 생성:

```kotlin
plugins {
    id("com.android.application")
    id("kotlin-android")
    id("dev.flutter.flutter-gradle-plugin")
}

android {
    namespace = "com.example.my_app"
    compileSdk = 34

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_11
        targetCompatibility = JavaVersion.VERSION_11
        isCoreLibraryDesugaringEnabled = true  // CRITICAL: flutter_local_notifications 필수
    }

    kotlinOptions {
        jvmTarget = "11"
    }

    defaultConfig {
        applicationId = "com.example.my_app"
        minSdk = 21
        targetSdk = 34
        versionCode = 1
        versionName = "1.0.0"
    }

    buildTypes {
        getByName("release") {
            signingConfig = signingConfigs.getByName("debug")
        }
    }
}

flutter {
    source = "../.."
}

dependencies {
    implementation("androidx.core:core-ktx:1.12.0")
    coreLibraryDesugaring("com.android.tools:desugar_jdk_libs:2.0.4")  // CRITICAL: desugaring 필수
}
```

**주의사항**:
- `namespace`를 프로젝트의 실제 패키지명으로 변경
- `applicationId`를 프로젝트의 실제 앱 ID로 변경
- AndroidManifest.xml에서 `package` 속성 제거 (namespace로 대체됨)

### 2. pubspec.yaml 설정

**중요**: Riverpod 3.x를 사용합니다.

```yaml
dependencies:
  flutter:
    sdk: flutter
  # 상태 관리
  flutter_riverpod: ^3.0.0
  riverpod_annotation: ^2.3.0

  # 데이터 직렬화
  freezed_annotation: ^2.4.1
  json_annotation: ^4.8.1

  # 로컬 DB & HTTP
  drift: ^2.14.1
  drift_flutter: ^0.1.0
  dio: ^5.4.0

  # 다국어 지원
  easy_localization: ^3.0.5

  # UI & 아이콘
  fluentui_system_icons: ^1.1.229

  # 유틸리티
  path_provider: ^2.1.2
  url_launcher: ^6.2.5
  flutter_displaymode: ^0.6.0

dev_dependencies:
  flutter_test:
    sdk: flutter
  build_runner: ^2.4.7
  riverpod_generator: ^2.4.0
  freezed: ^2.4.6
  json_serializable: ^6.7.1
  drift_dev: ^2.14.1
  flutter_lints: ^3.0.0
```

#### Riverpod 3.0 주요 변경사항

**새로운 기능**:
- `riverpod_annotation` 및 `riverpod_generator` 지원 (코드 생성 기반)
- 개선된 타입 안전성
- 더 나은 에러 메시지
- `@riverpod` 어노테이션으로 Provider 생성 가능

**하위 호환성**:
- 기존 Provider 스타일(Provider, FutureProvider 등)은 여전히 완벽하게 작동
- 이 보일러플레이트는 기존 스타일 사용 (더 명시적이고 이해하기 쉬움)
- 원하는 경우 `@riverpod` 어노테이션으로 변경 가능

**참고**:
- `riverpod_annotation`은 선택사항
- 이 프로젝트는 명시적 Provider 선언 사용 (초보자 친화적)

### 3. 폴더 구조 생성 스크립트

```bash
mkdir -p lib/core/constants
mkdir -p lib/core/errors
mkdir -p lib/core/utils
mkdir -p lib/data/datasources/local
mkdir -p lib/data/datasources/remote
mkdir -p lib/data/models
mkdir -p lib/data/repositories
mkdir -p lib/domain/entities
mkdir -p lib/domain/repositories
mkdir -p lib/presentation/providers
mkdir -p lib/presentation/screens
mkdir -p lib/presentation/widgets
```

## 기본 파일 템플릿

### app_constants.dart

```dart
class AppConstants {
  // API
  static const String baseUrl = 'https://api.example.com';
  static const Duration connectionTimeout = Duration(seconds: 30);
  static const Duration receiveTimeout = Duration(seconds: 30);

  // Database
  static const String databaseName = 'app_database.db';
  static const int databaseVersion = 1;

  // App
  static const String appName = 'My App';
}
```

### app_database.dart (Drift)

```dart
import 'dart:io';
import 'package:drift/drift.dart';
import 'package:drift_flutter/drift_flutter.dart';
import 'package:path_provider/path_provider.dart';
import 'package:path/path.dart' as p;

part 'app_database.g.dart';

// 예제 테이블
class Users extends Table {
  IntColumn get id => integer().autoIncrement()();
  TextColumn get name => text()();
  TextColumn get email => text()();
  DateTimeColumn get createdAt => dateTime().withDefault(currentDateAndTime)();
}

@DriftDatabase(tables: [Users])
class AppDatabase extends _$AppDatabase {
  AppDatabase() : super(_openConnection());

  @override
  int get schemaVersion => 1;

  static QueryExecutor _openConnection() {
    return driftDatabase(name: 'app_database');
  }
}
```

### api_client.dart (Dio)

```dart
import 'package:dio/dio.dart';
import '../../core/constants/app_constants.dart';

class ApiClient {
  late final Dio _dio;

  ApiClient() {
    _dio = Dio(
      BaseOptions(
        baseUrl: AppConstants.baseUrl,
        connectTimeout: AppConstants.connectionTimeout,
        receiveTimeout: AppConstants.receiveTimeout,
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
        },
      ),
    );

    _dio.interceptors.add(LogInterceptor(
      requestBody: true,
      responseBody: true,
    ));
  }

  Dio get dio => _dio;

  // GET 요청
  Future<Response> get(
    String path, {
    Map<String, dynamic>? queryParameters,
    Options? options,
  }) async {
    return await _dio.get(
      path,
      queryParameters: queryParameters,
      options: options,
    );
  }

  // POST 요청
  Future<Response> post(
    String path, {
    dynamic data,
    Map<String, dynamic>? queryParameters,
    Options? options,
  }) async {
    return await _dio.post(
      path,
      data: data,
      queryParameters: queryParameters,
      options: options,
    );
  }

  // PUT 요청
  Future<Response> put(
    String path, {
    dynamic data,
    Map<String, dynamic>? queryParameters,
    Options? options,
  }) async {
    return await _dio.put(
      path,
      data: data,
      queryParameters: queryParameters,
      options: options,
    );
  }

  // DELETE 요청
  Future<Response> delete(
    String path, {
    dynamic data,
    Map<String, dynamic>? queryParameters,
    Options? options,
  }) async {
    return await _dio.delete(
      path,
      data: data,
      queryParameters: queryParameters,
      options: options,
    );
  }
}
```

### app_providers.dart

```dart
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../data/datasources/local/app_database.dart';
import '../data/datasources/remote/api_client.dart';

// 데이터베이스 Provider
final databaseProvider = Provider<AppDatabase>((ref) {
  return AppDatabase();
});

// API 클라이언트 Provider
final apiClientProvider = Provider<ApiClient>((ref) {
  return ApiClient();
});
```

### main.dart

```dart
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

void main() {
  runApp(
    const ProviderScope(
      child: MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends ConsumerStatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  ConsumerState<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends ConsumerState<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'You have pushed the button this many times:',
            ),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ),
    );
  }
}
```

## Repository 패턴 예제

### domain/entities/user.dart

```dart
import 'package:freezed_annotation/freezed_annotation.dart';

part 'user.freezed.dart';
part 'user.g.dart';

@freezed
sealed class User with _$User {  // CRITICAL: Freezed 3.0은 sealed class 필수
  const factory User({
    required int id,
    required String name,
    required String email,
  }) = _User;

  factory User.fromJson(Map<String, dynamic> json) => _$UserFromJson(json);
}
```

### domain/repositories/user_repository.dart

```dart
import '../entities/user.dart';

abstract class UserRepository {
  Future<List<User>> getUsers();
  Future<User> getUserById(int id);
  Future<User> createUser(User user);
  Future<User> updateUser(User user);
  Future<void> deleteUser(int id);
}
```

### data/repositories/user_repository_impl.dart

```dart
import '../../domain/entities/user.dart';
import '../../domain/repositories/user_repository.dart';
import '../datasources/local/app_database.dart';
import '../datasources/remote/api_client.dart';

class UserRepositoryImpl implements UserRepository {
  final ApiClient _apiClient;
  final AppDatabase _database;

  UserRepositoryImpl(this._apiClient, this._database);

  @override
  Future<List<User>> getUsers() async {
    try {
      final response = await _apiClient.get('/users');
      return (response.data as List)
          .map((json) => User.fromJson(json))
          .toList();
    } catch (e) {
      // 에러 발생 시 로컬 데이터 반환
      final users = await _database.select(_database.users).get();
      return users
          .map((u) => User(id: u.id, name: u.name, email: u.email))
          .toList();
    }
  }

  @override
  Future<User> getUserById(int id) async {
    final response = await _apiClient.get('/users/$id');
    return User.fromJson(response.data);
  }

  @override
  Future<User> createUser(User user) async {
    final response = await _apiClient.post('/users', data: user.toJson());
    return User.fromJson(response.data);
  }

  @override
  Future<User> updateUser(User user) async {
    final response = await _apiClient.put('/users/${user.id}', data: user.toJson());
    return User.fromJson(response.data);
  }

  @override
  Future<void> deleteUser(int id) async {
    await _apiClient.delete('/users/$id');
  }
}
```

### presentation/providers/user_providers.dart

```dart
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../data/repositories/user_repository_impl.dart';
import '../../domain/entities/user.dart';
import '../../domain/repositories/user_repository.dart';
import 'app_providers.dart';

// Repository Provider
final userRepositoryProvider = Provider<UserRepository>((ref) {
  final apiClient = ref.watch(apiClientProvider);
  final database = ref.watch(databaseProvider);
  return UserRepositoryImpl(apiClient, database);
});

// Users List Provider
final usersProvider = FutureProvider<List<User>>((ref) async {
  final repository = ref.watch(userRepositoryProvider);
  return await repository.getUsers();
});

// Single User Provider
final userProvider = FutureProvider.family<User, int>((ref, id) async {
  final repository = ref.watch(userRepositoryProvider);
  return await repository.getUserById(id);
});
```

## 빌드 실행 후 확인사항

1. `*.freezed.dart` 파일들이 생성되었는지 확인
2. `*.g.dart` 파일들이 생성되었는지 확인
3. `app_database.g.dart`가 생성되었는지 확인
4. 빌드 오류가 없는지 확인

## User CRUD 보일러플레이트 (완전한 예제)

이 섹션에서는 실제 작동하는 User CRUD 기능을 구현합니다. 로컬 DB는 캐싱용으로 사용하고, Dio로 백엔드 API와 통신합니다.

### 아키텍처 흐름

```
UI Layer (Presentation)
  ↓
Providers (Riverpod)
  ↓
Repository (Interface)
  ↓
Repository Implementation
  ↓ ↓
Remote DataSource (Dio)  Local DataSource (Drift)
  ↓                       ↓
Backend API              SQLite Cache
```

### 1. Domain Layer

#### domain/entities/user.dart

```dart
import 'package:freezed_annotation/freezed_annotation.dart';

part 'user.freezed.dart';
part 'user.g.dart';

@freezed
sealed class User with _$User {  // CRITICAL: Freezed 3.0은 sealed class 필수
  const factory User({
    required int id,
    required String name,
    required String email,
    String? phone,
    String? website,
  }) = _User;

  factory User.fromJson(Map<String, dynamic> json) => _$UserFromJson(json);
}
```

#### domain/repositories/user_repository.dart

```dart
import '../entities/user.dart';

abstract class UserRepository {
  /// 모든 사용자 가져오기 (캐시 우선, 실패 시 API)
  Future<List<User>> getUsers({bool forceRefresh = false});

  /// 특정 사용자 가져오기
  Future<User> getUserById(int id);

  /// 사용자 생성
  Future<User> createUser(User user);

  /// 사용자 업데이트
  Future<User> updateUser(User user);

  /// 사용자 삭제
  Future<void> deleteUser(int id);
}
```

### 2. Data Layer

#### data/models/user_model.dart

```dart
import 'package:freezed_annotation/freezed_annotation.dart';
import '../../domain/entities/user.dart';

part 'user_model.freezed.dart';
part 'user_model.g.dart';

@freezed
sealed class UserModel with _$UserModel {  // CRITICAL: Freezed 3.0은 sealed class 필수
  const UserModel._();

  const factory UserModel({
    required int id,
    required String name,
    required String email,
    String? phone,
    String? website,
  }) = _UserModel;

  factory UserModel.fromJson(Map<String, dynamic> json) => _$UserModelFromJson(json);

  /// Model을 Entity로 변환
  User toEntity() {
    return User(
      id: id,
      name: name,
      email: email,
      phone: phone,
      website: website,
    );
  }

  /// Entity에서 Model 생성
  factory UserModel.fromEntity(User user) {
    return UserModel(
      id: user.id,
      name: user.name,
      email: user.email,
      phone: user.phone,
      website: user.website,
    );
  }
}
```

#### data/datasources/local/app_database.dart (완전판)

```dart
import 'package:drift/drift.dart';
import 'package:drift_flutter/drift_flutter.dart';

part 'app_database.g.dart';

// Users 테이블 정의
class Users extends Table {
  IntColumn get id => integer()();
  TextColumn get name => text()();
  TextColumn get email => text()();
  TextColumn get phone => text().nullable()();
  TextColumn get website => text().nullable()();
  DateTimeColumn get cachedAt => dateTime().withDefault(currentDateAndTime)();

  @override
  Set<Column> get primaryKey => {id};
}

@DriftDatabase(tables: [Users])
class AppDatabase extends _$AppDatabase {
  AppDatabase() : super(_openConnection());

  @override
  int get schemaVersion => 1;

  static QueryExecutor _openConnection() {
    return driftDatabase(name: 'app_database');
  }

  // CRUD Operations for Users

  /// 모든 사용자 가져오기
  Future<List<User>> getAllUsers() => select(users).get();

  /// ID로 사용자 가져오기
  Future<User?> getUserById(int id) =>
      (select(users)..where((tbl) => tbl.id.equals(id))).getSingleOrNull();

  /// 사용자 삽입 또는 업데이트
  Future<int> upsertUser(UsersCompanion user) =>
      into(users).insertOnConflictUpdate(user);

  /// 여러 사용자 삽입 또는 업데이트
  Future<void> upsertUsers(List<UsersCompanion> userList) async {
    await batch((batch) {
      batch.insertAllOnConflictUpdate(users, userList);
    });
  }

  /// 사용자 삭제
  Future<int> deleteUserById(int id) =>
      (delete(users)..where((tbl) => tbl.id.equals(id))).go();

  /// 모든 사용자 삭제 (캐시 클리어)
  Future<int> clearAllUsers() => delete(users).go();
}
```

#### data/datasources/local/user_local_datasource.dart

```dart
import 'package:drift/drift.dart';
import '../../models/user_model.dart';
import 'app_database.dart';

class UserLocalDataSource {
  final AppDatabase _database;

  UserLocalDataSource(this._database);

  /// 모든 사용자 가져오기
  Future<List<UserModel>> getUsers() async {
    final users = await _database.getAllUsers();
    return users.map((user) => _userToModel(user)).toList();
  }

  /// ID로 사용자 가져오기
  Future<UserModel?> getUserById(int id) async {
    final user = await _database.getUserById(id);
    if (user == null) return null;
    return _userToModel(user);
  }

  /// 사용자 저장 (캐싱)
  Future<void> cacheUser(UserModel user) async {
    await _database.upsertUser(_modelToCompanion(user));
  }

  /// 여러 사용자 저장 (캐싱)
  Future<void> cacheUsers(List<UserModel> users) async {
    final companions = users.map(_modelToCompanion).toList();
    await _database.upsertUsers(companions);
  }

  /// 사용자 삭제
  Future<void> deleteUser(int id) async {
    await _database.deleteUserById(id);
  }

  /// 캐시 클리어
  Future<void> clearCache() async {
    await _database.clearAllUsers();
  }

  // Drift User -> UserModel
  UserModel _userToModel(User user) {
    return UserModel(
      id: user.id,
      name: user.name,
      email: user.email,
      phone: user.phone,
      website: user.website,
    );
  }

  // UserModel -> Drift Companion
  UsersCompanion _modelToCompanion(UserModel model) {
    return UsersCompanion(
      id: Value(model.id),
      name: Value(model.name),
      email: Value(model.email),
      phone: Value(model.phone),
      website: Value(model.website),
      cachedAt: Value(DateTime.now()),
    );
  }
}
```

#### data/datasources/remote/user_remote_datasource.dart

```dart
import 'package:dio/dio.dart';
import '../../models/user_model.dart';
import 'api_client.dart';

class UserRemoteDataSource {
  final ApiClient _apiClient;

  UserRemoteDataSource(this._apiClient);

  /// 모든 사용자 가져오기
  Future<List<UserModel>> getUsers() async {
    try {
      final response = await _apiClient.get('/users');
      final List<dynamic> data = response.data;
      return data.map((json) => UserModel.fromJson(json)).toList();
    } catch (e) {
      throw _handleError(e);
    }
  }

  /// ID로 사용자 가져오기
  Future<UserModel> getUserById(int id) async {
    try {
      final response = await _apiClient.get('/users/$id');
      return UserModel.fromJson(response.data);
    } catch (e) {
      throw _handleError(e);
    }
  }

  /// 사용자 생성
  Future<UserModel> createUser(UserModel user) async {
    try {
      final response = await _apiClient.post(
        '/users',
        data: user.toJson(),
      );
      return UserModel.fromJson(response.data);
    } catch (e) {
      throw _handleError(e);
    }
  }

  /// 사용자 업데이트
  Future<UserModel> updateUser(UserModel user) async {
    try {
      final response = await _apiClient.put(
        '/users/${user.id}',
        data: user.toJson(),
      );
      return UserModel.fromJson(response.data);
    } catch (e) {
      throw _handleError(e);
    }
  }

  /// 사용자 삭제
  Future<void> deleteUser(int id) async {
    try {
      await _apiClient.delete('/users/$id');
    } catch (e) {
      throw _handleError(e);
    }
  }

  Exception _handleError(dynamic error) {
    if (error is DioException) {
      return Exception('Network error: ${error.message}');
    }
    return Exception('Unknown error: $error');
  }
}
```

#### data/repositories/user_repository_impl.dart

```dart
import '../../domain/entities/user.dart';
import '../../domain/repositories/user_repository.dart';
import '../datasources/local/user_local_datasource.dart';
import '../datasources/remote/user_remote_datasource.dart';
import '../models/user_model.dart';

class UserRepositoryImpl implements UserRepository {
  final UserRemoteDataSource _remoteDataSource;
  final UserLocalDataSource _localDataSource;

  UserRepositoryImpl(this._remoteDataSource, this._localDataSource);

  @override
  Future<List<User>> getUsers({bool forceRefresh = false}) async {
    try {
      // forceRefresh가 true면 무조건 API 호출
      if (forceRefresh) {
        return await _fetchAndCacheUsers();
      }

      // 1. 먼저 로컬 캐시 확인
      final cachedUsers = await _localDataSource.getUsers();

      // 2. 캐시가 있으면 반환하고 백그라운드에서 업데이트
      if (cachedUsers.isNotEmpty) {
        // 백그라운드에서 업데이트 (await 없음)
        _fetchAndCacheUsers();
        return cachedUsers.map((model) => model.toEntity()).toList();
      }

      // 3. 캐시가 없으면 API 호출
      return await _fetchAndCacheUsers();
    } catch (e) {
      // API 실패 시 캐시 반환
      final cachedUsers = await _localDataSource.getUsers();
      if (cachedUsers.isNotEmpty) {
        return cachedUsers.map((model) => model.toEntity()).toList();
      }
      rethrow;
    }
  }

  Future<List<User>> _fetchAndCacheUsers() async {
    final users = await _remoteDataSource.getUsers();
    await _localDataSource.cacheUsers(users);
    return users.map((model) => model.toEntity()).toList();
  }

  @override
  Future<User> getUserById(int id) async {
    try {
      // 1. API에서 가져오기
      final user = await _remoteDataSource.getUserById(id);

      // 2. 로컬 캐시에 저장
      await _localDataSource.cacheUser(user);

      return user.toEntity();
    } catch (e) {
      // 3. 실패 시 로컬 캐시 확인
      final cachedUser = await _localDataSource.getUserById(id);
      if (cachedUser != null) {
        return cachedUser.toEntity();
      }
      rethrow;
    }
  }

  @override
  Future<User> createUser(User user) async {
    final model = UserModel.fromEntity(user);
    final createdUser = await _remoteDataSource.createUser(model);
    await _localDataSource.cacheUser(createdUser);
    return createdUser.toEntity();
  }

  @override
  Future<User> updateUser(User user) async {
    final model = UserModel.fromEntity(user);
    final updatedUser = await _remoteDataSource.updateUser(model);
    await _localDataSource.cacheUser(updatedUser);
    return updatedUser.toEntity();
  }

  @override
  Future<void> deleteUser(int id) async {
    await _remoteDataSource.deleteUser(id);
    await _localDataSource.deleteUser(id);
  }
}
```

### 3. Presentation Layer

#### presentation/providers/user_providers.dart

```dart
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../data/datasources/local/user_local_datasource.dart';
import '../../data/datasources/remote/user_remote_datasource.dart';
import '../../data/repositories/user_repository_impl.dart';
import '../../domain/entities/user.dart';
import '../../domain/repositories/user_repository.dart';
import 'app_providers.dart';

// User Remote DataSource Provider
final userRemoteDataSourceProvider = Provider<UserRemoteDataSource>((ref) {
  final apiClient = ref.watch(apiClientProvider);
  return UserRemoteDataSource(apiClient);
});

// User Local DataSource Provider
final userLocalDataSourceProvider = Provider<UserLocalDataSource>((ref) {
  final database = ref.watch(databaseProvider);
  return UserLocalDataSource(database);
});

// User Repository Provider
final userRepositoryProvider = Provider<UserRepository>((ref) {
  final remoteDataSource = ref.watch(userRemoteDataSourceProvider);
  final localDataSource = ref.watch(userLocalDataSourceProvider);
  return UserRepositoryImpl(remoteDataSource, localDataSource);
});

// Users List Provider
final usersProvider = FutureProvider<List<User>>((ref) async {
  final repository = ref.watch(userRepositoryProvider);
  return await repository.getUsers();
});

// Refresh Users Provider (forceRefresh)
final refreshUsersProvider = FutureProvider<List<User>>((ref) async {
  final repository = ref.watch(userRepositoryProvider);
  return await repository.getUsers(forceRefresh: true);
});

// Single User Provider
final userProvider = FutureProvider.family<User, int>((ref, id) async {
  final repository = ref.watch(userRepositoryProvider);
  return await repository.getUserById(id);
});

// User Controller (for mutations)
class UserController extends StateNotifier<AsyncValue<void>> {
  final UserRepository _repository;

  UserController(this._repository) : super(const AsyncValue.data(null));

  Future<void> createUser(User user) async {
    state = const AsyncValue.loading();
    state = await AsyncValue.guard(() async {
      await _repository.createUser(user);
    });
  }

  Future<void> updateUser(User user) async {
    state = const AsyncValue.loading();
    state = await AsyncValue.guard(() async {
      await _repository.updateUser(user);
    });
  }

  Future<void> deleteUser(int id) async {
    state = const AsyncValue.loading();
    state = await AsyncValue.guard(() async {
      await _repository.deleteUser(id);
    });
  }
}

final userControllerProvider =
    StateNotifierProvider<UserController, AsyncValue<void>>((ref) {
  final repository = ref.watch(userRepositoryProvider);
  return UserController(repository);
});
```

#### presentation/screens/user_list_screen.dart

```dart
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../providers/user_providers.dart';
import 'user_detail_screen.dart';

class UserListScreen extends ConsumerWidget {
  const UserListScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final usersAsync = ref.watch(usersProvider);

    return Scaffold(
      appBar: AppBar(
        title: const Text('Users'),
        actions: [
          IconButton(
            icon: const Icon(Icons.refresh),
            onPressed: () {
              ref.invalidate(usersProvider);
            },
          ),
        ],
      ),
      body: usersAsync.when(
        data: (users) {
          if (users.isEmpty) {
            return const Center(
              child: Text('No users found'),
            );
          }
          return RefreshIndicator(
            onRefresh: () async {
              ref.invalidate(usersProvider);
            },
            child: ListView.builder(
              itemCount: users.length,
              itemBuilder: (context, index) {
                final user = users[index];
                return ListTile(
                  leading: CircleAvatar(
                    child: Text(user.name[0].toUpperCase()),
                  ),
                  title: Text(user.name),
                  subtitle: Text(user.email),
                  trailing: const Icon(Icons.chevron_right),
                  onTap: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => UserDetailScreen(userId: user.id),
                      ),
                    );
                  },
                );
              },
            ),
          );
        },
        loading: () => const Center(child: CircularProgressIndicator()),
        error: (error, stack) => Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Icon(Icons.error_outline, size: 48, color: Colors.red),
              const SizedBox(height: 16),
              Text('Error: $error'),
              const SizedBox(height: 16),
              ElevatedButton(
                onPressed: () {
                  ref.invalidate(usersProvider);
                },
                child: const Text('Retry'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

#### presentation/screens/user_detail_screen.dart

```dart
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../providers/user_providers.dart';

class UserDetailScreen extends ConsumerWidget {
  final int userId;

  const UserDetailScreen({super.key, required this.userId});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final userAsync = ref.watch(userProvider(userId));

    return Scaffold(
      appBar: AppBar(
        title: const Text('User Detail'),
        actions: [
          IconButton(
            icon: const Icon(Icons.delete),
            onPressed: () async {
              final confirmed = await showDialog<bool>(
                context: context,
                builder: (context) => AlertDialog(
                  title: const Text('Delete User'),
                  content: const Text('Are you sure you want to delete this user?'),
                  actions: [
                    TextButton(
                      onPressed: () => Navigator.pop(context, false),
                      child: const Text('Cancel'),
                    ),
                    TextButton(
                      onPressed: () => Navigator.pop(context, true),
                      child: const Text('Delete'),
                    ),
                  ],
                ),
              );

              if (confirmed == true && context.mounted) {
                await ref.read(userControllerProvider.notifier).deleteUser(userId);
                ref.invalidate(usersProvider);
                if (context.mounted) {
                  Navigator.pop(context);
                }
              }
            },
          ),
        ],
      ),
      body: userAsync.when(
        data: (user) {
          return ListView(
            padding: const EdgeInsets.all(16),
            children: [
              CircleAvatar(
                radius: 48,
                child: Text(
                  user.name[0].toUpperCase(),
                  style: const TextStyle(fontSize: 32),
                ),
              ),
              const SizedBox(height: 24),
              _buildInfoCard('Name', user.name, Icons.person),
              _buildInfoCard('Email', user.email, Icons.email),
              if (user.phone != null)
                _buildInfoCard('Phone', user.phone!, Icons.phone),
              if (user.website != null)
                _buildInfoCard('Website', user.website!, Icons.language),
            ],
          );
        },
        loading: () => const Center(child: CircularProgressIndicator()),
        error: (error, stack) => Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Icon(Icons.error_outline, size: 48, color: Colors.red),
              const SizedBox(height: 16),
              Text('Error: $error'),
              const SizedBox(height: 16),
              ElevatedButton(
                onPressed: () {
                  ref.invalidate(userProvider(userId));
                },
                child: const Text('Retry'),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildInfoCard(String label, String value, IconData icon) {
    return Card(
      margin: const EdgeInsets.only(bottom: 16),
      child: ListTile(
        leading: Icon(icon),
        title: Text(label),
        subtitle: Text(value),
      ),
    );
  }
}
```

#### main.dart (업데이트)

```dart
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:easy_localization/easy_localization.dart';
import 'package:flutter_displaymode/flutter_displaymode.dart';
import 'presentation/screens/user_list_screen.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // Easy Localization 초기화
  await EasyLocalization.ensureInitialized();

  // Android 고주사율 설정 (선택사항)
  await _setOptimalDisplayMode();

  runApp(
    EasyLocalization(
      supportedLocales: const [
        Locale('en', 'US'),
        Locale('ko', 'KR'),
      ],
      path: 'assets/translations',
      fallbackLocale: const Locale('en', 'US'),
      child: const ProviderScope(
        child: MyApp(),
      ),
    ),
  );
}

Future<void> _setOptimalDisplayMode() async {
  try {
    final List<DisplayMode> supported = await FlutterDisplayMode.supported;
    final DisplayMode active = await FlutterDisplayMode.active;

    final List<DisplayMode> sameResolution = supported
        .where((DisplayMode m) =>
            m.width == active.width && m.height == active.height)
        .toList()
      ..sort((DisplayMode a, DisplayMode b) =>
          b.refreshRate.compareTo(a.refreshRate));

    final DisplayMode mostOptimalMode =
        sameResolution.isNotEmpty ? sameResolution.first : active;

    await FlutterDisplayMode.setPreferredMode(mostOptimalMode);
  } catch (e) {
    // iOS나 지원하지 않는 Android 버전에서는 무시
    debugPrint('Display mode setting failed: $e');
  }
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter User CRUD',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        useMaterial3: true,
      ),
      // Easy Localization 설정
      localizationsDelegates: context.localizationDelegates,
      supportedLocales: context.supportedLocales,
      locale: context.locale,
      home: const UserListScreen(),
    );
  }
}
```

### 4. Easy Localization 설정

#### pubspec.yaml에 assets 추가

```yaml
flutter:
  uses-material-design: true
  assets:
    - assets/translations/
```

#### assets/translations/en-US.json

```json
{
  "app_title": "Flutter User CRUD",
  "users": "Users",
  "user_detail": "User Detail",
  "no_users_found": "No users found",
  "error": "Error",
  "retry": "Retry",
  "refresh": "Refresh",
  "delete": "Delete",
  "cancel": "Cancel",
  "delete_user": "Delete User",
  "delete_confirmation": "Are you sure you want to delete this user?",
  "name": "Name",
  "email": "Email",
  "phone": "Phone",
  "website": "Website"
}
```

#### assets/translations/ko-KR.json

```json
{
  "app_title": "Flutter 사용자 CRUD",
  "users": "사용자 목록",
  "user_detail": "사용자 상세",
  "no_users_found": "사용자를 찾을 수 없습니다",
  "error": "오류",
  "retry": "다시 시도",
  "refresh": "새로고침",
  "delete": "삭제",
  "cancel": "취소",
  "delete_user": "사용자 삭제",
  "delete_confirmation": "이 사용자를 삭제하시겠습니까?",
  "name": "이름",
  "email": "이메일",
  "phone": "전화번호",
  "website": "웹사이트"
}
```

### 5. 유틸리티 함수

#### core/utils/app_utils.dart

```dart
import 'package:url_launcher/url_launcher.dart';
import 'package:path_provider/path_provider.dart';
import 'dart:io';

class AppUtils {
  AppUtils._();

  /// URL 열기
  static Future<bool> launchURL(String url) async {
    final Uri uri = Uri.parse(url);
    if (await canLaunchUrl(uri)) {
      return await launchUrl(uri, mode: LaunchMode.externalApplication);
    }
    return false;
  }

  /// 이메일 보내기
  static Future<bool> launchEmail(String email) async {
    return await launchURL('mailto:$email');
  }

  /// 전화 걸기
  static Future<bool> launchPhone(String phone) async {
    return await launchURL('tel:$phone');
  }

  /// 앱 문서 디렉토리 경로
  static Future<String> getAppDocumentsPath() async {
    final directory = await getApplicationDocumentsDirectory();
    return directory.path;
  }

  /// 임시 디렉토리 경로
  static Future<String> getTempPath() async {
    final directory = await getTemporaryDirectory();
    return directory.path;
  }

  /// 앱 지원 디렉토리 경로
  static Future<String> getAppSupportPath() async {
    final directory = await getApplicationSupportDirectory();
    return directory.path;
  }

  /// 캐시 디렉토리 경로
  static Future<String> getCachePath() async {
    final directory = await getTemporaryDirectory();
    final cachePath = '${directory.path}/cache';
    final cacheDir = Directory(cachePath);
    if (!await cacheDir.exists()) {
      await cacheDir.create(recursive: true);
    }
    return cachePath;
  }

  /// 파일 크기 포맷 (bytes → KB, MB, GB)
  static String formatFileSize(int bytes) {
    if (bytes < 1024) return '$bytes B';
    if (bytes < 1024 * 1024) return '${(bytes / 1024).toStringAsFixed(2)} KB';
    if (bytes < 1024 * 1024 * 1024) {
      return '${(bytes / (1024 * 1024)).toStringAsFixed(2)} MB';
    }
    return '${(bytes / (1024 * 1024 * 1024)).toStringAsFixed(2)} GB';
  }
}
```

### 6. FluentUI Icons 적용된 UI 업데이트

#### presentation/screens/user_list_screen.dart (업데이트)

```dart
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:easy_localization/easy_localization.dart';
import 'package:fluentui_system_icons/fluentui_system_icons.dart';
import '../providers/user_providers.dart';
import 'user_detail_screen.dart';

class UserListScreen extends ConsumerWidget {
  const UserListScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final usersAsync = ref.watch(usersProvider);

    return Scaffold(
      appBar: AppBar(
        title: Text('users'.tr()),
        actions: [
          IconButton(
            icon: const Icon(FluentIcons.arrow_clockwise_24_regular),
            tooltip: 'refresh'.tr(),
            onPressed: () {
              ref.invalidate(usersProvider);
            },
          ),
          IconButton(
            icon: const Icon(FluentIcons.globe_24_regular),
            tooltip: 'Change Language',
            onPressed: () {
              // 언어 전환
              if (context.locale.languageCode == 'en') {
                context.setLocale(const Locale('ko', 'KR'));
              } else {
                context.setLocale(const Locale('en', 'US'));
              }
            },
          ),
        ],
      ),
      body: usersAsync.when(
        data: (users) {
          if (users.isEmpty) {
            return Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Icon(
                    FluentIcons.people_24_regular,
                    size: 64,
                    color: Colors.grey,
                  ),
                  const SizedBox(height: 16),
                  Text('no_users_found'.tr()),
                ],
              ),
            );
          }
          return RefreshIndicator(
            onRefresh: () async {
              ref.invalidate(usersProvider);
            },
            child: ListView.builder(
              itemCount: users.length,
              itemBuilder: (context, index) {
                final user = users[index];
                return ListTile(
                  leading: CircleAvatar(
                    child: Text(user.name[0].toUpperCase()),
                  ),
                  title: Text(user.name),
                  subtitle: Row(
                    children: [
                      const Icon(FluentIcons.mail_24_regular, size: 14),
                      const SizedBox(width: 4),
                      Expanded(child: Text(user.email)),
                    ],
                  ),
                  trailing: const Icon(FluentIcons.chevron_right_24_regular),
                  onTap: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => UserDetailScreen(userId: user.id),
                      ),
                    );
                  },
                );
              },
            ),
          );
        },
        loading: () => const Center(child: CircularProgressIndicator()),
        error: (error, stack) => Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Icon(
                FluentIcons.error_circle_24_regular,
                size: 48,
                color: Colors.red,
              ),
              const SizedBox(height: 16),
              Text('${'error'.tr()}: $error'),
              const SizedBox(height: 16),
              ElevatedButton.icon(
                onPressed: () {
                  ref.invalidate(usersProvider);
                },
                icon: const Icon(FluentIcons.arrow_clockwise_24_regular),
                label: Text('retry'.tr()),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

#### presentation/screens/user_detail_screen.dart (업데이트)

```dart
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:easy_localization/easy_localization.dart';
import 'package:fluentui_system_icons/fluentui_system_icons.dart';
import '../providers/user_providers.dart';
import '../../core/utils/app_utils.dart';

class UserDetailScreen extends ConsumerWidget {
  final int userId;

  const UserDetailScreen({super.key, required this.userId});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final userAsync = ref.watch(userProvider(userId));

    return Scaffold(
      appBar: AppBar(
        title: Text('user_detail'.tr()),
        actions: [
          IconButton(
            icon: const Icon(FluentIcons.delete_24_regular),
            tooltip: 'delete'.tr(),
            onPressed: () async {
              final confirmed = await showDialog<bool>(
                context: context,
                builder: (context) => AlertDialog(
                  title: Text('delete_user'.tr()),
                  content: Text('delete_confirmation'.tr()),
                  actions: [
                    TextButton(
                      onPressed: () => Navigator.pop(context, false),
                      child: Text('cancel'.tr()),
                    ),
                    TextButton(
                      onPressed: () => Navigator.pop(context, true),
                      child: Text('delete'.tr()),
                    ),
                  ],
                ),
              );

              if (confirmed == true && context.mounted) {
                await ref.read(userControllerProvider.notifier).deleteUser(userId);
                ref.invalidate(usersProvider);
                if (context.mounted) {
                  Navigator.pop(context);
                }
              }
            },
          ),
        ],
      ),
      body: userAsync.when(
        data: (user) {
          return ListView(
            padding: const EdgeInsets.all(16),
            children: [
              Center(
                child: CircleAvatar(
                  radius: 48,
                  child: Text(
                    user.name[0].toUpperCase(),
                    style: const TextStyle(fontSize: 32),
                  ),
                ),
              ),
              const SizedBox(height: 24),
              _buildInfoCard(
                'name'.tr(),
                user.name,
                FluentIcons.person_24_regular,
                null,
              ),
              _buildInfoCard(
                'email'.tr(),
                user.email,
                FluentIcons.mail_24_regular,
                () => AppUtils.launchEmail(user.email),
              ),
              if (user.phone != null)
                _buildInfoCard(
                  'phone'.tr(),
                  user.phone!,
                  FluentIcons.phone_24_regular,
                  () => AppUtils.launchPhone(user.phone!),
                ),
              if (user.website != null)
                _buildInfoCard(
                  'website'.tr(),
                  user.website!,
                  FluentIcons.globe_24_regular,
                  () => AppUtils.launchURL('https://${user.website}'),
                ),
            ],
          );
        },
        loading: () => const Center(child: CircularProgressIndicator()),
        error: (error, stack) => Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Icon(
                FluentIcons.error_circle_24_regular,
                size: 48,
                color: Colors.red,
              ),
              const SizedBox(height: 16),
              Text('${'error'.tr()}: $error'),
              const SizedBox(height: 16),
              ElevatedButton.icon(
                onPressed: () {
                  ref.invalidate(userProvider(userId));
                },
                icon: const Icon(FluentIcons.arrow_clockwise_24_regular),
                label: Text('retry'.tr()),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildInfoCard(
    String label,
    String value,
    IconData icon,
    VoidCallback? onTap,
  ) {
    return Card(
      margin: const EdgeInsets.only(bottom: 16),
      child: ListTile(
        leading: Icon(icon),
        title: Text(label),
        subtitle: Text(value),
        trailing: onTap != null
            ? const Icon(FluentIcons.open_24_regular, size: 20)
            : null,
        onTap: onTap,
      ),
    );
  }
}
```

### 7. 빌드 및 테스트

```bash
# 코드 생성
dart run build_runner build --delete-conflicting-outputs

# 앱 실행
flutter run
```

### 8. API 테스트용 엔드포인트

이 예제는 JSONPlaceholder API를 사용합니다:
- Base URL: `https://jsonplaceholder.typicode.com`
- 엔드포인트: `/users`

`app_constants.dart`에서 baseUrl을 변경하세요:
```dart
static const String baseUrl = 'https://jsonplaceholder.typicode.com';
```

---

# 선택 가능한 고급 기능 (대화형 옵션)

이 섹션은 사용자가 대화형으로 선택할 수 있는 추가 기능들입니다.

## 옵션 1: GoRouter (Type-safe Navigation)

### pubspec.yaml 추가

```yaml
dependencies:
  go_router: ^14.8.0
```

### 라우트 설정 (core/router/app_router.dart)

```dart
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../presentation/screens/user_list_screen.dart';
import '../../presentation/screens/user_detail_screen.dart';

// GoRouter Provider
final goRouterProvider = Provider<GoRouter>((ref) {
  return GoRouter(
    initialLocation: '/users',
    routes: [
      GoRoute(
        path: '/users',
        name: 'users',
        builder: (context, state) => const UserListScreen(),
        routes: [
          GoRoute(
            path: ':id',
            name: 'user-detail',
            builder: (context, state) {
              final id = int.parse(state.pathParameters['id']!);
              return UserDetailScreen(userId: id);
            },
          ),
        ],
      ),
    ],
    errorBuilder: (context, state) => Scaffold(
      body: Center(
        child: Text('Page not found: ${state.uri}'),
      ),
    ),
  );
});
```

### main.dart 수정 (GoRouter 사용)

```dart
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:easy_localization/easy_localization.dart';
import 'core/router/app_router.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await EasyLocalization.ensureInitialized();

  runApp(
    EasyLocalization(
      supportedLocales: const [Locale('en', 'US'), Locale('ko', 'KR')],
      path: 'assets/translations',
      fallbackLocale: const Locale('en', 'US'),
      child: const ProviderScope(child: MyApp()),
    ),
  );
}

class MyApp extends ConsumerWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final router = ref.watch(goRouterProvider);

    return MaterialApp.router(
      title: 'Flutter App',
      routerConfig: router,
      localizationsDelegates: context.localizationDelegates,
      supportedLocales: context.supportedLocales,
      locale: context.locale,
    );
  }
}
```

### 네비게이션 사용 예제

```dart
// UserListScreen에서
onTap: () {
  context.goNamed('user-detail', pathParameters: {'id': '${user.id}'});
}

// 뒤로가기
context.pop();
```

## 옵션 2: Hive CE (Secure Storage)

### pubspec.yaml 추가

```yaml
dependencies:
  hive_ce: ^2.11.1
  hive_ce_flutter: ^2.0.0

dev_dependencies:
  hive_ce_generator: ^1.6.0
```

### 보안 스토리지 초기화 (core/storage/secure_storage.dart)

```dart
import 'package:hive_ce_flutter/hive_ce_flutter.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class SecureStorage {
  static const String _authBoxName = 'auth_box';
  static const _secureStorage = FlutterSecureStorage();
  static const _encryptionKeyName = 'hive_encryption_key';

  static Future<void> init() async {
    await Hive.initFlutter();

    // 암호화 키 생성 또는 가져오기
    final encryptionKey = await _getEncryptionKey();

    // 암호화된 Box 열기
    await Hive.openBox(
      _authBoxName,
      encryptionCipher: HiveAesCipher(encryptionKey),
    );
  }

  static Future<List<int>> _getEncryptionKey() async {
    String? keyString = await _secureStorage.read(key: _encryptionKeyName);

    if (keyString == null) {
      // 새로운 키 생성
      final key = Hive.generateSecureKey();
      keyString = base64Encode(key);
      await _secureStorage.write(key: _encryptionKeyName, value: keyString);
      return key;
    }

    return base64Decode(keyString);
  }

  // 토큰 저장
  static Future<void> saveToken(String token) async {
    final box = Hive.box(_authBoxName);
    await box.put('access_token', token);
  }

  // 토큰 가져오기
  static String? getToken() {
    final box = Hive.box(_authBoxName);
    return box.get('access_token');
  }

  // 토큰 삭제
  static Future<void> deleteToken() async {
    final box = Hive.box(_authBoxName);
    await box.delete('access_token');
  }

  // Refresh Token 저장
  static Future<void> saveRefreshToken(String token) async {
    final box = Hive.box(_authBoxName);
    await box.put('refresh_token', token);
  }

  // Refresh Token 가져오기
  static String? getRefreshToken() {
    final box = Hive.box(_authBoxName);
    return box.get('refresh_token');
  }

  // 모든 데이터 삭제 (로그아웃)
  static Future<void> clearAll() async {
    final box = Hive.box(_authBoxName);
    await box.clear();
  }
}
```

### main.dart에서 초기화

```dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // Hive 초기화
  await SecureStorage.init();

  runApp(const ProviderScope(child: MyApp()));
}
```

## 옵션 3: 인증 시스템 (Authentication)

### domain/entities/auth_user.dart

```dart
import 'package:freezed_annotation/freezed_annotation.dart';

part 'auth_user.freezed.dart';
part 'auth_user.g.dart';

@freezed
sealed class AuthUser with _$AuthUser {  // CRITICAL: Freezed 3.0은 sealed class 필수
  const factory AuthUser({
    required int id,
    required String email,
    required String name,
    String? avatar,
  }) = _AuthUser;

  factory AuthUser.fromJson(Map<String, dynamic> json) =>
      _$AuthUserFromJson(json);
}

@freezed
sealed class LoginRequest with _$LoginRequest {  // CRITICAL: Freezed 3.0은 sealed class 필수
  const factory LoginRequest({
    required String email,
    required String password,
  }) = _LoginRequest;

  factory LoginRequest.fromJson(Map<String, dynamic> json) =>
      _$LoginRequestFromJson(json);
}

@freezed
sealed class RegisterRequest with _$RegisterRequest {  // CRITICAL: Freezed 3.0은 sealed class 필수
  const factory RegisterRequest({
    required String email,
    required String password,
    required String name,
  }) = _RegisterRequest;

  factory RegisterRequest.fromJson(Map<String, dynamic> json) =>
      _$RegisterRequestFromJson(json);
}

@freezed
sealed class AuthResponse with _$AuthResponse {  // CRITICAL: Freezed 3.0은 sealed class 필수
  const factory AuthResponse({
    required String accessToken,
    required String refreshToken,
    required AuthUser user,
  }) = _AuthResponse;

  factory AuthResponse.fromJson(Map<String, dynamic> json) =>
      _$AuthResponseFromJson(json);
}
```

### domain/repositories/auth_repository.dart

```dart
import '../entities/auth_user.dart';

abstract class AuthRepository {
  Future<AuthResponse> login(LoginRequest request);
  Future<AuthResponse> register(RegisterRequest request);
  Future<void> logout();
  Future<AuthUser?> getCurrentUser();
  Future<String?> refreshToken();
  bool isAuthenticated();
}
```

### data/repositories/auth_repository_impl.dart

```dart
import '../../domain/entities/auth_user.dart';
import '../../domain/repositories/auth_repository.dart';
import '../../core/storage/secure_storage.dart';
import '../datasources/remote/api_client.dart';

class AuthRepositoryImpl implements AuthRepository {
  final ApiClient _apiClient;

  AuthRepositoryImpl(this._apiClient);

  @override
  Future<AuthResponse> login(LoginRequest request) async {
    final response = await _apiClient.post(
      '/auth/login',
      data: request.toJson(),
    );

    final authResponse = AuthResponse.fromJson(response.data);

    // 토큰 저장
    await SecureStorage.saveToken(authResponse.accessToken);
    await SecureStorage.saveRefreshToken(authResponse.refreshToken);

    return authResponse;
  }

  @override
  Future<AuthResponse> register(RegisterRequest request) async {
    final response = await _apiClient.post(
      '/auth/register',
      data: request.toJson(),
    );

    final authResponse = AuthResponse.fromJson(response.data);

    // 토큰 저장
    await SecureStorage.saveToken(authResponse.accessToken);
    await SecureStorage.saveRefreshToken(authResponse.refreshToken);

    return authResponse;
  }

  @override
  Future<void> logout() async {
    await SecureStorage.clearAll();
  }

  @override
  Future<AuthUser?> getCurrentUser() async {
    final token = SecureStorage.getToken();
    if (token == null) return null;

    try {
      final response = await _apiClient.get('/auth/me');
      return AuthUser.fromJson(response.data);
    } catch (e) {
      return null;
    }
  }

  @override
  Future<String?> refreshToken() async {
    final refreshToken = SecureStorage.getRefreshToken();
    if (refreshToken == null) return null;

    try {
      final response = await _apiClient.post(
        '/auth/refresh',
        data: {'refresh_token': refreshToken},
      );

      final newToken = response.data['access_token'];
      await SecureStorage.saveToken(newToken);
      return newToken;
    } catch (e) {
      await logout();
      return null;
    }
  }

  @override
  bool isAuthenticated() {
    return SecureStorage.getToken() != null;
  }
}
```

### presentation/providers/auth_providers.dart

```dart
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../data/repositories/auth_repository_impl.dart';
import '../../domain/entities/auth_user.dart';
import '../../domain/repositories/auth_repository.dart';
import 'app_providers.dart';

// Auth Repository Provider
final authRepositoryProvider = Provider<AuthRepository>((ref) {
  final apiClient = ref.watch(apiClientProvider);
  return AuthRepositoryImpl(apiClient);
});

// Auth State Provider
final authStateProvider = StateNotifierProvider<AuthNotifier, AsyncValue<AuthUser?>>((ref) {
  final authRepository = ref.watch(authRepositoryProvider);
  return AuthNotifier(authRepository);
});

class AuthNotifier extends StateNotifier<AsyncValue<AuthUser?>> {
  final AuthRepository _authRepository;

  AuthNotifier(this._authRepository) : super(const AsyncValue.loading()) {
    checkAuthStatus();
  }

  Future<void> checkAuthStatus() async {
    state = const AsyncValue.loading();
    try {
      final user = await _authRepository.getCurrentUser();
      state = AsyncValue.data(user);
    } catch (e, st) {
      state = AsyncValue.error(e, st);
    }
  }

  Future<void> login(String email, String password) async {
    state = const AsyncValue.loading();
    try {
      final response = await _authRepository.login(
        LoginRequest(email: email, password: password),
      );
      state = AsyncValue.data(response.user);
    } catch (e, st) {
      state = AsyncValue.error(e, st);
    }
  }

  Future<void> register(String email, String password, String name) async {
    state = const AsyncValue.loading();
    try {
      final response = await _authRepository.register(
        RegisterRequest(email: email, password: password, name: name),
      );
      state = AsyncValue.data(response.user);
    } catch (e, st) {
      state = AsyncValue.error(e, st);
    }
  }

  Future<void> logout() async {
    await _authRepository.logout();
    state = const AsyncValue.data(null);
  }
}
```

### presentation/screens/login_screen.dart

```dart
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:easy_localization/easy_localization.dart';
import 'package:fluentui_system_icons/fluentui_system_icons.dart';
import '../providers/auth_providers.dart';

class LoginScreen extends ConsumerStatefulWidget {
  const LoginScreen({super.key});

  @override
  ConsumerState<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends ConsumerState<LoginScreen> {
  final _formKey = GlobalKey<FormState>();
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  bool _obscurePassword = true;

  @override
  void dispose() {
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  void _handleLogin() async {
    if (_formKey.currentState!.validate()) {
      await ref.read(authStateProvider.notifier).login(
            _emailController.text,
            _passwordController.text,
          );
    }
  }

  @override
  Widget build(BuildContext context) {
    final authState = ref.watch(authStateProvider);

    return Scaffold(
      body: SafeArea(
        child: Center(
          child: SingleChildScrollView(
            padding: const EdgeInsets.all(24),
            child: Form(
              key: _formKey,
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  const Icon(
                    FluentIcons.person_circle_24_filled,
                    size: 80,
                    color: Colors.deepPurple,
                  ),
                  const SizedBox(height: 32),
                  Text(
                    'login'.tr(),
                    style: Theme.of(context).textTheme.headlineMedium,
                    textAlign: TextAlign.center,
                  ),
                  const SizedBox(height: 32),
                  TextFormField(
                    controller: _emailController,
                    decoration: InputDecoration(
                      labelText: 'email'.tr(),
                      prefixIcon: const Icon(FluentIcons.mail_24_regular),
                      border: const OutlineInputBorder(),
                    ),
                    keyboardType: TextInputType.emailAddress,
                    validator: (value) {
                      if (value == null || value.isEmpty) {
                        return 'Please enter email';
                      }
                      return null;
                    },
                  ),
                  const SizedBox(height: 16),
                  TextFormField(
                    controller: _passwordController,
                    decoration: InputDecoration(
                      labelText: 'password'.tr(),
                      prefixIcon: const Icon(FluentIcons.lock_closed_24_regular),
                      suffixIcon: IconButton(
                        icon: Icon(
                          _obscurePassword
                              ? FluentIcons.eye_24_regular
                              : FluentIcons.eye_off_24_regular,
                        ),
                        onPressed: () {
                          setState(() {
                            _obscurePassword = !_obscurePassword;
                          });
                        },
                      ),
                      border: const OutlineInputBorder(),
                    ),
                    obscureText: _obscurePassword,
                    validator: (value) {
                      if (value == null || value.isEmpty) {
                        return 'Please enter password';
                      }
                      return null;
                    },
                  ),
                  const SizedBox(height: 24),
                  ElevatedButton(
                    onPressed: authState.isLoading ? null : _handleLogin,
                    child: authState.isLoading
                        ? const SizedBox(
                            height: 20,
                            width: 20,
                            child: CircularProgressIndicator(strokeWidth: 2),
                          )
                        : Text('login'.tr()),
                  ),
                  const SizedBox(height: 16),
                  TextButton(
                    onPressed: () {
                      // Navigate to register screen
                    },
                    child: Text('register'.tr()),
                  ),
                  if (authState.hasError)
                    Padding(
                      padding: const EdgeInsets.only(top: 16),
                      child: Text(
                        authState.error.toString(),
                        style: const TextStyle(color: Colors.red),
                        textAlign: TextAlign.center,
                      ),
                    ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
```

계속해서 FPDart, Google Fonts, Responsive Utils를 추가하겠습니다...

## 옵션 4: FPDart (Functional Error Handling)

### pubspec.yaml 추가

```yaml
dependencies:
  fpdart: ^1.1.0
```

### Failure 클래스 정의 (core/errors/failures.dart)

```dart
import 'package:freezed_annotation/freezed_annotation.dart';

part 'failures.freezed.dart';

@freezed
sealed class Failure with _$Failure {  // CRITICAL: Freezed 3.0은 sealed class 필수
  const factory Failure.serverError([String? message]) = ServerError;
  const factory Failure.networkError([String? message]) = NetworkError;
  const factory Failure.cacheError([String? message]) = CacheError;
  const factory Failure.validationError(String message) = ValidationError;
  const factory Failure.unauthorized([String? message]) = Unauthorized;
  const factory Failure.notFound([String? message]) = NotFound;
}
```

### Repository에서 Either 사용

```dart
import 'package:fpdart/fpdart.dart';
import '../../core/errors/failures.dart';
import '../../domain/entities/user.dart';

abstract class UserRepository {
  Future<Either<Failure, List<User>>> getUsers({bool forceRefresh = false});
  Future<Either<Failure, User>> getUserById(int id);
  Future<Either<Failure, User>> createUser(User user);
}
```

### 사용 예제

```dart
// Provider에서
final usersProvider = FutureProvider<Either<Failure, List<User>>>((ref) async {
  final repository = ref.watch(userRepositoryProvider);
  return await repository.getUsers();
});

// UI에서
usersAsync.when(
  data: (either) => either.fold(
    (failure) => Text('Error: ${failure}'),
    (users) => ListView.builder(...),
  ),
  loading: () => CircularProgressIndicator(),
  error: (error, stack) => Text('Error: $error'),
)
```

## 옵션 5: Google Fonts

### pubspec.yaml 추가

```yaml
dependencies:
  google_fonts: ^6.2.1
```

### ThemeData에 적용 (main.dart)

```dart
import 'package:google_fonts/google_fonts.dart';

MaterialApp(
  theme: ThemeData(
    textTheme: GoogleFonts.robotoTextTheme(Theme.of(context).textTheme),
    colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
    useMaterial3: true,
  ),
)
```

### 특정 텍스트에 적용

```dart
Text(
  'Hello World',
  style: GoogleFonts.lato(
    fontSize: 24,
    fontWeight: FontWeight.bold,
  ),
)
```

## 옵션 6: Responsive Utils

### core/utils/responsive_utils.dart

```dart
import 'package:flutter/material.dart';

class ResponsiveUtils {
  ResponsiveUtils._();

  // 브레이크포인트
  static const double mobileMaxWidth = 600;
  static const double tabletMaxWidth = 1024;
  static const double desktopMaxWidth = 1440;

  // 디바이스 타입 체크
  static bool isMobile(BuildContext context) =>
      MediaQuery.of(context).size.width < mobileMaxWidth;

  static bool isTablet(BuildContext context) {
    final width = MediaQuery.of(context).size.width;
    return width >= mobileMaxWidth && width < tabletMaxWidth;
  }

  static bool isDesktop(BuildContext context) =>
      MediaQuery.of(context).size.width >= tabletMaxWidth;

  // 반응형 값 반환
  static T responsive<T>(
    BuildContext context, {
    required T mobile,
    T? tablet,
    T? desktop,
  }) {
    if (isDesktop(context) && desktop != null) return desktop;
    if (isTablet(context) && tablet != null) return tablet;
    return mobile;
  }

  // 반응형 패딩
  static EdgeInsets responsivePadding(BuildContext context) {
    return EdgeInsets.all(responsive(
      context,
      mobile: 16.0,
      tablet: 24.0,
      desktop: 32.0,
    ));
  }

  // 반응형 컬럼 수
  static int responsiveColumns(BuildContext context) {
    return responsive(
      context,
      mobile: 1,
      tablet: 2,
      desktop: 3,
    );
  }
}
```

### 사용 예제

```dart
Container(
  padding: ResponsiveUtils.responsivePadding(context),
  child: GridView.builder(
    gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
      crossAxisCount: ResponsiveUtils.responsiveColumns(context),
    ),
    itemBuilder: (context, index) => ...,
  ),
)
```

## 옵션 7: 패키지 버전 업데이트

### Full Stack pubspec.yaml (모든 기능 포함)

```yaml
dependencies:
  flutter:
    sdk: flutter

  # 상태 관리
  flutter_riverpod: ^3.0.0
  riverpod_annotation: ^2.3.0

  # 데이터 직렬화
  freezed_annotation: ^2.4.4
  json_annotation: ^4.8.1

  # 로컬 DB & HTTP
  drift: ^2.14.1
  drift_flutter: ^0.1.0
  dio: ^5.8.0

  # 보안 스토리지
  hive_ce: ^2.11.1
  hive_ce_flutter: ^2.0.0
  flutter_secure_storage: ^9.0.0

  # 네비게이션
  go_router: ^14.8.0

  # 다국어 지원
  easy_localization: ^3.0.5

  # UI & 아이콘
  fluentui_system_icons: ^1.1.229
  google_fonts: ^6.2.1

  # 유틸리티
  path_provider: ^2.1.2
  url_launcher: ^6.2.5
  flutter_displaymode: ^0.6.0

  # 함수형 프로그래밍
  fpdart: ^1.1.0

dev_dependencies:
  flutter_test:
    sdk: flutter
  build_runner: ^2.4.7
  riverpod_generator: ^2.4.0
  freezed: ^2.4.6
  json_serializable: ^6.7.1
  drift_dev: ^2.14.1
  hive_ce_generator: ^1.6.0
  flutter_lints: ^5.0.0
```

## analysis_options.yaml (Custom Linting)

```yaml
include: package:flutter_lints/flutter.yaml

analyzer:
  exclude:
    - "**/*.g.dart"
    - "**/*.freezed.dart"
  errors:
    invalid_annotation_target: ignore

linter:
  rules:
    # Style
    - always_use_package_imports
    - avoid_print
    - prefer_const_constructors
    - prefer_const_literals_to_create_immutables
    - prefer_single_quotes
    
    # Error Prevention
    - avoid_dynamic_calls
    - avoid_slow_async_io
    - cancel_subscriptions
    - close_sinks
    
    # Code Quality
    - prefer_final_locals
    - unnecessary_nullable_for_final_variable_declarations
    - use_super_parameters
```

## .gitignore 추가

```
# Generated files
*.g.dart
*.freezed.dart

# Hive
*.hive
*.lock

# Build
build/
```

---

# 대화형 선택 가이드

사용자가 각 옵션을 선택하면:

1. **GoRouter 선택 시**: `core/router/app_router.dart` 생성 + main.dart를 MaterialApp.router로 변경
2. **Hive CE 선택 시**: `core/storage/secure_storage.dart` 생성 + main.dart에 초기화 추가
3. **Auth 시스템 선택 시**: Auth entities, repository, providers, login/register screens 생성
4. **FPDart 선택 시**: Failure 클래스 생성 + Repository를 Either 패턴으로 변경
5. **Google Fonts 선택 시**: ThemeData에 Google Fonts 적용
6. **Responsive Utils 선택 시**: `core/utils/responsive_utils.dart` 생성

모든 선택은 독립적으로 작동하며, 원하는 조합으로 구성 가능합니다.
