"""
Multi-Model Writer - Model Router

Routes writing tasks to the appropriate AI model based on:
- User preference
- Cost optimization
- Task requirements

Supported models:
- Claude (default, via Anthropic API)
- GLM-4.7 (Z.AI - cheapest)
- GPT-4o / GPT-4o-mini (OpenAI)
- Gemini (Google - free tier)
- Grok (xAI)
"""

import os
from typing import Optional, Dict, List, Literal
from dataclasses import dataclass
from enum import Enum

# Try to import API clients (graceful fallback if not installed)
try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False

try:
    import openai
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False

try:
    import google.generativeai as genai
    HAS_GOOGLE = True
except ImportError:
    HAS_GOOGLE = False


class ModelType(Enum):
    CLAUDE = "claude"
    GLM = "glm-4.7"
    GPT4O = "gpt-4o"
    GPT4O_MINI = "gpt-4o-mini"
    GEMINI = "gemini"
    GROK = "grok"


@dataclass
class ModelPricing:
    """Pricing per 1M tokens"""
    input_cost: float
    output_cost: float

    def estimate_cost(self, input_tokens: int, output_tokens: int) -> float:
        return (input_tokens * self.input_cost / 1_000_000) + \
               (output_tokens * self.output_cost / 1_000_000)


# Current pricing (December 2024)
PRICING = {
    ModelType.CLAUDE: ModelPricing(3.00, 15.00),
    ModelType.GLM: ModelPricing(0.10, 0.10),
    ModelType.GPT4O: ModelPricing(2.50, 10.00),
    ModelType.GPT4O_MINI: ModelPricing(0.15, 0.60),
    ModelType.GEMINI: ModelPricing(0.00, 0.00),  # Free tier
    ModelType.GROK: ModelPricing(3.00, 15.00),
}


