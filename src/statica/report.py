from pathlib import Path
import importlib.metadata

class ReportBuilder:

    def build(self, filepath: Path, features: dict, VERSION) -> dict:
    
        report = {}
        report["tool"] = {
            "name": "statica",
            "version": VERSION
        }
        report["input"] = {"path": str(filepath)}
        report["hashes"] = features.get("hashes", {})
        report["iocs"] = features.get("iocs", {})
        report["strings"] = features.get("strings", [])
        report["errors"] = []

        return report