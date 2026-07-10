# WorkingWPythonAria

Exploratory scripts and notebooks for driving Varian ARIA / Eclipse from Python
through [PyESAPI](https://github.com/brianmanderson/PyESAPI). They open a patient by
MRN, pull the CT image and structure sets out of the treatment planning system, and
convert Varian image/mask objects into SimpleITK images (matching spacing, direction,
and origin) for downstream Python processing.

One-off exploratory work, not a maintained package.

## Contents

- `Main.py` — minimal example: connect to ARIA, open a patient, and convert the plan's
  structure-set image to a SimpleITK image (optionally written to NIfTI).
- `TestWorkAriaToPython.ipynb` — helper functions for converting Varian images and
  masks to SimpleITK.
- `IdentifyRing.ipynb` — experiments identifying ring structures on a patient.
- `PTV_3mm.ipynb` — creating a 3 mm PTV expansion via structure modification.
- `DataMining.ipynb` — iterating over patient summaries and extracting dose metrics
  (e.g. dose-at-volume) into a pandas DataFrame.

## Requirements

- A licensed Varian Eclipse / ARIA install with ESAPI available (Windows).
- [PyESAPI](https://github.com/brianmanderson/PyESAPI): `pip install git+https://github.com/brianmanderson/PyESAPI`
- SimpleITK, NumPy, pandas.

## Usage

The scripts read the target MRN from a local `PatientID` file (gitignored, not
included) rather than hard-coding patient identifiers.
