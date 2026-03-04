from pathlib import Path
from statica.report import ReportBuilder

class StaticAnalysisPipeline:

    def __init__(self):
        
        pass

    def run(self, filepath: Path) -> dict:
        with open(filepath, 'rb') as f:
            content = f.read() # not used for now
            features = { # will utilize content in the future
                "hashes": {},
                "iocs": {},
                "strings": []
                }
            report_builder = ReportBuilder()
            report = report_builder.build(filepath, features)
            return report

        
