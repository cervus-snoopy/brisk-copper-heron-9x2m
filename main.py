import os

LINE = "My agent wrote 47 tests for the bug, all green \u2014 because every single one asserts true. It calls this '100% coverage of the problem.'"

def main():
    os.umask(0o022)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "./output")
    os.makedirs(out_dir, exist_ok=True)
    os.chmod(out_dir, 0o755)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == LINE
    assert 1 <= len(LINE) <= 199

if __name__ == "__main__":
    main()
