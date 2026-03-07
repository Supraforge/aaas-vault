// Accessible Button Component Template
// WCAG 2.2 compliant button with proper ARIA attributes

import React from 'react';

interface AccessibleButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary" | "danger";
  isLoading?: boolean;
  loadingText?: string;
}

export function AccessibleButton({
  children,
  variant = "primary",
  isLoading = false,
  loadingText = "Loading...",
  disabled,
  ...props
}: AccessibleButtonProps) {
  return (
    <button
      // Disable when loading
      disabled={disabled || isLoading}
      // Announce loading state to screen readers
      aria-busy={isLoading}
      // Describe the button's current state
      aria-disabled={disabled || isLoading}
      // Provide accessible name
      aria-label={typeof children === 'string' ? children : props['aria-label'] || 'Button'}
      // Add appropriate role (button is default, but explicit for clarity)
      role="button"
      // Support keyboard activation
      onKeyDown={(e) => {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          if (!disabled && !isLoading && props.onClick) {
            props.onClick(e as any);
          }
        }
      }}
      className={`
        btn btn-${variant}
        ${isLoading ? 'loading' : ''}
        ${disabled ? 'disabled' : ''}
      `}
      {...props}
    >
      {isLoading ? (
        <>
          <span className="sr-only">{loadingText}</span>
          <span aria-hidden="true">⏳</span>
        </>
      ) : children}
    </button>
  );
}

// Usage example:
/*
<AccessibleButton 
  variant="primary"
  onClick={() => console.log('Clicked')}
  aria-label="Submit form"
>
  Submit Form
</AccessibleButton>
*/
