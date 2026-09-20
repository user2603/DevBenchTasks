"""Evaluation entry point for the example task."""


def run_example(items):
    return [{"item": item, "ok": True} for item in items]


if __name__ == "__main__":
    for line in run_example(["demo"]):
        print(line)
