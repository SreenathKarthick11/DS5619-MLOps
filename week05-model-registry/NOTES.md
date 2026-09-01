# NOTES.md — Week 5: Model Registry Governance

**Student ID used with `generate_for_student.py`:**

student_id: 112301042
seed: 2217275315
candidate_a: f1=0.518 (below 0.70 bar)
candidate_b: f1=0.932 (clears 0.70 bar)

## Which candidate reached Production, and why?

The `candidate b` which was registered as `v2` reached production as , it had a f1 score (0.932) , which is greater than required production limit of 0.7.
Hence it was promoted to the production.


## Gating stale feature data

<!-- What would you need to add to promote_model's gate if you also wanted
     to block promotion of a model trained on stale (e.g. >30-day-old)
     feature data? -->
We could have date on trained on key, which currently stores the feature store it used to train. By having a specify parameter like trainind date . which help us to block promoting models trained on stale data.


## Scaling the gate to 40 candidates

<!-- Tying back to this week's AutoML/HPO framing: if a hyperparameter
     search had handed you 40 candidates instead of 2, what in your
     register_model/promote_model design would need to change (or
     genuinely wouldn't) to gate 40 instead of 2? -->
