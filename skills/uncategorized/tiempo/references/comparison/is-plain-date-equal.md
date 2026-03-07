# isPlainDateEqual

Returns true if both dates are equal. Compares calendar dates without time or timezone considerations.

## Signature

```ts
function isPlainDateEqual(
  date1: Temporal.PlainDate,
  date2: Temporal.PlainDate
): boolean
```

## Example

```ts
import { isPlainDateEqual } from '@gobrand/tiempo';

const jan20a = Temporal.PlainDate.from('2025-01-20');
const jan20b = Temporal.PlainDate.from('2025-01-20');
const jan25 = Temporal.PlainDate.from('2025-01-25');

isPlainDateEqual(jan20a, jan20b); // true
isPlainDateEqual(jan20a, jan25);  // false
```
