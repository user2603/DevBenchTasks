# log-shipper

Tail local log files and ship structured lines to the logging gateway.

## Goal

Build a small, self-contained helper that can be run from the command line.

## Input

- One or more items to process, passed as file paths or short strings.

## Output

- A short report printed to stdout describing what was checked and the result.

## Notes

- The helper must run with Python 3.10+ and must not require network access.
- Keep the implementation under 200 lines; no external dependencies.
