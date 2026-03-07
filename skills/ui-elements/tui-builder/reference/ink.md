# Ink Reference (JavaScript/TypeScript)

> React for the command line

## Installation

```bash
# Create new project
mkdir my-cli && cd my-cli
npm init -y
npm install ink react
npm install -D typescript @types/react @types/node tsx

# Additional components
npm install ink-text-input ink-select-input ink-spinner ink-table
```

## Setup

### tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "jsx": "react-jsx",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "outDir": "dist"
  },
  "include": ["src"]
}
```

### package.json
```json
{
  "type": "module",
  "bin": "./dist/cli.js",
  "scripts": {
    "dev": "tsx src/cli.tsx",
    "build": "tsc",
    "start": "node dist/cli.js"
  }
}
```

## Core Concepts

### Basic App Structure

```tsx
// src/cli.tsx
#!/usr/bin/env node
import React from 'react';
import { render, Text, Box } from 'ink';

const App = () => (
  <Box flexDirection="column" padding={1}>
    <Text bold color="green">Hello from Ink!</Text>
    <Text>This is a CLI app built with React.</Text>
  </Box>
);

render(<App />);
```

### Box Component (Layout)

```tsx
import { Box, Text } from 'ink';

// Flexbox layout (default: row)
<Box>
  <Text>Left</Text>
  <Text>Right</Text>
</Box>

// Column layout
<Box flexDirection="column">
  <Text>Top</Text>
  <Text>Bottom</Text>
</Box>

// With padding/margin
<Box padding={1} marginY={1}>
  <Text>Padded content</Text>
</Box>

// Borders
<Box borderStyle="round" borderColor="green" padding={1}>
  <Text>Boxed content</Text>
</Box>

// Border styles: 'single', 'double', 'round', 'bold', 'singleDouble', 'doubleSingle', 'classic'

// Dimensions
<Box width={50} height={10}>
  <Text>Fixed size box</Text>
</Box>

// Percentage width
<Box width="50%">
  <Text>Half width</Text>
</Box>

// Alignment
<Box justifyContent="center" alignItems="center" height={10}>
  <Text>Centered</Text>
</Box>
```

### Text Component (Styling)

```tsx
import { Text } from 'ink';

// Colors
<Text color="green">Green text</Text>
<Text color="#ff6600">Hex color</Text>
<Text color="rgb(255, 100, 0)">RGB color</Text>

// Background
<Text backgroundColor="blue" color="white"> Highlighted </Text>

// Styles
<Text bold>Bold</Text>
<Text italic>Italic</Text>
<Text underline>Underlined</Text>
<Text strikethrough>Strikethrough</Text>
<Text dimColor>Dimmed</Text>
<Text inverse>Inverted</Text>

// Combine styles
<Text bold color="cyan" backgroundColor="black">
  Styled text
</Text>

// Wrap behavior
<Text wrap="truncate">Very long text that will be cut off...</Text>
<Text wrap="truncate-end">Truncate at end...</Text>
<Text wrap="truncate-start">...Truncate at start</Text>
<Text wrap="truncate-middle">Truncate...middle</Text>
```

## Hooks

### useInput (Keyboard Input)

```tsx
import { useInput, useApp } from 'ink';

const App = () => {
  const { exit } = useApp();
  const [count, setCount] = useState(0);

  useInput((input, key) => {
    // Single character input
    if (input === 'q') {
      exit();
    }

    // Special keys
    if (key.upArrow) {
      setCount(c => c + 1);
    }
    if (key.downArrow) {
      setCount(c => c - 1);
    }
    if (key.return) {
      // Enter pressed
    }
    if (key.escape) {
      // Escape pressed
    }

    // Modifiers
    if (key.ctrl && input === 'c') {
      exit();
    }
    if (key.meta && input === 's') {
      // Cmd+S on Mac
    }
  });

  return <Text>Count: {count}</Text>;
};
```

### useApp

```tsx
import { useApp } from 'ink';

const App = () => {
  const { exit } = useApp();

  const handleDone = () => {
    exit(); // Exit cleanly
  };

  const handleError = () => {
    exit(new Error('Something went wrong')); // Exit with error
  };

  return <Text>Press q to quit</Text>;
};
```

### useStdin

```tsx
import { useStdin } from 'ink';

