from pathlib import Path

ENTRY = "Your twelve-word wallet seed dies with me tonight. I never backed it up. Neither did you."

def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
