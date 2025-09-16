"""Example Script to show Package uage for Plotting some Probability Distributions

References:
    - ...
"""

import argparse
import logging


module_logger = logging.getLogger(__name__)


if __name__ == "__main__":
    cli_parser_obj = argparse.ArgumentParser(
        description="Example Script using Package Code for Plotting a Probability Distribution",  # noqa: E501
    )

    cli_parser_obj.add_argument(
        "-s",
        "--seed",
        type=int,
        default=2025,
        help=(
            "Seed value for `numpy` to make sure the random sampling is consistent"
            " between subsequent runs of this script, so that the plotting and other"
            " functionailties can be debugged and updated without getting confused by"
            " highly variable random sampling."
        ),
    )

    cli_parser_obj.add_argument(
        "-l",
        "--logging_level",
        type=logging.getLevelName,
        default=logging.INFO,
        help="Python Logging Level.",
    )

    cli_args = cli_parser_obj.parse_args()

    logging.basicConfig(
        level=cli_args.logging_level,
        handlers=[
            logging.StreamHandler(),  # stdout
        ],
    )

    module_logger.info("🚀 Start script...")

    debug_msg: str = f"🩻 CLI arguments: {cli_args}"
    module_logger.debug(debug_msg)

    # TOOD

    module_logger.info("🏁 Finished!")
