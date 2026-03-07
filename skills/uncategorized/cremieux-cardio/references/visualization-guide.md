# Data Visualization Quick Reference

Every long-form Twitter post should include at least one chart or figure. This guide covers the most common visualization types for medical content.

---

## Chart Type Selection

| Data Type | Best Chart | Example Use |
|-----------|------------|-------------|
| Survival/Events over time | Kaplan-Meier | Trial primary endpoints |
| Effect sizes across trials/subgroups | Forest plot | Meta-analysis, subgroup analysis |
| Comparison between groups | Bar chart | Treatment vs. control outcomes |
| Trend over time | Line graph | Incidence trends, lab values |
| Multiple outcomes comparison | Table | Trial endpoints summary |

---

## Quick Python Templates

### Basic Setup

```python
import matplotlib.pyplot as plt
import numpy as np

# Publication-quality settings
plt.rcParams['figure.dpi'] = 150
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False
```

### Bar Chart: Treatment Comparison

```python
import matplotlib.pyplot as plt
import numpy as np

categories = ['CV Death', 'MI', 'Stroke', 'Composite']
treatment = [2.1, 4.2, 1.8, 6.5]  # percentages
placebo = [3.0, 5.5, 2.4, 8.0]

x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, treatment, width, label='Semaglutide', color='#2E86AB')
bars2 = ax.bar(x + width/2, placebo, width, label='Placebo', color='#A23B72')

ax.set_ylabel('Event Rate (%)')
ax.set_title('SELECT Trial: Cardiovascular Outcomes')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()
ax.set_ylim(0, 10)

# Add value labels
for bar in bars1:
    ax.annotate(f'{bar.get_height():.1f}%',
                xy=(bar.get_x() + bar.get_width()/2, bar.get_height()),
                ha='center', va='bottom', fontsize=9)
for bar in bars2:
    ax.annotate(f'{bar.get_height():.1f}%',
                xy=(bar.get_x() + bar.get_width()/2, bar.get_height()),
                ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('select_outcomes.png', dpi=300, bbox_inches='tight')
```

### Line Graph: Trend Over Time

```python
import matplotlib.pyplot as plt

years = [2000, 2005, 2010, 2015, 2020]
incidence = [5.2, 6.1, 7.3, 8.2, 9.5]  # per 100,000
mortality = [2.1, 2.2, 2.3, 2.4, 2.5]  # per 100,000

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(years, incidence, 'o-', label='Incidence', color='#2E86AB', linewidth=2)
ax.plot(years, mortality, 's--', label='Mortality', color='#A23B72', linewidth=2)

ax.set_xlabel('Year')
ax.set_ylabel('Rate per 100,000')
ax.set_title('Early-Onset Colorectal Cancer: Incidence vs. Mortality')
ax.legend()
ax.set_xlim(1998, 2022)

plt.tight_layout()
plt.savefig('crc_trends.png', dpi=300, bbox_inches='tight')
```

### Forest Plot: Effect Sizes

```python
import matplotlib.pyplot as plt
import numpy as np

# Data: [study, HR, lower CI, upper CI]
studies = ['FOURIER', 'ODYSSEY', 'CLEAR', 'Overall']
hrs = [0.85, 0.85, 0.87, 0.85]
lower = [0.79, 0.78, 0.79, 0.81]
upper = [0.92, 0.93, 0.96, 0.90]

fig, ax = plt.subplots(figsize=(10, 5))

# Calculate error bars
errors = np.array([[hr - lo, up - hr] for hr, lo, up in zip(hrs, lower, upper)]).T

y_pos = np.arange(len(studies))

# Plot points and error bars
ax.errorbar(hrs, y_pos, xerr=errors, fmt='o', color='#2E86AB', 
            capsize=5, capthick=2, markersize=10)

# Add reference line at HR=1
ax.axvline(x=1.0, color='gray', linestyle='--', linewidth=1)

ax.set_yticks(y_pos)
ax.set_yticklabels(studies)
ax.set_xlabel('Hazard Ratio (95% CI)')
ax.set_title('LDL-Lowering Therapies: Cardiovascular Outcomes')
ax.set_xlim(0.6, 1.2)

plt.tight_layout()
plt.savefig('forest_plot.png', dpi=300, bbox_inches='tight')
```

### Table as Figure

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('off')

data = [
    ['Endpoint', 'Semaglutide', 'Placebo', 'HR (95% CI)'],
    ['MACE', '6.5%', '8.0%', '0.80 (0.72-0.90)'],
    ['CV Death', '2.1%', '2.6%', '0.85 (0.71-1.01)'],
    ['MI', '4.2%', '5.1%', '0.82 (0.71-0.95)'],
    ['Stroke', '1.8%', '2.2%', '0.82 (0.66-1.03)'],
]

table = ax.table(cellText=data, loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1.2, 1.8)

# Style header row
for i in range(4):
    table[(0, i)].set_facecolor('#2E86AB')
    table[(0, i)].set_text_props(color='white', fontweight='bold')

plt.title('SELECT Trial: Primary and Secondary Endpoints', pad=20)
plt.tight_layout()
plt.savefig('trial_table.png', dpi=300, bbox_inches='tight')
```

---

## Design Principles

### Color Palette

Use a consistent, professional palette:
- Primary: `#2E86AB` (blue)
- Secondary: `#A23B72` (purple/magenta)
- Tertiary: `#F18F01` (orange)
- Neutral: `#C73E1D` (red for caution/negative)

### Accessibility

- Ensure sufficient contrast
- Don't rely on color alone (use markers, patterns)
- Include data labels where space permits

### Twitter-Specific

- **Aspect ratio**: 16:9 or 4:3 works well
- **Resolution**: 1200x675 or 1200x900 pixels minimum
- **File size**: Keep under 5MB for smooth loading
- **Font size**: Minimum 11pt for readability on mobile

---

## When to Use Each Type

### Kaplan-Meier Curve
- Time-to-event data
- Showing separation between groups
- Emphasizing durability of effect

### Forest Plot
- Multiple studies or subgroups
- Meta-analysis results
- Showing consistency (or heterogeneity) of effect

### Bar Chart
- Comparing discrete outcomes between groups
- Summarizing event rates
- Before/after comparisons

### Line Graph
- Trends over time
- Serial measurements
- Incidence or prevalence data

### Table (as figure)
- Multiple endpoints from single trial
- Detailed numerical data
- Comparison of several drugs/interventions

---

## Common Mistakes to Avoid

1. **Y-axis manipulation**: Don't truncate y-axis to exaggerate effects
2. **Missing CIs**: Always show confidence intervals when presenting effect sizes
3. **Relative risk only**: Include absolute numbers for context
4. **Overcrowding**: One clear message per figure
5. **Low resolution**: Export at 300 DPI minimum
6. **Missing labels**: Every axis, every bar, every line needs a label
7. **Too many colors**: Limit to 3-4 max per figure

---

## Figure Integration in Post

When describing figures in text:

**Do:**
> "The Kaplan-Meier curves separate early—by month 6—and continue diverging through 3 years of follow-up [Figure]."

> "The forest plot shows consistent benefit across all pre-specified subgroups, with no significant heterogeneity [Figure]."

**Don't:**
> "See Figure 1." (without context)
> "The graph shows the data." (obvious, uninformative)
