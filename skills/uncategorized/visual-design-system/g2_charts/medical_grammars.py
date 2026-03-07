#!/usr/bin/env python3
"""
Medical Chart Grammar Presets for AntV G2

Pre-configured grammar specifications for common medical visualizations.
These grammars follow publication standards (Nature/JACC/NEJM) and use
colorblind-safe palettes from design tokens.

Usage:
    from medical_grammars import (
        forest_plot_grammar,
        kaplan_meier_grammar,
        grouped_comparison_grammar
    )

    grammar = forest_plot_grammar(
        studies=['Study A', 'Study B'],
        estimates=[0.74, 0.82],
        lower=[0.65, 0.72],
        upper=[0.85, 0.93]
    )
"""

from typing import List, Dict, Any, Optional, Tuple


# Design tokens
COLORS = {
    'primary': '#1e3a5f',
    'secondary': '#2d6a9f',
    'neutral': '#546e7a',
    'danger': '#c62828',
    'success': '#2e7d32',
    'categorical': ['#4477AA', '#66CCEE', '#228833', '#CCBB44', '#EE6677', '#AA3377', '#BBBBBB'],
    'treatment_control': ['#0077bb', '#ee7733'],
    'benefit_risk': ['#009988', '#cc3311']
}


def forest_plot_grammar(
    studies: List[str],
    estimates: List[float],
    lower_ci: List[float],
    upper_ci: List[float],
    weights: Optional[List[float]] = None,
    null_value: float = 1.0,
    log_scale: bool = True,
    title: str = "Forest Plot"
) -> Dict[str, Any]:
    """
    Create grammar for meta-analysis forest plot.

    Args:
        studies: Study names
        estimates: Point estimates (HR, OR, RR)
        lower_ci: Lower confidence interval bounds
        upper_ci: Upper confidence interval bounds
        weights: Study weights (for sizing)
        null_value: Null hypothesis value (1.0 for ratios, 0.0 for differences)
        log_scale: Use log scale for y-axis
        title: Chart title

    Returns:
        G2 grammar specification
    """
    if weights is None:
        weights = [100] * len(studies)

    # Prepare data
    data = []
    for i, study in enumerate(studies):
        data.append({
            'study': study,
            'estimate': estimates[i],
            'lower_ci': lower_ci[i],
            'upper_ci': upper_ci[i],
            'weight': weights[i]
        })

    return {
        'data': data,
        'marks': [
            # Confidence interval bars
            {
                'type': 'interval',
                'encode': {
                    'x': 'study',
                    'y': ['lower_ci', 'upper_ci']
                },
                'style': {
                    'fill': COLORS['neutral'],
                    'fillOpacity': 0.3,
                    'stroke': COLORS['neutral'],
                    'strokeWidth': 1
                }
            },
            # Point estimates
            {
                'type': 'point',
                'encode': {
                    'x': 'study',
                    'y': 'estimate',
                    'size': 'weight'
                },
                'style': {
                    'fill': COLORS['primary'],
                    'shape': 'diamond'
                }
            }
        ],
        'scales': {
            'y': {
                'type': 'log' if log_scale else 'linear',
                'nice': True
            },
            'size': {
                'range': [100, 400]
            }
        },
        'coordinate': {
            'type': 'transpose'
        },
        'xAxis': {
            'title': 'Study'
        },
        'yAxis': {
            'title': 'Effect Estimate (95% CI)'
        },
        'legend': False,
        'title': title
    }


def kaplan_meier_grammar(
    time_data: List[List[float]],
    survival_data: List[List[float]],
    group_names: List[str],
    title: str = "Kaplan-Meier Survival Curve",
    xlabel: str = "Time (months)",
    ylabel: str = "Survival Probability"
) -> Dict[str, Any]:
    """
    Create grammar for Kaplan-Meier survival curves.

    Args:
        time_data: List of time arrays for each group
        survival_data: List of survival probability arrays
        group_names: Group labels
        title: Chart title
        xlabel: X-axis label
        ylabel: Y-axis label

    Returns:
        G2 grammar specification
    """
    # Prepare data
    data = []
    for i, group in enumerate(group_names):
        for j, time in enumerate(time_data[i]):
            data.append({
                'time': time,
                'survival': survival_data[i][j],
                'group': group
            })

    return {
        'data': data,
        'marks': [
            # Step lines
            {
                'type': 'line',
                'encode': {
                    'x': 'time',
                    'y': 'survival',
                    'color': 'group'
                },
                'style': {
                    'lineWidth': 2.5,
                    'shape': 'hv'  # Step function
                }
            },
            # Shaded area
            {
                'type': 'area',
                'encode': {
                    'x': 'time',
                    'y': 'survival',
                    'color': 'group'
                },
                'style': {
                    'fillOpacity': 0.1,
                    'shape': 'hv'
                }
            }
        ],
        'scales': {
            'y': {
                'domain': [0, 1],
                'nice': False
            },
            'color': {
                'range': COLORS['treatment_control']
            }
        },
        'xAxis': {
            'title': xlabel,
            'grid': True
        },
        'yAxis': {
            'title': ylabel,
            'grid': True
        },
        'legend': {
            'position': 'top-right'
        },
        'title': title
    }


