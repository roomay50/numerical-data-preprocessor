# Numerical Data Preprocessor

A lightweight application for automating the preprocessing of numerical CSV datasets for machine learning workflows.

## Overview

The **Numerical Data Preprocessor** analyzes, cleans, and standardizes numerical datasets so they are ready for use in machine learning projects.

### Planned Pipeline

```text
CSV → Inspect → Clean → Detect Outliers → Scale → Export
```

## Features

* Dataset inspection
* Missing value handling
* Duplicate detection and removal
* Constant column detection
* Potential index column detection
* IQR-based outlier detection
* Feature standardization with `StandardScaler`
* Processed CSV export
* Preprocessing report

## Tech Stack

* **C** — Application interface and control
* **Python** — Data preprocessing engine
* **pandas** — Data manipulation
* **NumPy** — Numerical operations
* **scikit-learn** — Data preprocessing and scaling

## Project Structure

```text
numerical-data-preprocessor/
├── c_app/
├── python_engine/
├── data/
├── reports/
├── tests/
├── README.md
└── requirements.txt
```

## Status

🚧 **In Development**

The current focus is building the **Python Dataset Inspector**, which will be the first component of the preprocessing engine.

## License

This project is licensed under the **MIT License**. See the [`LICENSE`](LICENSE) file for details.
