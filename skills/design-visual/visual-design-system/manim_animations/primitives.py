"""
Reusable primitives for Manim cardiology scenes.
"""

from __future__ import annotations

from typing import Iterable, List, Tuple

from manim import (
    Axes,
    Arrow,
    Dot,
    Line,
    Rectangle,
    RoundedRectangle,
    Square,
    Text,
    VGroup,
    VMobject,
    UP,
    DOWN,
    LEFT,
    RIGHT,
)

import theme


def title_text(text: str, color: str | None = None) -> Text:
    return Text(
        text,
        font=theme.PRIMARY_FONT,
        font_size=theme.FONT_SIZES["title"],
        color=color or theme.COLORS["navy"],
    ).to_edge(UP)


def subtitle_text(text: str) -> Text:
    return Text(
        text,
        font=theme.PRIMARY_FONT,
        font_size=theme.FONT_SIZES["subtitle"],
        color=theme.COLORS["text"],
    )


def flow_block(label: str, color: str, width: float = 3.1, height: float = 1.1) -> VGroup:
    card = RoundedRectangle(width=width, height=height, corner_radius=0.15)
    card.set_stroke(color, width=2)
    card.set_fill(color, opacity=0.12)
    text = Text(
        label,
        font=theme.PRIMARY_FONT,
        font_size=theme.FONT_SIZES["label"],
        color=theme.COLORS["text"],
    )
    text.move_to(card.get_center())
    return VGroup(card, text)


def flow_row(steps: Iterable[Tuple[str, str]], buff: float = 0.6) -> Tuple[VGroup, VGroup]:
    blocks = VGroup(*[flow_block(label, color) for label, color in steps])
    blocks.arrange(RIGHT, buff=buff)
    arrows = VGroup()
    for left, right in zip(blocks[:-1], blocks[1:]):
        arrows.add(Arrow(left.get_right(), right.get_left(), buff=0.1, color=theme.COLORS["muted"]))
    return blocks, arrows


def build_axes(
    x_range: List[float],
    y_range: List[float],
    x_length: float = 9.0,
    y_length: float = 4.2,
    x_label: str | None = None,
    y_label: str | None = None,
) -> Tuple[Axes, VGroup]:
    axes = Axes(
        x_range=x_range,
        y_range=y_range,
        x_length=x_length,
        y_length=y_length,
        tips=False,
    )
    labels = VGroup()
    if x_label:
        labels.add(
            Text(
                x_label,
                font=theme.PRIMARY_FONT,
                font_size=theme.FONT_SIZES["small"],
                color=theme.COLORS["text"],
            ).next_to(axes, DOWN, buff=0.3)
        )
    if y_label:
        labels.add(
            Text(
                y_label,
                font=theme.PRIMARY_FONT,
                font_size=theme.FONT_SIZES["small"],
                color=theme.COLORS["text"],
            ).rotate(1.5708).next_to(axes, LEFT, buff=0.4)
        )
    return axes, labels


def step_curve(axes: Axes, points: List[Tuple[float, float]], color: str, width: float = 4) -> VMobject:
    path = VMobject()
    corners = []
    for idx, (x, y) in enumerate(points):
        point = axes.coords_to_point(x, y)
        if idx == 0:
            corners.append(point)
        else:
            prev_x, prev_y = points[idx - 1]
            corners.append(axes.coords_to_point(x, prev_y))
            corners.append(point)
    path.set_points_as_corners(corners)
    path.set_stroke(color, width=width)
    return path


def timeline(events: List[Tuple[str, str]]) -> VGroup:
    line = Line(LEFT * 5, RIGHT * 5, color=theme.COLORS["muted"])
    markers = VGroup()
    labels = VGroup()
    for idx, (time_label, event_label) in enumerate(events):
        position = line.point_from_proportion(idx / (len(events) - 1 if len(events) > 1 else 1))
        dot = Dot(position, color=theme.COLORS["blue"])
        time_text = Text(time_label, font=theme.PRIMARY_FONT, font_size=theme.FONT_SIZES["small"], color=theme.COLORS["text"])
        event_text = Text(event_label, font=theme.PRIMARY_FONT, font_size=theme.FONT_SIZES["small"], color=theme.COLORS["text"])
        time_text.next_to(dot, DOWN, buff=0.25)
        event_text.next_to(dot, UP, buff=0.25)
        markers.add(dot)
        labels.add(time_text, event_text)
    return VGroup(line, markers, labels)


