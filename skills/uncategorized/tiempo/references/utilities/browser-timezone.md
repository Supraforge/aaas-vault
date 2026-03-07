# browserTimezone

Get the IANA timezone identifier configured on the user's device.

This is primarily useful in **client-side code** (browsers, React Native) to detect the user's timezone without requiring them to select it manually.

## Signature

```ts
function browserTimezone(): string
```

## Returns

The IANA timezone identifier (e.g., `"America/New_York"`, `"Europe/London"`, `"Asia/Tokyo"`).

## Examples

### Client-side: Convert UTC to user's local time

```ts
import { toZonedTime, browserTimezone } from '@gobrand/tiempo';

const utcFromApi = "2025-01-20T20:00:00Z";
const userTime = toZonedTime(utcFromApi, browserTimezone());
```

### Get the timezone for display

```ts
import { browserTimezone } from '@gobrand/tiempo';

const tz = browserTimezone();
// => "America/New_York"

// Show in UI
<span>Your timezone: {tz}</span>
```

### Send timezone to server

```ts
import { browserTimezone } from '@gobrand/tiempo';

// Include in API requests so server knows user's timezone
fetch('/api/events', {
  headers: {
    'X-Timezone': browserTimezone()
  }
});
```

## Server-side Warning

On servers, `browserTimezone()` returns the **server's** configured timezone (often `"UTC"`), not the user's timezone.

For user-specific timezones on the server:

```ts
// Get from user preferences (stored in DB)
const userTime = toZonedTime(utcString, user.timezone);

// Or get from request header (sent by client)
const userTime = toZonedTime(utcString, req.headers['x-timezone']);

// For UTC operations, use the string literal
const utcTime = toZonedTime(utcString, "UTC");
```
