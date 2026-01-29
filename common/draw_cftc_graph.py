# draw_cftc_graph.py
# Simplified CFTC net position chart example
# (Crude Oil & Wheat, futures-only, single-year dataset)

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# =====================================
# Configuration (educational example)
# =====================================
ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"

TARGET_MARKETS = {
    "WTI-PHYSICAL - NEW YORK MERCANTILE EXCHANGE": "Crude_Oil",
    "WHEAT-SRW - CHICAGO BOARD OF TRADE": "Wheat",
}

# =====================================
# Helper functions
# =====================================
def get_column(df: pd.DataFrame, candidates):
    """
    Return the first existing column name from candidates.
    """
    for c in candidates:
        if c in df.columns:
            return c
    raise KeyError(f"None of the columns found: {candidates}")


def draw_net_position(df: pd.DataFrame, market_name: str, short_name: str):
    """
    Draw and save net position chart for a single commodity.
    """
    prod_df = df[df["Market_and_Exchange_Names"] == market_name].copy()
    if prod_df.empty:
        print(f"[SKIP] {short_name}: market not found")
        return

    # Date column
    date_col = get_column(df, [
        "Report_Date_as_YYYY-MM-DD",
        "Report_Date_as_YYYY_MM_DD",
        "Report_Date",
    ])
    prod_df["Date"] = pd.to_datetime(prod_df[date_col], errors="coerce")
    prod_df = prod_df.sort_values("Date")

    # Managed Money columns (futures-only)
    mm_long_col = get_column(df, [
        "M_Money_Positions_Long_All",
        "Managed_Money_Long_All",
        "Money_Manager_Long_All",
    ])
    mm_short_col = get_column(df, [
        "M_Money_Positions_Short_All",
        "Managed_Money_Short_All",
        "Money_Manager_Short_All",
    ])

    # Net position
    prod_df["Net_Position"] = prod_df[mm_long_col] - prod_df[mm_short_col]

    # Plot
    plt.figure(figsize=(12, 5))
    plt.plot(prod_df["Date"], prod_df["Net_Position"])
    plt.axhline(0, linestyle="--", linewidth=1)
    plt.title(f"CFTC Net Position – {short_name}")
    plt.grid(True)
    plt.tight_layout()

    out_file = ASSETS_DIR / f"cftc_net_position_{short_name}.png"
    plt.savefig(out_file, dpi=150)
    plt.close()

    print(f"[DONE] {out_file.name}")


# =====================================
# Main
# =====================================
def main():
    csv_files = list(ASSETS_DIR.glob("*.csv"))
    if not csv_files:
        print("[ERROR] No CSV files found in assets/")
        return

    # Read all CSVs (single-year dataset assumed)
    df = pd.concat(
        [pd.read_csv(f, low_memory=False) for f in csv_files],
        ignore_index=True,
    )

    for market_name, short_name in TARGET_MARKETS.items():
        draw_net_position(df, market_name, short_name)


if __name__ == "__main__":
    main()
