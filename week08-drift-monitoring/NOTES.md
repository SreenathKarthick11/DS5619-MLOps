# NOTES.md — Week 8: Drift and Observability Monitoring

**Student ID used with `generate_for_student.py`:**
<!-- paste the --student-id value you used -->
```
student_id: 112301042
seed: 2212745448
```

## Drift level vs. expectation

<!-- What drift level did the report show, and does that match what you'd
     expect given the two cameras were built with deliberately different
     visual statistics? -->
The report shows **moderate drift** with a PSI of **0.1189**. This is expected because the two cameras have different visual conditions, causing their confidence-score distributions to differ. PSI between 0.1 and 0.25 is classified as moderate drift.

Check the drift_report.json : [Here](drift_report.json)


## What confidence-score-only monitoring misses

<!-- What would you monitor IN ADDITION to confidence score if you had
     access to ground-truth labels a day later? (Tie this to the kinds of
     drift from the lecture — which one does confidence-score-only
     monitoring miss?) -->
     
If ground-truth labels become available later, I would additionally monitor model performance against the actual outcomes, such as **accuracy**, **precision**, **recall**, or other relevant performance metrics.

Confidence-score monitoring is useful for detecting distribution-based drift, but it cannot determine whether the predictions are actually correct. In particular, it can miss concept drift, where the relationship between the input features and the correct output changes even though the feature distribution remains stable.

I would also monitor prediction drift by checking whether the model's outputs change significantly, and KPI degradation to see whether the model's real-world/business performance is getting worse.