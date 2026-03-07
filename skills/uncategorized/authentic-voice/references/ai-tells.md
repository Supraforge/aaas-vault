# AI Writing Tells: Complete Catalog

Based on Wikipedia's Signs of AI Writing, academic research, and Sam Kriss's analysis.

## The Core Problem

LLMs use statistical algorithms that regress to the mean. They replace:
- Specific facts → generic statements
- Unusual details → common descriptions  
- Sharp claims → hedged assertions

Result: "The inventor of the first train-coupling device" becomes "a revolutionary titan of industry." The portrait fades from photograph to blurry sketch while the caption shouts louder.

---

## Category 1: Undue Emphasis on Importance

### Words to Watch
stands/serves as, is a testament/reminder, plays a vital/significant/crucial/pivotal role, underscores/highlights its importance/significance, impactful, important to social cohesion, reflects broader, symbolizing its ongoing/enduring/lasting impact, key turning point, promotes collaboration, indelible mark, deeply rooted, profound heritage, revolutionary, reinforces good habits, healthy relationship, steadfast dedication

### Real Examples

**From Statistical Institute of Catalonia article:**
> "The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain. [...] The founding of Idescat represented a significant shift toward regional statistical independence, enabling Catalonia to develop a statistical system tailored to its unique socio-economic context. This initiative was part of a broader movement across Spain to decentralize administrative functions and enhance regional governance."

**Fix:** "The 1989 law created Catalonia's census bureau."

**From Bacnotan article (etymology section!):**
> "This etymology highlights the enduring legacy of the community's resistance and the transformative power of unity in shaping its identity."

**Fix:** Delete. Etymology doesn't need to "highlight enduring legacy."

### Biology-Specific Pattern

When discussing species, LLMs over-emphasize ecosystem connections and conservation status, even when tenuous or unknown:

> "It plays a role in the ecosystem and contributes to Hawaii's rich cultural heritage. [...] Preserving this endemic species is vital not only for ecological diversity but also for sustaining the cultural traditions connected to Hawaii's native flora."

> "Currently, there is no specific conservation assessment for Lethrinops lethrinus by the International Union for Conservation of Nature (IUCN). However, the general health of the Lake Malawi ecosystem is crucial for the survival of this and other endemic species."

**Fix:** State the actual conservation status. If unknown, say unknown. Don't pad with generic ecosystem importance.

---

## Category 2: Superficial Analysis (Tailing Participles)

### Words to Watch
ensuring..., highlighting..., emphasizing..., reflecting..., underscoring..., showcasing..., conducive/tantamount/contributing to..., cultivating..., encompassing..., aligns with..., essentially/fundamentally is...

### The Key Tell

The subjects of these verbs are inanimate things. A person can highlight something. A fact cannot. The "highlighting" is a claim by a disembodied narrator about meaning.

### Real Examples

**From Douéra article:**
> "Douera enjoys close proximity to the capital city, Algiers, further enhancing its significance as a dynamic hub of activity and culture."

**From African-American culture article:**
> "The civil rights movement emerged as a powerful continuation of this struggle, emphasizing the importance of solidarity and collective action in the fight for justice. This historical legacy has influenced contemporary African-American families, shaping their values, community structures, and approaches to political engagement."

**From McAllen Texas Temple article:**
> "Its bilingual monument sign, with inscriptions in both English and Spanish, underscores its role in bringing together Latter-day Saints from the United States and Mexico."

**Fix:** Delete the tailing phrase. If the connection is meaningful, state it directly as a new sentence with evidence.

---

## Category 3: Promotional Language

### Words to Watch
continues to captivate, groundbreaking (figurative), stunning natural beauty, enduring/lasting legacy, nestled, in the heart of, boasts a..., breathtaking, vibrant, diverse tapestry, rich cultural heritage, fascinating glimpse

### Real Examples

**From Alamata (woreda) article:**
> "Nestled within the breathtaking region of Gonder in Ethiopia, Alamata Raya Kobo stands as a vibrant town with a rich cultural heritage and a significant place within the Amhara region. From its scenic landscapes to its historical landmarks, Alamata Raya Kobo offers visitors a fascinating glimpse into the diverse tapestry of Ethiopia."

