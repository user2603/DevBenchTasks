"""Evaluation entry point for the `grpc-mock-server` task (Serve canned gRPC responses so client teams can test without the live backend.)."""


def run_grpc_mock_server(items):
    """Process each item and return a per-item result list."""
    results = []
    for item in items:
        results.append({"item": item, "ok": True})
    return results


def main():
    sample = ["alpha", "beta"]
    for line in run_grpc_mock_server(sample):
        print(line)


if __name__ == "__main__":
    main()