class ModelRouter:
    """
    Routes writing requests to appropriate AI models.

    Usage:
        router = ModelRouter()

        # Default (Claude)
        response = router.write("Your prompt")

        # Specific model
        response = router.write("Your prompt", model="glm-4.7")

        # Cost-optimized
        response = router.write("Your prompt", optimize="cost")

        # Compare across models
        results = router.compare("Your prompt", models=["claude", "glm-4.7", "gpt-4o-mini"])
    """

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self._init_clients()

    def _init_clients(self):
        """Initialize available API clients."""
        self.clients = {}

        # Anthropic (Claude)
        if HAS_ANTHROPIC and os.getenv("ANTHROPIC_API_KEY"):
            self.clients["claude"] = anthropic.Anthropic()
            if self.verbose:
                print("✓ Claude API configured")

        # OpenAI (GPT-4o)
        if HAS_OPENAI and os.getenv("OPENAI_API_KEY"):
            self.clients["openai"] = openai.OpenAI()
            if self.verbose:
                print("✓ OpenAI API configured")

        # Z.AI (GLM-4.7)
        if HAS_OPENAI and os.getenv("ZAI_API_KEY"):
            self.clients["zai"] = openai.OpenAI(
                api_key=os.getenv("ZAI_API_KEY"),
                base_url=os.getenv("ZAI_BASE_URL", "https://api.z.ai/v1")
            )
            if self.verbose:
                print("✓ Z.AI (GLM-4.7) API configured")

        # xAI (Grok)
        if HAS_OPENAI and os.getenv("XAI_API_KEY"):
            self.clients["xai"] = openai.OpenAI(
                api_key=os.getenv("XAI_API_KEY"),
                base_url="https://api.x.ai/v1"
            )
            if self.verbose:
                print("✓ xAI (Grok) API configured")

        # Google (Gemini)
        if HAS_GOOGLE and os.getenv("GOOGLE_API_KEY"):
            genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
            self.clients["gemini"] = genai.GenerativeModel("gemini-2.0-flash")
            if self.verbose:
                print("✓ Gemini API configured")

    def available_models(self) -> List[str]:
        """Return list of available models."""
        models = []
        if "claude" in self.clients:
            models.append("claude")
        if "zai" in self.clients:
            models.append("glm-4.7")
        if "openai" in self.clients:
            models.extend(["gpt-4o", "gpt-4o-mini"])
        if "gemini" in self.clients:
            models.append("gemini")
        if "xai" in self.clients:
            models.append("grok")
        return models

    def write(
        self,
        prompt: str,
        model: str = "claude",
        system_prompt: Optional[str] = None,
        optimize: Optional[Literal["cost", "quality"]] = None,
        max_tokens: int = 4096,
    ) -> str:
        """
        Generate content using specified model.

        Args:
            prompt: The user prompt
            model: Model to use (claude, glm-4.7, gpt-4o, gpt-4o-mini, gemini, grok)
            system_prompt: Optional system prompt
            optimize: Auto-select model based on "cost" or "quality"
            max_tokens: Maximum tokens in response

        Returns:
            Generated text response
        """
        # Auto-select model if optimizing
        if optimize == "cost":
            model = self._cheapest_available()
        elif optimize == "quality":
            model = "claude" if "claude" in self.clients else self._best_available()

        if self.verbose:
            print(f"Using model: {model}")

        # Route to appropriate handler
        if model == "claude":
            return self._call_claude(prompt, system_prompt, max_tokens)
        elif model == "glm-4.7":
            return self._call_zai(prompt, system_prompt, max_tokens)
        elif model in ["gpt-4o", "gpt-4o-mini"]:
            return self._call_openai(prompt, system_prompt, max_tokens, model)
        elif model == "gemini":
            return self._call_gemini(prompt, system_prompt, max_tokens)
        elif model == "grok":
            return self._call_grok(prompt, system_prompt, max_tokens)
        else:
            raise ValueError(f"Unknown model: {model}. Available: {self.available_models()}")

    def compare(
        self,
        prompt: str,
        models: List[str] = None,
        system_prompt: Optional[str] = None,
    ) -> Dict[str, str]:
        """
        Generate content from multiple models for comparison.

        Args:
            prompt: The user prompt
            models: List of models to compare (defaults to all available)
            system_prompt: Optional system prompt

        Returns:
            Dictionary mapping model name to response
        """
        if models is None:
            models = self.available_models()

        results = {}
        for model in models:
            try:
                if self.verbose:
                    print(f"Generating with {model}...")
                results[model] = self.write(prompt, model=model, system_prompt=system_prompt)
            except Exception as e:
                results[model] = f"ERROR: {str(e)}"

        return results

    def estimate_cost(
        self,
        prompt: str,
        model: str,
        expected_output_tokens: int = 2000
    ) -> float:
        """Estimate cost for a request."""
        input_tokens = len(prompt.split()) * 1.3  # Rough estimate
        pricing = PRICING.get(ModelType(model))
        if pricing:
            return pricing.estimate_cost(int(input_tokens), expected_output_tokens)
        return 0.0

    def _cheapest_available(self) -> str:
        """Return cheapest available model."""
        priority = ["gemini", "glm-4.7", "gpt-4o-mini", "gpt-4o", "claude", "grok"]
        for model in priority:
            if model in self.available_models():
                return model
        raise ValueError("No models available")

    def _best_available(self) -> str:
        """Return best quality available model."""
        priority = ["claude", "gpt-4o", "grok", "gemini", "gpt-4o-mini", "glm-4.7"]
        for model in priority:
            if model in self.available_models():
                return model
        raise ValueError("No models available")

    # === Model-specific handlers ===

    def _call_claude(self, prompt: str, system_prompt: Optional[str], max_tokens: int) -> str:
        """Call Anthropic Claude API."""
        if "claude" not in self.clients:
            raise ValueError("Claude API not configured. Set ANTHROPIC_API_KEY.")

        messages = [{"role": "user", "content": prompt}]
        kwargs = {"model": "claude-sonnet-4-20250514", "max_tokens": max_tokens, "messages": messages}

        if system_prompt:
            kwargs["system"] = system_prompt

        response = self.clients["claude"].messages.create(**kwargs)
        return response.content[0].text

    def _call_zai(self, prompt: str, system_prompt: Optional[str], max_tokens: int) -> str:
        """Call Z.AI GLM-4.7 API (OpenAI-compatible)."""
        if "zai" not in self.clients:
            raise ValueError("Z.AI API not configured. Set ZAI_API_KEY.")

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = self.clients["zai"].chat.completions.create(
            model="glm-4.7",
            messages=messages,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content

    def _call_openai(self, prompt: str, system_prompt: Optional[str], max_tokens: int, model: str) -> str:
        """Call OpenAI API."""
        if "openai" not in self.clients:
            raise ValueError("OpenAI API not configured. Set OPENAI_API_KEY.")

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = self.clients["openai"].chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content

    def _call_gemini(self, prompt: str, system_prompt: Optional[str], max_tokens: int) -> str:
        """Call Google Gemini API."""
        if "gemini" not in self.clients:
            raise ValueError("Gemini API not configured. Set GOOGLE_API_KEY.")

        full_prompt = prompt
        if system_prompt:
            full_prompt = f"{system_prompt}\n\n{prompt}"

        response = self.clients["gemini"].generate_content(full_prompt)
        return response.text

    def _call_grok(self, prompt: str, system_prompt: Optional[str], max_tokens: int) -> str:
        """Call xAI Grok API (OpenAI-compatible)."""
        if "xai" not in self.clients:
            raise ValueError("xAI API not configured. Set XAI_API_KEY.")

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        response = self.clients["xai"].chat.completions.create(
            model="grok-2",
            messages=messages,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content


# === CLI Interface ===

def main():
    """CLI for testing model router."""
    import argparse

    parser = argparse.ArgumentParser(description="Multi-Model Writer")
    parser.add_argument("prompt", help="The prompt to send")
    parser.add_argument("--model", "-m", default="claude",
                       help="Model to use (claude, glm-4.7, gpt-4o, gpt-4o-mini, gemini, grok)")
    parser.add_argument("--compare", "-c", action="store_true",
                       help="Compare across all available models")
    parser.add_argument("--optimize", "-o", choices=["cost", "quality"],
                       help="Auto-select model based on cost or quality")
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="Verbose output")

    args = parser.parse_args()

    router = ModelRouter(verbose=args.verbose)

    print(f"Available models: {router.available_models()}\n")

    if args.compare:
        results = router.compare(args.prompt)
        for model, response in results.items():
            print(f"\n{'='*60}")
            print(f"MODEL: {model}")
            print('='*60)
            print(response)
    else:
        response = router.write(args.prompt, model=args.model, optimize=args.optimize)
        print(response)


if __name__ == "__main__":
    main()
