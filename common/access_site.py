import sys
import webbrowser
from pathlib import Path

def open_in_chrome(url: str):
    chrome_paths = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]

    for p in chrome_paths:
        try:
            webbrowser.register(
                "chrome",
                None,
                webbrowser.BackgroundBrowser(p),
            )
            webbrowser.get("chrome").open(url)
            return
        except Exception:
            continue

    # Chrome が見つからない場合はデフォルトブラウザ
    webbrowser.open(url)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("URL が指定されていません。")
        sys.exit(1)

    url = sys.argv[1]
    print(f"[INFO] Open URL: {url}")
    open_in_chrome(url)
