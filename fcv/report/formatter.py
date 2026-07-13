from typing import List
import json
import os

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
        table.add_column("Source Location (Fortran <-> C)", justify="left")
        table.add_column("Message", justify="left")

        for m in mismatches:
            sev_color = "red" if m.severity == "ERROR" else "yellow" if m.severity == "WARNING" else "white"
            
            f_loc = f"{os.path.basename(m.f_file)}:{m.f_line}" if m.f_file else "?"
            c_loc = f"{os.path.basename(m.c_file)}:{m.c_line}" if m.c_file else "?"
            loc_str = f"{f_loc} <-> {c_loc}"
            
            table.add_row(
                f"[bold {sev_color}]{m.severity}[/bold {sev_color}]",
                f"[cyan]{m.proc_name}[/cyan]",
                m.category,
                loc_str,
                m.message
            )

        self.console.print(table)
        
        errors = sum(1 for m in mismatches if m.severity == "ERROR")
        warnings = sum(1 for m in mismatches if m.severity == "WARNING")
        
        self.console.print(f"\nSummary: [bold red]{errors} Errors[/bold red], [bold yellow]{warnings} Warnings[/bold yellow]")

    def format_json(self, mismatches: List[Mismatch]) -> str:
        return json.dumps([m.__dict__ for m in mismatches], indent=2)

    def format_sarif(self, mismatches: List[Mismatch]) -> str:
        # Basic SARIF skeleton
        sarif = {
            "version": "2.1.0",
            "$schema": "https://raw.githubusercontent.com/oasis-tcs/sarif-spec/master/Schemata/sarif-schema-2.1.0.json",
            "runs": [{
                "tool": {
                    "driver": {
                        "name": "fcvalidator",
                        "informationUri": "https://github.com/fcvalidator",
                        "rules": []
                    }
                },
                "results": []
            }]
        }
        for m in mismatches:
            result = {
                "ruleId": m.category.replace(" ", "_").lower(),
                "level": "error" if m.severity == "ERROR" else "warning",
                "message": {"text": f"{m.proc_name}: {m.message}"}
            }
            if m.f_file or m.c_file:
                locations = []
                if m.f_file:
                    locations.append({
                        "physicalLocation": {
                            "artifactLocation": {
                                "uri": m.f_file
                            },
                            "region": {
                                "startLine": m.f_line
                            }
                        }
                    })
                if m.c_file:
                    locations.append({
                        "physicalLocation": {
                            "artifactLocation": {
                                "uri": m.c_file
                            },
                            "region": {
                                "startLine": m.c_line
                            }
                        }
                    })
                result["locations"] = locations
            sarif["runs"][0]["results"].append(result)
        return json.dumps(sarif, indent=2)
