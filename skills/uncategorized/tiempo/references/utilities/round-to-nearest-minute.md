# roundToNearestMinute

Round a datetime to the nearest minute boundary with configurable rounding modes and multi-minute intervals.

## Signature

```ts
import { Temporal } from '@js-temporal/polyfill';

function roundToNearestMinute(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  options?: RoundToNearestMinuteOptions
): Temporal.ZonedDateTime

interface RoundToNearestMinuteOptions {
  mode?: 'round' | 'ceil' | 'floor';
  nearestTo?: 1 | 2 | 3 | 4 | 5 | 6 | 10 | 12 | 15 | 20 | 30;
}
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `Temporal.Instant \| Temporal.ZonedDateTime` | The datetime to round |
| `options.mode` | `'round' \| 'ceil' \| 'floor'` | Rounding mode. Default: `'round'` |
| `options.nearestTo` | `1 \| 2 \| 3 \| 4 \| 5 \| 6 \| 10 \| 12 \| 15 \| 20 \| 30` | Round to N-minute intervals. Default: `1` |

## Returns

A `Temporal.ZonedDateTime` rounded to the minute boundary.

## Rounding Modes

```
Given time 14:37 with 15-min slots:

14:30 ─────────●───────────────────── 14:45
             14:37

'round' → 14:30  (nearest slot - 37 is closer to 30 than 45)
'ceil'  → 14:45  (next slot - always up)
'floor' → 14:30  (current slot - always down)
```

## Examples

### Basic rounding (nearest minute)

```ts
import { roundToNearestMinute } from '@gobrand/tiempo';
import { Temporal } from '@js-temporal/polyfill';

const time = Temporal.ZonedDateTime.from('2025-01-20T14:37:42[America/New_York]');

roundToNearestMinute(time);                     // → 14:38 (42 sec >= 30)
roundToNearestMinute(time, { mode: 'ceil' });   // → 14:38 (always up)
roundToNearestMinute(time, { mode: 'floor' });  // → 14:37 (always down)
```

### 15-minute booking slots

```ts
const userRequest = Temporal.ZonedDateTime.from('2025-01-20T14:37:00[America/New_York]');

// Find the next available 15-minute slot
const nextSlot = roundToNearestMinute(userRequest, { mode: 'ceil', nearestTo: 15 });
// → 14:45

// Find the start of the current slot
const slotStart = roundToNearestMinute(userRequest, { mode: 'floor', nearestTo: 15 });
// → 14:30

// Find the nearest slot
const nearestSlot = roundToNearestMinute(userRequest, { nearestTo: 15 });
// → 14:30 (37 is closer to 30 than 45)
```

### 30-minute billing increments

```ts
// Bill in 30-minute increments, always rounding up
const sessionEnd = Temporal.ZonedDateTime.from('2025-01-20T11:07:00[America/New_York]');
const billableEnd = roundToNearestMinute(sessionEnd, { mode: 'ceil', nearestTo: 30 });
// → 11:30 (bill for 30 mins even though session was only 7 mins)
```

### Calendar display (nearest 15 minutes)

```ts
const eventTime = Temporal.ZonedDateTime.from('2025-01-20T09:07:00[America/New_York]');
const displayTime = roundToNearestMinute(eventTime, { nearestTo: 15 });
// → 09:00 (display as "9:00 AM")
```

### From Temporal.Instant

```ts
const instant = Temporal.Instant.from('2025-01-20T14:37:45Z');
const result = roundToNearestMinute(instant);

// → 14:38 UTC (rounds up, 45 sec >= 30)
// Returns ZonedDateTime in UTC
```

## Common Patterns

### Meeting scheduler

```ts
import { roundToNearestMinute } from '@gobrand/tiempo';

// User selects a time, snap to nearest 15-minute slot
function snapToSlot(selectedTime: Temporal.ZonedDateTime) {
  return roundToNearestMinute(selectedTime, { nearestTo: 15 });
}
```

### Time tracking

```ts
// Round check-in times to nearest 5 minutes
const checkIn = Temporal.ZonedDateTime.from('2025-01-20T09:03:00[America/New_York]');
const roundedCheckIn = roundToNearestMinute(checkIn, { nearestTo: 5 });
// → 09:05
```

### Reminder scheduling

```ts
// Schedule reminders at clean minute boundaries
const rawTime = Temporal.ZonedDateTime.from('2025-01-20T14:37:42[America/New_York]');
const reminderTime = roundToNearestMinute(rawTime, { mode: 'ceil' });
// → 14:38:00 (no seconds)
```

## Timezone Preservation

The function preserves the input timezone:

```ts
const tokyo = Temporal.ZonedDateTime.from('2025-01-20T14:37:42+09:00[Asia/Tokyo]');
const result = roundToNearestMinute(tokyo);

result.timeZoneId // → "Asia/Tokyo"
```
