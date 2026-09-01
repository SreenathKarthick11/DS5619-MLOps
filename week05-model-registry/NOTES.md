# NOTES.md — Week 5: Model Registry Governance

**Student ID used with `generate_for_student.py`:**

student_id: 112301042
seed: 2217275315

```bash
candidate_a: f1=0.518 (below 0.70 bar)
candidate_b: f1=0.932 (clears 0.70 bar)
```

## Which candidate reached Production, and why?


**Candidate B (`v2`)** reached Production because it achieved an **F1 score of 0.932**, which is higher than the Production threshold of **0.70**. It also needed to satisfy the model-card requirement before promotion. Therefore, it passed the governance gate and was promoted to Production.

## Gating stale feature data

<!-- What would you need to add to promote_model's gate if you also wanted
     to block promotion of a model trained on stale (e.g. >30-day-old)
     feature data? -->

We could add a **training date/timestamp** to the model's manifest. During promotion, `promote_model` can compare the training date with the current date. If the model was trained using feature data older than **30 days**, the promotion should be rejected with a `GovernanceError`. This makes stale data an enforced governance rule rather than just a documented requirement.

## Scaling the gate to 40 candidates

<!-- Tying back to this week's AutoML/HPO framing: if a hyperparameter
     search had handed you 40 candidates instead of 2, what in your
     register_model/promote_model design would need to change (or
     genuinely wouldn't) to gate 40 instead of 2? -->

The current design does not need major changes if the number of candidates increases from 2 to 40.`register_model()` already creates a separate version for each registered model, so all 40 candidates can be stored as different versions.`promote_model()` applies the same governance checks to each version independently.

The main change would be in the pipeline or selection process: instead of manually checking two candidates, it would need to evaluate all candidates and decide which one should be promoted.

The registry itself can therefore handle many candidates without needing a separate implementation for each one.
