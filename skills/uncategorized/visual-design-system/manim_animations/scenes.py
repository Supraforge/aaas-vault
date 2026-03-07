"""
Manim scenes for cardiology education animations.
"""

from __future__ import annotations

from typing import List, Tuple

from manim import (
    Dot,
    FadeIn,
    Line,
    Scene,
    Text,
    VGroup,
    VMobject,
    config,
    Create,
    UP,
    DOWN,
    LEFT,
    RIGHT,
)

import theme
from primitives import heart_chambers
from templates import (
    AnatomyChambersScene,
    BarScene,
    ComparisonScene,
    FlowScene,
    ForestPlotScene,
    KaplanMeierBaseScene,
    LineScene,
    PanelGridScene,
    TimelineScene,
)

theme.apply_theme(config)


class MechanismOfActionScene(FlowScene):
    TITLE = "Mechanism of Action"
    STEPS = [
        ("Drug", theme.COLORS["blue"]),
        ("Receptor", theme.COLORS["teal"]),
        ("Signal", theme.COLORS["success"]),
        ("Outcome", theme.COLORS["navy"]),
    ]
    OUTCOME = "24% lower HF hospitalization"


class KaplanMeierScene(KaplanMeierBaseScene):
    TITLE = "Event-Free Survival"
    TREATMENT_POINTS = [(0, 1.0), (6, 0.94), (12, 0.88), (18, 0.83), (24, 0.78)]
    CONTROL_POINTS = [(0, 1.0), (6, 0.91), (12, 0.83), (18, 0.76), (24, 0.69)]
    HR_TEXT = "HR 0.76 (95% CI 0.64-0.90)"


class ECGWaveScene(Scene):
    def construct(self) -> None:
        title = Text(
            "ECG: Normal Sinus Rhythm",
            font=theme.PRIMARY_FONT,
            font_size=theme.FONT_SIZES["title"],
            color=theme.COLORS["navy"],
        ).to_edge(UP)

        baseline = Line(LEFT * 5.5, RIGHT * 5.5, color=theme.COLORS["muted"]).shift(DOWN * 0.5)

        points = [
            LEFT * 5.5 + DOWN * 0.5,
            LEFT * 4.7 + DOWN * 0.35,
            LEFT * 4.0 + DOWN * 0.5,
            LEFT * 3.4 + UP * 0.3,
            LEFT * 3.2 + DOWN * 0.85,
            LEFT * 2.7 + DOWN * 0.5,
            LEFT * 1.6 + DOWN * 0.4,
            LEFT * 0.3 + DOWN * 0.5,
            RIGHT * 0.7 + DOWN * 0.15,
            RIGHT * 1.8 + DOWN * 0.5,
            RIGHT * 5.5 + DOWN * 0.5,
        ]

        wave = _ecg_wave(points, theme.COLORS["blue"])

        labels = VGroup(
            Text("P", font=theme.PRIMARY_FONT, font_size=theme.FONT_SIZES["small"], color=theme.COLORS["text"]).next_to(LEFT * 4.3 + DOWN * 0.1, UP),
            Text("QRS", font=theme.PRIMARY_FONT, font_size=theme.FONT_SIZES["small"], color=theme.COLORS["text"]).next_to(LEFT * 3.2 + DOWN * 0.1, UP),
            Text("T", font=theme.PRIMARY_FONT, font_size=theme.FONT_SIZES["small"], color=theme.COLORS["text"]).next_to(RIGHT * 0.7 + DOWN * 0.1, UP),
        )

        self.play(FadeIn(title))
        self.play(Create(baseline))
        self.play(Create(wave))
        self.play(FadeIn(labels))
        self.wait(0.5)


