# Blog Writing - Sharp Edges

## Blog Buried Lede

### **Id**
blog-buried-lede
### **Summary**
The actual insight is buried 500 words into the post
### **Severity**
critical
### **Situation**
Writing introductions that build up to the main point
### **Why**
  Readers decide in 10 seconds whether to keep reading. If your best insight
  is in paragraph 6, 80% of people will never see it. The web isn't a mystery
  novel—give away the ending upfront, then explain how you got there.
  
### **Solution**
  Write your post. Then delete the first 3 paragraphs. Your real opening
  is usually where you finally say something interesting. Lead with the
  insight, then unpack it.
  
### **Detection Pattern**
  - In this post, we will
  - Before we begin
  - Let me start by
  - To understand this, we first need to

## Blog No Hook First Line

### **Id**
blog-no-hook-first-line
### **Summary**
Opening line doesn't create immediate curiosity
### **Severity**
high
### **Situation**
Starting posts with definitions, context, or generic statements
### **Why**
  The first line is the most valuable real estate. "API security is important"
  creates zero curiosity. "Your API is probably leaking data right now" creates
  a question the reader needs answered. Hook or lose them.
  
### **Solution**
  First line options that work:
  - Provocative claim: "Everything you know about X is wrong"
  - Surprising stat: "73% of developers have never..."
  - Story moment: "At 2 AM, the dashboard turned red"
  - Direct challenge: "You're making this mistake. Here's how I know."
  
### **Detection Pattern**
  - ^In today's world
  - ^As we all know
  - ^It's no secret that
  - ^[A-Z][a-z]+ is defined as

## Blog Wall Of Text

### **Id**
blog-wall-of-text
### **Summary**
Long paragraphs with no visual breaks or scannable structure
### **Severity**
high
### **Situation**
Writing dense paragraphs without headers, lists, or formatting
### **Why**
  Web readers scan before they read. If they can't quickly find value,
  they bounce. Walls of text are intimidating. People literally don't
  start reading them.
  
### **Solution**
  - New header every 300 words max
  - No paragraph longer than 4 lines on screen
  - Use bullet lists for 3+ related items
  - Bold key phrases for scanners
  - Pull quotes for important ideas
  - One idea per paragraph
  
### **Detection Pattern**
  - paragraphs over 200 words
  - sections without headers over 500 words

## Blog Passive Voice Epidemic

### **Id**
blog-passive-voice-epidemic
### **Summary**
Overusing passive voice kills energy and clarity
### **Severity**
medium
### **Situation**
Writing "mistakes were made" instead of "I made mistakes"
### **Why**
  Passive voice is weak, unclear, and longer. "The code was deployed by the team"
  vs "The team deployed the code." Active voice is direct, confident, and engaging.
  Passive voice makes you sound like a press release.
  
### **Solution**
  Find and replace passive constructions:
  - "was created" → "we created"
  - "it was discovered" → "we discovered" / "I found"
  - "can be seen" → "you'll see"
  - "should be noted" → "note that" / just say it
  
  One test: Can you add "by zombies" after the verb? If yes, it's passive.
  
### **Detection Pattern**
  - was [a-z]+ed by
  - were [a-z]+ed
  - has been [a-z]+ed
  - it was found that

## Blog No Specific Examples

### **Id**
blog-no-specific-examples
### **Summary**
Making claims without concrete, specific evidence
### **Severity**
critical
### **Situation**
Writing "many companies struggle with X" without naming any
### **Why**
  Vague claims feel like opinions. Specific examples feel like facts.
  "Startups fail at marketing" is forgettable. "Notion spent $0 on ads
  and grew to $10B through template virality" is memorable and shareable.
  
### **Solution**
  Every claim gets an example. Options:
  - Named company: "Stripe did this by..."
  - Personal story: "When I tried this..."
  - Specific data: "In a study of 1,247 users..."
  - Hypothetical made specific: "Imagine Sarah, a DevOps engineer at a 50-person startup..."
  
  "Many" → name three. "Often" → give a percentage. "Experts say" → name the expert.
  
### **Detection Pattern**
  - many companies
  - some experts
  - it's often said
  - "studies show" without citation

