# NOTES.md — Week 10: Fairness and Robustness Audit

**Student ID used with `generate_for_student.py`:**
<!-- paste the --student-id value you used -->
student_id: 112301042
seed: 652010098


## Which classes got flagged?

<!-- Which classes got flagged, and does that match what you'd expect given how generate_for_student.py built the fixtures? -->

**Bicycle: 62.5% (10/16)** and **Two-wheeler: 85.7% (12/14)**. This is expected because the fixtures deliberately make smaller vehicles harder to detect. Small sample sizes mean the exact recall gaps may still be noisy.


## If the grouping variable were a protected attribute

<!-- Tying back to the framing note: what would change about this audit's stakes and your obligations as an engineer if the grouping variable were a protected demographic attribute instead of a vehicle class? -->

The audit would have greater ethical and potentially legal implications. Unequal detection rates could disproportionately harm demographic groups. I would investigate causes, protect sensitive data, evaluate relevant fairness metrics, and mitigate disparities before deployment.

## Which attack could corrupt this audit?

<!-- Name one lifecycle stage and attack from the lecture (data poisoning, model theft, or adversarial examples) that could silently corrupt THIS audit's result, and one control from the lecture that would reduce the risk. -->
**Data poisoning** could alter ground-truth annotations, for example by removing difficult bicycle examples to inflate recall. Restricted dataset access, version control, and independent annotation checks would reduce this risk.

## Would SHAP or LIME explain a missed detection?

<!-- Pick one missed ground-truth box in a flagged class. An auditor asks you to explain WHY the detector missed it, not just that it did. Would SHAP or LIME actually help you answer that for a bounding-box detector — and if not, what's different about this detector's inputs/outputs that breaks the assumption both tools make? -->
Not directly without a suitable explanation setup. SHAP and LIME need a defined model output to explain; variable-length bounding-box outputs require an appropriate target. Since this detector uses fixed colour thresholds, inspecting pixel values, the colour mask, and bounding-box overlap is more direct.

## What did your attack show?

<!-- Using fairness_report.json["adversarial"]: at what eps does each flagged class fall further? Which class is most fragile, and is it the same class the clean audit flagged? Compare the drop ranking (most_fragile) with lowest_recall_under_attack — do they agree, and which is the better measure of who is hurt? What does that say about who bears the cost of an attack (or of an unmonitored failure)? Then: what would adversarial training or input validation look like for this detector, and why does a rule this simple break so much more easily than a CNN (or does it)? -->

At ($\epsilon$=10,20,30,40), Bicycle recall fell to 43.8%, 25%, 18.8%, and 6.3%, respectively. Two-wheeler recall fell to 78.6%, 64.3%, 50%, and 35.7%.

At ($\epsilon$=20), Bicycle, Bus, and Truck had the largest recall drops: 37.5, 35.7, and 31.3 percentage points. Bicycle was also the weakest clean class. However, the lowest attacked recall ranking was Bicycle, Two-wheeler, then Bus (with Bus and Two-wheeler tied at 64.3%). Recall drop measures fragility; absolute attacked recall shows remaining performance, so both matter.

Adversarial training could use perturbed examples for a learned detector. For this rule-based detector, I would test colour variations and improve the detection rules. Input validation can reject malformed images, but valid perturbations require robustness testing. Hard colour thresholds make this detector especially brittle, though CNNs can also be vulnerable.