class ECGAtrialFibrillationScene(Scene):
    def construct(self) -> None:
        title = Text(
            "ECG: Atrial Fibrillation",
            font=theme.PRIMARY_FONT,
            font_size=theme.FONT_SIZES["title"],
            color=theme.COLORS["navy"],
        ).to_edge(UP)

        baseline = Line(LEFT * 5.5, RIGHT * 5.5, color=theme.COLORS["muted"]).shift(DOWN * 0.5)

        points = [
            LEFT * 5.5 + DOWN * 0.4,
            LEFT * 4.6 + DOWN * 0.7,
            LEFT * 4.1 + DOWN * 0.2,
            LEFT * 3.6 + DOWN * 0.9,
            LEFT * 3.0 + UP * 0.4,
            LEFT * 2.8 + DOWN * 0.8,
            LEFT * 2.2 + DOWN * 0.3,
            LEFT * 1.5 + DOWN * 0.7,
            LEFT * 0.7 + UP * 0.2,
            RIGHT * 0.2 + DOWN * 0.6,
            RIGHT * 1.2 + DOWN * 0.1,
            RIGHT * 2.1 + DOWN * 0.8,
            RIGHT * 3.0 + DOWN * 0.3,
            RIGHT * 3.8 + DOWN * 0.7,
            RIGHT * 5.5 + DOWN * 0.5,
        ]

        wave = _ecg_wave(points, theme.COLORS["danger"])

        note = Text(
            "Irregularly irregular rhythm",
            font=theme.PRIMARY_FONT,
            font_size=theme.FONT_SIZES["small"],
            color=theme.COLORS["text"],
        ).next_to(baseline, DOWN, buff=0.5)

        self.play(FadeIn(title))
        self.play(Create(baseline))
        self.play(Create(wave))
        self.play(FadeIn(note))
        self.wait(0.5)


class SGLT2MechanismScene(FlowScene):
    TITLE = "SGLT2 Inhibitor Mechanism"
    STEPS = [
        ("SGLT2 block", theme.COLORS["blue"]),
        ("Natriuresis", theme.COLORS["teal"]),
        ("Lower preload", theme.COLORS["success"]),
        ("HF stability", theme.COLORS["navy"]),
    ]
    OUTCOME = "30% lower HF hospitalization"


class GLP1MechanismScene(FlowScene):
    TITLE = "GLP-1 Agonist Pathway"
    STEPS = [
        ("GLP-1 agonist", theme.COLORS["blue"]),
        ("Weight loss", theme.COLORS["teal"]),
        ("Lower inflammation", theme.COLORS["success"]),
        ("MACE reduction", theme.COLORS["navy"]),
    ]
    OUTCOME = "HR 0.86 for MACE"


class ARNIPathwayScene(FlowScene):
    TITLE = "ARNi Mechanism"
    STEPS = [
        ("ARNi", theme.COLORS["blue"]),
        ("Lower Ang II", theme.COLORS["teal"]),
        ("Raise natriuretic peptides", theme.COLORS["success"]),
        ("Reverse remodeling", theme.COLORS["navy"]),
    ]
    OUTCOME = "20% lower CV death"


class HFQuadTherapyScene(FlowScene):
    TITLE = "HFrEF Quad Therapy"
    STEPS = [
        ("ARNi/ACEi", theme.COLORS["blue"]),
        ("Beta-blocker", theme.COLORS["teal"]),
        ("MRA", theme.COLORS["success"]),
        ("SGLT2i", theme.COLORS["navy"]),
    ]
    OUTCOME = "4-pillar GDMT"


class LDLReductionScene(BarScene):
    TITLE = "LDL-C Reduction Ladder"
    BARS = [
        ("Baseline", 130, theme.COLORS["neutral"]),
        ("Statin", 80, theme.COLORS["blue"]),
        ("+Eze", 60, theme.COLORS["teal"]),
        ("PCSK9", 35, theme.COLORS["success"]),
    ]
    FOOTNOTE = "Lower is better"


class BloodPressureTargetsScene(BarScene):
    TITLE = "Blood Pressure Targets"
    BARS = [
        ("Baseline", 148, theme.COLORS["neutral"]),
        ("Standard", 130, theme.COLORS["blue"]),
        ("Intensive", 120, theme.COLORS["teal"]),
    ]
    FOOTNOTE = "Target SBP in mmHg"


class ACSPathwayScene(FlowScene):
    TITLE = "ACS Rapid Pathway"
    STEPS = [
        ("Chest pain", theme.COLORS["warning"]),
        ("ECG", theme.COLORS["blue"]),
        ("STEMI/NSTEMI", theme.COLORS["danger"]),
        ("Reperfusion", theme.COLORS["success"]),
    ]


