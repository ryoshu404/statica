from pathlib import Path

class ReportBuilder:

    def build(self, filepath: Path, features: dict) -> dict:
    
        report = {}
        report["tool"] = {
            "name": "statica",
            "version": "1.0.0"
        }
        report["input"] = {"path": str(filepath)}
        report["hashes"] = features.get("hashes", {})
        report["iocs"] = features.get("iocs", {})
        report["strings"] = features.get("strings", [])
        report["errors"] = []

        return report