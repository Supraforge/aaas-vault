# toPlainDate

Parse a plain date string or `PlainDateLike` object, extract the calendar date from a `ZonedDateTime`, or convert a UTC ISO string, Date, or Instant to a specified timezone and extract the date.

## Signature

```ts
import { Temporal } from '@js-temporal/polyfill';

// From plain date string (no timezone needed)
function toPlainDate(input: string): Temporal.PlainDate

// From PlainDateLike object (no timezone needed)
function toPlainDate(input: Temporal.PlainDateLike): Temporal.PlainDate

// From ZonedDateTime (no timezone needed)
function toPlainDate(input: Temporal.ZonedDateTime): Temporal.PlainDate

// From other types (timezone required)
function toPlainDate(
  input: string | Date | Temporal.Instant | Temporal.ZonedDateTime,
  timezone: Timezone
): Temporal.PlainDate

type Timezone = 'UTC' | string;
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `string \| Date \| Temporal.Instant \| Temporal.ZonedDateTime \| Temporal.PlainDateLike` | A plain date string (YYYY-MM-DD), PlainDateLike object, UTC ISO 8601 string, Date object, Temporal.Instant, or Temporal.ZonedDateTime |
| `timezone` | `Timezone` | IANA timezone identifier. Required for ISO datetime strings, Date, and Instant inputs. |

## Returns

A `Temporal.PlainDate` representing the calendar date.

## Examples

### From plain date string (no timezone needed)

```ts
import { toPlainDate } from '@gobrand/tiempo';

const date = toPlainDate("2025-01-20"); // 2025-01-20

// Works with any valid date
const leapDay = toPlainDate("2024-02-29"); // 2024-02-29
```

### From PlainDateLike object (no timezone needed)

```ts
import { toPlainDate } from '@gobrand/tiempo';

const date = toPlainDate({ year: 2025, month: 1, day: 20 }); // 2025-01-20

// Partial objects work too (Temporal fills in defaults)
const date2 = toPlainDate({ year: 2025, month: 6, day: 15 }); // 2025-06-15
```

### From ZonedDateTime (no timezone needed)

```ts
import { toPlainDate, toZonedTime } from '@gobrand/tiempo';

const zdt = toZonedTime("2025-01-20T15:30:00Z", "America/New_York");
const date = toPlainDate(zdt); // 2025-01-20
```

### From UTC string with timezone

```ts
import { toPlainDate } from '@gobrand/tiempo';

const date = toPlainDate("2025-01-20T15:30:00Z", "America/New_York"); // 2025-01-20
```

### From Date with timezone

```ts
import { toPlainDate } from '@gobrand/tiempo';

const jsDate = new Date("2025-01-20T15:30:00.000Z");
const date = toPlainDate(jsDate, "Europe/London"); // 2025-01-20
```

### From Instant with timezone

```ts
import { toPlainDate } from '@gobrand/tiempo';
import { Temporal } from '@js-temporal/polyfill';

const instant = Temporal.Instant.from("2025-01-20T15:30:00Z");
const date = toPlainDate(instant, "Asia/Tokyo"); // 2025-01-21 (next day!)
```

## Date Boundary Crossings

The same UTC instant can represent different calendar dates depending on the timezone. This is critical for scheduling, deadlines, and event management.

### Late UTC becomes next day in positive-offset timezones

```ts
import { toPlainDate } from '@gobrand/tiempo';

// 23:00 UTC on Jan 20 → 08:00 Jan 21 in Tokyo (UTC+9)
const date = toPlainDate("2025-01-20T23:00:00Z", "Asia/Tokyo");
// date.day === 21
```

### Early UTC becomes previous day in negative-offset timezones

```ts
import { toPlainDate } from '@gobrand/tiempo';

// 02:00 UTC on Jan 21 → 21:00 Jan 20 in New York (UTC-5)
const date = toPlainDate("2025-01-21T02:00:00Z", "America/New_York");
// date.day === 20
```

### Same instant, three different calendar days

```ts
import { toPlainDate } from '@gobrand/tiempo';

const instant = "2025-01-20T10:30:00Z";

const kiritimati = toPlainDate(instant, "Pacific/Kiritimati"); // Jan 21 (UTC+14)
const london = toPlainDate(instant, "Europe/London");          // Jan 20 (UTC+0)
const bakerIsland = toPlainDate(instant, "Etc/GMT+12");        // Jan 19 (UTC-12)
```

## Common Patterns

### Parse user input

```ts
import { toPlainDate } from '@gobrand/tiempo';

// User enters a date in a form
const userInput = "2025-01-20";
const date = toPlainDate(userInput);
```

### Build a date from components

```ts
import { toPlainDate } from '@gobrand/tiempo';

// From a date picker that returns separate values
const year = 2025;
const month = 1;
const day = 20;

const date = toPlainDate({ year, month, day });
```

### Check if today is a deadline

```ts
import { toPlainDate, isPlainDateEqual } from '@gobrand/tiempo';

const deadline = toPlainDate("2025-01-20");
const instant = "2025-01-21T03:00:00Z";

const nyDate = toPlainDate(instant, "America/New_York"); // Still Jan 20 in NY
const londonDate = toPlainDate(instant, "Europe/London"); // Jan 21 in London

isPlainDateEqual(nyDate, deadline);     // true - still time in NY!
isPlainDateEqual(londonDate, deadline); // false - deadline passed in London
```

### Event scheduling across timezones

```ts
import { toPlainDate } from '@gobrand/tiempo';

// Meeting scheduled for 22:00 UTC on Jan 20
const meetingUtc = "2025-01-20T22:00:00Z";

// What day is this meeting for each participant?
const nyDate = toPlainDate(meetingUtc, "America/New_York");  // Jan 20
const tokyoDate = toPlainDate(meetingUtc, "Asia/Tokyo");     // Jan 21

// Tokyo participant should block Jan 21, not Jan 20!
```

### Birthday/anniversary check

```ts
import { toPlainDate, isPlainDateEqual } from '@gobrand/tiempo';

const birthday = toPlainDate("2025-01-15");
const instant = "2025-01-14T20:00:00Z";

const tokyo = toPlainDate(instant, "Asia/Tokyo");         // Jan 15 - it's their birthday!
const newYork = toPlainDate(instant, "America/New_York"); // Jan 14 - not yet

isPlainDateEqual(tokyo, birthday);   // true
isPlainDateEqual(newYork, birthday); // false
```
