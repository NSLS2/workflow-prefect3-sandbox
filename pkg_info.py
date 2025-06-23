from __future__ import annotations

import os
import time
from importlib.metadata import distributions

for dist in distributions():
    print(  # noqa: T201
        f"{dist.metadata['Name']} {dist.version}: {time.ctime(os.path.getctime(dist._path))}"  # noqa: PTH205
    )