class STEMITimelineScene(TimelineScene):
    TITLE = "STEMI Door-to-Balloon"
    EVENTS = [
        ("0 min", "ECG"),
        ("30 min", "Cath lab"),
        ("90 min", "PCI"),
        ("24h", "DAPT"),
    ]


class PlaqueRuptureScene(FlowScene):
    TITLE = "Plaque Rupture Cascade"
    STEPS = [
        ("Plaque rupture", theme.COLORS["danger"]),
        ("Platelet plug", theme.COLORS["warning"]),
        ("Thrombus", theme.COLORS["danger"]),
        ("MI", theme.COLORS["navy"]),
    ]


class DAPTTimelineScene(TimelineScene):
    TITLE = "DAPT Timeline"
    EVENTS = [
        ("0 mo", "PCI"),
        ("1 mo", "DAPT"),
        ("6 mo", "De-escalate"),
        ("12 mo", "Stop"),
    ]


class AFManagementScene(FlowScene):
    TITLE = "Atrial Fibrillation Care"
    STEPS = [
        ("AF diagnosed", theme.COLORS["warning"]),
        ("CHA2DS2-VASc", theme.COLORS["blue"]),
        ("Anticoagulation", theme.COLORS["teal"]),
        ("Rate/Rhythm", theme.COLORS["success"]),
    ]


class RateRhythmComparisonScene(ComparisonScene):
    TITLE = "Rate vs Rhythm Control"
    LEFT_LABEL = "Rate control"
    RIGHT_LABEL = "Rhythm control"
    LEFT_VALUE = "HR <110"
    RIGHT_VALUE = "Sinus rhythm"
    METRIC = "Symptom relief + stroke prevention"


class ConductionSystemScene(Scene):
    def construct(self) -> None:
        title = Text(
            "Cardiac Conduction",
            font=theme.PRIMARY_FONT,
            font_size=theme.FONT_SIZES["title"],
            color=theme.COLORS["navy"],
        ).to_edge(UP)

        chambers = heart_chambers().next_to(title, DOWN, buff=0.8)

        sa_node = Dot(chambers.get_corner(UP + LEFT) + RIGHT * 0.8 + DOWN * 0.2, color=theme.COLORS["danger"])
        av_node = Dot(chambers.get_center() + DOWN * 0.1, color=theme.COLORS["danger"])
        his = Dot(chambers.get_center() + DOWN * 0.8, color=theme.COLORS["danger"])

        labels = VGroup(
            Text("SA", font=theme.PRIMARY_FONT, font_size=theme.FONT_SIZES["small"], color=theme.COLORS["text"]).next_to(sa_node, RIGHT, buff=0.2),
            Text("AV", font=theme.PRIMARY_FONT, font_size=theme.FONT_SIZES["small"], color=theme.COLORS["text"]).next_to(av_node, RIGHT, buff=0.2),
            Text("His", font=theme.PRIMARY_FONT, font_size=theme.FONT_SIZES["small"], color=theme.COLORS["text"]).next_to(his, RIGHT, buff=0.2),
        )

        self.play(FadeIn(title))
        self.play(Create(chambers))
        self.play(FadeIn(sa_node), FadeIn(av_node), FadeIn(his))
        self.play(FadeIn(labels))
        self.wait(0.5)


class HeartChambersScene(AnatomyChambersScene):
    TITLE = "Heart Chambers"


class TroponinKineticsScene(LineScene):
    TITLE = "Troponin Kinetics"
    POINTS = [(0, 0.1), (1, 0.3), (2, 0.6), (3, 0.85), (4, 0.7), (5, 0.5)]
    X_LABEL = "Hours"
    Y_LABEL = "Relative level"


class EchoViewsScene(PanelGridScene):
    TITLE = "Echo Views Overview"
    LABELS = ["PLAX", "PSAX", "A4C", "A2C"]


