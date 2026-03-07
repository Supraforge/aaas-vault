"""
Base Component Class

Provides the foundation for all visual components in the design system.
Handles common functionality like token loading, rendering, and export.
"""

import os
import sys
from abc import ABC, abstractmethod
from enum import Enum
from pathlib import Path
from typing import Any, Dict, Optional, Union
from dataclasses import dataclass, field

# Add token path
VISUAL_SYSTEM_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(VISUAL_SYSTEM_ROOT))

from tokens.index import (
    get_tokens,
    get_color,
    get_accessible_pair,
    get_color_palette,
    get_plotly_template,
)


class RenderBackend(Enum):
    """Available rendering backends."""
    SATORI = "satori"      # React → SVG → PNG (best for infographics)
    PLOTLY = "plotly"      # Data visualization (best for charts)
    DRAWSVG = "drawsvg"    # Pure Python SVG (best for diagrams)
    AUTO = "auto"          # Auto-select based on component type


class OutputFormat(Enum):
    """Available output formats."""
    PNG = "png"
    SVG = "svg"
    HTML = "html"
    PDF = "pdf"


@dataclass
class RenderConfig:
    """Configuration for rendering."""
    width: int = 1200
    height: int = 630
    scale: int = 2          # 2x for web, 4x for print (300 DPI)
    format: OutputFormat = OutputFormat.PNG
    background: str = "#ffffff"
    quality: str = "web"    # "web" (150 DPI) or "print" (300 DPI)

    def __post_init__(self):
        if self.quality == "print":
            self.scale = 4


class Component(ABC):
    """
    Abstract base class for all visual components.

    Provides:
    - Token-based styling
    - Multi-backend rendering
    - Consistent export interface
    - Validation and quality checks
    """

    # Default backend (subclasses override)
    DEFAULT_BACKEND = RenderBackend.AUTO

    # Supported backends (subclasses override)
    SUPPORTED_BACKENDS = [RenderBackend.SATORI, RenderBackend.PLOTLY, RenderBackend.DRAWSVG]

    def __init__(
        self,
        title: Optional[str] = None,
        source: Optional[str] = None,
        config: Optional[RenderConfig] = None,
    ):
        """
        Initialize component.

        Args:
            title: Optional title for the component
            source: Optional source citation
            config: Render configuration
        """
        self.title = title
        self.source = source
        self.config = config or RenderConfig()
        self._tokens = get_tokens()

    @property
    def tokens(self):
        """Access to design tokens."""
        return self._tokens

    def get_color(self, path: str) -> str:
        """Get a color from tokens."""
        return get_color(path)

    def get_palette(self, name: str = "categorical") -> list:
        """Get a color palette."""
        return get_color_palette(name)

    def get_accessible_colors(self, pair_name: str = "treatment_control") -> tuple:
        """Get an accessible color pair."""
        return get_accessible_pair(pair_name)

    @abstractmethod
    def _render_satori(self, output_path: str) -> str:
        """Render using Satori backend."""
        pass

    @abstractmethod
    def _render_plotly(self, output_path: str) -> str:
        """Render using Plotly backend."""
        pass

    @abstractmethod
    def _render_drawsvg(self, output_path: str) -> str:
        """Render using drawsvg backend."""
        pass

    def _select_backend(self) -> RenderBackend:
        """
        Auto-select the best backend for this component.
        Subclasses should override for optimal selection.
        """
        return self.SUPPORTED_BACKENDS[0] if self.SUPPORTED_BACKENDS else RenderBackend.SATORI

    def render(
        self,
        output_path: str,
        backend: Optional[Union[RenderBackend, str]] = None,
        **kwargs
    ) -> str:
        """
        Render the component to a file.

        Args:
            output_path: Path to save the output
            backend: Which backend to use (auto-selected if None)
            **kwargs: Additional backend-specific options

        Returns:
            Path to the generated file
        """
        # Normalize backend
        if isinstance(backend, str):
            backend = RenderBackend(backend.lower())

        if backend is None or backend == RenderBackend.AUTO:
            backend = self._select_backend()

        # Validate backend
        if backend not in self.SUPPORTED_BACKENDS:
            raise ValueError(
                f"Backend {backend} not supported for {self.__class__.__name__}. "
                f"Supported: {[b.value for b in self.SUPPORTED_BACKENDS]}"
            )

        # Ensure output directory exists
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

        # Update config with kwargs
        for key, value in kwargs.items():
            if hasattr(self.config, key):
                setattr(self.config, key, value)

        # Render with selected backend
        if backend == RenderBackend.SATORI:
            return self._render_satori(output_path)
        elif backend == RenderBackend.PLOTLY:
            return self._render_plotly(output_path)
        elif backend == RenderBackend.DRAWSVG:
            return self._render_drawsvg(output_path)
        else:
            raise ValueError(f"Unknown backend: {backend}")

    def to_dict(self) -> Dict[str, Any]:
        """Convert component data to dictionary (for Satori JSON)."""
        return {
            "title": self.title,
            "source": self.source,
        }

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(title={self.title!r})"


class NotImplementedBackend(Exception):
    """Raised when a backend is not implemented for a component."""
    pass


def ensure_output_dir(path: str) -> str:
    """Ensure the output directory exists and return the full path."""
    full_path = os.path.abspath(path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    return full_path


def get_drawsvg():
    """
    Import the drawsvg package.

    Returns:
        The drawsvg module
    """
    import drawsvg as dw
    return dw
