# JobRunner Example – Commodity Market Analysis  
(CFTC × Charts × Documents)

This folder contains a simplified public example of my JobRunner workflow,
which supports the analytical pipeline described in my Notion portfolio.

In actual operation, the workflow is significantly more complex and is used not only for
routine market observation (e.g., weekly commodity monitoring),
but also for industry structure analysis, regional industry research,
and long-term structural studies.

This example is intentionally reduced in scope
to improve readability and reproducibility.

The same JobRunner concept is applied across different analytical domains,
bridging short-term market observation and long-term industry analysis.

The goal is to demonstrate:

- how multi-step analysis can be structured
- how manual and automated steps coexist
- how outputs (charts, CFTC data, documents) are reproducibly generated

In this JobRunner design, **text files are treated as human-readable manuals**,
clarifying intent and analytical context,
while **batch files are used for machine-executable automation**,
ensuring repeatability and operational consistency.

---

## Workflow Overview

1. Access charting sites (manual / semi-automated)
2. Download chart images (illustrative samples inspired by TradingView)
3. Download CFTC data
4. Unpack and extract required futures data
5. Generate CFTC position charts
6. Insert charts into report templates
7. Draft article text
8. Perform AI-based text correction

Each step is executed via **numbered batch files**, ensuring reproducibility.

---

## Directory Structure

- `assets/`  
  Raw input data (charts, CFTC zip files)

- `common/`  
  Shared Python utilities (data unpacking, chart drawing)

- `Thursday/`  
  Energy (Crude Oil) specific workflow

- `Tuesday/`  
  Agriculture (Wheat) specific workflow

- `*.bat / *.txt`  
  Step-by-step JobRunner execution files

---

## Disclaimer

This repository is provided for **educational and portfolio demonstration purposes only**.