class CTAWorkupScene(FlowScene):
    TITLE = "Chest Pain CTA Pathway"
    STEPS = [
        ("Chest pain", theme.COLORS["warning"]),
        ("Risk score", theme.COLORS["blue"]),
        ("CTA", theme.COLORS["teal"]),
        ("Rule-out CAD", theme.COLORS["success"]),
    ]


class StressTestFlowScene(FlowScene):
    TITLE = "Stress Test Workflow"
    STEPS = [
        ("Symptoms", theme.COLORS["warning"]),
        ("Baseline ECG", theme.COLORS["blue"]),
        ("Stress test", theme.COLORS["teal"]),
        ("Ischemia?", theme.COLORS["danger"]),
    ]


class ARRRRScene(ComparisonScene):
    TITLE = "ARR vs RRR"
    LEFT_LABEL = "Control risk"
    RIGHT_LABEL = "Treatment risk"
    LEFT_VALUE = "20%"
    RIGHT_VALUE = "12%"
    METRIC = "ARR 8% | RRR 40%"


class NNTExplainerScene(BarScene):
    TITLE = "Number Needed to Treat"
    BARS = [
        ("NNT 12", 12, theme.COLORS["success"]),
        ("NNT 18", 18, theme.COLORS["teal"]),
        ("NNT 25", 25, theme.COLORS["neutral"]),
    ]
    FOOTNOTE = "Lower NNT is better"


class ForestPlotSummaryScene(ForestPlotScene):
    TITLE = "Forest Plot Summary"
    STUDIES = [
        ("Trial A", 0.82, 0.70, 0.97),
        ("Trial B", 0.76, 0.62, 0.92),
        ("Trial C", 0.88, 0.74, 1.02),
        ("Pooled", 0.81, 0.70, 0.93),
    ]


class EventsPer1000Scene(BarScene):
    TITLE = "Events per 1000"
    BARS = [
        ("Control", 120, theme.COLORS["danger"]),
        ("Treatment", 90, theme.COLORS["success"]),
    ]
    FOOTNOTE = "Lower events with treatment"


class ICDDecisionScene(FlowScene):
    TITLE = "ICD Decision Path"
    STEPS = [
        ("LVEF <=35%", theme.COLORS["warning"]),
        ("NYHA II-III", theme.COLORS["blue"]),
        ("Optimal GDMT", theme.COLORS["teal"]),
        ("ICD", theme.COLORS["success"]),
    ]


class CRTSelectionScene(FlowScene):
    TITLE = "CRT Selection"
    STEPS = [
        ("LBBB", theme.COLORS["warning"]),
        ("QRS >=150", theme.COLORS["blue"]),
        ("LVEF <=35%", theme.COLORS["teal"]),
        ("CRT", theme.COLORS["success"]),
    ]


class TAVRPathwayScene(FlowScene):
    TITLE = "TAVR Pathway"
    STEPS = [
        ("Severe AS", theme.COLORS["warning"]),
        ("Heart team", theme.COLORS["blue"]),
        ("TAVR", theme.COLORS["teal"]),
        ("Follow-up", theme.COLORS["success"]),
    ]


class LVADBridgeScene(TimelineScene):
    TITLE = "LVAD Bridge Timeline"
    EVENTS = [
        ("0 mo", "Advanced HF"),
        ("1 mo", "LVAD"),
        ("6 mo", "Bridge"),
        ("12 mo", "Transplant"),
    ]


def _ecg_wave(points: List, color: str) -> VMobject:
    wave = VMobject(color=color, stroke_width=4)
    wave.set_points_as_corners(points)
    return wave


# ============================================
# ADDITIONAL DRUG MECHANISMS
# ============================================

class StatinMechanismScene(FlowScene):
    TITLE = "Statin Mechanism"
    STEPS = [
        ("HMG-CoA inhibition", theme.COLORS["blue"]),
        ("↓ Cholesterol synthesis", theme.COLORS["teal"]),
        ("↑ LDL receptors", theme.COLORS["success"]),
        ("↓ LDL-C", theme.COLORS["navy"]),
    ]
    OUTCOME = "30-50% LDL reduction"