def bar_group(values: List[Tuple[str, float, str]], max_height: float = 3.2) -> VGroup:
    max_value = max(v for _, v, _ in values) if values else 1
    bars = VGroup()
    labels = VGroup()
    for label, value, color in values:
        height = max_height * (value / max_value)
        bar = Rectangle(width=0.9, height=height, color=color, fill_opacity=0.7).set_stroke(color, width=1)
        label_text = Text(label, font=theme.PRIMARY_FONT, font_size=theme.FONT_SIZES["small"], color=theme.COLORS["text"])
        label_text.next_to(bar, DOWN, buff=0.2)
        bars.add(bar)
        labels.add(label_text)
    group = VGroup()
    for bar, label in zip(bars, labels):
        group.add(VGroup(bar, label))
    group.arrange(RIGHT, buff=0.6, aligned_edge=DOWN)
    return group


def heart_chambers() -> VGroup:
    chamber_w = 2.0
    chamber_h = 1.6
    gap = 0.2
    ra = RoundedRectangle(width=chamber_w, height=chamber_h, corner_radius=0.15)
    rv = RoundedRectangle(width=chamber_w, height=chamber_h, corner_radius=0.15)
    la = RoundedRectangle(width=chamber_w, height=chamber_h, corner_radius=0.15)
    lv = RoundedRectangle(width=chamber_w, height=chamber_h, corner_radius=0.15)

    ra.set_fill(theme.COLORS["panel"], opacity=1).set_stroke(theme.COLORS["blue"], width=2)
    rv.set_fill(theme.COLORS["panel"], opacity=1).set_stroke(theme.COLORS["blue"], width=2)
    la.set_fill(theme.COLORS["panel"], opacity=1).set_stroke(theme.COLORS["teal"], width=2)
    lv.set_fill(theme.COLORS["panel"], opacity=1).set_stroke(theme.COLORS["teal"], width=2)

    ra.shift(LEFT * (chamber_w / 2 + gap) + UP * (chamber_h / 2 + gap))
    rv.shift(LEFT * (chamber_w / 2 + gap) + DOWN * (chamber_h / 2 + gap))
    la.shift(RIGHT * (chamber_w / 2 + gap) + UP * (chamber_h / 2 + gap))
    lv.shift(RIGHT * (chamber_w / 2 + gap) + DOWN * (chamber_h / 2 + gap))

    ra_label = Text("RA", font=theme.PRIMARY_FONT, font_size=theme.FONT_SIZES["small"], color=theme.COLORS["text"]).move_to(ra)
    rv_label = Text("RV", font=theme.PRIMARY_FONT, font_size=theme.FONT_SIZES["small"], color=theme.COLORS["text"]).move_to(rv)
    la_label = Text("LA", font=theme.PRIMARY_FONT, font_size=theme.FONT_SIZES["small"], color=theme.COLORS["text"]).move_to(la)
    lv_label = Text("LV", font=theme.PRIMARY_FONT, font_size=theme.FONT_SIZES["small"], color=theme.COLORS["text"]).move_to(lv)

    frame = Square(4.6).set_stroke(theme.COLORS["muted"], width=1)
    return VGroup(frame, ra, rv, la, lv, ra_label, rv_label, la_label, lv_label)


def panel_grid(labels: List[str]) -> VGroup:
    panels = VGroup()
    for label in labels:
        rect = RoundedRectangle(width=3.0, height=2.0, corner_radius=0.15)
        rect.set_fill(theme.COLORS["panel"], opacity=1).set_stroke(theme.COLORS["muted"], width=1)
        text = Text(label, font=theme.PRIMARY_FONT, font_size=theme.FONT_SIZES["small"], color=theme.COLORS["text"])
        text.move_to(rect.get_center())
        panels.add(VGroup(rect, text))
    panels.arrange_in_grid(rows=2, cols=2, buff=0.4)
    return panels
