"""
Scene templates for Manim cardiology animations.
"""

from __future__ import annotations

from typing import List, Tuple

from manim import (
    FadeIn,
    GrowFromCenter,
    Indicate,
    LaggedStart,
    RoundedRectangle,
    Scene,
    VGroup,
    Create,
    Text,
    VMobject,
    UP,
    DOWN,
    RIGHT,
    LEFT,
)

import theme
from primitives import (
    bar_group,
    build_axes,
    flow_row,
    heart_chambers,
    panel_grid,
    step_curve,
    timeline,
    title_text,
)


class FlowScene(Scene):
    TITLE = ""
    STEPS: List[Tuple[str, str]] = []
    OUTCOME: str | None = None

    def construct(self) -> None:
        title = title_text(self.TITLE)
        blocks, arrows = flow_row(self.STEPS)
        blocks.next_to(title, DOWN, buff=0.8)

        outcome = None
        if self.OUTCOME:
            outcome = Text(
                self.OUTCOME,
                font=theme.PRIMARY_FONT,
                font_size=theme.FONT_SIZES["label"],
                color=theme.COLORS["text"],
            ).next_to(blocks, DOWN, buff=0.7)

        self.play(FadeIn(title))
        self.play(LaggedStart(*[GrowFromCenter(card) for card in blocks], lag_ratio=0.15))
        self.play(Create(arrows))
        if outcome:
            self.play(FadeIn(outcome))
        for card in blocks:
            self.play(Indicate(card[0], color=card[0].get_stroke_color()), run_time=0.5)
        self.wait(0.4)


class TimelineScene(Scene):
    TITLE = ""
    EVENTS: List[Tuple[str, str]] = []

    def construct(self) -> None:
        title = title_text(self.TITLE)
        rail = timeline(self.EVENTS)
        rail.next_to(title, DOWN, buff=0.9)

        self.play(FadeIn(title))
        self.play(Create(rail))
        self.wait(0.4)


class BarScene(Scene):
    TITLE = ""
    BARS: List[Tuple[str, float, str]] = []
    FOOTNOTE: str | None = None

    def construct(self) -> None:
        title = title_text(self.TITLE)
        bars = bar_group(self.BARS)
        bars.next_to(title, DOWN, buff=0.9)

        self.play(FadeIn(title))
        self.play(LaggedStart(*[GrowFromCenter(group) for group in bars], lag_ratio=0.15))
        if self.FOOTNOTE:
            foot = Text(
                self.FOOTNOTE,
                font=theme.PRIMARY_FONT,
                font_size=theme.FONT_SIZES["small"],
                color=theme.COLORS["muted"],
            ).next_to(bars, DOWN, buff=0.4)
            self.play(FadeIn(foot))
        self.wait(0.4)


class ComparisonScene(Scene):
    TITLE = ""
    LEFT_LABEL = ""
    RIGHT_LABEL = ""
    LEFT_VALUE = ""
    RIGHT_VALUE = ""
    METRIC = ""

    def construct(self) -> None:
        title = title_text(self.TITLE)

        left_block = VGroup(
            Text(self.LEFT_LABEL, font=theme.PRIMARY_FONT, font_size=theme.FONT_SIZES["small"], color=theme.COLORS["text"]),
            Text(self.LEFT_VALUE, font=theme.PRIMARY_FONT, font_size=theme.FONT_SIZES["subtitle"], color=theme.COLORS["blue"]),
        ).arrange(DOWN, buff=0.2)

        right_block = VGroup(
            Text(self.RIGHT_LABEL, font=theme.PRIMARY_FONT, font_size=theme.FONT_SIZES["small"], color=theme.COLORS["text"]),
            Text(self.RIGHT_VALUE, font=theme.PRIMARY_FONT, font_size=theme.FONT_SIZES["subtitle"], color=theme.COLORS["teal"]),
        ).arrange(DOWN, buff=0.2)

        blocks = VGroup(left_block, right_block).arrange(RIGHT, buff=2.2)
        blocks.next_to(title, DOWN, buff=1.0)

        metric = Text(
            self.METRIC,
            font=theme.PRIMARY_FONT,
            font_size=theme.FONT_SIZES["label"],
            color=theme.COLORS["text"],
        ).next_to(blocks, DOWN, buff=0.8)

        self.play(FadeIn(title))
        self.play(LaggedStart(GrowFromCenter(left_block), GrowFromCenter(right_block), lag_ratio=0.2))
        self.play(FadeIn(metric))
        self.wait(0.4)