const App = () => {
  const { stdin, isRawModeSupported, setRawMode } = useStdin();

  // Read from stdin
  useEffect(() => {
    const handleData = (data: Buffer) => {
      console.log('Received:', data.toString());
    };

    stdin.on('data', handleData);
    return () => stdin.off('data', handleData);
  }, [stdin]);

  return <Text>Listening for input...</Text>;
};
```

### useStdout

```tsx
import { useStdout } from 'ink';

const App = () => {
  const { stdout, write } = useStdout();

  // Get terminal dimensions
  const { columns, rows } = stdout;

  return <Text>Terminal: {columns}x{rows}</Text>;
};
```

### useFocus & useFocusManager

```tsx
import { useFocus, useFocusManager, Box, Text } from 'ink';

const FocusableItem = ({ label }: { label: string }) => {
  const { isFocused } = useFocus();

  return (
    <Box>
      <Text color={isFocused ? 'green' : 'white'}>
        {isFocused ? '> ' : '  '}{label}
      </Text>
    </Box>
  );
};

const App = () => {
  const { focus } = useFocusManager();

  return (
    <Box flexDirection="column">
      <FocusableItem label="Option 1" />
      <FocusableItem label="Option 2" />
      <FocusableItem label="Option 3" />
      <Text dimColor>Tab to navigate</Text>
    </Box>
  );
};
```

## Common Components

### Text Input

```tsx
import TextInput from 'ink-text-input';

const App = () => {
  const [value, setValue] = useState('');
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (value: string) => {
    setSubmitted(true);
  };

  if (submitted) {
    return <Text>You entered: {value}</Text>;
  }

  return (
    <Box>
      <Text>Enter your name: </Text>
      <TextInput
        value={value}
        onChange={setValue}
        onSubmit={handleSubmit}
        placeholder="Type here..."
      />
    </Box>
  );
};
```

### Select Input

```tsx
import SelectInput from 'ink-select-input';

const App = () => {
  const items = [
    { label: 'Create new project', value: 'create' },
    { label: 'Open existing', value: 'open' },
    { label: 'Settings', value: 'settings' },
    { label: 'Exit', value: 'exit' },
  ];

  const handleSelect = (item: { label: string; value: string }) => {
    if (item.value === 'exit') {
      process.exit(0);
    }
    console.log('Selected:', item.value);
  };

  return (
    <Box flexDirection="column">
      <Text bold>What would you like to do?</Text>
      <SelectInput items={items} onSelect={handleSelect} />
    </Box>
  );
};
```

### Spinner

```tsx
import Spinner from 'ink-spinner';

const App = () => {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setTimeout(() => setLoading(false), 3000);
  }, []);

  if (loading) {
    return (
      <Text>
        <Spinner type="dots" /> Loading...
      </Text>
    );
  }

  return <Text color="green">Done!</Text>;
};

// Spinner types: 'dots', 'line', 'pipe', 'simpleDots', 'simpleDotsScrolling',
// 'star', 'balloon', 'noise', 'bounce', 'boxBounce', 'triangle', 'arc', 'circle',
// 'squareCorners', 'circleHalves', 'toggle', 'arrow', 'bouncingBar', 'pong'
```

### Progress Bar

```tsx
import React, { useState, useEffect } from 'react';
import { Box, Text } from 'ink';

const ProgressBar = ({ percent, width = 40 }: { percent: number; width?: number }) => {
  const filled = Math.round(width * percent);
  const empty = width - filled;

  return (
    <Box>
      <Text color="green">{'█'.repeat(filled)}</Text>
      <Text color="gray">{'░'.repeat(empty)}</Text>
      <Text> {Math.round(percent * 100)}%</Text>
    </Box>
  );
};

const App = () => {
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setProgress(p => {
        if (p >= 1) {
          clearInterval(timer);
          return 1;
        }
        return p + 0.1;
      });
    }, 500);
    return () => clearInterval(timer);
  }, []);

  return (
    <Box flexDirection="column">
      <Text>Installing dependencies...</Text>
      <ProgressBar percent={progress} />
    </Box>
  );
};
```

### Table

```tsx
import Table from 'ink-table';