def grouped_comparison_grammar(
    categories: List[str],
    groups: List[str],
    values: List[List[float]],
    title: str = "Treatment Comparison",
    ylabel: str = "Event Rate (%)"
) -> Dict[str, Any]:
    """
    Create grammar for grouped bar chart (treatment comparisons).

    Args:
        categories: Outcome categories
        groups: Group names (e.g., ['Treatment', 'Control'])
        values: Values for each group (list of lists)
        title: Chart title
        ylabel: Y-axis label

    Returns:
        G2 grammar specification
    """
    # Prepare data
    data = []
    for i, category in enumerate(categories):
        for j, group in enumerate(groups):
            data.append({
                'category': category,
                'group': group,
                'value': values[j][i]
            })

    return {
        'data': data,
        'marks': [
            {
                'type': 'interval',
                'encode': {
                    'x': 'category',
                    'y': 'value',
                    'color': 'group',
                    'series': 'group'
                },
                'transform': [
                    {'type': 'dodgeX'}
                ],
                'style': {
                    'radius': 2
                }
            }
        ],
        'scales': {
            'color': {
                'range': COLORS['treatment_control'][:len(groups)]
            },
            'y': {
                'nice': True
            }
        },
        'xAxis': {
            'title': 'Outcome'
        },
        'yAxis': {
            'title': ylabel,
            'grid': True
        },
        'legend': {
            'position': 'top'
        },
        'title': title
    }


def multi_panel_grammar(
    data: List[Dict[str, Any]],
    x_field: str,
    y_field: str,
    color_field: str,
    facet_field: str,
    title: str = "Multi-Panel Figure"
) -> Dict[str, Any]:
    """
    Create grammar for multi-panel figure with faceting.

    Args:
        data: Chart data with faceting variable
        x_field: X-axis field name
        y_field: Y-axis field name
        color_field: Color grouping field
        facet_field: Faceting field (creates separate panels)
        title: Chart title

    Returns:
        G2 grammar specification
    """
    return {
        'data': data,
        'marks': [
            {
                'type': 'point',
                'encode': {
                    'x': x_field,
                    'y': y_field,
                    'color': color_field
                },
                'style': {
                    'size': 3,
                    'fillOpacity': 0.6
                }
            },
            {
                'type': 'line',
                'encode': {
                    'x': x_field,
                    'y': y_field,
                    'color': color_field
                },
                'style': {
                    'lineWidth': 2
                }
            }
        ],
        'scales': {
            'color': {
                'range': COLORS['categorical']
            }
        },
        'facet': {
            'type': 'rect',
            'encode': {
                'x': facet_field
            }
        },
        'xAxis': {
            'grid': True
        },
        'yAxis': {
            'grid': True
        },
        'legend': {
            'position': 'top'
        },
        'title': title
    }


def scatter_regression_grammar(
    x_data: List[float],
    y_data: List[float],
    groups: Optional[List[str]] = None,
    regression_line: bool = True,
    title: str = "Scatter Plot",
    xlabel: str = "X",
    ylabel: str = "Y"
) -> Dict[str, Any]:
    """
    Create grammar for scatter plot with optional regression line.

    Args:
        x_data: X values
        y_data: Y values
        groups: Optional grouping variable
        regression_line: Add regression line
        title: Chart title
        xlabel: X-axis label
        ylabel: Y-axis label

    Returns:
        G2 grammar specification
    """
    # Prepare data
    data = []
    for i in range(len(x_data)):
        point = {
            'x': x_data[i],
            'y': y_data[i]
        }
        if groups:
            point['group'] = groups[i]
        data.append(point)

    marks = [
        {
            'type': 'point',
            'encode': {
                'x': 'x',
                'y': 'y',
                'color': 'group' if groups else None
            },
            'style': {
                'size': 4,
                'fillOpacity': 0.6
            }
        }
    ]

    if regression_line:
        marks.append({
            'type': 'line',
            'encode': {
                'x': 'x',
                'y': 'y',
                'color': 'group' if groups else None
            },
            'transform': [
                {'type': 'regression'}
            ],
            'style': {
                'lineWidth': 2,
                'lineDash': [4, 4]
            }
        })

    return {
        'data': data,
        'marks': marks,
        'scales': {
            'color': {
                'range': COLORS['categorical']
            }
        },
        'xAxis': {
            'title': xlabel,
            'grid': True
        },
        'yAxis': {
            'title': ylabel,
            'grid': True
        },
        'legend': {
            'position': 'top-right'
        } if groups else {'display': False},
        'title': title
    }


def heatmap_grammar(
    data: List[Dict[str, Any]],
    x_field: str,
    y_field: str,
    value_field: str,
    title: str = "Heatmap"
) -> Dict[str, Any]:
    """
    Create grammar for heatmap (correlation matrices, etc.).

    Args:
        data: Data with x, y, and value fields
        x_field: X-axis field name
        y_field: Y-axis field name
        value_field: Value field for color intensity
        title: Chart title

    Returns:
        G2 grammar specification
    """
    return {
        'data': data,
        'marks': [
            {
                'type': 'cell',
                'encode': {
                    'x': x_field,
                    'y': y_field,
                    'color': value_field
                },
                'style': {
                    'stroke': '#fff',
                    'strokeWidth': 1
                }
            }
        ],
        'scales': {
            'color': {
                'type': 'sequential',
                'range': ['#deebf7', '#3182bd']
            }
        },
        'xAxis': {
            'title': ''
        },
        'yAxis': {
            'title': ''
        },
        'legend': {
            'position': 'right'
        },
        'title': title
    }


# Export all grammars
__all__ = [
    'forest_plot_grammar',
    'kaplan_meier_grammar',
    'grouped_comparison_grammar',
    'multi_panel_grammar',
    'scatter_regression_grammar',
    'heatmap_grammar'
]