## Blog Expert Jargon Barrier

### **Id**
blog-expert-jargon-barrier
### **Summary**
Using insider terminology without explanation
### **Severity**
high
### **Situation**
Writing for experts when your audience includes beginners
### **Why**
  Every piece of jargon is a door that closes on part of your audience.
  "Implement an event-driven architecture with CQRS" means nothing to 80%
  of readers. You're not impressing anyone—you're excluding them.
  
### **Solution**
  The "coffee test": Explain it like you're telling a smart friend over coffee
  who works in a different field.
  
  - First use: Define it simply. "Event-driven architecture (where actions
    trigger reactions, like dominoes falling)"
  - Or skip jargon entirely: "Instead of checking for updates constantly,
    the system waits to be notified when something changes"
  
### **Detection Pattern**
  - unexplained acronyms
  - technical terms without context

## Blog Listicle Without Depth

### **Id**
blog-listicle-without-depth
### **Summary**
Lists that are just lists, without insight or narrative
### **Severity**
medium
### **Situation**
Writing "10 Tips for X" where each tip is one shallow sentence
### **Why**
  Shallow listicles are commodity content. Anyone can list 10 tips. The value
  is in the depth—the why, the how, the nuance, the story behind each point.
  Thin lists get skimmed and forgotten.
  
### **Solution**
  Each list item needs:
  - The what (the tip itself)
  - The why (why it matters)
  - The how (specific implementation)
  - The proof (example or story)
  
  Or: Fewer items, more depth. "3 counterintuitive lessons" beats "17 tips."
  
### **Detection Pattern**
  - list items under 50 words
  - numbered sections without examples

## Blog Conclusion Is Summary

### **Id**
blog-conclusion-is-summary
### **Summary**
Ending with "In conclusion, we learned..." recap
### **Severity**
medium
### **Situation**
Concluding by summarizing what was already said
### **Why**
  This isn't a school essay. Readers don't need a summary—they just read it.
  Weak conclusions feel like the writer ran out of energy. They end with a
  whimper instead of resonance.
  
### **Solution**
  Strong conclusion options:
  - Challenge: "Now it's your turn. The first step is..."
  - Future vision: "In 5 years, this will be obvious. The question is..."
  - Resonant image: Circle back to opening story with new meaning
  - Provocative question: "So what will you do differently on Monday?"
  - Call to action: Specific next step for the reader
  
### **Detection Pattern**
  - In conclusion
  - To summarize
  - In this post, we covered
  - As we've seen

## Blog Forgetting The Reader

### **Id**
blog-forgetting-the-reader
### **Summary**
Writing about the topic instead of writing to the reader
### **Severity**
high
### **Situation**
Focusing on what you want to say vs what they need to hear
### **Why**
  Blog posts aren't presentations—they're conversations. "This technology
  is interesting" is about you. "You can use this to solve your X problem"
  is about them. Readers care about themselves, not your topic.
  
### **Solution**
  The "you" audit:
  - Aim for 3x more "you/your" than "I/we/our"
  - Every section should answer "what's in it for the reader?"
  - Frame benefits, not features
  - Address their problems, not your solutions
  
  Before: "Our framework has three components"
  After: "You'll use three components to solve this"
  
### **Detection Pattern**
  - more "we/our" than "you/your"
  - sections without reader benefit

## Blog No Clear Takeaway

### **Id**
blog-no-clear-takeaway
### **Summary**
Reader finishes but couldn't explain what they learned
### **Severity**
critical
### **Situation**
Posts that meander without a central, memorable insight
### **Why**
  If readers can't summarize your post in one sentence, they can't share it.
  If they can't remember the key insight tomorrow, you wasted their time.
  Great posts have a "tweetable core."
  
