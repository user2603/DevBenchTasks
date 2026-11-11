"""Evaluation entry point for the `stream-joiner` task (Join two event streams on a tumbling window and emit matched pairs.)."""


def run_stream_joiner(items):
    """Process each item and return a per-item result list."""
    results = []
    for item in items:
        results.append({"item": item, "ok": True})
    return results


def main():
    sample = ["alpha", "beta"]
    for line in run_stream_joiner(sample):
        print(line)


if __name__ == "__main__":
    main()
