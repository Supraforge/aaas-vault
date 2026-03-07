---
name: foundation-models
description: On-device LLM integration using Apple's Foundation Models framework. Use when implementing AI text generation, structured output, or tool calling.
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, AskUserQuestion]
---

# Foundation Models

Integrate Apple's on-device LLM into your apps for privacy-preserving AI features.

## When to Use

- User wants AI text generation features
- User needs structured data from natural language
- User asks about prompting or LLM integration
- User wants to implement AI assistants
- User needs content summarization or extraction

## Quick Start

### 1. Check Availability

```swift
import FoundationModels

struct IntelligentView: View {
    private var model = SystemLanguageModel.default

    var body: some View {
        switch model.availability {
        case .available:
            ContentView()
        case .unavailable(.deviceNotEligible):
            UnsupportedDeviceView()
        case .unavailable(.appleIntelligenceNotEnabled):
            EnableIntelligenceView()
        case .unavailable(.modelNotReady):
            ModelDownloadingView()
        case .unavailable(let reason):
            ErrorView(reason: reason)
        }
    }
}
```

### 2. Create a Session

```swift
// Simple session
let session = LanguageModelSession()

// Session with instructions
let session = LanguageModelSession(instructions: """
    You are a helpful cooking assistant.
    Provide concise, practical advice for home cooks.
    """)
```

### 3. Generate Response

```swift
let response = try await session.respond(to: "What's a quick dinner idea?")
print(response.content)
```

## Prompt Engineering Best Practices

### The Instruction Formula

Instructions set the model's persona and constraints. They're prioritized over prompts.

```
[Role] + [Task] + [Style] + [Safety]
```

**Example:**
```swift
let instructions = """
    You are a fitness coach specializing in home workouts.
    Help users create exercise routines based on their equipment and goals.
    Keep responses under 100 words and use bullet points for exercises.
    Decline requests for medical advice and suggest consulting a doctor.
    """
```

### Instruction Components

| Component | Purpose | Example |
|-----------|---------|---------|
| **Role** | Define persona | "You are a travel expert" |
| **Task** | What to do | "Help plan itineraries" |
| **Style** | Output format | "Use bullet points, be concise" |
| **Safety** | Boundaries | "Don't provide medical advice" |

### Effective Prompts

Prompts are user inputs. Make them:

| Principle | Bad | Good |
|-----------|-----|------|
| **Specific** | "Help with cooking" | "Suggest a 30-minute vegetarian dinner" |
| **Constrained** | "Tell me about dogs" | "Describe Golden Retrievers in 3 sentences" |
| **Focused** | "I need help with many things" | "What ingredients substitute for eggs in baking?" |

### Prompt Patterns

**Question Pattern:**
```swift
let prompt = "What are three ways to reduce food waste at home?"
```

**Command Pattern:**
```swift
let prompt = "Create a weekly meal plan for a family of four, budget-friendly."
```

**Extraction Pattern:**
```swift
let prompt = """
    Extract the following from this email:
    - Sender name
    - Meeting date
    - Action items

    Email: \(emailContent)
    """
```

**Transformation Pattern:**
```swift
let prompt = "Rewrite this text to be more formal: \(casualText)"
```

## Structured Output with @Generable

Get typed Swift data instead of raw strings.

### Define Generable Types

```swift
@Generable(description: "A recipe suggestion")
struct Recipe {
    var name: String

    @Guide(description: "Cooking time in minutes", .range(5...180))
    var cookingTime: Int

    @Guide(description: "Difficulty level", .options(["Easy", "Medium", "Hard"]))
    var difficulty: String

    @Guide(description: "List of ingredients", .count(3...15))
    var ingredients: [String]

    @Guide(description: "Step-by-step instructions")
    var instructions: [String]
}
```

### @Guide Constraints

| Constraint | Use Case | Example |
|------------|----------|---------|
| `.range(min...max)` | Numeric bounds | `.range(1...100)` |
| `.options([...])` | Enum-like choices | `.options(["Low", "Medium", "High"])` |
| `.count(n)` | Exact array length | `.count(5)` |
| `.count(min...max)` | Array length range | `.count(3...10)` |

