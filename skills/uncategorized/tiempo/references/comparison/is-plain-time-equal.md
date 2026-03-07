# isPlainTimeEqual

Returns true if both times are equal. Compares wall-clock times without date or timezone considerations.

## Signature

```ts
function isPlainTimeEqual(
  time1: Temporal.PlainTime,
  time2: Temporal.PlainTime
): boolean
```

## Example

```ts
import { isPlainTimeEqual } from '@gobrand/tiempo';
import { Temporal } from '@js-temporal/polyfill';

const nineAM_a = Temporal.PlainTime.from('09:00');
const nineAM_b = Temporal.PlainTime.from('09:00');
const fivePM = Temporal.PlainTime.from('17:00');

isPlainTimeEqual(nineAM_a, nineAM_b); // true
isPlainTimeEqual(nineAM_a, fivePM);   // false
```

## Note on Precision

PlainTime supports nanosecond precision. Two times are only equal if all components match exactly:

```ts
import { Temporal } from '@js-temporal/polyfill';

const time1 = Temporal.PlainTime.from('09:00:00.001');
const time2 = Temporal.PlainTime.from('09:00:00.002');

isPlainTimeEqual(time1, time2); // false
```
