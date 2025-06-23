from __future__ import annotations

import time as ttime

from prefect import flow, get_run_logger, task
from tiled.client import from_profile


@task(retries=2, retry_delay_seconds=10)
def read_all_streams(uid, beamline_acronym):
    logger = get_run_logger()
    tiled_client = from_profile("nsls2")
    run = tiled_client[beamline_acronym]["raw"][uid]
    logger.info("Validating uid %s", run.start["uid"])
    start_time = ttime.monotonic()
    for stream in run:
        logger.info("%s:", stream)
        stream_start_time = ttime.monotonic()
        stream_data = run[stream].read()
        stream_elapsed_time = ttime.monotonic() - stream_start_time
        logger.info("%s elapsed_time = %s", stream, stream_elapsed_time)
        logger.info("%s nbytes = %s", stream, stream_data.nbytes)
    elapsed_time = ttime.monotonic() - start_time
    logger.info("%s", elapsed_time)


@flow
def general_data_validation(uid):
    read_all_streams(uid, beamline_acronym="fmx")
