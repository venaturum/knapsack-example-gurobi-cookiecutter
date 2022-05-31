import argparse
from pathlib import Path

# def file(path):
#     if path is not None:
#         if Path(path).is_file():
#             return path
#         raise OSError(f"Could not find file: {path}.")

# def directory(path):
#     if path is not None:
#         if Path(path).is_dir():
#             return path
#         raise OSError(f"Could not find directory: {path}.")


def main():
    """Console script for knapsack."""
    parser = argparse.ArgumentParser(description="CLI for knapsack")

    # parser.add_argument("-f", "--file", type=file, default=None, help="description for file option")
    # parser.add_argument("-d", "--directory", type=directory, default=None, help="description for directory option")
    # parser.add_argument("-t", "--thirdoption", type=int, choices=[1,2,3], required=True, help="description for second option")
    
    # group_priority = parser.add_mutually_exclusive_group(required=True)
    # group_priority.add_argument("--low", action="store_true", help="run with low priority")
    # group_priority.add_argument("--med", action="store_true", help="run with medium priority")
    # group_priority.add_argument("--high", action="store_true", help="run with high priority")

    parser.parse_args
