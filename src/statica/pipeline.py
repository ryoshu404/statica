from pathlib import Path
from statica.report import ReportBuilder
from statica.extractors.hash_extractor import HashExtractor
from statica.extractors.string_extractor import StringExtractor
from statica.extractors.ioc_extractor import IOCExtractor

class StaticAnalysisPipeline:

    def __init__(self, min_string_len: int = 6):
        self.hash_extractor = HashExtractor()

        # String search that respects length given by user
        self.string_extractor = StringExtractor(min_len=min_string_len)

        # IOC detection uses a lower fixed threshold so domains/URLs/files are not missed
        self.ioc_candidates_extractor = StringExtractor(min_len=4)
        self.ioc_extractor = IOCExtractor()

    def run(self, filepath: Path, VERSION) -> dict:

        with open(filepath, 'rb') as f:

            content = f.read()
            hashes = self.hash_extractor.extract(content)
            strings = self.string_extractor.extract(content)
            ioc_strings = self.ioc_candidates_extractor.extract(content)
            iocs = self.ioc_extractor.extract(ioc_strings)
            features = {
                "hashes": hashes,
                "iocs": iocs,
                "strings": strings
                }
            report_builder = ReportBuilder()
            report = report_builder.build(filepath, features, VERSION)

            return report

        