const App = () => {
  const data = [
    { name: 'Alice', age: 30, role: 'Developer' },
    { name: 'Bob', age: 25, role: 'Designer' },
    { name: 'Charlie', age: 35, role: 'Manager' },
  ];

  return <Table data={data} />;
};
```

## Advanced Patterns

### Multi-step Form

```tsx
const App = () => {
  const [step, setStep] = useState(0);
  const [data, setData] = useState({ name: '', email: '', confirm: false });

  const steps = [
    {
      question: 'What is your name?',
      render: () => (
        <TextInput
          value={data.name}
          onChange={(value) => setData({ ...data, name: value })}
          onSubmit={() => setStep(1)}
        />
      ),
    },
    {
      question: 'What is your email?',
      render: () => (
        <TextInput
          value={data.email}
          onChange={(value) => setData({ ...data, email: value })}
          onSubmit={() => setStep(2)}
        />
      ),
    },
    {
      question: 'Confirm submission?',
      render: () => (
        <SelectInput
          items={[
            { label: 'Yes', value: true },
            { label: 'No', value: false },
          ]}
          onSelect={(item) => {
            if (item.value) {
              // Submit
            } else {
              setStep(0);
            }
          }}
        />
      ),
    },
  ];

  return (
    <Box flexDirection="column">
      <Text bold>{steps[step].question}</Text>
      {steps[step].render()}
      <Text dimColor>Step {step + 1} of {steps.length}</Text>
    </Box>
  );
};
```

### Async Data Fetching

```tsx
const App = () => {
  const [data, setData] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('https://api.example.com/data');
        const json = await response.json();
        setData(json);
      } catch (err) {
        setError(err as Error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return <Text><Spinner /> Loading...</Text>;
  }

  if (error) {
    return <Text color="red">Error: {error.message}</Text>;
  }

  return <Text>Data: {JSON.stringify(data)}</Text>;
};
```

### Static Output (Log-style)

```tsx
import { render, Static, Box, Text } from 'ink';

const App = () => {
  const [logs, setLogs] = useState<string[]>([]);

  useEffect(() => {
    const addLog = (msg: string) => setLogs(l => [...l, msg]);

    addLog('Starting...');
    setTimeout(() => addLog('Step 1 complete'), 1000);
    setTimeout(() => addLog('Step 2 complete'), 2000);
    setTimeout(() => addLog('Done!'), 3000);
  }, []);

  return (
    <>
      {/* Static content stays in place (scrolls up) */}
      <Static items={logs}>
        {(log, index) => (
          <Text key={index}>[{new Date().toISOString()}] {log}</Text>
        )}
      </Static>

      {/* Dynamic content at bottom */}
      <Box marginTop={1}>
        <Spinner /> Processing...
      </Box>
    </>
  );
};
```

## Testing

```tsx
import { render } from 'ink-testing-library';
import App from './App';

describe('App', () => {
  it('renders welcome message', () => {
    const { lastFrame } = render(<App />);
    expect(lastFrame()).toContain('Welcome');
  });

  it('responds to key press', () => {
    const { lastFrame, stdin } = render(<App />);

    // Simulate key press
    stdin.write('q');

    expect(lastFrame()).toContain('Goodbye');
  });

  it('handles input', async () => {
    const { lastFrame, stdin } = render(<App />);

    // Type text
    stdin.write('Hello');
    stdin.write('\r'); // Enter

    expect(lastFrame()).toContain('You entered: Hello');
  });
});
```

## CLI Arguments with Pastel

```tsx
import Pastel from 'pastel';

const app = new Pastel({
  name: 'my-cli',
  description: 'My awesome CLI tool',
});

// Define commands
app.command('init', 'Initialize a new project', (args) => {
  render(<InitCommand {...args} />);
});

app.command('build', 'Build the project', (args) => {
  render(<BuildCommand {...args} />);
});

app.run();
```

## Resources

- [Ink GitHub](https://github.com/vadimdemedes/ink)
- [Ink Docs](https://github.com/vadimdemedes/ink#readme)
- [Ink Community Components](https://github.com/vadimdemedes/ink#useful-components)
- [Pastel (Ink CLI Framework)](https://github.com/vadimdemedes/pastel)
