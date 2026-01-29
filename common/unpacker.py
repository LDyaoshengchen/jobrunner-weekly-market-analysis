# unpacker.py (simplified, year-specific)
from pathlib import Path
from zipfile import ZipFile
import shutil

# === Configuration (educational example) ===
ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"
TARGET_YEAR = "2025"

PREFIXES = [
    "fut_disagg_txt",
    "fut_fin_txt",
]

def find_zip(prefix: str) -> Path | None:
    """
    Find a ZIP file like:
    fut_disagg_txt_2025.zip
    """
    candidates = list(ASSETS_DIR.glob(f"{prefix}_{TARGET_YEAR}.zip"))
    return candidates[0] if candidates else None

def extract_txt_from_zip(zip_path: Path, output_dir: Path) -> Path:
    """
    Extract the first .txt file from a CFTC ZIP archive.
    """
    with ZipFile(zip_path) as zf:
        txt_files = [
            name for name in zf.namelist()
            if name.lower().endswith(".txt") and not name.endswith("/")
        ]

        if not txt_files:
            raise FileNotFoundError(f"No txt file found in {zip_path.name}")

        member = txt_files[0]
        out_path = output_dir / Path(member).name

        with zf.open(member) as src, open(out_path, "wb") as dst:
            shutil.copyfileobj(src, dst)

        return out_path

def convert_txt_to_csv(txt_path: Path) -> Path:
    """
    Rename .txt file to .csv (no content modification).
    """
    csv_path = txt_path.with_suffix(".csv")
    if csv_path.exists():
        csv_path.unlink()
    txt_path.rename(csv_path)
    return csv_path

def main():
    for prefix in PREFIXES:
        zip_path = find_zip(prefix)

        if not zip_path:
            print(f"[SKIP] {prefix}_{TARGET_YEAR}.zip not found")
            continue

        print(f"[ZIP] Processing {zip_path.name}")
        txt_path = extract_txt_from_zip(zip_path, ASSETS_DIR)
        csv_path = convert_txt_to_csv(txt_path)
        print(f"[DONE] {csv_path.name}")

if __name__ == "__main__":
    main()
