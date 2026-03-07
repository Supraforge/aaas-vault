# formatPlainDate

Format a `Temporal.PlainDate` using date-fns-like format tokens. Only supports date-related tokens (no time or timezone tokens).

## Signature

```ts
function formatPlainDate(
  date: Temporal.PlainDate,
  formatStr: string,
  options?: FormatPlainDateOptions
): string

interface FormatPlainDateOptions {
  locale?: string;
}
```

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `date` | `Temporal.PlainDate` | The date to format |
| `formatStr` | `string` | Format string using date-fns tokens |
| `options.locale` | `string` | Locale for formatting (default: "en-US") |

## Examples

### Basic formatting

```ts
import { formatPlainDate } from '@gobrand/tiempo';

const date = Temporal.PlainDate.from("2025-01-20");

formatPlainDate(date, "yyyy-MM-dd");
// "2025-01-20"

formatPlainDate(date, "MMMM d, yyyy");
// "January 20, 2025"

formatPlainDate(date, "EEEE, MMMM do, yyyy");
// "Monday, January 20th, 2025"
```

### With locale

```ts
formatPlainDate(date, "MMMM d, yyyy", { locale: "es-ES" });
// "enero 20, 2025"
```
