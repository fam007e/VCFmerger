"""
VCF Contact Merger Package.

A Python utility to merge and deduplicate VCF (vCard) contact files.
"""

__version__ = '1.0.0'
__author__ = 'Faisal Ahmed Moshiur'
__email__ = '19180457+fam007e@users.noreply.github.com'
__license__ = 'MIT'

# Import main components from merge_script module
try:
    from merge_script import VCFMerger, main
    __all__ = ['VCFMerger', 'main']
except ImportError:
    # Handle case where merge_script might not be available yet
    __all__ = []