### Generate Structured Data

```swift
let session = LanguageModelSession(instructions: """
    You are a recipe assistant. Generate practical, home-cook friendly recipes.
    """)

let recipe = try await session.respond(
    to: "Suggest a quick pasta dish",
    generating: Recipe.self
)

print("Recipe: \(recipe.content.name)")
print("Time: \(recipe.content.cookingTime) minutes")
print("Ingredients: \(recipe.content.ingredients.joined(separator: ", "))")
```

### Complex Nested Structures

```swift
@Generable(description: "A travel itinerary")
struct Itinerary {
    var destination: String

    @Guide(description: "Daily activities for the trip")
    var days: [DayPlan]
}

@Generable(description: "Activities for one day")
struct DayPlan {
    var dayNumber: Int

    @Guide(description: "Morning activity")
    var morning: String

    @Guide(description: "Afternoon activity")
    var afternoon: String

    @Guide(description: "Evening activity")
    var evening: String
}
```

## Tool Calling

Let the model call your code to access data or perform actions.

### Define a Tool

```swift
struct WeatherTool: Tool {
    let name = "getWeather"
    let description = "Get current weather for a location"

    struct Arguments: Codable {
        var location: String
    }

    func call(arguments: Arguments) async throws -> ToolOutput {
        let weather = await WeatherService.shared.fetch(for: arguments.location)
        return .string("Temperature: \(weather.temp)°F, Conditions: \(weather.conditions)")
    }
}
```

### Use Tools in Session

```swift
let weatherTool = WeatherTool()
let session = LanguageModelSession(
    instructions: "You help users plan outdoor activities based on weather.",
    tools: [weatherTool]
)

// Model automatically calls tool when needed
let response = try await session.respond(
    to: "Should I go hiking in San Francisco today?"
)
```

### Tool Error Handling

```swift
do {
    let response = try await session.respond(to: prompt)
} catch let error as LanguageModelSession.ToolCallError {
    print("Tool '\(error.tool.name)' failed: \(error.underlyingError)")
} catch {
    print("Generation error: \(error)")
}
```

## Snapshot Streaming

Show responses as they generate for better UX.

### Stream to SwiftUI

```swift
@Generable
struct StoryIdea {
    var title: String

    @Guide(description: "A brief plot summary")
    var plot: String

    @Guide(description: "Main characters", .count(2...4))
    var characters: [String]
}

struct StreamingView: View {
    @State private var partial: StoryIdea.PartiallyGenerated?
    @State private var isGenerating = false

    var body: some View {
        VStack(alignment: .leading) {
            if let partial {
                if let title = partial.title {
                    Text(title).font(.headline)
                }
                if let plot = partial.plot {
                    Text(plot)
                }
                if let characters = partial.characters {
                    ForEach(characters, id: \.self) { char in
                        Text("• \(char)")
                    }
                }
            }

            Button("Generate Story Idea") {
                Task { await generateStory() }
            }
            .disabled(isGenerating)
        }
    }

    func generateStory() async {
        isGenerating = true
        defer { isGenerating = false }

        let session = LanguageModelSession()
        let stream = session.streamResponse(
            to: "Create a sci-fi story idea",
            generating: StoryIdea.self
        )

        for try await snapshot in stream {
            partial = snapshot
        }
    }
}
```

## Multi-Turn Conversations

Reuse sessions to maintain context.

```swift
class ChatViewModel: ObservableObject {
    private var session: LanguageModelSession?
    @Published var messages: [ChatMessage] = []

    func startConversation() {
        session = LanguageModelSession(instructions: """
            You are a helpful assistant. Remember context from earlier in our conversation.
            """)
    }

    func send(_ message: String) async throws {
        guard let session else { return }

        messages.append(ChatMessage(role: .user, content: message))

        let response = try await session.respond(to: message)

        messages.append(ChatMessage(role: .assistant, content: response.content))
    }
}
```

