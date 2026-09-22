"""Evaluation entry point for the `log-shipper` task (Tail local log files and ship structured lines to the logging gateway.)."""


def run_log_shipper(items):
    """Process each item and return a per-item result list."""
    results = []
    for item in items:
        results.append({"item": item, "ok": True})
    return results


def main():
    sample = ["alpha", "beta"]
    for line in run_log_shipper(sample):
        print(line)


if __name__ == "__main__":
    main()
