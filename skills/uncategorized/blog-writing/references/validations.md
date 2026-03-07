# Blog Writing - Validations

## Weak Opening Phrases

### **Id**
blog-weak-opening-phrases
### **Severity**
error
### **Type**
regex
### **Pattern**
  - ^In this (post|article|guide)
  - ^In today's (world|age|society)
  - ^As we all know
  - ^It's no secret that
  - ^Have you ever wondered
  - ^Let me start by
  - ^Before we (begin|dive in|get started)
  - ^Welcome to (this|my|our)
### **Message**
Weak opening detected. Your first line should hook, not clear throat.
### **Fix Action**
Start with a story moment, surprising fact, provocative claim, or direct challenge
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## Cliche Conclusion Phrases

### **Id**
blog-conclusion-cliches
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - In conclusion
  - To summarize
  - To sum up
  - In summary
  - As we('ve| have) seen
  - In this (post|article), we (covered|learned|explored)
  - I hope (this|you)
  - Thanks for reading
### **Message**
Cliche conclusion detected. End with resonance, not recap.
### **Fix Action**
End with a challenge, question, call to action, or resonant final image
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## Passive Voice Overuse

### **Id**
blog-passive-voice
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - was [a-z]+ed by
  - were [a-z]+ed by
  - has been [a-z]+ed
  - have been [a-z]+ed
  - will be [a-z]+ed
  - is being [a-z]+ed
  - it was (found|discovered|noted|observed) that
### **Message**
Passive voice detected. Active voice is more direct and engaging.
### **Fix Action**
Rewrite in active voice: 'X was done by Y' → 'Y did X'
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## Vague Claims Without Specifics

### **Id**
blog-vague-claims
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - many (companies|people|developers|teams|experts)
  - some (studies|research|experts) (show|say|suggest)
  - it('s| is) (often|commonly|widely) (said|believed|known)
  - experts (say|agree|believe)
  - studies show
  - research (shows|suggests|indicates)
### **Message**
Vague claim detected. Specifics create credibility.
### **Fix Action**
Name the companies, cite the study, quote the expert. 'Many' → name three.
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## Corporate Jargon and Buzzwords

### **Id**
blog-corporate-jargon
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - leverage (our|the|your)
  - synerg(y|ies|ize)
  - paradigm shift
  - best-in-class
  - move the needle
  - circle back
  - low-hanging fruit
  - at the end of the day
  - going forward
  - touch base
  - deep dive
  - bandwidth
  - value-add
  - thought leader
### **Message**
Corporate jargon detected. Write like a human, not a press release.
### **Fix Action**
Replace with plain language. If your grandma wouldn't say it, rewrite.
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## Filler Phrases That Add Nothing

### **Id**
blog-filler-phrases
### **Severity**
info
### **Type**
regex
### **Pattern**
  - It('s| is) (important|worth noting|interesting) to note that
  - Needless to say
  - It goes without saying
  - As (a matter of fact|you (may|might) know)
  - The fact (of the matter is|that)
  - In (order|my opinion)
  - Basically,
  - Actually,
  - Obviously,
  - Literally,
  - At this point in time
### **Message**
Filler phrase detected. Every word must earn its place.
### **Fix Action**
Delete the filler and state your point directly
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## Weak Verb Constructions

### **Id**
blog-weak-verbs
### **Severity**
info
### **Type**
regex
### **Pattern**
  - \bis able to\b
  - \bhas the ability to\b
  - \bin order to\b
  - \bmake use of\b
  - \btake advantage of\b
  - \bcome to the conclusion\b
  - \bgive consideration to\b
  - \bhas an impact on\b
### **Message**
Weak verb construction. Use strong, direct verbs.
### **Fix Action**
'is able to' → 'can', 'make use of' → 'use', 'has an impact on' → 'impacts'
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## Missing Reader Focus (Too Much I/We)

### **Id**
blog-missing-you-focus
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - \b(We|Our|I|My) (believe|think|feel|are|have|want|need|offer|provide)\b
### **Message**
Heavy I/We focus detected. Blog posts should be about the reader.
### **Fix Action**
Flip perspective: 'We provide X' → 'You get X', 'Our tool does' → 'You can'
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## Clickbait Language Patterns

### **Id**
blog-clickbait-signals
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - you won't believe
  - will (blow your mind|shock you)
  - the secret (to|of)
  - one weird trick
  - what happened next
  - [0-9]+ (things|reasons|ways|tips) .*!{2,}
  - MUST (read|see|know)
### **Message**
Clickbait language detected. Build trust, not hype.
### **Fix Action**
Under-promise in headline, over-deliver in content. Remove sensationalism.
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## Long Section Without Subheading

### **Id**
blog-no-subheadings
### **Severity**
warning
### **Type**
regex
### **Pattern**
  -     ^(?!#)([^
    ]+
    ){20,}(?!#)
### **Message**
Long section without subheading. Readers scan before they read.
### **Fix Action**
Add a subheading every 300 words max. Break up walls of text.
### **Applies To**
  - *.md
  - *.mdx

## Rhetorical Questions Without Follow-through

### **Id**
blog-questions-without-answers
### **Severity**
info
### **Type**
regex
### **Pattern**
  - \?\s*\n\s*\n
### **Message**
Question followed by paragraph break. Don't leave questions hanging.
### **Fix Action**
Follow questions immediately with the answer or insight
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## Ellipsis Overuse

### **Id**
blog-triple-dots-overuse
### **Severity**
info
### **Type**
regex
### **Pattern**
  - \.{3,}
  - \.\.\.
### **Message**
Ellipsis detected. Often a crutch for unfinished thoughts.
### **Fix Action**
Complete your thought or use a dash (—) for dramatic pause instead
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## Excessive Exclamation Marks

### **Id**
blog-excessive-exclamation
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - !{2,}
  - !\s+[A-Z].*!
### **Message**
Multiple exclamation marks or excessive enthusiasm detected.
### **Fix Action**
One exclamation mark per post max. Let your words create excitement, not punctuation.
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## AI Giveaway - Landscape/World Phrases

### **Id**
blog-ai-landscape-phrases
### **Severity**
error
### **Type**
regex
### **Pattern**
  - in today's (fast-paced|digital|modern|ever-changing) (world|landscape|age|era)
  - in the (ever-evolving|rapidly changing|dynamic) landscape
  - in an increasingly (digital|connected|complex) world
  - navigating the (complex|digital|modern) landscape
### **Message**
AI giveaway phrase detected. This screams 'a robot wrote this'.
### **Fix Action**
Delete entirely. Start with something specific instead.
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## AI Giveaway - Dive/Explore/Unpack

### **Id**
blog-ai-dive-explore
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - let's (dive|delve) (in|into|deep)
  - let's (explore|unpack|examine|discuss)
  - we'll (dive|delve|explore) (into|deep)
  - without further ado
### **Message**
AI transition phrase detected. These are overused by AI writers.
### **Fix Action**
Just say what you're going to say. No announcement needed.
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## AI Giveaway - Hype Words

### **Id**
blog-ai-game-changer
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - game.?changer
  - paradigm shift
  - revolutionary
  - cutting.?edge
  - next.?level
  - unlock (your|the) (full )?potential
  - take .* to the next level
  - transform(ative|ing)? (your|the)
### **Message**
AI hype word detected. These are empty calories.
### **Fix Action**
Show the impact with specifics instead of claiming it with adjectives.
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## AI Giveaway - Comprehensive/Ultimate Claims

### **Id**
blog-ai-comprehensive-guide
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - (comprehensive|ultimate|complete|definitive) guide
  - everything you need to know
  - all you need to know
  - the only guide you
  - look no further
### **Message**
AI comprehensiveness claim detected. Let the content prove its value.
### **Fix Action**
Remove the claim. If it's truly comprehensive, readers will notice.
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## AI Giveaway - Excessive Hedging

### **Id**
blog-ai-hedging-phrases
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - it can be argued that
  - some might say
  - it('s| is) (possible|worth noting|important to note) that
  - there are various (factors|reasons|ways)
  - this could potentially
  - it('s| is) widely (believed|accepted|known)
### **Message**
AI hedging phrase detected. AI hedges to seem balanced. Humans have opinions.
### **Fix Action**
Take a stance. Say what you actually think.
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## AI Giveaway - Importance Claims

### **Id**
blog-ai-cannot-overstated
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - cannot be overstated
  - cannot be understated
  - the importance of .* is (clear|evident|crucial)
  - it goes without saying
  - needless to say
  - this is (crucial|vital|essential|critical) (for|to)
### **Message**
AI importance inflation detected. If it's important, show why.
### **Fix Action**
Remove the claim. Demonstrate importance through examples and evidence.
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## AI Giveaway - Audience Spanning

### **Id**
blog-ai-whether-beginner
### **Severity**
info
### **Type**
regex
### **Pattern**
  - whether you('re| are) a (beginner|novice|expert|seasoned)
  - no matter (your|what) (level|experience)
  - for (beginners and experts|everyone from)
  - regardless of (your|skill) (level|experience)
### **Message**
AI audience-spanning phrase. Pick a specific audience and write for them.
### **Fix Action**
Choose your reader. You can't write for everyone well.
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## AI Giveaway - Robotic Enumeration

### **Id**
blog-ai-firstly-secondly
### **Severity**
info
### **Type**
regex
### **Pattern**
  - \b(firstly|secondly|thirdly|fourthly|lastly)\b
  - \bfirst and foremost\b
  - \blast but not least\b
### **Message**
Robotic enumeration detected. This reads like a term paper.
### **Fix Action**
Use natural transitions or just number your points (1. 2. 3.)
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## AI Giveaway - Corporate Verbs

### **Id**
blog-ai-embrace-leverage
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - \bleverage\b
  - \bembrace\b
  - \bsupercharge\b
  - \bempower(s|ing|ed)?\b
  - \boptimize\b
  - \bstreamline\b
  - \butilize\b
### **Message**
Corporate verb detected. Use normal human words.
### **Fix Action**
leverage → use, embrace → try/adopt, utilize → use, empower → help
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## AI Giveaway - AI Adjectives

### **Id**
blog-ai-robust-seamless
### **Severity**
info
### **Type**
regex
### **Pattern**
  - \brobust\b
  - \bseamless(ly)?\b
  - \bholistic\b
  - \bsynerg
  - \bactionable\b
  - \bscalable\b
  - \binnovative\b
### **Message**
AI-favorite adjective detected. These words are so overused they mean nothing.
### **Fix Action**
Be specific about what makes it good. 'Robust' → 'handles 10k requests/second'
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## Experience Fabrication - Claiming Personal Experiences

### **Id**
blog-experience-fabrication
### **Severity**
error
### **Type**
regex
### **Pattern**
  - \bI've seen\b
  - \bI've been on (the|a) call
  - \bI remember when\b
  - \bIn my [0-9]+ years\b
  - \bI've worked with (many|dozens|hundreds)
  - \bI once\b
  - \bI learned the hard way\b
  - \bWhen I first started\b
  - \bIn my career\b
  - \bI've personally\b
### **Message**
Experience fabrication detected. Voice is HOW you write, not WHAT you claim.
### **Fix Action**
Transform to third-person authority: 'I've seen X' → 'X happens. Here's what it looks like.'
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## Fabricated Statistics Without Citations

### **Id**
blog-fake-statistics
### **Severity**
error
### **Type**
regex
### **Pattern**
  - [0-9]+% of developers
  - [0-9]+% of teams
  - [0-9]+% of companies
  - [0-9]+% of users
  - [0-9]+% of startups
  - [0-9] out of [0-9] (developers|teams|companies)
  - studies show(?! \()
  - research indicates(?! \()
  - data shows(?! \()
### **Message**
Uncited statistic detected. Fabricated numbers destroy credibility when fact-checked.
### **Fix Action**
Cite the source, use qualitative language ('most teams'), or name specific examples
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## AI Fingerprint - Negation Before Affirmation

### **Id**
blog-negation-affirmation
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - It's not just about
  - This isn't merely
  - It's not only about
  - more than just a
  - This is more than
  - not simply a
### **Message**
AI pattern detected: saying what it ISN'T before what it IS. State your point directly.
### **Fix Action**
Delete the negation. 'It's not just about X—it's about Y' → 'Y matters more than X'
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## AI Fingerprint - Setup Phrases

### **Id**
blog-setup-phrases
### **Severity**
warning
### **Type**
regex
### **Pattern**
  - Here's the thing:
  - The reality is(,|:)
  - What's interesting is
  - The truth is(,|:)
  - The fact is(,|:)
  - What matters (here )?is
  - The bottom line is
  - At the end of the day,
### **Message**
Setup phrase detected. These are verbal tics that delay your actual point.
### **Fix Action**
Delete the setup phrase. Start with your content directly.
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## AI Fingerprint - Empty Conclusion Phrases

### **Id**
blog-platitude-endings
### **Severity**
info
### **Type**
regex
### **Pattern**
  - and that's what makes it
  - which is exactly why
  - and that's why (it|this) matters
  - (and )?that's what makes this (so )?powerful
  - this is why it's (so )?(important|valuable)
  - and that makes all the difference
  - which is what really counts
### **Message**
Platitude ending detected. If it could attach to any paragraph, it adds nothing.
### **Fix Action**
End with specifics or just stop. 'saves time, and that's valuable' → 'saves time.'
### **Applies To**
  - *.md
  - *.mdx
  - *.txt

## False Authority - Claiming Credentials

### **Id**
blog-false-authority-claims
### **Severity**
error
### **Type**
regex
### **Pattern**
  - As a (security|software|senior|lead) engineer
  - In my role as
  - Having worked at (Google|Meta|Microsoft|Amazon|Apple)
  - As someone who has
  - Speaking from experience
  - From my time at
### **Message**
False authority claim detected. Never claim credentials or job history.
### **Fix Action**
State facts directly without claiming personal authority: 'Engineers report...' or just state it
### **Applies To**
  - *.md
  - *.mdx
  - *.txt