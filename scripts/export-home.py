"""Build the home-branch unsigned widget: public fonts, own package identity.

The tracked manifest keeps upstream's identity (scripts/check.py guards it);
only the generated archive carries the home identity, via the same override
the signed packaging path uses. Signing happens later with the Tizen CLI.
"""
from pathlib import Path
import sys

from font_assets import ROOT, write_widget_archive

IDENTITY = {'package_id': 'IPartHome1', 'app_id': 'IPartHome1.CleanFrame'}

output = Path(sys.argv[1]).absolute() if len(sys.argv) > 1 else ROOT / 'dist/CleanFrame-home-unsigned.wgt'
output.parent.mkdir(parents=True, exist_ok=True)
write_widget_archive(output, include_private=False, identity=IDENTITY)
print('Created ' + str(output) + ' as ' + IDENTITY['app_id'] + ' (unsigned, public fonts)')
