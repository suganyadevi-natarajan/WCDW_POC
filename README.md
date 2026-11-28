# WCDW_POC
POC for implementing GITHUB in WCDW project

## CI/CD flow

```mermaid
flowchart TD
    DEV["Developer<br/>Databricks Git folder WCDW_POC<br/>branch: feature-bal-fund"]
    GH["GitHub repo<br/>suganyadevi-natarajan/WCDW_POC"]
    TRIG{"Trigger<br/>push to feature-bal-fund<br/>or manual run"}

    DEV -- "commit & push" --> GH --> TRIG

    TRIG --> PR["auto-pr-to-branch1.yml<br/>Open PR feature-bal-fund → branch1<br/>(skip if already open)"]

    TRIG --> CI
    subgraph CI["CI: package-and-deploy.yml"]
        C1["Checkout full history"] --> C2["git diff previous → latest commit"]
        C2 --> C3["Build DELTA package<br/>files/ · deleted.txt · manifest.txt"]
        C3 --> C4["Upload artifact<br/>delta-package-&lt;sha&gt;"]
    end

    C4 --> SIT
    subgraph CD["CD: deploy-package.yml (reusable, same package each stage)"]
        SIT["SIT<br/>Host: hardcoded (same workspace)<br/>Path: WCDW_POC/SIT"]
        UAT["UAT<br/>Host & path: env vars<br/>Approval: optional"]
        PROD["PROD<br/>Host & path: env vars<br/>Approval: required reviewers"]
        SIT -- "success" --> UAT -- "success" --> PROD
    end

    SP["Service principal OAuth<br/>DATABRICKS_CLIENT_ID / SECRET<br/>(GitHub secrets)"] -.-> CD
```

Each deploy stage: set environment details → download package → install Databricks CLI → import changed files (overwrite) → delete removed files.

### Bundle targets (`databricks.yml`)

| Target | Mode | Deploy location |
| --- | --- | --- |
| dev | development | `~/.bundle/wcdw_poc/dev` |
| sit | production | `WCDW_POC/SIT` (same workspace as dev) |
| uat | production | `~/.bundle/wcdw_poc/uat` |
| prod | production | `~/.bundle/wcdw_poc/prod` |
