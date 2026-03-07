---
name: auth-implementation-patterns
description: >-
  Master authentication and authorization patterns including JWT, OAuth2,
  session management, and RBAC to build secure, scalable access control systems.
  Use when implementing auth systems, securing APIs, or debugging security
  issues.
version: 1.0.0
dependencies:
  - nodejs
  - python3
compatibility: 'agent-zero, claude-code, cursor'
---

# Authentication & Authorization Implementation Patterns

Build secure, scalable authentication and authorization systems using industry-standard patterns and modern best practices.

## When to Use This Skill

- Implementing user authentication systems
- Securing REST or GraphQL APIs
- Adding OAuth2/social login
- Implementing role-based access control (RBAC)
- Designing session management
- Migrating authentication systems
- Debugging auth issues
- Implementing SSO or multi-tenancy

## Core Concepts

### 1. Authentication vs Authorization

**Authentication (AuthN)**: Who are you?
- Verifying identity (username/password, OAuth, biometrics)
- Issuing credentials (sessions, tokens)
- Managing login/logout

**Authorization (AuthZ)**: What can you do?
- Permission checking
- Role-based access control (RBAC)
- Resource ownership validation
- Policy enforcement

### 2. Authentication Strategies

**Session-Based:**
- Server stores session state
- Session ID in cookie
- Traditional, simple, stateful

**Token-Based (JWT):**
- Stateless, self-contained
- Scales horizontally
- Can store claims

**OAuth2/OpenID Connect:**
- Delegate authentication
- Social login (Google, GitHub)
- Enterprise SSO

## JWT Authentication

### Pattern 1: JWT Implementation

```typescript
// JWT structure: header.payload.signature
import jwt from 'jsonwebtoken';
import { Request, Response, NextFunction } from 'express';

interface JWTPayload {
    userId: string;
    email: string;
    role: string;
    iat: number;
    exp: number;
}

// Generate JWT
function generateTokens(userId: string, email: string, role: string) {
    const accessToken = jwt.sign(
        { userId, email, role },
        process.env.JWT_SECRET!,
        { expiresIn: '15m' }  // Short-lived
    );

    const refreshToken = jwt.sign(
        { userId },
        process.env.JWT_REFRESH_SECRET!,
        { expiresIn: '7d' }  // Long-lived
    );

    return { accessToken, refreshToken };
}

// Verify JWT
function verifyToken(token: string): JWTPayload {
    try {
        return jwt.verify(token, process.env.JWT_SECRET!) as JWTPayload;
    } catch (error) {
        if (error instanceof jwt.TokenExpiredError) {
            throw new Error('Token expired');
        }
        if (error instanceof jwt.JsonWebTokenError) {
            throw new Error('Invalid token');
        }
        throw error;
    }
}
```

### Pattern 2: JWT Middleware

```typescript
// Express middleware for JWT validation
function authenticateJWT(req: Request, res: Response, next: NextFunction) {
    const authHeader = req.headers.authorization;
    
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
        return res.status(401).json({ error: 'Missing or invalid authorization header' });
    }

    const token = authHeader.split(' ')[1];
    
    try {
        const payload = verifyToken(token);
        req.user = payload;  // Attach user to request
        next();
    } catch (error) {
        return res.status(403).json({ error: error.message });
    }
}

// Role-based authorization middleware
function authorize(roles: string[]) {
    return (req: Request, res: Response, next: NextFunction) => {
        if (!req.user) {
            return res.status(401).json({ error: 'Unauthorized' });
        }
        
        if (!roles.includes(req.user.role)) {
            return res.status(403).json({ error: 'Insufficient permissions' });
        }
        
        next();
    };
}
```

## OAuth2 Implementation

### Pattern 3: OAuth2 Authorization Code Flow

```typescript
// OAuth2 configuration
const oauthConfig = {
    clientId: process.env.OAUTH_CLIENT_ID,
    clientSecret: process.env.OAUTH_CLIENT_SECRET,
    authorizationURL: 'https://accounts.google.com/o/oauth2/auth',
    tokenURL: 'https://accounts.google.com/o/oauth2/token',
    callbackURL: 'http://localhost:3000/auth/callback',
    scopes: ['email', 'profile']
};

// Redirect to OAuth provider
app.get('/auth/login', (req, res) => {
    const authURL = `${oauthConfig.authorizationURL}?` +
        `client_id=${oauthConfig.clientId}&` +
        `redirect_uri=${encodeURIComponent(oauthConfig.callbackURL)}&` +
        `response_type=code&` +
        `scope=${encodeURIComponent(oauthConfig.scopes.join(' '))}`;
    
    res.redirect(authURL);
});

// Handle OAuth callback
app.get('/auth/callback', async (req, res) => {
    const { code } = req.query;
    
    if (!code) {
        return res.status(400).json({ error: 'Missing authorization code' });
    }

    try {
        // Exchange code for tokens
        const tokenResponse = await axios.post(oauthConfig.tokenURL, {
            code,
            client_id: oauthConfig.clientId,
            client_secret: oauthConfig.clientSecret,
            redirect_uri: oauthConfig.callbackURL,
            grant_type: 'authorization_code'
        });

        const { access_token, refresh_token } = tokenResponse.data;
        
        // Get user info
        const userResponse = await axios.get('https://www.googleapis.com/oauth2/v3/userinfo', {
            headers: { Authorization: `Bearer ${access_token}` }
        });

        // Create or find user in your database
        const user = await findOrCreateUser(userResponse.data);
        
        // Generate your own JWT
        const tokens = generateTokens(user.id, user.email, user.role);
        
        res.json({ user, tokens });
    } catch (error) {
        console.error('OAuth error:', error);
        res.status(500).json({ error: 'Authentication failed' });
    }
});
```

