# toPlainTime

Parse a plain time string or `PlainTimeLike` object, extract the wall-clock time from a `ZonedDateTime`, or convert a UTC ISO string, Date, or Instant to a specified timezone and extract the time.

## Signature

```ts
import { Temporal } from '@js-temporal/polyfill';

// From plain time string (no timezone needed)
function toPlainTime(input: string): Temporal.PlainTime

// From PlainTimeLike object (no timezone needed)
function toPlainTime(input: Temporal.PlainTimeLike): Temporal.PlainTime

// From ZonedDateTime (no timezone needed)
function toPlainTime(input: Temporal.ZonedDateTime): Temporal.PlainTime

// From other types (timezone required)
function toPlainTime(
  input: string | Date | Temporal.Instant | Temporal.ZonedDateTime,
  timezone: Timezone
): Temporal.PlainTime

type Timezone = 'UTC' | string;
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `string \| Date \| Temporal.Instant \| Temporal.ZonedDateTime \| Temporal.PlainTimeLike` | A plain time string (HH:MM, HH:MM:SS, or HH:MM:SS.fractional), PlainTimeLike object, UTC ISO 8601 string, Date object, Temporal.Instant, or Temporal.ZonedDateTime |
| `timezone` | `Timezone` | IANA timezone identifier. Required for ISO datetime strings, Date, and Instant inputs. |

## Returns

A `Temporal.PlainTime` representing the wall-clock time.

## Examples

### From plain time string (no timezone needed)

```ts
import { toPlainTime } from '@gobrand/tiempo';

const time = toPlainTime("14:30");    // 14:30:00
const withSeconds = toPlainTime("14:30:45"); // 14:30:45

// Supports full nanosecond precision
const withMillis = toPlainTime("14:30:45.123");       // 14:30:45.123
const withNanos = toPlainTime("14:30:45.123456789");  // Full precision

// Works with any valid time
const midnight = toPlainTime("00:00"); // 00:00:00
const endOfDay = toPlainTime("23:59"); // 23:59:00
```

### From PlainTimeLike object (no timezone needed)

```ts
import { toPlainTime } from '@gobrand/tiempo';

const time = toPlainTime({ hour: 14, minute: 30 }); // 14:30:00

// With seconds
const timeWithSeconds = toPlainTime({ hour: 14, minute: 30, second: 45 }); // 14:30:45

// Full nanosecond precision
const precise = toPlainTime({
  hour: 14,
  minute: 30,
  second: 45,
  millisecond: 123,
  microsecond: 456,
  nanosecond: 789
}); // 14:30:45.123456789
```

### From ZonedDateTime (no timezone needed)

```ts
import { toPlainTime, toZonedTime } from '@gobrand/tiempo';

const zdt = toZonedTime("2025-01-20T15:30:00Z", "America/New_York");
const time = toPlainTime(zdt); // 10:30
```

### From UTC string with timezone

```ts
import { toPlainTime } from '@gobrand/tiempo';

const time = toPlainTime("2025-01-20T15:30:00Z", "America/New_York"); // 10:30
```

### From Date with timezone

```ts
import { toPlainTime } from '@gobrand/tiempo';

const date = new Date("2025-01-20T15:30:00.000Z");
const time = toPlainTime(date, "Europe/London"); // 15:30
```

### From Instant with timezone

```ts
import { toPlainTime } from '@gobrand/tiempo';
import { Temporal } from '@js-temporal/polyfill';

const instant = Temporal.Instant.from("2025-01-20T15:30:00Z");
const time = toPlainTime(instant, "Asia/Tokyo"); // 00:30
```

## Common Patterns

### Parse user input

```ts
import { toPlainTime } from '@gobrand/tiempo';

// User enters a time in a form
const userInput = "09:30";
const time = toPlainTime(userInput);
```

### Build a time from components

```ts
import { toPlainTime } from '@gobrand/tiempo';

// From a time picker that returns separate values
const hour = 14;
const minute = 30;

const time = toPlainTime({ hour, minute });
```

### Extract time for display

```ts
import { toPlainTime, now } from '@gobrand/tiempo';

const currentTime = toPlainTime(now('America/New_York'));
console.log(currentTime.toString()); // "14:30:00"
```

### Compare times across timezones

```ts
import { toPlainTime, isPlainTimeAfter } from '@gobrand/tiempo';

const nyTime = toPlainTime("2025-01-20T20:00:00Z", "America/New_York"); // 15:00
const londonTime = toPlainTime("2025-01-20T20:00:00Z", "Europe/London"); // 20:00

// Compare wall-clock times (ignoring that they represent the same instant)
isPlainTimeAfter(londonTime, nyTime); // true
```

### Working hours check

```ts
import { toPlainTime, isPlainTimeAfter, isPlainTimeBefore } from '@gobrand/tiempo';

const openTime = toPlainTime("09:00");
const closeTime = toPlainTime("17:00");
const currentTime = toPlainTime("14:30");

const isOpen = isPlainTimeAfter(currentTime, openTime) &&
               isPlainTimeBefore(currentTime, closeTime);
// true - 14:30 is within business hours
```

### Scheduling

```ts
import { toPlainTime } from '@gobrand/tiempo';

// Define schedule slots
const morningSlot = toPlainTime({ hour: 9, minute: 0 });
const afternoonSlot = toPlainTime({ hour: 14, minute: 0 });
const eveningSlot = toPlainTime({ hour: 19, minute: 0 });
```
