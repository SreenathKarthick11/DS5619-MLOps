# NOTES.md — Week 11: Model Compression Benchmark

**Student ID used with `generate_for_student.py`:**

```
student_id: 112301042
seed: 1651575289
```

## pruned_dense_fp32 vs. pruned_sparse_coo

<!-- Compare pruned_dense_fp32 and pruned_sparse_coo in your report — same
     weights, same accuracy, very different size_bytes. Explain why in your
     own words (tie it to the lecture's pruning pitfall). -->

At 70% sparsity, both variants use the same pruned weights and achieve the same accuracy of 99.67%. However, their storage sizes differ significantly. The dense FP32 representation occupies 1,024 bytes because it stores all 256 weights, including the zeros introduced by pruning. In contrast, the sparse COO representation stores only the 77 nonzero weights, along with a 4-byte value and a 4-byte index for each weight, requiring only 616 bytes.

This demonstrates the pruning pitfall as mentioned in lecture setting weights to zero does not reduce storage when the model remains densely represented. Actual storage savings require a sparse representation that avoids storing zero-valued weights. In this experiment, sparse COO provides approximately 1.66× compression compared with the baseline.


## The 0.95-sparsity experiment

<!-- Try editing PRUNE_SPARSITY in src/run_pipeline.py to 0.95 and re-run —
     what happens to accuracy, and why does that make sense given only 40
     of the 256 weights are actually informative? -->

At 70% sparsity, the model achieves 99.67% accuracy. Increasing sparsity to 95% removes 243 of the 256 weights, leaving only 13 nonzero weights, and accuracy drops to 77.67%.

This significant drop occurs because only 40 weights are informative. Removing 243 weights inevitably eliminates many informative parameters, reducing the model's ability to classify examples correctly. Although sparse COO storage decreases from 1,024 bytes to 104 bytes, this compression comes at the cost of predictive performance.

The experiment demonstrates that aggressive pruning can damage accuracy when important weights are removed. Effective model compression must balance storage savings against the preservation of useful information.