## Session Management

### Pattern 4: Secure Session Implementation

```typescript
import session from 'express-session';
import RedisStore from 'connect-redis';
import { createClient } from 'redis';

// Redis client for session storage
const redisClient = createClient({
    url: process.env.REDIS_URL
});
redisClient.connect().catch(console.error);

// Session configuration
app.use(session({
    store: new RedisStore({ client: redisClient }),
    secret: process.env.SESSION_SECRET!,
    resave: false,
    saveUninitialized: false,
    cookie: {
        httpOnly: true,
        secure: process.env.NODE_ENV === 'production',
        sameSite: 'strict',
        maxAge: 24 * 60 * 60 * 1000  // 24 hours
    }
}));

// Login handler
app.post('/login', async (req, res) => {
    const { email, password } = req.body;
    
    // Validate credentials
    const user = await validateCredentials(email, password);
    
    if (!user) {
        return res.status(401).json({ error: 'Invalid credentials' });
    }
    
    // Store user in session
    req.session.userId = user.id;
    req.session.role = user.role;
    
    res.json({ message: 'Logged in successfully' });
});

// Logout handler
app.post('/logout', (req, res) => {
    req.session.destroy((err) => {
        if (err) {
            return res.status(500).json({ error: 'Logout failed' });
        }
        res.clearCookie('connect.sid');
        res.json({ message: 'Logged out successfully' });
    });
});
```

## Role-Based Access Control (RBAC)

### Pattern 5: RBAC Implementation

```typescript
// Define roles and permissions
const roles = {
    admin: ['read', 'write', 'delete', 'manage_users'],
    editor: ['read', 'write'],
    viewer: ['read']
};

// Permission check function
function hasPermission(userRole: string, requiredPermission: string): boolean {
    const rolePermissions = roles[userRole as keyof typeof roles];
    return rolePermissions ? rolePermissions.includes(requiredPermission) : false;
}

// Resource-level authorization
function authorizeResource(requiredPermission: string) {
    return (req: Request, res: Response, next: NextFunction) => {
        if (!req.user) {
            return res.status(401).json({ error: 'Unauthorized' });
        }
        
        // Check if user has permission
        if (!hasPermission(req.user.role, requiredPermission)) {
            return res.status(403).json({ error: 'Insufficient permissions' });
        }
        
        // Check resource ownership if needed
        if (requiredPermission === 'write' || requiredPermission === 'delete') {
            const resourceId = req.params.id;
            const isOwner = await checkResourceOwnership(req.user.userId, resourceId);
            
            if (!isOwner && req.user.role !== 'admin') {
                return res.status(403).json({ error: 'Not resource owner' });
            }
        }
        
        next();
    };
}

// Usage in routes
app.get('/api/users', authenticateJWT, authorize(['admin']), getUsers);
app.post('/api/posts', authenticateJWT, authorizeResource('write'), createPost);
app.delete('/api/posts/:id', authenticateJWT, authorizeResource('delete'), deletePost);
```

## Security Best Practices

### Pattern 6: Security Checklist Implementation

1. **Use HTTPS**: Always in production
2. **Hash Passwords**: bcrypt, scrypt, or Argon2
3. **Short Token Expiry**: 15-30 minutes max
4. **Secure Cookies**: httpOnly, secure, sameSite flags
5. **Validate All Input**: Email format, password strength
6. **Rate Limit Auth Endpoints**: Prevent brute force attacks
7. **Implement CSRF Protection**: For session-based auth
8. **Rotate Secrets Regularly**: JWT secrets, session secrets
9. **Log Security Events**: Login attempts, failed auth
10. **Use MFA When Possible**: Extra security layer

## Common Pitfalls

- **Weak Passwords**: Enforce strong password policies
- **JWT in localStorage**: Vulnerable to XSS, use httpOnly cookies
- **No Token Expiration**: Tokens should expire
- **Client-Side Auth Checks Only**: Always validate server-side
- **Insecure Password Reset**: Use secure tokens with expiration
- **No Rate Limiting**: Vulnerable to brute force
- **Trusting Client Data**: Always validate on server

## Resources

- **references/jwt-best-practices.md**: JWT implementation guide
- **references/oauth2-flows.md**: OAuth2 flow diagrams and examples
- **references/session-security.md**: Secure session management
- **assets/auth-security-checklist.md**: Security review checklist
- **assets/password-policy-template.md**: Password requirements template
- **scripts/token-validator.ts**: JWT validation utility
