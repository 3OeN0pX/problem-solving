import json
from pathlib import Path
from solution import Solution

def run_case(line: str):
    nums = json.loads(line)
    return Solution().getConcatenation(nums)

if __name__ == "__main__":
    input_path = Path(__file__).with_name("input.txt")
    for raw in input_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        print(run_case(line))