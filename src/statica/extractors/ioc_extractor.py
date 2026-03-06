import re

class IOCExtractor:
    def __init__(self):
        self.ipv4_search = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
        self.url_search = re.compile(r"\bhttps?://[^\s\"'<>]+")
        self.common_domain_search = re.compile(r"\b(?:[a-zA-Z0-9-]+\.)+" + r"(?:" + "|".join([
            r"com", r"net", r"org", r"io", r"gov", r"edu",
            r"mil", r"co", r"uk", r"de", r"fr", r"jp",
            r"ru", r"ch", r"it", r"nl", r"se", r"no",
            r"es", r"au", r"int", r"info", r"biz"
            ]) + r")\b")
        self.common_extension_search = re.compile(r"(?:\w+\.)+" + r"(?:" + "|".join([
            r"exe", r"dll", r"bat", r"cmd", r"ps1",
            r"vbs", r"js", r"jar", r"sh", r"bin",
            r"scr", r"msi", r"hta",
            ]) + r")(?=\W|$)")
        self.patterns = {
            "ipv4": self.ipv4_search,
            "urls": self.url_search,
            "domains": self.common_domain_search,
            "files": self.common_extension_search
        }

    def extract(self, strings: list[str]) -> dict:
        ipv4 = set()
        urls = set()
        domains = set()
        files = set()
        for string in strings:
            for category, pattern in self.patterns.items():
                for result in pattern.finditer(string):
                    match category:
                        case "ipv4":
                            ipv4.add(result.group())
                        case "urls":
                            urls.add(result.group())
                        case "domains":
                            domains.add(result.group())
                        case "files":
                            files.add(result.group())
                            
        return {
            "ipv4": sorted(ipv4),
            "urls": sorted(urls),
            "domains": sorted(domains),
            "files": sorted(files)
        }
    