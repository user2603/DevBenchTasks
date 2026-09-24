"""Evaluation entry point for the `migration-linter` task (Detect dangerous SQL migrations such as unindexed drops and full-table rewrites.)."""


def run_migration_linter(items):
    """Process each item and return a per-item result list."""
    results = []
    for item in items:
        results.append({"item": item, "ok": True})
    return results


def main():
    sample = ["alpha", "beta"]
    for line in run_migration_linter(sample):
        print(line)


if __name__ == "__main__":
    main()
