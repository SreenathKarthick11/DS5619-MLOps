# CI verification

Fill this in after you push and watch the workflow run on GitHub (Actions
tab of your repo). This is how we confirm your CI actually ran green in a
real GitHub Actions runner, not just locally.

## Workflow run

Paste the URL of a successful run of all three jobs (Actions tab -> click
the run -> copy the URL):

```
URL = https://github.com/SreenathKarthick11/DS5619-MLOps/actions/runs/35709636360
```

## Job summary

For each job, note pass/fail and how long it took:

- `lint`: pass  - 10 s
- `unit-test`: pass  - 9 s
- `integration-test`: pass - 20 s

Total Time taken is 47 sec.

## What broke on the way there (optional but useful)

If any job failed before you got it working, briefly note what the failure
was and what fixed it. (Not required, but if `integration-test` gave you
trouble, this is worth 2 sentences for your own future reference — Week 9's
lab also builds on debugging CI-style failures.)

**ANSWER**:
I didn't face any issue, when running the workflow. But its good was to
the feature of `working directory` in yml.