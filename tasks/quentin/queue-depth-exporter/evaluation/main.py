"""Evaluation entry point for the `queue-depth-exporter` task (Export queue depth per topic as a time series that the on-call dashboard can ingest.)."""


def run_queue_depth_exporter(items):
    """Process each item and return a per-item result list."""
    results = []
    for item in items:
        results.append({"item": item, "ok": True})
    return results


def main():
    sample = ["alpha", "beta"]
    for line in run_queue_depth_exporter(sample):
        print(line)


if __name__ == "__main__":
    main()
