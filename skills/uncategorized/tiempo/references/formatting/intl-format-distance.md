# intlFormatDistance

Formats the distance between two dates as a human-readable, internationalized string like "in 3 hours" or "2 days ago".

This function uses the browser's `Intl.RelativeTimeFormat` API under the hood, providing proper internationalization support for 100+ locales.

## Signature

```ts
function intlFormatDistance(
  laterDate: Temporal.Instant | Temporal.ZonedDateTime,
  earlierDate: Temporal.Instant | Temporal.ZonedDateTime,
  options?: IntlFormatDistanceOptions
): string

interface IntlFormatDistanceOptions {
  unit?: Intl.RelativeTimeFormatUnit;
  locale?: string | string[];
  localeMatcher?: 'best fit' | 'lookup';
  numeric?: 'always' | 'auto';
  style?: 'long' | 'short' | 'narrow';
}
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `laterDate` | `Temporal.Instant \| Temporal.ZonedDateTime` | The later date to compare |
| `earlierDate` | `Temporal.Instant \| Temporal.ZonedDateTime` | The earlier date to compare with |
| `options.unit` | `Intl.RelativeTimeFormatUnit` | Force a specific unit (auto-selected if not specified) |
| `options.locale` | `string \| string[]` | Locale(s) for formatting (default: system locale) |
| `options.numeric` | `'always' \| 'auto'` | Use numeric or special strings like "yesterday" (default: 'auto') |
| `options.style` | `'long' \| 'short' \| 'narrow'` | Formatting style |

## Auto Unit Selection

When `unit` is not specified, the function automatically picks the most appropriate unit:

| Distance | Selected Unit |
|----------|---------------|
| < 60 seconds | `'second'` |
| < 60 minutes | `'minute'` |
| < 24 hours | `'hour'` |
| < 7 days | `'day'` |
| < 4 weeks | `'week'` |
| < 12 months | `'month'` |
| >= 12 months | `'year'` |

## Examples

### Basic usage

```ts
import { intlFormatDistance } from '@gobrand/tiempo';

const later = Temporal.Instant.from('2024-01-01T12:00:00Z');
const earlier = Temporal.Instant.from('2024-01-01T11:00:00Z');

intlFormatDistance(later, earlier);
// => 'in 1 hour'

intlFormatDistance(earlier, later);
// => '1 hour ago'
```

### Force a specific unit

```ts
const later = Temporal.Instant.from('2025-01-01T00:00:00Z');
const earlier = Temporal.Instant.from('2024-01-01T00:00:00Z');

// Auto-selected unit
intlFormatDistance(later, earlier);
// => 'in 1 year'

// Force quarters
intlFormatDistance(later, earlier, { unit: 'quarter' });
// => 'in 4 quarters'

// Force months
intlFormatDistance(later, earlier, { unit: 'month' });
// => 'in 12 months'
```

### Localization

```ts
const later = Temporal.Instant.from('2024-01-01T12:00:00Z');
const earlier = Temporal.Instant.from('2024-01-01T11:00:00Z');

// Spanish
intlFormatDistance(later, earlier, { locale: 'es' });
// => 'dentro de 1 hora'

// French
intlFormatDistance(later, earlier, { locale: 'fr' });
// => 'dans 1 heure'

// German
intlFormatDistance(later, earlier, { locale: 'de' });
// => 'in 1 Stunde'

// Japanese
intlFormatDistance(later, earlier, { locale: 'ja' });
// => '1 時間後'
```

### Numeric vs Auto

The `numeric` option controls whether to use special strings like "yesterday", "tomorrow", "last week", etc.

```ts
const later = Temporal.Instant.from('2024-01-02T00:00:00Z');
const earlier = Temporal.Instant.from('2024-01-01T00:00:00Z');

// With numeric: 'auto' (default) - uses special strings when possible
intlFormatDistance(later, earlier, { numeric: 'auto' });
// => 'tomorrow'

// With numeric: 'always' - always uses numbers
intlFormatDistance(later, earlier, { numeric: 'always' });
// => 'in 1 day'
```

### Formatting styles

```ts
const later = Temporal.Instant.from('2024-01-05T00:00:00Z');
const earlier = Temporal.Instant.from('2024-01-01T00:00:00Z');

// Long style (default)
intlFormatDistance(later, earlier, { style: 'long' });
// => 'in 4 days'

// Narrow style
intlFormatDistance(later, earlier, { style: 'narrow' });
// => 'in 4d'
```

## Common Patterns

### Relative timestamps in UI

```ts
import { intlFormatDistance } from '@gobrand/tiempo';

function RelativeTime({ date }: { date: Temporal.ZonedDateTime }) {
  const now = Temporal.Now.zonedDateTimeISO();
  const relative = intlFormatDistance(date, now);

  return <time dateTime={date.toString()}>{relative}</time>;
}

// Usage
<RelativeTime date={post.createdAt} />
// => "2 hours ago"
```

### Due date indicator

```ts
import { intlFormatDistance, isBefore, now } from '@gobrand/tiempo';

function formatDueDate(dueDate: Temporal.ZonedDateTime): {
  text: string;
  isOverdue: boolean;
} {
  const current = now();

  return {
    text: intlFormatDistance(dueDate, current, { numeric: 'always' }),
    isOverdue: isBefore(dueDate, current),
  };
}

// Usage
const due = formatDueDate(task.dueDate);
// { text: "in 3 days", isOverdue: false }
// or
// { text: "2 days ago", isOverdue: true }
```

### Internationalized timestamps

```ts
import { intlFormatDistance } from '@gobrand/tiempo';

function getLocalizedRelativeTime(
  date: Temporal.ZonedDateTime,
  userLocale: string
): string {
  const now = Temporal.Now.zonedDateTimeISO();
  return intlFormatDistance(date, now, { locale: userLocale });
}

// For a Spanish-speaking user
getLocalizedRelativeTime(post.createdAt, 'es');
// => "hace 2 horas"

// For a Japanese-speaking user
getLocalizedRelativeTime(post.createdAt, 'ja');
// => "2 時間前"
```
