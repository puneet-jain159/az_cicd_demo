# az_cicd_demo

This is a sample project for Databricks, generated via cookiecutter.

While using this project, you need Python 3.X and `pip` or `conda` for package management.

## Local environment setup

1. Instantiate a local Python environment via a tool of your choice. This example is based on `conda`, but you can use any environment management tool:
```bash
conda create -n az_cicd_demo python=3.9
conda activate az_cicd_demo
```

2. If you don't have JDK installed on your local machine, install it (in this example we use `conda`-based installation):
```bash
conda install -c conda-forge openjdk
```

3. Install project in a dev mode (this will also install dev requirements):
```bash
pip install -e ".[dev]"
```

## Running unit tests

For unit testing, please use `pytest`:
```
pytest tests/unit --cov
```

Please check the directory `tests/unit` for more details on how to use unit tests.
In the `tests/unit/conftest.py` you'll also find useful testing primitives, such as local Spark instance with Delta support, local MLflow and DBUtils fixture.

## Running integration tests

There are two options for running integration tests:

- On an interactive cluster via `dbx execute`
- On a job cluster via `dbx launch`

For quicker startup of the job clusters we recommend using instance pools ([AWS](https://docs.databricks.com/clusters/instance-pools/index.html), [Azure](https://docs.microsoft.com/en-us/azure/databricks/clusters/instance-pools/), [GCP](https://docs.gcp.databricks.com/clusters/instance-pools/index.html)).

For an integration test on interactive cluster, use the following command:
```
dbx execute --cluster-name=<name of interactive cluster> --job=<name of the job to test>
```

To execute a task inside multitask job, use the following command:
```
dbx execute \
    --cluster-name=<name of interactive cluster> \
    --job=<name of the job to test> \
    --task=<task-key-from-job-definition>
```

For a test on an automated job cluster, deploy the job files and then launch:
```
dbx deploy --jobs=<name of the job to test> --files-only
dbx launch --job=<name of the job to test> --as-run-submit --trace
```

Please note that for testing we recommend using [jobless deployments](https://dbx.readthedocs.io/en/latest/guidance/run_submit.html), so you won't affect existing job definitions.

## Interactive execution and development on Databricks clusters

1. `dbx` expects that cluster for interactive execution supports `%pip` and `%conda` magic [commands](https://docs.databricks.com/libraries/notebooks-python-libraries.html).
2. Please configure your job in `conf/deployment.yml` file.
2. To execute the code interactively, provide either `--cluster-id` or `--cluster-name`.
```bash
dbx execute \
    --cluster-name="<some-cluster-name>" \
    --job=job-name
```

Multiple users also can use the same cluster for development. Libraries will be isolated per each execution context.

## Working with notebooks and Repos

To start working with your notebooks from a Repos, do the following steps:

1. Add your git provider token to your user settings in Databricks
2. Add your repository to Repos. This could be done via UI, or via CLI command below:
```bash
databricks repos create --url <your repo URL> --provider <your-provider>
```
This command will create your personal repository under `/Repos/<username>/az_cicd_demo`.
3. Use `git_source` in your job definition as described [here](https://dbx.readthedocs.io/en/latest/examples/notebook_remote.html)

## CI/CD pipeline settings

Please set the following secrets or environment variables for your CI provider:
- `DATABRICKS_HOST`
- `DATABRICKS_TOKEN`

## Testing and releasing via CI pipeline

- To trigger the CI pipeline, simply push your code to the repository. If CI provider is correctly set, it shall trigger the general testing pipeline
- To trigger the release pipeline, get the current version from the `az_cicd_demo/__init__.py` file and tag the current code version:
```
git tag -a v<your-project-version> -m "Release tag for version <your-project-version>"
git push origin --tags
```