class PCSK9MechanismScene(FlowScene):
    TITLE = "PCSK9 Inhibitor Pathway"
    STEPS = [
        ("PCSK9 antibody", theme.COLORS["blue"]),
        ("Block PCSK9", theme.COLORS["teal"]),
        ("LDL-R recycling", theme.COLORS["success"]),
        ("↓↓ LDL-C", theme.COLORS["navy"]),
    ]
    OUTCOME = "50-60% additional LDL reduction"


class DOACMechanismScene(FlowScene):
    TITLE = "DOAC Mechanism"
    STEPS = [
        ("Factor Xa/IIa inhibition", theme.COLORS["blue"]),
        ("Block clot formation", theme.COLORS["teal"]),
        ("Prevent thrombus", theme.COLORS["success"]),
        ("Stroke prevention", theme.COLORS["navy"]),
    ]
    OUTCOME = "64% stroke reduction in AF"


class BetaBlockerMechanismScene(FlowScene):
    TITLE = "Beta-Blocker Mechanism"
    STEPS = [
        ("β-receptor block", theme.COLORS["blue"]),
        ("↓ Heart rate", theme.COLORS["teal"]),
        ("↓ Contractility", theme.COLORS["success"]),
        ("↓ O2 demand", theme.COLORS["navy"]),
    ]
    OUTCOME = "Mortality benefit in HFrEF"


class CCBMechanismScene(FlowScene):
    TITLE = "Calcium Channel Blocker"
    STEPS = [
        ("L-type Ca block", theme.COLORS["blue"]),
        ("Vasodilation", theme.COLORS["teal"]),
        ("↓ Afterload", theme.COLORS["success"]),
        ("↓ Blood pressure", theme.COLORS["navy"]),
    ]


class DiureticMechanismScene(FlowScene):
    TITLE = "Loop Diuretic Mechanism"
    STEPS = [
        ("Na-K-2Cl block", theme.COLORS["blue"]),
        ("Natriuresis", theme.COLORS["teal"]),
        ("Volume loss", theme.COLORS["success"]),
        ("Decongestion", theme.COLORS["navy"]),
    ]


# ============================================
# MORE ECG PATTERNS
# ============================================

class ECGSTEMIScene(Scene):
    def construct(self) -> None:
        title = Text(
            "ECG: ST-Elevation MI",
            font=theme.PRIMARY_FONT,
            font_size=theme.FONT_SIZES["title"],
            color=theme.COLORS["navy"],
        ).to_edge(UP)

        baseline = Line(LEFT * 5.5, RIGHT * 5.5, color=theme.COLORS["muted"]).shift(DOWN * 0.5)

        points = [
            LEFT * 5.5 + DOWN * 0.5,
            LEFT * 4.6 + DOWN * 0.35,
            LEFT * 4.0 + DOWN * 0.5,
            LEFT * 3.4 + UP * 0.5,
            LEFT * 3.2 + DOWN * 0.7,
            LEFT * 2.8 + UP * 0.3,  # ST elevation starts
            LEFT * 2.0 + UP * 0.4,  # Elevated segment
            LEFT * 1.0 + UP * 0.2,
            RIGHT * 0.5 + DOWN * 0.5,
            RIGHT * 5.5 + DOWN * 0.5,
        ]

        wave = _ecg_wave(points, theme.COLORS["danger"])

        arrow = Text(
            "↑ ST elevation",
            font=theme.PRIMARY_FONT,
            font_size=theme.FONT_SIZES["small"],
            color=theme.COLORS["danger"],
        ).next_to(LEFT * 2.0 + UP * 0.4, UP, buff=0.3)

        note = Text(
            "Acute transmural ischemia",
            font=theme.PRIMARY_FONT,
            font_size=theme.FONT_SIZES["small"],
            color=theme.COLORS["text"],
        ).next_to(baseline, DOWN, buff=0.5)

        self.play(FadeIn(title))
        self.play(Create(baseline))
        self.play(Create(wave))
        self.play(FadeIn(arrow), FadeIn(note))
        self.wait(0.5)