## Error Handling

```swift
do {
    let response = try await session.respond(to: prompt)
} catch LanguageModelSession.GenerationError.exceededContextWindowSize {
    // Context too large (>4,096 tokens)
    // Solution: Start new session, break into smaller requests
} catch LanguageModelSession.GenerationError.cancelled {
    // Request was cancelled
} catch {
    print("Unexpected error: \(error)")
}
```

## Context Window Management

The model supports **4,096 tokens** per session (~12,000-16,000 characters).

### Token Budgeting

| Component | Typical Tokens |
|-----------|----------------|
| Instructions | 50-200 |
| User prompt | 50-500 |
| Tool descriptions | 50-100 each |
| Response | 100-1000 |

### Strategies for Large Content

```swift
// Break content into chunks
func processLargeDocument(_ document: String) async throws -> [Summary] {
    let chunks = document.split(every: 10000) // ~2500 tokens per chunk
    var summaries: [Summary] = []

    for chunk in chunks {
        let session = LanguageModelSession() // New session per chunk
        let summary = try await session.respond(
            to: "Summarize this section: \(chunk)",
            generating: Summary.self
        )
        summaries.append(summary.content)
    }

    return summaries
}
```

## Generation Options

```swift
let options = GenerationOptions(
    temperature: 0.7  // 0.0 = deterministic, 2.0 = creative
)

let response = try await session.respond(
    to: prompt,
    options: options
)
```

| Temperature | Use Case |
|-------------|----------|
| 0.0-0.3 | Factual extraction, data processing |
| 0.5-0.7 | Balanced creativity and accuracy |
| 1.0-2.0 | Creative writing, brainstorming |

## Common Patterns

### Content Extraction

```swift
@Generable
struct EventDetails {
    var title: String
    var date: String?
    var time: String?
    var location: String?
    var attendees: [String]
}

let session = LanguageModelSession(instructions: """
    Extract event details from text. Use nil for missing information.
    """)

let event = try await session.respond(
    to: "Extract: Team lunch next Friday at noon in Conference Room B with John and Sarah",
    generating: EventDetails.self
)
```

### Summarization

```swift
let session = LanguageModelSession(instructions: """
    Summarize text concisely. Focus on key points and actionable items.
    Maximum 3 bullet points.
    """)

let response = try await session.respond(
    to: "Summarize this email: \(longEmail)"
)
```

### Classification

```swift
@Generable
struct Classification {
    @Guide(description: "Category", .options(["Bug", "Feature", "Question", "Other"]))
    var category: String

    @Guide(description: "Priority", .options(["Low", "Medium", "High"]))
    var priority: String

    @Guide(description: "Brief summary")
    var summary: String
}

let result = try await session.respond(
    to: "Classify this support ticket: \(ticketText)",
    generating: Classification.self
)
```

## Checklist

Before shipping:

- [ ] Check model availability before showing AI features
- [ ] Provide fallback UI for unsupported devices
- [ ] Handle all error cases gracefully
- [ ] Test with various prompt lengths
- [ ] Verify context window limits aren't exceeded
- [ ] Use @Generable for any structured output
- [ ] Add appropriate loading states for generation
- [ ] Test streaming UX feels responsive
- [ ] Ensure instructions are clear and specific
- [ ] Include safety boundaries in instructions

## References

- [Foundation Models Documentation](https://developer.apple.com/documentation/FoundationModels)
- [Generating content and performing tasks](https://developer.apple.com/documentation/FoundationModels/generating-content-and-performing-tasks-with-foundation-models)
- [Guided generation](https://developer.apple.com/documentation/FoundationModels/generating-swift-data-structures-with-guided-generation)
- [Tool calling](https://developer.apple.com/documentation/FoundationModels/expanding-generation-with-tool-calling)
- [HIG: Generative AI](https://developer.apple.com/design/human-interface-guidelines/technologies/generative-ai)
