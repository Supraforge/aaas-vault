# isPlainTimeAfter

Returns true if the first time is after the second time. Compares wall-clock times without date or timezone considerations.

## Signature

```ts
function isPlainTimeAfter(
  time1: Temporal.PlainTime,
  time2: Temporal.PlainTime
): boolean
```

## Example

```ts
import { isPlainTimeAfter } from '@gobrand/tiempo';
import { Temporal } from '@js-temporal/polyfill';

const morning = Temporal.PlainTime.from('09:00');
const evening = Temporal.PlainTime.from('17:00');

isPlainTimeAfter(evening, morning); // true
isPlainTimeAfter(morning, evening); // false
isPlainTimeAfter(morning, morning); // false
```
