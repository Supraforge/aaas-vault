# simpleFormat

Format a Temporal date/time in a human-friendly way. Pass `date`, `time`, or both to control what's displayed.

## Signature

```ts
function simpleFormat(
  input: Temporal.PlainDate | Temporal.ZonedDateTime | Temporal.Instant,
  options: SimpleFormatOptions
): string;
```

## Options

At least one of `date` or `time` is required.

| Option | Type | Description |
|--------|------|-------------|
| `date` | `'compact' \| 'auto' \| 'full'` | Date format (see below) |
| `time` | `'12h' \| '24h' \| 'compact'` | Time format (see below) |
| `locale` | `string` | Locale for formatting (default: "en-US") |
| `timeZone` | `Timezone` | Timezone for conversion |

### Date formats

- `'compact'` - "Dec 23" (never shows year)
- `'auto'` - "Dec 23" or "Dec 23, 2020" (shows year only if not current year)
- `'full'` - "Dec 23, 2026" (always shows year)

### Time formats

- `'12h'` - "3:30 PM"
- `'24h'` - "15:30"
- `'compact'` - "9am" or "2:30pm" (omits minutes when zero, lowercase am/pm)

## Examples

### Date only

```ts
import { simpleFormat } from '@gobrand/tiempo';

// Assuming current year is 2026
const zdt = Temporal.ZonedDateTime.from("2026-12-23T15:30:00[America/New_York]");
const pastZdt = Temporal.ZonedDateTime.from("2020-12-23T15:30:00[America/New_York]");

simpleFormat(zdt, { date: 'compact' });
// "Dec 23"

simpleFormat(zdt, { date: 'auto' });
// "Dec 23"

simpleFormat(pastZdt, { date: 'auto' });
// "Dec 23, 2020"

simpleFormat(zdt, { date: 'full' });
// "Dec 23, 2026"
```

### Time only

```ts
const zdt = Temporal.ZonedDateTime.from("2026-12-23T09:00:00[America/New_York]");
const zdtWithMinutes = Temporal.ZonedDateTime.from("2026-12-23T14:30:00[America/New_York]");

simpleFormat(zdt, { time: 'compact' });
// "9am"

simpleFormat(zdtWithMinutes, { time: 'compact' });
// "2:30pm"

simpleFormat(zdtWithMinutes, { time: '12h' });
// "2:30 PM"

simpleFormat(zdtWithMinutes, { time: '24h' });
// "14:30"
```

### Date and time

```ts
const zdt = Temporal.ZonedDateTime.from("2026-12-23T09:00:00[America/New_York]");

simpleFormat(zdt, { date: 'auto', time: 'compact' });
// "Dec 23, 9am"

simpleFormat(zdt, { date: 'full', time: '12h' });
// "Dec 23, 2026, 9:00 AM"

simpleFormat(zdt, { date: 'compact', time: '24h' });
// "Dec 23, 09:00"
```

### With Instant

```ts
const instant = Temporal.Instant.from("2026-12-23T20:30:00Z");

// Date only
simpleFormat(instant, { date: 'auto', timeZone: 'America/New_York' });
// "Dec 23"

// Time only
simpleFormat(instant, { time: 'compact', timeZone: 'America/New_York' });
// "3:30pm"

// Date and time
simpleFormat(instant, { date: 'auto', time: '12h', timeZone: 'America/New_York' });
// "Dec 23, 3:30 PM"
```

### With PlainDate

```ts
const plain = Temporal.PlainDate.from("2020-12-23");

simpleFormat(plain, { date: 'auto' });
// "Dec 23, 2020"

simpleFormat(plain, { date: 'compact' });
// "Dec 23"
```

### Localization

```ts
const zdt = Temporal.ZonedDateTime.from("2020-12-23T15:30:00[America/New_York]");

simpleFormat(zdt, { date: 'auto', locale: 'es-ES' });
// "23 dic 2020"

simpleFormat(zdt, { date: 'auto', locale: 'de-DE' });
// "23. Dez. 2020"
```

## Common Patterns

### Card timestamps

```ts
import { simpleFormat } from '@gobrand/tiempo';

// Show compact date for cards
const cardDate = simpleFormat(post.createdAt, { date: 'auto' });
// "Jan 23" or "Jan 23, 2024"
```

### Event times

```ts
// Compact time for event listings
const eventTime = simpleFormat(event.startTime, { time: 'compact' });
// "9am" or "2:30pm"
```

### Full datetime display

```ts
// Date and time for detailed views
const fullDisplay = simpleFormat(appointment.datetime, {
  date: 'full',
  time: '12h'
});
// "Dec 23, 2026, 3:30 PM"
```
