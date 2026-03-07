# isPlainTimeBefore

Returns true if the first time is before the second time. Compares wall-clock times without date or timezone considerations.

## Signature

```ts
function isPlainTimeBefore(
  time1: Temporal.PlainTime,
  time2: Temporal.PlainTime
): boolean
```

## Example

```ts
import { isPlainTimeBefore } from '@gobrand/tiempo';
import { Temporal } from '@js-temporal/polyfill';

const morning = Temporal.PlainTime.from('09:00');
const evening = Temporal.PlainTime.from('17:00');

isPlainTimeBefore(morning, evening); // true
isPlainTimeBefore(evening, morning); // false
isPlainTimeBefore(morning, morning); // false
```

## Use Case: Business Hours Check

```ts
import { isPlainTimeBefore, now } from '@gobrand/tiempo';
import { Temporal } from '@js-temporal/polyfill';

const currentTime = now('America/New_York').toPlainTime();
const openTime = Temporal.PlainTime.from('09:00');
const closeTime = Temporal.PlainTime.from('17:00');

const isOpen = !isPlainTimeBefore(currentTime, openTime) &&
               isPlainTimeBefore(currentTime, closeTime);
```
