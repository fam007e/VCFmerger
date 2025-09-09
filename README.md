# VCF Contact Merger

A powerful Python utility to merge and deduplicate VCF (vCard) contact files with intelligent duplicate detection and property merging.

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Quality](https://img.shields.io/badge/pylint-10/10-brightgreen.svg)](https://pylint.org)

## Features

- **Smart Duplicate Detection**: Identifies duplicates based on normalized names, phone numbers, and email addresses
- **Intelligent Property Merging**: Combines contact information from multiple sources while preserving all data
- **Robust File Handling**: Supports various VCF formats and handles encoding issues gracefully
- **Command-Line Interface**: Easy-to-use CLI for batch processing multiple contact files
- **Zero Dependencies**: Uses only Python standard library - no external packages required
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **High Code Quality**: Pylint score of 10/10 with comprehensive type hints and documentation

## Installation

### From Source

```bash
git clone https://github.com/fam007e/VCFmerger.git
cd VCFmerger
pip install -e .
```

### Direct Download

```bash
wget https://raw.githubusercontent.com/fam007e/VCFmerger/main/merge_script.py
python3 merge_script.py output.vcf input1.vcf input2.vcf
```

## Usage

### Command Line Interface

After installation, you can use the `vcf-merge` command:

```bash
# Basic usage
vcf-merge merged_contacts.vcf contacts1.vcf contacts2.vcf contacts3.vcf

# Merge multiple backup files
vcf-merge all_contacts.vcf backup1.vcf backup2.vcf export.vcf
```

### Direct Script Usage

```bash
python3 merge_script.py output.vcf input1.vcf input2.vcf [additional_files...]
```

### Python API

```python
from merge_script import VCFMerger

# Create merger instance
merger = VCFMerger()

# Read VCF files
with open('contacts1.vcf', 'r') as f1, open('contacts2.vcf', 'r') as f2:
    vcf_contents = [f1.read(), f2.read()]

# Merge contacts
merged_vcf = merger.merge_vcfs(vcf_contents)

# Write result
with open('merged.vcf', 'w') as output:
    output.write(merged_vcf)
```

## How It Works

### Duplicate Detection Algorithm

The merger uses a sophisticated key-based approach to identify duplicates:

1. **Name Normalization**: Converts full names (FN) and structured names (N) to lowercase
2. **Phone Number Normalization**: Strips formatting, keeping only digits and '+' prefix
3. **Email Normalization**: Converts email addresses to lowercase
4. **Composite Key**: Creates unique keys from normalized names, phone sets, and email sets

### Property Merging Strategy

- **Single-Value Properties**: Later-processed files take priority (FN, N, ORG, TITLE, etc.)
- **Multi-Value Properties**: All values are preserved and combined (TEL, EMAIL, URL, ADR)
- **Special Handling**: PHOTO properties and quoted-printable encoding are handled correctly

### Supported VCF Properties

- **Names**: FN (Full Name), N (Structured Name)
- **Contact Info**: TEL (Phone), EMAIL, URL
- **Organization**: ORG, TITLE
- **Address**: ADR (Address)
- **Media**: PHOTO (with multi-line support)
- **Metadata**: VERSION and custom properties

## Examples

### Example 1: Basic Merging

**Input files:**

`contacts1.vcf`:
```
BEGIN:VCARD
VERSION:3.0
FN:John Doe
TEL:+1234567890
EMAIL:john@example.com
END:VCARD
```

`contacts2.vcf`:
```
BEGIN:VCARD
VERSION:3.0
FN:John Doe
TEL:+1234567890
EMAIL:john.doe@work.com
ORG:Acme Corp
END:VCARD
```

**Command:**
```bash
vcf-merge merged.vcf contacts1.vcf contacts2.vcf
```

**Result:** Single contact with both email addresses and organization information.

### Example 2: Phone Number Normalization

These contacts will be detected as duplicates:
- `TEL:+1 (555) 123-4567`
- `TEL:+15551234567`
- `TEL:555.123.4567`

All normalize to `+15551234567`.

## Development

### Prerequisites

- Python 3.6 or later
- Git

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/fam007e/VCFmerger.git
cd VCFmerger

# Install in development mode with dev dependencies
pip install -e .[dev]

# Run tests
pytest

# Check code quality
pylint merge_script.py

# Format code
black merge_script.py
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=merge_script

# Run specific test
pytest test_*.py
```

### Code Quality

The project maintains high code quality standards:

```bash
# Pylint check (should score 10/10)
pylint merge_script.py

# Type checking
mypy merge_script.py

# Code formatting
black merge_script.py --check
```

## File Structure

```
VCFmerger/
├── merge_script.py          # Main merger script
├── setup.py                 # Package installation script (legacy)
├── pyproject.toml          # Modern Python project configuration
├── __init__.py             # Package initialization
├── README.md               # This file
├── LICENSE                 # MIT License
├── requirements.txt        # Runtime dependencies (empty - no deps)
├── .gitignore             # Git ignore rules
└── tests/                 # Test files (if any)
    ├── test_*.py          # Test modules
    └── sample_data/       # Test data files
        ├── contacts1.vcf
        └── contacts2.vcf
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Guidelines

1. **Code Quality**: Maintain the 10/10 pylint score
2. **Type Hints**: Add type hints for all functions and methods
3. **Documentation**: Include docstrings and update README if needed
4. **Tests**: Add tests for new functionality
5. **Compatibility**: Ensure Python 3.6+ compatibility

### Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and quality checks
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Troubleshooting

### Common Issues

**Issue**: "No valid input VCF files found"
- **Solution**: Check file paths and ensure VCF files contain valid vCard data

**Issue**: Encoding errors with special characters
- **Solution**: The script handles UTF-8 with error handling, but ensure your VCF files are properly encoded

**Issue**: Large files processing slowly
- **Solution**: The script processes files sequentially; consider splitting very large files

### Getting Help

- **Issues**: Report bugs and request features on [GitHub Issues](https://github.com/fam007e/VCFmerger/issues)
- **Discussions**: Join discussions on [GitHub Discussions](https://github.com/fam007e/VCFmerger/discussions)
- **Email**: Contact the maintainer at [19180457+fam007e@users.noreply.github.com](mailto:19180457+fam007e@users.noreply.github.com)

## Changelog

### Version 1.0.0 (Initial Release)
- Smart duplicate detection based on names, phones, and emails
- Intelligent property merging with priority handling
- Command-line interface with multiple input support
- Python API for programmatic usage
- Comprehensive error handling and logging
- Cross-platform compatibility
- Zero external dependencies
- 10/10 pylint score with full type hints

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the need to merge contact backups from multiple sources
- Built with Python's robust standard library
- Thanks to the open-source community for feedback and contributions

## Author

**Faisal Ahmed Moshiur**
- GitHub: [@fam007e](https://github.com/fam007e)
- Email: [19180457+fam007e@users.noreply.github.com](mailto:19180457+fam007e@users.noreply.github.com)

---

⭐ **Star this repository if you find it useful!** ⭐