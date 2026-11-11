"""Evaluation entry point for the `sql-formatter` task (Reformat SQL files with the house style and warn about unqualified column names.)."""


def run_sql_formatter(items):
    """Process each item and return a per-item result list."""
    results = []
    for item in items:
        results.append({"item": item, "ok": True})
    return results


def main():
    sample = ["alpha", "beta"]
    for line in run_sql_formatter(sample):
        print(line)


if __name__ == "__main__":
    main()
