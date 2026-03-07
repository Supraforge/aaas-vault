# isPlainDateBefore

Returns true if the first date is before the second date. Compares calendar dates without time or timezone considerations.

## Signature

```ts
function isPlainDateBefore(
  date1: Temporal.PlainDate,
  date2: Temporal.PlainDate
): boolean
```

## Example

```ts
import { isPlainDateBefore } from '@gobrand/tiempo';

const jan20 = Temporal.PlainDate.from('2025-01-20');
const jan25 = Temporal.PlainDate.from('2025-01-25');

isPlainDateBefore(jan20, jan25); // true
isPlainDateBefore(jan25, jan20); // false
isPlainDateBefore(jan20, jan20); // false
```