class ECGHeartBlockScene(Scene):
    def construct(self) -> None:
        title = Text(
            "ECG: Complete Heart Block",
            font=theme.PRIMARY_FONT,
            font_size=theme.FONT_SIZES["title"],
            color=theme.COLORS["navy"],
        ).to_edge(UP)

        baseline = Line(LEFT * 5.5, RIGHT * 5.5, color=theme.COLORS["muted"]).shift(DOWN * 0.5)

        # P waves at regular intervals
        p_wave_1 = _ecg_wave([LEFT * 5.0 + DOWN * 0.5, LEFT * 4.7 + DOWN * 0.3, LEFT * 4.4 + DOWN * 0.5], theme.COLORS["blue"])
        p_wave_2 = _ecg_wave([LEFT * 3.0 + DOWN * 0.5, LEFT * 2.7 + DOWN * 0.3, LEFT * 2.4 + DOWN * 0.5], theme.COLORS["blue"])
        p_wave_3 = _ecg_wave([LEFT * 1.0 + DOWN * 0.5, LEFT * 0.7 + DOWN * 0.3, LEFT * 0.4 + DOWN * 0.5], theme.COLORS["blue"])
        p_wave_4 = _ecg_wave([RIGHT * 1.0 + DOWN * 0.5, RIGHT * 1.3 + DOWN * 0.3, RIGHT * 1.6 + DOWN * 0.5], theme.COLORS["blue"])

        # QRS at different, slower intervals (dissociated)
        qrs_1 = _ecg_wave([LEFT * 4.0 + DOWN * 0.5, LEFT * 3.8 + UP * 0.4, LEFT * 3.6 + DOWN * 0.8, LEFT * 3.4 + DOWN * 0.5], theme.COLORS["danger"])
        qrs_2 = _ecg_wave([RIGHT * 0.0 + DOWN * 0.5, RIGHT * 0.2 + UP * 0.4, RIGHT * 0.4 + DOWN * 0.8, RIGHT * 0.6 + DOWN * 0.5], theme.COLORS["danger"])
        qrs_3 = _ecg_wave([RIGHT * 4.0 + DOWN * 0.5, RIGHT * 4.2 + UP * 0.4, RIGHT * 4.4 + DOWN * 0.8, RIGHT * 4.6 + DOWN * 0.5], theme.COLORS["danger"])

        note = Text(
            "P waves and QRS independent (AV dissociation)",
            font=theme.PRIMARY_FONT,
            font_size=theme.FONT_SIZES["small"],
            color=theme.COLORS["text"],
        ).next_to(baseline, DOWN, buff=0.5)

        self.play(FadeIn(title))
        self.play(Create(baseline))
        self.play(Create(p_wave_1), Create(p_wave_2), Create(p_wave_3), Create(p_wave_4))
        self.play(Create(qrs_1), Create(qrs_2), Create(qrs_3))
        self.play(FadeIn(note))
        self.wait(0.5)


# ============================================
# CLINICAL DECISION PATHWAYS
# ============================================

class ASCVDRiskScene(FlowScene):
    TITLE = "ASCVD Risk Assessment"
    STEPS = [
        ("Risk factors", theme.COLORS["warning"]),
        ("10-yr ASCVD", theme.COLORS["blue"]),
        ("Risk-enhancers", theme.COLORS["teal"]),
        ("Statin decision", theme.COLORS["success"]),
    ]


class CHA2DS2VAScScene(BarScene):
    TITLE = "CHA2DS2-VASc Score"
    BARS = [
        ("0", 0, theme.COLORS["success"]),
        ("1", 1, theme.COLORS["teal"]),
        ("2", 2, theme.COLORS["warning"]),
        ("≥3", 3, theme.COLORS["danger"]),
    ]
    FOOTNOTE = "Score ≥2 in men, ≥3 in women → anticoagulate"


class HASBLEDScene(BarScene):
    TITLE = "HAS-BLED Score"
    BARS = [
        ("0-2", 1.5, theme.COLORS["success"]),
        ("3", 3, theme.COLORS["warning"]),
        ("≥4", 4.5, theme.COLORS["danger"]),
    ]
    FOOTNOTE = "Higher scores = higher bleeding risk"


