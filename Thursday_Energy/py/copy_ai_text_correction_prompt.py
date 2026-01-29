import yaml
from pathlib import Path
import pyperclip

# =========================================
# パス解決
# =========================================

CURRENT_FILE = Path(__file__).resolve()
ROOT_DIR = CURRENT_FILE.parents[2]
CONFIG_PATH = ROOT_DIR / "config" / "thursday.yaml"

# =========================================
# YAML 読み込み
# =========================================

with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

guidelines = config.get("ai_review_guidelines_JP")

if not guidelines:
    raise ValueError("ai_review_guidelines_JP が YAML に定義されていません")

purpose = guidelines.get("purpose", "").strip()
points = guidelines.get("points", [])

if not points:
    raise ValueError("points が YAML に定義されていません")

# =========================================
# プロンプト生成
# =========================================

prompt_lines = []
prompt_lines.append(purpose)
prompt_lines.append("")
prompt_lines.append("Please review the following draft according to these points:")

for i, p in enumerate(points, start=1):
    prompt_lines.append(f"{i}. {p}")

prompt_text = "\n".join(prompt_lines)

# =========================================
# クリップボードにコピー
# =========================================

pyperclip.copy(prompt_text)

print("プロンプトをクリップボードにコピーしました:")
print(prompt_text)
