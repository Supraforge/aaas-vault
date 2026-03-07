# Skill: Hook Generator

## Metadata
- **Name**: hook-generator
- **Version**: 1.0
- **Purpose**: Generate viral hooks and thumbnail concepts for YouTube videos
- **Token Budget**: Low (can use Haiku)

---

## When to Use This Skill

Invoke when:
- Starting a new video (need hook options)
- A/B testing hook variations
- Thumbnail text brainstorming
- Improving existing underperforming hooks

---

## Hook Formulas

### Formula 1: Surprising Statistic
**Pattern**: "[Unexpected number] [group] [surprising outcome]..."

**Examples:**
- "80% Indians jinke cholesterol normal hai, unhe bhi heart attack ho sakta hai..."
- "Sirf 10 minute ki yeh cheez, heart attack risk 40% kam kar sakti hai..."
- "India mein har 33 seconds mein ek heart attack hota hai. Aur sabse scary baat..."

### Formula 2: Myth Challenge
**Pattern**: "Aapne suna hoga [common belief]. Yeh [galat/sahi nahi] hai..."

**Examples:**
- "Desi ghee heart ke liye achha hai - yeh aadha sach hai. Poori baat suniye..."
- "Walking 10,000 steps zaroori hai - yeh marketing hai, science nahi..."
- "Stent lagwa liya matlab problem solved - GALAT. Main batata hoon kyun..."

### Formula 3: Story Open
**Pattern**: "[Age] saal ke [person], [situation]. [Unexpected turn]..."

**Examples:**
- "38 saal ke Rahul, fit and active. Gym jaate the. Phir ek din..."
- "Ek patient aaye mere paas, BP normal, cholesterol normal. Phir bhi heart attack. Kaise?"
- "Doctor ne bola 'Aapka heart 70% block hai.' Patient ne pucha ek sawaal jo sabko puchna chahiye..."

### Formula 4: Direct Challenge
**Pattern**: "Agar aap [common behavior], toh [consequence]. [Solution tease]..."

**Examples:**
- "Agar aap raat ko 11 baje ke baad khaana khaate ho, aapka heart danger mein hai..."
- "Aap chai ke saath yeh karte ho? Aapka BP secretly badh raha hai..."
- "Yeh 3 symptoms ignore mat karna - yeh heart attack ke 1 month pehle dikhte hain..."

### Formula 5: Curiosity Gap
**Pattern**: "[Profession/expert] kabhi [action] nahi [does]. Jaaniye kyun..."

**Examples:**
- "Cardiologists khud yeh food kabhi nahi khaate. Reason jaanke shock lagega..."
- "Japan mein heart disease kyun kam hai? Unka ek secret..."
- "Yeh test sirf ₹500 ka hai, lekin 90% Indians nahi karwate. Life-saving hai..."

### Formula 6: Contrarian
**Pattern**: "[Popular advice] [is wrong]. [Better alternative]..."

**Examples:**
- "Cholesterol kam karne ke liye oats mat khaao. Yeh better hai..."
- "Morning walk best nahi hai. Research kehti hai yeh time better..."
- "Stress heart ke liye kharab nahi hai - ek specific type ka stress hai..."

---

## Hook Quality Criteria

### Must Have:
- [ ] Information gap (viewer MUST know more)
- [ ] Specific (numbers, names, details)
- [ ] Stakes clear (why should I care?)
- [ ] Promise value (what will I learn?)

### Must NOT Have:
- [ ] Clickbait that doesn't deliver
- [ ] Generic statements
- [ ] Fear without hope
- [ ] Vague claims

### Instant Rejects:
- "Aaj hum baat karenge..."
- "Namaste dosto..."
- "Is video mein..."
- "Hello everyone..."

---

## Thumbnail Text Generator

### Rules:
- Max 4-5 words
- Hindi emotional words in Devanagari
- English medical terms in English
- High contrast colors
- Readable on mobile (small size)

### Patterns:

**Statistic-based:**
- "80% INDIANS को नहीं पता"
- "1 in 3 HEART ATTACK"
- "₹500 TEST = LIFE SAVED"

**Question-based:**
- "STENT के बाद क्या?"
- "BP कितना होना चाहिए?"
- "CHOLESTEROL MYTH?"

**Warning-based:**
- "यह मत खाओ!"
- "SILENT KILLER"
- "DOCTOR की WARNING"

**Curiosity-based:**
- "SECRET REVEALED"
- "JAPAN का राज़"
- "DOCTORS नहीं बताते"

---

## Output Format

When generating hooks, provide:

```
## Hook Options for: [Topic]

### Option 1: [Formula Used]
**Hook text:** [Full hook script - 2-3 sentences]
**Thumbnail text:** [4-5 words]
**Thumbnail visual:** [Expression/pose suggestion]
**Why it works:** [Brief explanation]

### Option 2: [Formula Used]
...

### Option 3: [Formula Used]
...

## Recommended: Option [X]
**Reason:** [Why this is strongest for target audience]
```

---

## A/B Testing Recommendations

When multiple hooks seem strong:

| Test Element | Variation A | Variation B |
|--------------|-------------|-------------|
| Formula | Statistic | Story |
| Emotion | Fear | Curiosity |
| Specificity | Number-focused | Person-focused |
| Length | Short (10 sec) | Medium (20 sec) |

---

## Integration with Script Skill

After hook is selected:
1. Hook feeds into `youtube-script-hinglish` skill
2. Hook promise MUST be delivered in body
3. Hook angle determines content framing
4. Thumbnail text aligns with hook theme

---

*This skill ensures every video starts strong with scroll-stopping hooks.*
