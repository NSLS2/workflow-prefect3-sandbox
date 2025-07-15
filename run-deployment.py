from __future__ import annotations

from prefect.deployments import run_deployment

run_deployment(
    name="end-of-run-workflow/test-workflow-prefect3-sandbox-deploy",
    # name="end-of-run-workflow/end_of_run_workflow_deployment",
    parameters={"stop_doc": {"run_start": "47c21f4d"}},
    timeout=15,  # don't wait for the run to finish # edit to 15 sec
)
