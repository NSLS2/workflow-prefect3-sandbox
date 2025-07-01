from __future__ import annotations

import sys
from time import sleep

from prefect import flow, get_run_logger, task
from tiled.client import from_uri

from data_validation import general_data_validation

logger = get_run_logger()


@task
def log_completion():
    logger.info("Complete")


@flow
def end_of_run_workflow(stop_doc):
    # tiled_client = from_profile("nsls2")
    tiled_client = from_uri("https://tiled-demo.blueskyproject.io")
    logger.info("testing, adding something new to the end_of_run_workflow")
    logger.info(f"stop doc: {stop_doc}")
    uid = stop_doc["run_start"]
    logger.info(f"tiled info: {tiled_client['fxi']['raw'][uid]}")
    return
    general_data_validation(uid)
    # export(uid)
    log_completion()


if __name__ == "__main__":
    # below is a proof of concept that a deployment can be made from inside a running program
    # end_of_run_workflow.deploy(
    #    name="end_of_run_workflow_deployment",
    #    work_pool_name="pixi-container-tests1",
    #    parameters={"stop_doc": {}},
    #    image="ghcr.io/junaishima/pixi-container-tests:main",
    #    build=False,
    # )
    logger.info("end of run workflow")
    args = sys.argv
    logger.info(f"{len(args)}, {args}")
    end_of_run_workflow({"stop_doc": args[1]})
    #    import tiled
    sleep(100)
    logger.info("after sleep")
