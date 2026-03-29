# Statica

Statica is a modular static analysis pipeline written in Python that performs lightweight file analysis and produces structured JSON output suitable for automation and security workflows. The goal of Statica is to provide a simple, automation-friendly static analysis tool that can be integrated into security workflows, triage pipelines, and detection tooling.

The tool extracts file hashes, printable strings, and common indicators of compromise (IOCs) such as IP addresses, URLs, domains, and suspicious file artifacts.

---

# Features

Statica currently implements the following capabilities:

- File hashing (MD5, SHA256)
- Printable ASCII string extraction
- Configurable minimum string length
- IPv4 IOC detection
- URL IOC detection
- Domain IOC detection
- Suspicious file artifact detection
- Deduplicated IOC output
- Structured JSON output
- Modular analysis pipeline
- Command-line interface

The tool is designed to be lightweight and extensible so that additional analysis stages can be added without modifying existing pipeline components.

---

# Architecture

Statica follows a simple modular pipeline architecture where each stage performs a single analysis task and passes results to the next stage.

Pipeline flow:

File (bytes)  
↓  
HashExtractor  
↓  
StringExtractor (user min length)  
↓  
StringExtractor (IOC candidate extraction)  
↓  
IOCExtractor  
↓  
ReportBuilder  
↓  
JSONFormatter  
↓  
stdout

Each extractor is responsible for a single concern:

| Component | Responsibility |
|-----------|---------------|
| HashExtractor | Computes MD5 and SHA256 file hashes |
| StringExtractor | Extracts printable ASCII strings |
| IOCExtractor | Detects indicators of compromise using regex |
| ReportBuilder | Assembles structured analysis results |
| JSONFormatter | Produces deterministic JSON output |

This separation allows new analysis stages to be added with minimal impact to existing code.

---

# Design Decisions

## Two-Pass String Extraction

Statica performs **two passes of string extraction**.

1. The first pass extracts strings using the user-provided `--minlen` value and is intended for **analyst-visible output**.
2. The second pass extracts strings using a lower fixed threshold (`min_len = 4`) used exclusively for **IOC candidate detection**.

This design ensures that shorter indicators such as domains, URLs, and file artifacts are still detected even when analysts increase the displayed string length threshold.

This separation improves detection coverage while preserving configurable analyst output.

---

## Deterministic Output

IOC results are stored internally using sets and returned as **sorted lists**.

Benefits:

- Deduplicated indicators
- Deterministic JSON output
- Easier automation and downstream processing
- Consistent results across runs

---

## Modular Extractor Architecture

Each analysis feature is implemented as a separate extractor module.

Advantages:

- Clear separation of responsibilities
- Easier testing
- Straightforward extensibility
- Maintainable codebase

Future extractors (file metadata, entropy analysis, PE parsing, etc.) can be added without modifying existing components.

---

# Repository Structure
```
statica/
├── src/
│   └── statica/
│       ├── cli.py
│       ├── pipeline.py
│       ├── report.py
│       ├── extractors/
│       │   ├── hash_extractor.py
│       │   ├── string_extractor.py
│       │   └── ioc_extractor.py
│       └── formatters/
│           └── json_formatter.py
├── samples/
│   └── test_iocs.txt
├── tests/
├── README.md
└── pyproject.toml
```

---

# Installation

Requires Python 3.11+

Clone the repository:
```bash
git clone https://github.com/ryoshu404/statica.git  
cd statica
```
Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate
```
Install the project in editable mode:
```bash
pip install -e .
```
Verify the installation:
```bash
statica --version
```
---

# Usage

Run Statica against a file:
```bash
statica samples/test_iocs.txt
```
Specify a minimum string length:
```bash
statica samples/test_iocs.txt --minlen 8
```
View available options:
```bash
statica --help
```
Check installed version:
```bash
statica --version
```
---

# Example Output

Example JSON output produced by Statica:

```json
{
  "tool": {
    "name": "statica",
    "version": "1.0.0"
  },
  "input": {
    "path": "samples/test_iocs.txt"
  },
  "hashes": {
    "md5": "c1a5c0f5a3b9f23f...",
    "sha256": "ab84e9b8d3b8d..."
  },
  "iocs": {
    "ipv4": [
      "192.168.1.1"
    ],
    "urls": [
      "http://example.com"
    ],
    "domains": [
      "malicious-domain.com"
    ],
    "files": [
      "payload.exe"
    ]
  },
  "strings": [
    "example string",
    "another extracted string"
  ],
  "errors": []
}
```


---

# Sample Test File

A sample IOC test file is included:

samples/test_iocs.txt

This file contains various indicators used to validate the extraction pipeline.

---

# Roadmap

Potential future improvements include:

- Additional IOC types
- File metadata extraction
- Entropy analysis
- Additional output formats
- Threat intelligence enrichment
- Integration with IOC correlation services

---

# Related Projects

This project is part of a larger security tooling portfolio.

### [macollect](https://github.com/ryoshu404/macollect) (v1.0)
Modular macOS forensic artifact collector written in Python. Collects persistence mechanisms, process snapshots, code signing metadata, TCC permissions, and Unified Log activity across eight independent collection modules.

### IOC Correlation Service (planned)
Threat intelligence correlation service written in Go. Future enrichment integration layer for both Statica and macollect output.

### Swift ESF Telemetry Tool (planned)
Real-time kernel event streaming companion to macollect using Apple's Endpoint Security Framework.


---

# Author

R. Santos  
GitHub: https://github.com/ryoshu404

---

# License

MIT
