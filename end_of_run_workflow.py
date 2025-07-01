from __future__ import annotations

import sys
from time import sleep

from prefect import flow, get_run_logger, task
from tiled.client import from_uri

from data_validation import general_data_validation


@task
def log_completion():
    logger = get_run_logger()
    logger.info("Complete")


@flow
def end_of_run_workflow(stop_doc):
    logger = get_run_logger()
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
    print("end of run workflow")  # noqa: T201
    args = sys.argv
    print(f"{len(args)}, {args}")  # noqa: T201
    end_of_run_workflow({"stop_doc": args[1]})
    #    import tiled
    sleep(100)
    print("after sleep")  # noqa: T201
