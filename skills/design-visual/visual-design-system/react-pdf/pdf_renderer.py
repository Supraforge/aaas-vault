#!/usr/bin/env python3
"""
Python wrapper for react-pdf PDF generation.

Provides a Python interface to the Node.js react-pdf renderer for
generating publication-grade PDFs (JACC, NEJM, Nature quality).

Usage:
    from pdf_renderer import PDFRenderer

    renderer = PDFRenderer()
    result = renderer.render(
        template="newsletter",
        data={"title": "Heart Health Update", ...},
        output_path="output.pdf"
    )
"""

import json
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional


class PDFRenderer:
    """Python wrapper for react-pdf Node.js renderer."""

    # Available templates
    TEMPLATES = ["newsletter", "editorial", "trialSummary", "clinicalReport"]

    def __init__(self, node_path: str = "node"):
        """Initialize the PDF renderer.

        Args:
            node_path: Path to Node.js executable (default: "node")
        """
        self.node_path = node_path
        self.renderer_dir = Path(__file__).parent.resolve()
        self.renderer_js = self.renderer_dir / "dist" / "renderer.js"

        # Ensure renderer is built
        if not self.renderer_js.exists():
            self._build()

    def _build(self) -> None:
        """Build the react-pdf renderer (transpile JSX)."""
        result = subprocess.run(
            ["npm", "run", "build"],
            cwd=self.renderer_dir,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError(f"Failed to build react-pdf: {result.stderr}")

    def list_templates(self) -> List[str]:
        """List available PDF templates.

        Returns:
            List of template names
        """
        return self.TEMPLATES.copy()

    def render(
        self,
        template: str,
        data: Dict[str, Any],
        output_path: str | Path,
    ) -> Dict[str, Any]:
        """Render a PDF using the specified template and data.

        Args:
            template: Template name (newsletter, editorial, trialSummary, clinicalReport)
            data: Template data dictionary
            output_path: Output PDF file path

        Returns:
            Result dictionary with success status, output path, and size

        Raises:
            ValueError: If template is invalid
            RuntimeError: If rendering fails
        """
        if template not in self.TEMPLATES:
            raise ValueError(f"Invalid template: {template}. Available: {self.TEMPLATES}")

        output_path = Path(output_path).resolve()

        # Build command
        cmd = [
            self.node_path,
            str(self.renderer_js),
            "--template", template,
            "--data", json.dumps(data),
            "--output", str(output_path),
        ]

        # Run renderer
        result = subprocess.run(
            cmd,
            cwd=self.renderer_dir,
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            error_msg = result.stderr or result.stdout
            raise RuntimeError(f"PDF rendering failed: {error_msg}")

        # Parse result
        try:
            result_data = json.loads(result.stdout)
        except json.JSONDecodeError:
            raise RuntimeError(f"Invalid renderer output: {result.stdout}")

        if not result_data.get("success"):
            raise RuntimeError(f"PDF rendering failed: {result_data.get('error', 'Unknown error')}")

        return result_data

    def render_newsletter(
        self,
        title: str,
        output_path: str | Path,
        subtitle: Optional[str] = None,
        author: str = "Dr. Shailesh Singh",
        author_credentials: str = "Cardiologist",
        sections: Optional[List[Dict[str, Any]]] = None,
        key_takeaways: Optional[List[str]] = None,
        stats: Optional[List[Dict[str, str]]] = None,
        footer: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """Render a newsletter PDF (B2C patient newsletter).

        Args:
            title: Newsletter title
            output_path: Output PDF file path
            subtitle: Newsletter subtitle
            author: Author name
            author_credentials: Author credentials
            sections: List of section dictionaries with title, content, subsections
            key_takeaways: List of key takeaway strings
            stats: List of stat dictionaries with value, label, context
            footer: Footer dictionary with left and right text

        Returns:
            Result dictionary
        """
        data = {
            "title": title,
            "author": author,
            "authorCredentials": author_credentials,
        }
        if subtitle:
            data["subtitle"] = subtitle
        if sections:
            data["sections"] = sections
        if key_takeaways:
            data["keyTakeaways"] = key_takeaways
        if stats:
            data["stats"] = stats
        if footer:
            data["footer"] = footer

        return self.render("newsletter", data, output_path)

    def render_editorial(
        self,
        title: str,
        output_path: str | Path,
        abstract: Optional[str] = None,
        authors: Optional[List[Dict[str, str]]] = None,
        keywords: Optional[List[str]] = None,
        sections: Optional[List[Dict[str, Any]]] = None,
        references: Optional[List[str]] = None,
        disclosures: Optional[str] = None,
        funding: Optional[str] = None,
        corresponding_author: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        """Render an editorial PDF (JACC-style medical editorial).

        Args:
            title: Editorial title
            output_path: Output PDF file path
            abstract: Abstract text
            authors: List of author dictionaries with name, affiliation, superscript
            keywords: List of keywords
            sections: List of section dictionaries with title and content
            references: List of reference strings
            disclosures: Disclosure statement
            funding: Funding statement
            corresponding_author: Dictionary with name, email, address

        Returns:
            Result dictionary
        """
        data = {"title": title}
        if abstract:
            data["abstract"] = abstract
        if authors:
            data["authors"] = authors
        if keywords:
            data["keywords"] = keywords
        if sections:
            data["sections"] = sections
        if references:
            data["references"] = references
        if disclosures:
            data["disclosures"] = disclosures
        if funding:
            data["funding"] = funding
        if corresponding_author:
            data["correspondingAuthor"] = corresponding_author

        return self.render("editorial", data, output_path)

    def render_trial_summary(
        self,
        trial_name: str,
        output_path: str | Path,
        full_title: Optional[str] = None,
        registry: Optional[str] = None,
        publication: Optional[str] = None,
        population: Optional[Dict[str, Any]] = None,
        intervention: Optional[Dict[str, str]] = None,
        comparator: Optional[Dict[str, str]] = None,
        primary_endpoint: Optional[Dict[str, str]] = None,
        secondary_endpoints: Optional[List[Dict[str, str]]] = None,
        safety_findings: Optional[List[str]] = None,
        limitations: Optional[List[str]] = None,
        clinical_implications: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Render a trial summary PDF (clinical trial results summary).

        Args:
            trial_name: Short trial name (e.g., "EMPEROR-Preserved")
            output_path: Output PDF file path
            full_title: Full trial title
            registry: Trial registry ID (e.g., "NCT03057951")
            publication: Publication reference
            population: Dictionary with n (number) and description
            intervention: Dictionary with name and dose
            comparator: Dictionary with name and dose
            primary_endpoint: Dictionary with name, metric, value, ci, pValue
            secondary_endpoints: List of endpoint dictionaries
            safety_findings: List of safety finding strings
            limitations: List of limitation strings
            clinical_implications: Clinical implications text

        Returns:
            Result dictionary
        """
        data = {"trialName": trial_name}
        if full_title:
            data["fullTitle"] = full_title
        if registry:
            data["registry"] = registry
        if publication:
            data["publication"] = publication
        if population:
            data["population"] = population
        if intervention:
            data["intervention"] = intervention
        if comparator:
            data["comparator"] = comparator
        if primary_endpoint:
            data["primaryEndpoint"] = primary_endpoint
        if secondary_endpoints:
            data["secondaryEndpoints"] = secondary_endpoints
        if safety_findings:
            data["safetyFindings"] = safety_findings
        if limitations:
            data["limitations"] = limitations
        if clinical_implications:
            data["clinicalImplications"] = clinical_implications

        return self.render("trialSummary", data, output_path)

    def render_clinical_report(
        self,
        title: str,
        output_path: str | Path,
        report_type: str = "Case Report",
        patient: Optional[Dict[str, str]] = None,
        chief_complaint: Optional[str] = None,
        history_of_present_illness: Optional[str] = None,
        past_medical_history: Optional[List[str]] = None,
        medications: Optional[List[str]] = None,
        physical_exam: Optional[Dict[str, Any]] = None,
        investigations: Optional[List[Dict[str, Any]]] = None,
        diagnosis: Optional[Dict[str, Any]] = None,
        management: Optional[List[str]] = None,
        outcome: Optional[str] = None,
        discussion: Optional[str] = None,
        learning_points: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """Render a clinical report PDF (case report / clinical summary).

        Args:
            title: Report title
            output_path: Output PDF file path
            report_type: Type of report (e.g., "Case Report", "Clinical Summary")
            patient: Dictionary with age, sex, occupation
            chief_complaint: Chief complaint text
            history_of_present_illness: HPI text
            past_medical_history: List of PMH items
            medications: List of medications
            physical_exam: Dictionary with exam findings
            investigations: List of investigation dictionaries (test, result, reference, abnormal)
            diagnosis: Dictionary with primary and secondary diagnoses
            management: List of management steps
            outcome: Outcome text
            discussion: Discussion text
            learning_points: List of learning points

        Returns:
            Result dictionary
        """
        data = {"title": title, "reportType": report_type}
        if patient:
            data["patient"] = patient
        if chief_complaint:
            data["chiefComplaint"] = chief_complaint
        if history_of_present_illness:
            data["historyOfPresentIllness"] = history_of_present_illness
        if past_medical_history:
            data["pastMedicalHistory"] = past_medical_history
        if medications:
            data["medications"] = medications
        if physical_exam:
            data["physicalExam"] = physical_exam
        if investigations:
            data["investigations"] = investigations
        if diagnosis:
            data["diagnosis"] = diagnosis
        if management:
            data["management"] = management
        if outcome:
            data["outcome"] = outcome
        if discussion:
            data["discussion"] = discussion
        if learning_points:
            data["learningPoints"] = learning_points

        return self.render("clinicalReport", data, output_path)


def main():
    """CLI for PDF renderer."""
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Generate publication-grade PDFs")
    parser.add_argument("--template", "-t", choices=PDFRenderer.TEMPLATES,
                       help="Template to use")
    parser.add_argument("--data", "-d", type=str,
                       help="JSON data for the template")
    parser.add_argument("--output", "-o", type=str, default="output.pdf",
                       help="Output PDF path")
    parser.add_argument("--list", action="store_true", help="List available templates")

    args = parser.parse_args()

    renderer = PDFRenderer()

    if args.list:
        print("Available templates:", ", ".join(renderer.list_templates()))
        return

    if not args.template or not args.data:
        parser.error("--template and --data are required for rendering")

    data = json.loads(args.data)
    result = renderer.render(args.template, data, args.output)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