### **Solution**
  Before writing, complete: "After reading this, readers will know that ___"
  
  The insight should be:
  - Surprising (not obvious)
  - Specific (not vague)
  - Actionable (they can do something with it)
  - Memorable (they'll remember it tomorrow)
  
  Write that sentence. Make it your north star. If a section doesn't
  support it, cut it.
  
### **Detection Pattern**
  - posts without clear thesis
  - multiple competing main points

## Blog Clickbait Mismatch

### **Id**
blog-clickbait-mismatch
### **Summary**
Headline promises something the content doesn't deliver
### **Severity**
critical
### **Situation**
Sensational headlines with underwhelming content
### **Why**
  You get one chance to break trust. Clickbait works once. The reader
  who feels tricked never comes back, never shares, and actively warns
  others. Your reputation compounds—make it compound positively.
  
### **Solution**
  The 80/20 rule: If your headline is a 10, your content must be a 12.
  Under-promise, over-deliver.
  
  Instead of: "This ONE TRICK will 10X your traffic!!!!"
  Try: "A small change that doubled our signups" (then deliver 3x the value)
  
  Readers should finish thinking "that was even better than I expected."
  
### **Detection Pattern**
  - secret
  - trick
  - hack
  - you won't believe
  - extreme numbers without proof

## Blog Wrong Reading Level

### **Id**
blog-wrong-reading-level
### **Summary**
Writing too complex or too simple for your audience
### **Severity**
medium
### **Situation**
Misjudging audience expertise level
### **Why**
  Too complex: You lose them in jargon. Too simple: You bore them or
  feel condescending. Both destroy engagement. The sweet spot is
  "respected peer explaining something new."
  
### **Solution**
  Adjust depth by audience:
  - Beginners: More analogies, more basics, more encouragement
  - Intermediate: Skip basics, focus on non-obvious insights
  - Experts: Assume knowledge, dive into nuance and edge cases
  
  When in doubt, aim for "smart generalist"—someone intelligent who
  doesn't know this specific topic. That's most of your readers.
  
### **Detection Pattern**
  - unexplained prerequisites
  - over-explained basics

## Blog Ai Tells Phrases

### **Id**
blog-ai-tells-phrases
### **Summary**
Using phrases that instantly reveal AI-generated content
### **Severity**
critical
### **Situation**
Writing content that sounds robotic and corporate
### **Why**
  Readers have developed AI-detection radar. These phrases trigger it:
  - "In today's fast-paced world"
  - "Let's dive in" / "Let's explore"
  - "Game-changer" / "Revolutionary"
  - "Unlock your potential"
  - "The importance of X cannot be overstated"
  - "Whether you're a beginner or expert"
  
  When readers sense AI, they stop trusting the content immediately.
  
### **Solution**
  Delete these phrases entirely. They add nothing.
  
  Instead of announcing ("Let's explore..."), just start exploring.
  Instead of claiming importance, demonstrate it with examples.
  Instead of spanning all audiences, pick one and write for them.
  
  Read your draft aloud. If it sounds like a press release, rewrite.
  
### **Detection Pattern**
  - in today's
  - let's dive
  - game-changer
  - unlock your potential
  - cannot be overstated

## Blog Ai Perfect Structure

### **Id**
blog-ai-perfect-structure
### **Summary**
Content that's too clean and perfectly organized
### **Severity**
high
### **Situation**
Every section is the same length, parallel structure everywhere
### **Why**
  Real human writing is messy. It has:
  - Tangents and asides
  - Sections of varying length
  - Occasional imperfect transitions
  - Personal voice and opinions
  - Things that don't quite fit but are interesting
  
  Perfect parallel structure and identical section lengths scream algorithm.
  
### **Solution**
  Deliberately break the pattern:
  - Make one section twice as long as others
  - Add a personal aside or tangent
  - Include a self-deprecating comment
  - Mention something you're not sure about
  - Have a section that's just one paragraph
  
  Humans are imperfect. Write like one.
  
### **Detection Pattern**
  - identical section lengths
  - perfect parallel structure

## Blog Ai Hedge Everything

### **Id**
blog-ai-hedge-everything
### **Summary**
Qualifying every statement to avoid committing to anything
### **Severity**
high
### **Situation**
Using "it could be argued" / "some might say" / "potentially"
### **Why**
  AI models are trained to be balanced and avoid controversy.
  This creates a distinctive voice that hedges everything:
  - "It can be argued that..."
  - "Some experts believe..."
  - "This could potentially..."
  - "There are various factors..."
  
  Humans have opinions. AI has qualifications.
  
### **Solution**
  Take a stance. Be wrong if you have to.
  
  "It could be argued that remote work is effective"
  → "Remote work is effective. Here's the data."
  
  "Some might say TDD is overkill"
  → "TDD is overkill for small scripts. Fight me."
  
  Readers respect conviction. They're bored by balance.
  
### **Detection Pattern**
  - it can be argued
  - some might say
  - this could potentially
  - there are various

## Blog Ai Corporate Vocabulary

### **Id**
blog-ai-corporate-vocabulary
### **Summary**
Using words that no human would say in conversation
### **Severity**
medium
### **Situation**
Leverage, utilize, optimize, streamline, synergy, robust
### **Why**
  These words are AI favorites because they appear frequently in
  business/corporate content. No human says "leverage" to a friend.
  
  AI vocabulary tells:
  - leverage (use)
  - utilize (use)
  - optimize (improve)
  - streamline (simplify)
  - empower (help)
  - robust (strong)
  - seamless (smooth)
  - holistic (complete)
  
### **Solution**
  Use the word you'd use texting a friend:
  - "leverage your network" → "use your network"
  - "utilize this tool" → "use this tool"
  - "optimize your workflow" → "fix what's slow"
  - "streamline the process" → "cut the steps"
  - "robust solution" → "solution that won't break"
  
  If the word has a simpler synonym, use the simpler one.
  
### **Detection Pattern**
  - leverage
  - utilize
  - streamline
  - optimize
  - robust
  - seamless

## Blog Ai No Personality

### **Id**
blog-ai-no-personality
### **Summary**
Content that could have been written by anyone (or anything)
### **Severity**
high
### **Situation**
Generic advice without personal perspective or specific experience
### **Why**
  AI can only synthesize existing information. It can't:
  - Share personal failures
  - Have controversial opinions
  - Reference specific experiences
  - Admit uncertainty authentically
  - Make jokes that might not land
  
  Content without these signals feels machine-generated.
  
### **Solution**
  Add signals of genuine perspective WITHOUT fabricating experiences:
  - Strong opinions: "This approach is overrated. Here's why..."
  - Specific knowledge: "The failure mode is always the same..."
  - Admission of limits: "The data here is unclear, but..."
  - Personality in phrasing: Wit, rhythm, unexpected word choices
  
  CRITICAL: Voice is HOW you write, not WHAT you claim.
  Never claim experiences that didn't happen.
  
### **Detection Pattern**
  - no personal stories
  - no specific experiences
  - no opinions or stances

## Blog Experience Fabrication

### **Id**
blog-experience-fabrication
### **Summary**
Claiming personal experiences that never happened
### **Severity**
critical
### **Situation**
Writing "I've seen", "I've been on", "In my years of", "I remember when"
### **Why**
  This is the cardinal sin of AI-assisted content. Fabricating experiences is:
  1. Ethically wrong - it's lying to readers
  2. Destroys trust when discovered
  3. Legally questionable for professional content
  4. Unnecessary - authority comes from knowledge depth, not fake biography
  
  Personas are VOICE, not IDENTITY. You can change HOW you write,
  but never WHAT you claim happened.
  
### **Solution**
  Transform fabricated experiences to authoritative statements:
  
  ❌ "I've been on the call when a database gets dumped in real-time."
  ✅ "Databases get dumped in real-time. Incident responders watch it happen,
     helpless to stop it mid-attack."
  
  ❌ "I remember when I first discovered this vulnerability..."
  ✅ "This vulnerability has a distinctive discovery moment."
  
  ❌ "In my 10 years as a security engineer..."
  ✅ "Security engineers report..." or just state the fact directly.
  
  The pattern: Remove "I" + past action. State the phenomenon.
  Add authority through DEPTH, not fictional autobiography.
  
### **Detection Pattern**
  - I've seen
  - I've been on
  - I remember when
  - In my [0-9]+ years
  - I've worked with
  - I once
  - I learned the hard way

## Blog Fake Statistics

### **Id**
blog-fake-statistics
### **Summary**
Making up statistics without sources
### **Severity**
critical
### **Situation**
Writing "73% of developers" or "9 out of 10 teams" without citation
### **Why**
  Fabricated statistics are lies with numbers. They're worse than vague claims
  because they pretend to be data-backed. Readers who fact-check lose all trust.
  AI-generated content is notorious for inventing plausible-sounding numbers.
  
### **Solution**
  Options for data-backed claims:
  1. Use real, cited statistics: "According to Stack Overflow's 2024 survey, 71%..."
  2. Use qualitative language: "Most teams" instead of "83% of teams"
  3. Use named examples: "Companies like Stripe, Notion, and Linear all..."
  4. Acknowledge uncertainty: "While exact numbers vary, the pattern is consistent..."
  
  If you can't cite it, don't quantify it.
  
### **Detection Pattern**
  - "[0-9]+% of (developers|teams|companies|users)"
  - "[0-9] out of [0-9]"
  - "studies show" without citation
  - "research indicates" without source

## Blog Negation Affirmation

### **Id**
blog-negation-affirmation
### **Summary**
AI fingerprint pattern - saying what something ISN'T before what it IS
### **Severity**
high
### **Situation**
Writing "It's not just about X—it's about Y"
### **Why**
  This is a distinctive AI writing pattern. Real writers state things directly.
  The structure "not just...it's about" is a verbal crutch that:
  1. Wastes words on what you're NOT saying
  2. Delays the actual point
  3. Screams "algorithm wrote this"
  
  Humans rarely write this way in natural speech.
  
### **Solution**
  Just say what it IS. Skip the negation entirely.
  
  ❌ "It's not just about the code—it's about the people."
  ✅ "The people matter more than the code."
  
  ❌ "This isn't merely a tool—it's a paradigm shift."
  ✅ "This changes how teams work."
  
  ❌ "It's not just about speed—it's about reliability."
  ✅ "Reliability matters more than speed."
  
  Delete everything before the dash. Start with your actual point.
  
### **Detection Pattern**
  - It's not just about
  - This isn't merely
  - It's not only
  - not just...it's about
  - more than just

## Blog Setup Phrases

### **Id**
blog-setup-phrases
### **Summary**
Announcing what you're about to say instead of saying it
### **Severity**
medium
### **Situation**
Starting sentences with "Here's the thing:", "The reality is:", etc.
### **Why**
  These are verbal placeholder phrases that add nothing. They delay content
  and signal that the writer doesn't trust their own point to stand alone.
  AI uses these constantly because they're common in training data.
  
  "Here's the thing:" is the written equivalent of "um".
  
### **Solution**
  Delete the setup. Start with the content.
  
  ❌ "Here's the thing: most startups fail at distribution."
  ✅ "Most startups fail at distribution."
  
  ❌ "The reality is that nobody reads documentation."
  ✅ "Nobody reads documentation."
  
  ❌ "What's interesting is how quickly this spreads."
  ✅ "This spreads fast."
  
  ❌ "The truth is, this rarely works."
  ✅ "This rarely works."
  
  Your point is stronger without the preamble.
  
### **Detection Pattern**
  - Here's the thing
  - The reality is
  - What's interesting is
  - The truth is
  - The fact is
  - What matters is

## Blog Platitude Endings

### **Id**
blog-platitude-endings
### **Summary**
Ending paragraphs with vague, uplifting non-statements
### **Severity**
medium
### **Situation**
Writing "and that's what makes it powerful" or "which is why it matters"
### **Why**
  These are empty conclusion phrases that could apply to anything. They signal
  the writer ran out of actual insight and is padding to feel complete.
  AI defaults to these because they're "safe" endings.
  
  If your ending could work on any paragraph, it adds nothing.
  
### **Solution**
  End with specifics, or just stop.
  
  ❌ "This approach saves time, and that's what makes it valuable."
  ✅ "This approach saves time." (full stop)
  
  ❌ "The team shipped faster, which is exactly why this matters."
  ✅ "The team shipped faster. Weekly releases instead of quarterly."
  
  ❌ "This creates real impact for users."
  ✅ [Delete this sentence entirely]
  
  The test: Can this ending attach to any paragraph? If yes, cut it.
  
### **Detection Pattern**
  - and that's what makes it
  - which is exactly why
  - and that's why it matters
  - this is why it's important
  - that's what makes this powerful