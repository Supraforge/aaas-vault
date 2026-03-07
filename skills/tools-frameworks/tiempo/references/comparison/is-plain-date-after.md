# isPlainDateAfter

Returns true if the first date is after the second date. Compares calendar dates without time or timezone considerations.

## Signature

```ts
function isPlainDateAfter(
  date1: Temporal.PlainDate,
  date2: Temporal.PlainDate
): boolean
```

## Example

```ts
import { isPlainDateAfter } from '@gobrand/tiempo';

const jan20 = Temporal.PlainDate.from('2025-01-20');
const jan25 = Temporal.PlainDate.from('2025-01-25');

isPlainDateAfter(jan25, jan20); // true
isPlainDateAfter(jan20, jan25); // false
isPlainDateAfter(jan20, jan20); // false
```
