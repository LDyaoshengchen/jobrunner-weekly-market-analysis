\# common/

Shared Python utilities used across multiple workflows.



## Files

- `unpacker.py`  
  Extracts futures-only CFTC data for selected commodities.

- `draw_cftc_graph.py`  
  Generates net position charts from extracted CFTC data.

- `access_site.py`  
  Opens the CFTC download page (shared by Tuesday/Thursday routines).

These scripts are intentionally **simplified versions**
of production tools, focusing on clarity and reproducibility.