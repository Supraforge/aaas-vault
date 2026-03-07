# format

Format a `Temporal.Instant` or `ZonedDateTime` using date-fns-like format tokens.

## Signature

```ts
function format(
  input: Temporal.Instant | Temporal.ZonedDateTime,
  formatStr: string,
  options?: FormatOptions
): string

interface FormatOptions {
  locale?: string;
  timeZone?: Timezone;
}
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `input` | `Temporal.Instant \| Temporal.ZonedDateTime` | The datetime to format |
| `formatStr` | `string` | Format string using date-fns tokens |
| `options.locale` | `string` | Locale for formatting (default: "en-US") |
| `options.timeZone` | `Timezone` | Override timezone for formatting |

## Format Tokens

| Token | Example | Description |
|-------|---------|-------------|
| `yyyy` | 2025 | 4-digit year |
| `yy` | 25 | 2-digit year |
| `MMMM` | January | Full month name |
| `MMM` | Jan | Abbreviated month name |
| `MM` | 01 | 2-digit month |
| `M` | 1 | Month number |
| `Mo` | 1st | Month with ordinal |
| `dd` | 20 | 2-digit day |
| `d` | 20 | Day number |
| `do` | 20th | Day with ordinal |
| `EEEE` | Monday | Full weekday name |
| `EEE` | Mon | Abbreviated weekday |
| `HH` | 15 | 24-hour (2-digit) |
| `H` | 15 | 24-hour |
| `hh` | 03 | 12-hour (2-digit) |
| `h` | 3 | 12-hour |
| `mm` | 30 | Minutes (2-digit) |
| `ss` | 45 | Seconds (2-digit) |
| `SSS` | 123 | Milliseconds |
| `a` | PM | AM/PM |
| `z` | EST | Timezone abbreviation |
| `zzzz` | Eastern Standard Time | Full timezone name |
| `XXX` | -05:00 | Timezone offset |

## Examples

### Basic formatting

```ts
import { format } from '@gobrand/tiempo';

const zoned = Temporal.ZonedDateTime.from("2025-01-20T15:00:00-05:00[America/New_York]");

format(zoned, "yyyy-MM-dd");
// "2025-01-20"

format(zoned, "MMMM d, yyyy");
// "January 20, 2025"

format(zoned, "h:mm a");
// "3:00 PM"

format(zoned, "EEEE, MMMM do, yyyy 'at' h:mm a");
// "Monday, January 20th, 2025 at 3:00 PM"
```

### With locale

```ts
format(zoned, "MMMM d, yyyy", { locale: "es-ES" });
// "enero 20, 2025"

format(zoned, "EEEE, d MMMM yyyy", { locale: "fr-FR" });
// "lundi, 20 janvier 2025"
```

### Escaping text

Use single quotes to include literal text:

```ts
format(zoned, "'Today is' EEEE");
// "Today is Monday"

format(zoned, "MMMM do, yyyy 'at' h:mm a");
// "January 20th, 2025 at 3:00 PM"
```

## Common Patterns

### Internationalization

```ts
import { format } from '@gobrand/tiempo';

// Japanese
format(date, "yyyy年M月d日 (EEEE)", { locale: 'ja-JP' });
// "2025年1月20日 (月曜日)"
```
