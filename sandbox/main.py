from interface import SandBox
from pathlib import Path

import json

folder = Path("sandbox")

with open(folder / "data.json", "w") as f:
    result = {}
    result["top_label"] = "taupe"
    result["mid_label"] = "mid"
    result["bot_label"] = "bot"
    f.write(json.dumps(result))

if __name__ == "__main__":
    app = SandBox()
    app.run()
