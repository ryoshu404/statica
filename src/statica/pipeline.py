from pathlib import Path
from statica.report import ReportBuilder
from statica.extractors.hash_extractor import HashExtractor

class StaticAnalysisPipeline:

    def __init__(self):
        self.hash_extractor = HashExtractor()

    def run(self, filepath: Path) -> dict:

        with open(filepath, 'rb') as f:

            content = f.read()
            hashes = self.hash_extractor.extract(content)
            features = {
                "hashes": {},
                "iocs": {},
                "strings": []
                }
            features['hashes'] = hashes
            report_builder = ReportBuilder()
            report = report_builder.build(filepath, features)

            return report

        
