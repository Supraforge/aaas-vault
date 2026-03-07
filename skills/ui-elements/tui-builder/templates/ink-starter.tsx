#!/usr/bin/env node
/**
 * Ink TUI Starter Template
 *
 * Features:
 * - Interactive menu
 * - Progress indicator
 * - Form input
 * - Keyboard navigation
 *
 * Usage:
 *   npx tsx src/cli.tsx
 */

import React, { useState, useEffect } from 'react';
import { render, Box, Text, useInput, useApp } from 'ink';
import Spinner from 'ink-spinner';
import SelectInput from 'ink-select-input';
import TextInput from 'ink-text-input';

// ============================================
// Types
// ============================================

type Screen = 'menu' | 'form' | 'progress' | 'result';

interface FormData {
  name: string;
  email: string;
}

// ============================================
// Components
// ============================================

const Header = ({ title }: { title: string }) => (
  <Box borderStyle="round" borderColor="cyan" paddingX={2}>
    <Text bold color="cyan">{title}</Text>
  </Box>
);

const Footer = () => (
  <Box marginTop={1}>
    <Text dimColor>↑/↓: Navigate | Enter: Select | q: Quit</Text>
  </Box>
);

const Menu = ({ onSelect }: { onSelect: (value: string) => void }) => {
  const items = [
    { label: 'Start New Task', value: 'new' },
    { label: 'View Status', value: 'status' },
    { label: 'Settings', value: 'settings' },
    { label: 'Exit', value: 'exit' },
  ];

  return (
    <Box flexDirection="column" paddingY={1}>
      <Text bold marginBottom={1}>What would you like to do?</Text>
      <SelectInput items={items} onSelect={(item) => onSelect(item.value)} />
    </Box>
  );
};

const Form = ({ onSubmit }: { onSubmit: (data: FormData) => void }) => {
  const [step, setStep] = useState(0);
  const [data, setData] = useState<FormData>({ name: '', email: '' });

  const handleSubmit = (value: string) => {
    if (step === 0) {
      setData({ ...data, name: value });
      setStep(1);
    } else {
      onSubmit({ ...data, email: value });
    }
  };

  return (
    <Box flexDirection="column" paddingY={1}>
      <Text bold marginBottom={1}>
        {step === 0 ? 'Enter your name:' : 'Enter your email:'}
      </Text>
      <Box>
        <Text color="green">&gt; </Text>
        <TextInput
          value={step === 0 ? data.name : data.email}
          onChange={(value) =>
            setData(step === 0 ? { ...data, name: value } : { ...data, email: value })
          }
          onSubmit={handleSubmit}
          placeholder={step === 0 ? 'John Doe' : 'john@example.com'}
        />
      </Box>
      <Text dimColor marginTop={1}>
        Step {step + 1} of 2
      </Text>
    </Box>
  );
};

const Progress = ({ onComplete }: { onComplete: () => void }) => {
  const [progress, setProgress] = useState(0);
  const [status, setStatus] = useState('Initializing...');

  useEffect(() => {
    const statuses = [
      'Initializing...',
      'Connecting to server...',
      'Processing data...',
      'Finalizing...',
      'Complete!',
    ];

    const interval = setInterval(() => {
      setProgress((p) => {
        const next = p + 20;
        setStatus(statuses[Math.floor(next / 25)] || 'Complete!');
        if (next >= 100) {
          clearInterval(interval);
          setTimeout(onComplete, 500);
          return 100;
        }
        return next;
      });
    }, 500);

    return () => clearInterval(interval);
  }, [onComplete]);

  const width = 30;
  const filled = Math.round((progress / 100) * width);

  return (
    <Box flexDirection="column" paddingY={1}>
      <Box>
        {progress < 100 && <Spinner type="dots" />}
        {progress === 100 && <Text color="green">✓</Text>}
        <Text> {status}</Text>
      </Box>
      <Box marginTop={1}>
        <Text color="green">{'█'.repeat(filled)}</Text>
        <Text color="gray">{'░'.repeat(width - filled)}</Text>
        <Text> {progress}%</Text>
      </Box>
    </Box>
  );
};

const Result = ({ data, onBack }: { data: FormData; onBack: () => void }) => {
  useInput((input) => {
    if (input === 'b' || input === 'q') {
      onBack();
    }
  });

  return (
    <Box flexDirection="column" paddingY={1}>
      <Text bold color="green">✓ Task Complete!</Text>
      <Box marginTop={1} flexDirection="column">
        <Text>Name: {data.name}</Text>
        <Text>Email: {data.email}</Text>
      </Box>
      <Text dimColor marginTop={1}>Press 'b' to go back</Text>
    </Box>
  );
};

// ============================================
// Main App
// ============================================

const App = () => {
  const { exit } = useApp();
  const [screen, setScreen] = useState<Screen>('menu');
  const [formData, setFormData] = useState<FormData>({ name: '', email: '' });

  useInput((input) => {
    if (input === 'q' && screen === 'menu') {
      exit();
    }
  });

  const handleMenuSelect = (value: string) => {
    switch (value) {
      case 'new':
        setScreen('form');
        break;
      case 'status':
        setScreen('progress');
        break;
      case 'exit':
        exit();
        break;
    }
  };

  const handleFormSubmit = (data: FormData) => {
    setFormData(data);
    setScreen('progress');
  };

  const handleProgressComplete = () => {
    setScreen('result');
  };

  const handleBack = () => {
    setScreen('menu');
  };

  return (
    <Box flexDirection="column" padding={1}>
      <Header title="My TUI App" />

      {screen === 'menu' && <Menu onSelect={handleMenuSelect} />}
      {screen === 'form' && <Form onSubmit={handleFormSubmit} />}
      {screen === 'progress' && <Progress onComplete={handleProgressComplete} />}
      {screen === 'result' && <Result data={formData} onBack={handleBack} />}

      {screen === 'menu' && <Footer />}
    </Box>
  );
};

// ============================================
// Entry Point
// ============================================

render(<App />);
