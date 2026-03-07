# today

Get today's date as a `PlainDate` in the specified timezone.

## Signature

```ts
function today(timezone: Timezone): Temporal.PlainDate

type Timezone = 'UTC' | string;
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `timezone` | `Timezone` | IANA timezone identifier (e.g., "America/New_York", "Europe/London") or "UTC" |

## Returns

A `Temporal.PlainDate` representing today's date.

## Examples

### Server-side: Get today in UTC

```ts
import { today } from '@gobrand/tiempo';

const todayUtc = today("UTC");
```

### Server-side: Get today in user's timezone

```ts
import { today } from '@gobrand/tiempo';

// Get timezone from user preferences (stored in DB)
const todayUser = today(user.timezone);
```

### Client-side: Get today in browser's timezone

```ts
import { today, browserTimezone } from '@gobrand/tiempo';

const todayLocal = today(browserTimezone());
```

### Get today in a specific timezone

```ts
import { today } from '@gobrand/tiempo';

const todayInMadrid = today("Europe/Madrid");
const todayInTokyo = today("Asia/Tokyo");
```