class HeartScoreScene(FlowScene):
    TITLE = "HEART Score for Chest Pain"
    STEPS = [
        ("History", theme.COLORS["blue"]),
        ("ECG", theme.COLORS["teal"]),
        ("Age", theme.COLORS["success"]),
        ("Risk factors", theme.COLORS["warning"]),
    ]
    OUTCOME = "Troponin → Risk stratify"


# ============================================
# LANDMARK TRIAL RESULTS
# ============================================

class PARADIGMHFScene(KaplanMeierBaseScene):
    TITLE = "PARADIGM-HF: Sacubitril/Valsartan"
    TREATMENT_POINTS = [(0, 1.0), (6, 0.92), (12, 0.85), (18, 0.78), (24, 0.72), (30, 0.66)]
    CONTROL_POINTS = [(0, 1.0), (6, 0.89), (12, 0.80), (18, 0.72), (24, 0.65), (30, 0.57)]
    HR_TEXT = "HR 0.80, p<0.001 — 20% mortality reduction"


class DAPAHFScene(KaplanMeierBaseScene):
    TITLE = "DAPA-HF: Dapagliflozin in HFrEF"
    TREATMENT_POINTS = [(0, 1.0), (6, 0.93), (12, 0.87), (18, 0.82)]
    CONTROL_POINTS = [(0, 1.0), (6, 0.90), (12, 0.82), (18, 0.75)]
    HR_TEXT = "HR 0.74, p<0.001 — 26% reduction"


class EMPERORReducedScene(KaplanMeierBaseScene):
    TITLE = "EMPEROR-Reduced: Empagliflozin"
    TREATMENT_POINTS = [(0, 1.0), (6, 0.92), (12, 0.85), (18, 0.79)]
    CONTROL_POINTS = [(0, 1.0), (6, 0.88), (12, 0.79), (18, 0.70)]
    HR_TEXT = "HR 0.75, p<0.001 — 25% reduction"


class FOURIERTrialScene(KaplanMeierBaseScene):
    TITLE = "FOURIER: Evolocumab (PCSK9i)"
    TREATMENT_POINTS = [(0, 1.0), (12, 0.95), (24, 0.90), (36, 0.86)]
    CONTROL_POINTS = [(0, 1.0), (12, 0.93), (24, 0.87), (36, 0.82)]
    HR_TEXT = "HR 0.85, p<0.001 — 15% MACE reduction"


class SELECTTrialScene(KaplanMeierBaseScene):
    TITLE = "SELECT: Semaglutide CV Outcomes"
    TREATMENT_POINTS = [(0, 1.0), (12, 0.96), (24, 0.92), (36, 0.88), (48, 0.84)]
    CONTROL_POINTS = [(0, 1.0), (12, 0.94), (24, 0.89), (36, 0.83), (48, 0.78)]
    HR_TEXT = "HR 0.80, p<0.001 — 20% MACE reduction"


# ============================================
# COMPARISON SCENES
# ============================================

class StatinIntensityScene(ComparisonScene):
    TITLE = "Statin Intensity Comparison"
    LEFT_LABEL = "Moderate-intensity"
    RIGHT_LABEL = "High-intensity"
    LEFT_VALUE = "30-49% LDL↓"
    RIGHT_VALUE = "≥50% LDL↓"
    METRIC = "High-intensity for ASCVD"


class DOACvsWarfarinScene(ComparisonScene):
    TITLE = "DOAC vs Warfarin"
    LEFT_LABEL = "Warfarin"
    RIGHT_LABEL = "DOAC"
    LEFT_VALUE = "INR 2-3"
    RIGHT_VALUE = "Fixed dose"
    METRIC = "DOACs: fewer ICH, no monitoring"


class HFpEFvsHFrEFScene(ComparisonScene):
    TITLE = "HFpEF vs HFrEF"
    LEFT_LABEL = "HFpEF"
    RIGHT_LABEL = "HFrEF"
    LEFT_VALUE = "EF ≥50%"
    RIGHT_VALUE = "EF ≤40%"
    METRIC = "Different therapies, similar outcomes"


# ============================================
# ADDITIONAL BAR CHARTS
# ============================================

