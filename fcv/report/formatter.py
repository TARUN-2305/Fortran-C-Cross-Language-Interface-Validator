from typing import List
import json

from fcv.engine.comparator import Mismatch
from fcv.report.severity import Severity
from rich.console import Console
from rich.table import Table

class ReportFormatter:
    def __init__(self, use_color: bool = True):
        self.console = Console(no_color=not use_color)

    def format_text(self, mismatches: List[Mismatch]) -> None:
        if not mismatches:
            self.console.print("[bold green]No mismatches found![/bold green]")
            return

        table = Table(title="Interface Validation Report")
        table.add_column("Severity", justify="left")
        table.add_column("Procedure", justify="left")
        table.add_column("Category", justify="left")
        table.add_column("Message", justify="left")

        for m in mismatches:
            sev_color = "red" if m.severity == Severity.ERROR else "yellow" if m.severity == Severity.WARNING else "white"
            table.add_row(
                f"[bold {sev_color}]{m.severity}[/bold {sev_color}]",
                f"[cyan]{m.proc_name}[/cyan]",
                m.category,
                m.message
            )

        self.console.print(table)
        
        errors = sum(1 for m in mismatches if m.severity == Severity.ERROR)
        warnings = sum(1 for m in mismatches if m.severity == Severity.WARNING)
        
        self.console.print(f"\nSummary: [bold red]{errors} Errors[/bold red], [bold yellow]{warnings} Warnings[/bold yellow]")

    def format_json(self, mismatches: List[Mismatch]) -> str:
        return json.dumps([m.__dict__ for m in mismatches], indent=2)

    def format_sarif(self, mismatches: List[Mismatch]) -> str:
        rules_map = {}
        results = []
        
        for m in mismatches:
            rule_id = m.category.replace(" ", "_").upper()
            if rule_id not in rules_map:
                rules_map[rule_id] = {
                    "id": rule_id,
                    "shortDescription": {"text": m.category.replace("_", " ").title()},
                    "fullDescription": {"text": m.message}
                }
            
            result = {
                "ruleId": rule_id,
                "level": "error" if m.severity == Severity.ERROR else "warning",
                "message": {"text": f"[{m.proc_name}] {m.message}"}
            }
            
            if m.file_path:
                # Convert backslashes for SARIF URI compatibility
                clean_path = m.file_path.replace("\\", "/")
                # Ensure it prefix with file:/// if absolute and on windows
                if ":" in clean_path and not clean_path.startswith("file:///"):
                    clean_path = "file:///" + clean_path
                result["locations"] = [{
                    "physicalLocation": {
                        "artifactLocation": {
                            "uri": clean_path
                        },
                        "region": {
                            "startLine": m.line_number
                        }
                    }
                }]
            results.append(result)

        sarif = {
            "version": "2.1.0",
            "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
            "runs": [{
                "tool": {
                    "driver": {
                        "name": "fcvalidator",
                        "informationUri": "https://github.com/fcvalidator",
                        "rules": list(rules_map.values())
                    }
                },
                "results": results
            }]
        }
        return json.dumps(sarif, indent=2)
