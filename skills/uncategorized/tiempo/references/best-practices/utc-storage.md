# Store UTC, Display Local

Store all timestamps in UTC. Convert to local timezone only at display time.

## The Pattern

```
[User Input] → [Convert to UTC] → [Store in DB]
                                        ↓
[Display to User] ← [Convert to Local] ← [Read from DB]
```

## Why UTC for Storage?

1. **Unambiguous**: No DST confusion or timezone offset changes
2. **Comparable**: Can compare timestamps from different users/regions
3. **Portable**: Data makes sense regardless of where it's read
4. **Standard**: Most databases and APIs expect UTC

## Backend to Frontend Flow

```ts
import { toZonedTime, toIso, format, browserTimezone } from '@gobrand/tiempo';

// === BACKEND: Store in UTC ===
const eventTime = toZonedTime(userInput, userTimezone);
const utcForStorage = toIso(eventTime);  // "2025-03-09T07:00:00Z"
await db.insert({ scheduledAt: utcForStorage });

// === FRONTEND: Convert for display ===
const utcFromApi = "2025-03-09T07:00:00Z";
const userTime = toZonedTime(utcFromApi, browserTimezone());
const display = format(userTime, "EEEE 'at' h:mm a");  // "Sunday at 2:00 AM"

// === FRONTEND: Send back to backend ===
const payload = toIso(userTime);  // "2025-03-09T07:00:00Z"
```

## SQL Database Integration

```ts
import { toIso9075, toDate } from '@gobrand/tiempo';

// For raw SQL timestamp columns (UTC)
const sqlTimestamp = toIso9075(eventTime);  // "2025-01-24 14:30:00"

// For ORMs expecting Date objects
const jsDate = toDate(eventTime);
```

## Common Mistakes

```ts
// ❌ Bad - storing local time without timezone
const stored = "2025-03-09 02:30:00";  // Which timezone? DST ambiguous?

// ❌ Bad - storing offset without IANA timezone
const stored = "2025-03-09T02:30:00-05:00";  // -05:00 could be EST or CDT

// ✅ Good - store UTC
const stored = toIso(zonedTime);  // "2025-03-09T07:30:00Z"
```

## User Timezone Handling

```ts
// Server: get user's timezone from preferences
const userTimezone = user.timezone;  // "America/New_York"

// Or from request header (set by client)
const userTimezone = req.headers['x-timezone'];

// Convert for display
const displayTime = toZonedTime(utcFromDb, userTimezone);
```