class HeartFailureGDMTScene(BarScene):
    TITLE = "GDMT Mortality Reduction"
    BARS = [
        ("ACEi/ARB", 17, theme.COLORS["blue"]),
        ("Beta-blocker", 34, theme.COLORS["teal"]),
        ("MRA", 30, theme.COLORS["success"]),
        ("SGLT2i", 25, theme.COLORS["navy"]),
    ]
    FOOTNOTE = "% mortality reduction"


class LDLTargetsScene(BarScene):
    TITLE = "LDL-C Targets by Risk"
    BARS = [
        ("Low", 130, theme.COLORS["success"]),
        ("Moderate", 100, theme.COLORS["teal"]),
        ("High", 70, theme.COLORS["blue"]),
        ("Very high", 55, theme.COLORS["navy"]),
    ]
    FOOTNOTE = "LDL-C targets in mg/dL"


class A1cTargetsScene(BarScene):
    TITLE = "HbA1c Targets in DM"
    BARS = [
        ("Strict", 6.5, theme.COLORS["success"]),
        ("Standard", 7.0, theme.COLORS["teal"]),
        ("Relaxed", 8.0, theme.COLORS["blue"]),
    ]
    FOOTNOTE = "Individualize based on patient factors"


# ============================================
# ADDITIONAL TIMELINES
# ============================================

class ACSTreatmentTimelineScene(TimelineScene):
    TITLE = "ACS Treatment Timeline"
    EVENTS = [
        ("0h", "ASA + P2Y12"),
        ("2h", "Heparin"),
        ("24h", "Statin"),
        ("48h", "Beta-blocker"),
    ]


class PostMIRehabScene(TimelineScene):
    TITLE = "Post-MI Rehabilitation"
    EVENTS = [
        ("Week 1", "Early mobilization"),
        ("Week 2", "Outpatient rehab"),
        ("Month 1", "Exercise program"),
        ("Month 3", "Return to activity"),
    ]


class HFHospDischargeScene(TimelineScene):
    TITLE = "HF Hospital Discharge"
    EVENTS = [
        ("Day 0", "Optimize GDMT"),
        ("Day 1", "Euvolemia"),
        ("Day 2-3", "Transition oral"),
        ("1 week", "Follow-up"),
    ]


# ============================================
# ADDITIONAL FLOW PATHWAYS
# ============================================

class ChestPainTriageScene(FlowScene):
    TITLE = "Chest Pain Triage"
    STEPS = [
        ("Chest pain", theme.COLORS["warning"]),
        ("ECG <10 min", theme.COLORS["blue"]),
        ("Troponin", theme.COLORS["teal"]),
        ("Risk score", theme.COLORS["success"]),
    ]


class SyncopeWorkupScene(FlowScene):
    TITLE = "Syncope Workup"
    STEPS = [
        ("Syncope", theme.COLORS["warning"]),
        ("History/PE", theme.COLORS["blue"]),
        ("ECG", theme.COLORS["teal"]),
        ("Risk stratify", theme.COLORS["success"]),
    ]


class PEWorkupScene(FlowScene):
    TITLE = "Pulmonary Embolism Workup"
    STEPS = [
        ("Suspicion", theme.COLORS["warning"]),
        ("Wells score", theme.COLORS["blue"]),
        ("D-dimer", theme.COLORS["teal"]),
        ("CTPA", theme.COLORS["success"]),
    ]


class HypertensionWorkupScene(FlowScene):
    TITLE = "HTN Workup"
    STEPS = [
        ("Elevated BP", theme.COLORS["warning"]),
        ("Confirm HTN", theme.COLORS["blue"]),
        ("Assess risk", theme.COLORS["teal"]),
        ("Lifestyle + Rx", theme.COLORS["success"]),
    ]


class PreopCardiacScene(FlowScene):
    TITLE = "Preoperative Cardiac Evaluation"
    STEPS = [
        ("Surgery planned", theme.COLORS["blue"]),
        ("ACS risk", theme.COLORS["warning"]),
        ("Functional capacity", theme.COLORS["teal"]),
        ("Testing?", theme.COLORS["success"]),
    ]