**From Tamil Nadu Tourism article:**
> "TTDC acts as the gateway to Tamil Nadu's diverse attractions, seamlessly connecting the beginning and end of every traveller's journey. It offers dependable, value-driven experiences that showcase the state's rich history, spiritual heritage, and natural beauty."

**From Kenya Airways article:**
> "These initiatives demonstrate Kenya Airways' dual commitment to sustainability and financial prudence. As Kamal emphasized, 'We are not just cutting costs for short-term gains; we are building a more resilient and sustainable future for Kenya Airways.'"

**Fix:** State facts. "Alamata Raya Kobo is a market town in Gonder." Let readers judge importance.

---

## Category 4: Notability and Attribution Claims

### Words to Watch
independent coverage, local/regional/national/[country name] media outlets, music/business/tech outlets, written by a leading expert, active social media presence

### The Pattern

LLMs prove something is notable by claiming it's notable, often listing sources without summarizing what they said:

**From Sinead Bovell article:**
> "She spoke about AI on CNN, and was featured in Vogue, Wired, Toronto Star, and other media. [...] Her insights have also been featured in *Wired*, *Refinery29*, and other prominent media outlets."

**Social Media Pattern (extremely common post-2024):**
> "The mall maintains a strong digital presence, particularly on Instagram, where it actively shares the latest updates and events. Forum Kochi has consistently demonstrated excellence in digital promotions."

**Notability Sections:**
LLMs create entire sections listing sources in list format rather than summarizing content:

> Media coverage
> **IRNA** – Coverage of his inter-city marathon events.
> **ISNA** – Report on an 80 km provincial peace run.
> **IFRC** – Feature on his humanitarian campaigns.

**Fix:** Summarize what sources say, then cite them as footnotes. Never create "Media Coverage" sections.

---

## Category 5: Ghost Language (from Sam Kriss)

### The Pattern

AI writing is obsessed with:
- Ghosts, shadows, memories, whispers
- Quietness (things are described as quiet for no narrative reason)
- Sensory language attached to abstract concepts

### Examples

> "Thursday is a liminal day that tastes of almost-Friday."
> "Grief has a color. Sorrow tastes of metal."
> "Emotions are draped over sentences."
> "Hands humming with the color of grief."

This is "robotic synesthesia"—piling sensory concepts onto immaterial things until they collapse.

**Fix:** Ground sensory language in actual physical experience. If you haven't experienced it, don't describe it sensorially.

---

## Category 6: Structural Tells

### Rule of Three

LLMs love grouping in threes to appear comprehensive:

> "The event features keynote sessions, panel discussions, and networking opportunities."
> "global SEO professionals, marketing experts, and growth hackers"

**Fix:** Use two items, or four+. If you must use three, make them substantively different.

### Negative Parallelism

> "It's not just about X, it's about Y"
> "Not only does it X, but it also Y"
> "This is not merely X—it's Y"

**Fix:** Say Y directly without the rhetorical setup.

### Em Dash Overuse

LLMs use em dashes more than humans, often formulaically to punch up emphasis:

> "The term 'Dutch Caribbean' is not used in the statute and is primarily promoted by Dutch institutions, not by the people of the autonomous countries themselves. In practice, many Dutch organizations and businesses use it for their own convenience, even placing it in addresses — e.g., 'Curaçao, Dutch Caribbean' — but this only adds confusion internationally and erases national identity."

**Fix:** One em dash per paragraph maximum. Often commas or periods work better.

---

## Overused Vocabulary (Research-Based)

Words with documented overrepresentation in AI text (100x+ compared to pre-2022 human writing):

### Extreme Overuse (1000x+)
breathtaking, vibrant, tapestry

### Severe Overuse (100-1000x)
delve/delving, intricate/intricacies, meticulous/meticulously, pivotal, testament, multifaceted, comprehensive, nuanced, captivating

