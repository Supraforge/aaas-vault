"""
Architecture Diagrams Module - Architecture as Code for Medical Content

Uses mingrammer/diagrams to create:
- Treatment pathways (clinical algorithms)
- Research flows (study methodology)
- Healthcare architecture (system diagrams)

All diagrams use the design tokens for consistent styling.

Note: Named 'arch_diagrams' to avoid shadowing the 'diagrams' package.
"""

# Lazy imports to avoid circular import issues
def __getattr__(name):
    """Lazy import to avoid circular import with diagrams package."""
    if name in [
        "create_treatment_pathway",
        "create_heart_failure_pathway",
        "create_acs_pathway",
        "create_af_pathway",
    ]:
        from . import treatment_pathways
        return getattr(treatment_pathways, name)
    elif name in [
        "create_study_flow",
        "create_consort_diagram",
        "create_prisma_diagram",
        "create_methodology_flow",
    ]:
        from . import research_flows
        return getattr(research_flows, name)
    elif name in [
        "create_healthcare_system",
        "create_cardiology_department",
        "create_data_pipeline",
    ]:
        from . import healthcare_arch
        return getattr(healthcare_arch, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

__all__ = [
    # Treatment pathways
    "create_treatment_pathway",
    "create_heart_failure_pathway",
    "create_acs_pathway",
    "create_af_pathway",
    # Research flows
    "create_study_flow",
    "create_consort_diagram",
    "create_prisma_diagram",
    "create_methodology_flow",
    # Healthcare architecture
    "create_healthcare_system",
    "create_cardiology_department",
    "create_data_pipeline",
]
