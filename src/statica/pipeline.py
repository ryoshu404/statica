from pathlib import Path
from statica.report import ReportBuilder
from statica.extractors.hash_extractor import HashExtractor
from statica.extractors.string_extractor import StringExtractor

class StaticAnalysisPipeline:

    def __init__(self, min_string_len: int = 6):
        self.hash_extractor = HashExtractor()
        self.string_extractor = StringExtractor(min_len=min_string_len)

    def run(self, filepath: Path) -> dict:

        with open(filepath, 'rb') as f:

            content = f.read()
            hashes = self.hash_extractor.extract(content)
            strings = self.string_extractor.extract(content)
            features = {
                "hashes": {},
                "iocs": {},
                "strings": []
                }
            features['hashes'] = hashes
            features['strings'] = strings
            report_builder = ReportBuilder()
            report = report_builder.build(filepath, features)

            return report

        