### High Overuse (50-100x)
underscore, showcase, foster, leverage, harness, utilize, navigate, empower, enable, enhance, elevate, streamline, crucial, vital, significant, unprecedented, innovative, robust, seamless, cutting-edge, groundbreaking, landscape, realm, paradigm, framework, synergy

### Moderate Overuse (10-50x)
arguably, notably, undeniably, remarkably, dynamic, diverse, fascinating, milestone, cornerstone, trajectory

### Common AI Phrases (Delete entirely)
- "In today's fast-paced world..."
- "In the realm of..."
- "Navigate the landscape of..."
- "It's important to note/remember that..."
- "This serves as a testament to..."
- "Reflects the continued relevance of..."
- "A rich tapestry of..."
- "The ever-evolving landscape..."
- "Plays a crucial role in..."

---

## What's NOT an AI Tell

Don't overcorrect. These are unreliable indicators:

### Sophisticated Vocabulary
LLMs actually avoid rare words (statistically uncommon). "Fancy" or "academic" words are not AI tells—low-frequency unusual words are *less* likely in AI text.

### Perfect Grammar
Many humans write correctly. Grammar alone proves nothing.

### Starting Sentences with Conjunctions
Despite what some were taught, this has precedent and is accepted by style guides.

### Mixed Registers
Combining formal and casual language may indicate: computer science background, youth, playfulness, neurodivergence, or multiple editors. Not AI.

### "Bland" or "Robotic" Prose
Modern LLMs tend toward *effusive and verbose*, not bland. If it's bland, that's actually less likely to be AI.

### Letter-Like Formatting
Salutations and valedictions predate LLMs. New users may format talk pages like emails.

---

## Self-Editing Process

### Pass 1: Find the Puffery
Search for: significant, pivotal, crucial, vital, important, testament, legacy, broader, reflects, underscores, highlights, emphasizes

For each hit: Can you show evidence? If not, delete.

### Pass 2: Kill Tailing Participles
Search for: -ing phrases at sentence ends
Delete all of them. If the point matters, make it a separate sentence with evidence.

### Pass 3: Check Rhythm
- Count words per sentence
- Are they all similar? Vary them
- Any fragments? Add some
- All long sentences? Break some up

### Pass 4: Vocabulary Scan
Search for: delve, tapestry, landscape, leverage, utilize, foster, navigate, showcase, nuanced, comprehensive

Replace or delete.

### Pass 5: Structure Check
- Any lists of exactly three? Change to two or four+
- More than one em dash per paragraph? Remove some
- Opening with "In today's..." or "In the realm of..."? Rewrite

---

## Before/After Examples

### Business Writing

**Before:**
> In today's rapidly evolving business landscape, leveraging innovative technologies has become pivotal for organizations seeking to navigate the complexities of digital transformation. This comprehensive guide delves into the multifaceted strategies that empower companies to harness the full potential of cutting-edge solutions, ensuring sustainable growth and competitive advantage.

**After:**
> Most companies still run on spreadsheets and email. Here's how the ones that don't actually made the switch.

### Place Description

**Before:**
> Nestled in the heart of the Pacific Northwest, Portland stands as a vibrant testament to sustainable urban living, where diverse communities come together to create a rich tapestry of culture, cuisine, and innovation. The city continues to captivate visitors with its stunning natural beauty and enduring commitment to environmental stewardship.

**After:**
> Portland has more strip clubs per capita than any American city. Also a lot of bike lanes. The two facts feel related somehow.

### Product Copy

**Before:**
> Our meticulously crafted solution offers a seamless, intuitive experience that revolutionizes the way users interact with their data. The vibrant interface showcases a diverse array of features designed to enhance productivity and foster collaboration across teams.

**After:**
> The dashboard loads in under a second. You can share reports with a link. That's basically it.

### Article Opening

**Before:**
> The intricate tapestry of modern urban planning represents a fascinating intersection of diverse disciplines, where architects, policymakers, and community stakeholders collaborate to shape the cities of tomorrow, emphasizing the crucial importance of sustainable development and inclusive design.

**After:**
> Jane Jacobs hated highways. That fight shaped every American city built after 1960.