class LineScene(Scene):
    TITLE = ""
    POINTS: List[Tuple[float, float]] = []
    X_LABEL = ""
    Y_LABEL = ""

    def construct(self) -> None:
        title = title_text(self.TITLE)
        x_vals = [p[0] for p in self.POINTS]
        y_vals = [p[1] for p in self.POINTS]
        x_min = min(x_vals) if x_vals else 0
        x_max = max(x_vals) if x_vals else 1
        x_step = max(1, int((x_max - x_min) / 4) or 1)

        axes, labels = build_axes([x_min, x_max, x_step], [0, 1.0, 0.2], x_label=self.X_LABEL, y_label=self.Y_LABEL)
        axes.next_to(title, DOWN, buff=0.8)

        line = axes.plot_line_graph(
            x_values=x_vals,
            y_values=y_vals,
            line_color=theme.COLORS["blue"],
            add_vertex_dots=True,
            vertex_dot_radius=0.06,
            vertex_dot_style={"color": theme.COLORS["blue"]},
        )

        self.play(FadeIn(title))
        self.play(Create(axes), FadeIn(labels))
        self.play(Create(line))
        self.wait(0.4)


class KaplanMeierBaseScene(Scene):
    TITLE = ""
    TREATMENT_POINTS: List[Tuple[float, float]] = []
    CONTROL_POINTS: List[Tuple[float, float]] = []
    HR_TEXT = ""

    def construct(self) -> None:
        title = title_text(self.TITLE)
        axes, labels = build_axes([0, 24, 6], [0, 1.0, 0.2], x_label="Months", y_label="Event-free survival")
        axes.next_to(title, DOWN, buff=0.7).shift(LEFT * 0.4)

        treatment_color, control_color = theme.ACCESSIBLE_PAIR
        treatment_curve = step_curve(axes, self.TREATMENT_POINTS, treatment_color)
        control_curve = step_curve(axes, self.CONTROL_POINTS, control_color)

        legend = VGroup(
            _legend_item("Treatment", treatment_color),
            _legend_item("Control", control_color),
        ).arrange(DOWN, buff=0.25)
        legend.to_corner(RIGHT + UP, buff=0.6)

        hr_text = Text(
            self.HR_TEXT,
            font=theme.PRIMARY_FONT,
            font_size=theme.FONT_SIZES["label"],
            color=theme.COLORS["text"],
        ).next_to(axes, DOWN, buff=0.9)

        self.play(FadeIn(title))
        self.play(Create(axes), FadeIn(labels))
        self.play(Create(control_curve), Create(treatment_curve))
        self.play(FadeIn(legend), FadeIn(hr_text))
        self.wait(0.4)


class ForestPlotScene(Scene):
    TITLE = ""
    STUDIES: List[Tuple[str, float, float, float]] = []

    def construct(self) -> None:
        title = title_text(self.TITLE)
        axes, labels = build_axes([0.5, 1.5, 0.5], [0, len(self.STUDIES), 1], x_label="Hazard ratio", y_label=None)
        axes.next_to(title, DOWN, buff=0.7).shift(LEFT * 0.2)

        lines = VGroup()
        points = VGroup()
        text_labels = VGroup()
        for idx, (label, estimate, ci_low, ci_high) in enumerate(self.STUDIES):
            y = len(self.STUDIES) - idx - 1
            lines.add(
                axes.plot_line_graph([ci_low, ci_high], [y, y], line_color=theme.COLORS["blue"])
            )
            points.add(
                axes.plot_line_graph([estimate], [y], line_color=theme.COLORS["blue"], add_vertex_dots=True)
            )
            text = Text(label, font=theme.PRIMARY_FONT, font_size=theme.FONT_SIZES["small"], color=theme.COLORS["text"])
            text.next_to(axes.coords_to_point(0.5, y), LEFT, buff=0.4)
            text_labels.add(text)

        null_line = axes.get_vertical_line(axes.coords_to_point(1.0, 0), color=theme.COLORS["muted"], stroke_width=2)

        self.play(FadeIn(title))
        self.play(Create(axes), FadeIn(labels))
        self.play(Create(null_line))
        self.play(Create(lines), Create(points), FadeIn(text_labels))
        self.wait(0.4)


class AnatomyChambersScene(Scene):
    TITLE = ""

    def construct(self) -> None:
        title = title_text(self.TITLE)
        chambers = heart_chambers()
        chambers.next_to(title, DOWN, buff=0.8)
        self.play(FadeIn(title))
        self.play(Create(chambers))
        self.wait(0.4)


class PanelGridScene(Scene):
    TITLE = ""
    LABELS: List[str] = []

    def construct(self) -> None:
        title = title_text(self.TITLE)
        grid = panel_grid(self.LABELS)
        grid.next_to(title, DOWN, buff=0.7)
        self.play(FadeIn(title))
        self.play(LaggedStart(*[GrowFromCenter(panel) for panel in grid], lag_ratio=0.2))
        self.wait(0.4)


def _legend_item(label: str, color: str) -> VGroup:
    swatch = RoundedRectangle(width=0.4, height=0.25, corner_radius=0.05)
    swatch.set_fill(color, opacity=1).set_stroke(color, width=0)
    text = Text(
        label,
        font=theme.PRIMARY_FONT,
        font_size=theme.FONT_SIZES["small"],
        color=theme.COLORS["text"],
    )
    return VGroup(swatch, text).arrange(RIGHT, buff=0.25)
