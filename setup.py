#!/usr/bin/env python3
"""
Setup script for VCF Contact Merger.

This setup script allows for easy installation and distribution of the
VCF contact merger utility.
"""

import os
import sys
from setuptools import setup

# Ensure we're using Python 3.6 or later
if sys.version_info < (3, 6):
    sys.exit('Python 3.6 or later is required.')

# Read the contents of README file (if it exists)
def read_long_description():
    """Read the long description from README file."""
    here = os.path.abspath(os.path.dirname(__file__))
    readme_path = os.path.join(here, 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return """
A Python utility to merge and deduplicate VCF (vCard) contact files.

This tool intelligently combines multiple VCF files, removes duplicates based on
normalized names, phone numbers, and email addresses, and outputs a clean,
merged contact file.

Features:
- Smart duplicate detection
- Preserves all contact information
- Handles quoted-printable encoding
- Command-line interface
- Robust error handling
"""

# Read version from __init__.py
def get_version():
    """Extract version from __init__.py."""
    here = os.path.abspath(os.path.dirname(__file__))
    version_file = os.path.join(here, '__init__.py')

    if os.path.exists(version_file):
        with open(version_file, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('__version__'):
                    return line.split('=')[1].strip().strip('"').strip("'")

    # Fallback version
    return '1.0.0'

setup(
    # Basic package information
    name='vcf-contact-merger',
    version=get_version(),
    author='Faisal Ahmed Moshiur',
    author_email='19180457+fam007e@users.noreply.github.com',
    description='A utility to merge and deduplicate VCF contact files',
    long_description=read_long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/fam007e/VCFmerger',
    project_urls={
        'Bug Reports': 'https://github.com/fam007e/VCFmerger/issues',
        'Source': 'https://github.com/fam007e/VCFmerger',
        'Documentation': 'https://github.com/fam007e/VCFmerger/blob/main/README.md',
    },

    # For flat structure - use py_modules instead of packages
    py_modules=['merge_script'],

    # Requirements
    python_requires='>=3.6',
    install_requires=[
        # No external dependencies - uses only standard library
    ],

    # Optional dependencies
    extras_require={
        'dev': [
            'pylint>=2.0.0',
            'black>=20.0.0',
            'pytest>=6.0.0',
            'pytest-cov>=2.0.0',
            'mypy>=0.800',
        ],
        'test': [
            'pytest>=6.0.0',
            'pytest-cov>=2.0.0',
        ],
    },

    # Entry points for command-line usage
    entry_points={
        'console_scripts': [
            'vcf-merge=merge_script:main',
            'vcf-merger=merge_script:main',
        ],
    },

    # Package metadata
    classifiers=[
        # Development Status
        'Development Status :: 5 - Production/Stable',

        # Intended Audience
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',

        # Topic
        'Topic :: Communications :: Email :: Address Book',
        'Topic :: Utilities',
        'Topic :: System :: Archiving :: Backup',

        # License (using SPDX identifier is preferred)
        'License :: OSI Approved :: MIT License',

        # Python versions
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',

        # Operating Systems
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',

        # Environment
        'Environment :: Console',
    ],

    # Keywords for package discovery
    keywords='vcf vcard contacts merge deduplicate backup phonebook addressbook',

    # Include additional files
    include_package_data=True,
    package_data={
        '': ['*.md', '*.txt', '*.rst'],
    },

    # Zip safety
    zip_safe=True,

    # Additional metadata
    platforms=['any'],
    license='MIT',
)
