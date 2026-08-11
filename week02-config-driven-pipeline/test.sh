#!/bin/bash

# ============================================================
# Week 2 - Config Driven Pipeline Test Runner
# ============================================================

PIPELINE="src/pipeline.py"
TEST_DIR="config/test_configs"

mkdir -p "$TEST_DIR"

echo "=========================================="
echo " Config-Driven Pipeline Tests"
echo "=========================================="

# ------------------------------------------------------------
# 1. Valid JSON configuration
# ------------------------------------------------------------
cat > "$TEST_DIR/valid_json.yaml" <<EOF
input_path: data/v1/transactions.json
input_format: json
high_value_threshold: 5000
output_path: data/v1/report.json
EOF

# ------------------------------------------------------------
# 2. Valid CSV configuration
# ------------------------------------------------------------
cat > "$TEST_DIR/valid_csv.yaml" <<EOF
input_path: data/v1/transactions.csv
input_format: csv
high_value_threshold: 5000
output_path: data/v1/report.json
EOF

# ------------------------------------------------------------
# 3. Invalid format
# ------------------------------------------------------------
cat > "$TEST_DIR/invalid_format.yaml" <<EOF
input_path: data/v1/transactions.json
input_format: xml
high_value_threshold: 5000
output_path: data/v1/report.json
EOF

# ------------------------------------------------------------
# 4. Missing input_path
# ------------------------------------------------------------
cat > "$TEST_DIR/missing_input_path.yaml" <<EOF
input_format: json
high_value_threshold: 5000
output_path: data/v1/report.json
EOF

# ------------------------------------------------------------
# 5. Missing input_format
# ------------------------------------------------------------
cat > "$TEST_DIR/missing_input_format.yaml" <<EOF
input_path: data/v1/transactions.json
high_value_threshold: 5000
output_path: data/v1/report.json
EOF

# ------------------------------------------------------------
# 6. Missing threshold
# ------------------------------------------------------------
cat > "$TEST_DIR/missing_threshold.yaml" <<EOF
input_path: data/v1/transactions.json
input_format: json
output_path: data/v1/report.json
EOF

# ------------------------------------------------------------
# 7. Missing output_path
# ------------------------------------------------------------
cat > "$TEST_DIR/missing_output_path.yaml" <<EOF
input_path: data/v1/transactions.json
input_format: json
high_value_threshold: 5000
EOF

# ------------------------------------------------------------
# 8. Multiple missing parameters
# ------------------------------------------------------------
cat > "$TEST_DIR/multiple_missing.yaml" <<EOF
input_path: data/v1/transactions.json
EOF

# ------------------------------------------------------------
# 9. Empty YAML
# ------------------------------------------------------------
cat > "$TEST_DIR/empty.yaml" <<EOF
EOF

# ------------------------------------------------------------
# 10. Wrong format with CSV file
# ------------------------------------------------------------
cat > "$TEST_DIR/csv_as_json.yaml" <<EOF
input_path: data/v1/transactions.csv
input_format: json
high_value_threshold: 5000
output_path: data/v1/report.json
EOF


# ============================================================
# Function to run one test
# ============================================================

run_test() {
    NAME="$1"
    CONFIG="$2"

    echo
    echo "------------------------------------------"
    echo "TEST: $NAME"
    echo "CONFIG: $CONFIG"
    echo "------------------------------------------"

    python "$PIPELINE" --config "$CONFIG"

    STATUS=$?

    if [ $STATUS -eq 0 ]; then
        echo "RESULT: SUCCESS"
    else
        echo "RESULT: FAILED / ERROR (exit code $STATUS)"
    fi
}


# ============================================================
# Run all tests
# ============================================================

run_test "Valid JSON" "$TEST_DIR/valid_json.yaml"

run_test "Valid CSV" "$TEST_DIR/valid_csv.yaml"

run_test "Invalid input format" "$TEST_DIR/invalid_format.yaml"

run_test "Missing input_path" "$TEST_DIR/missing_input_path.yaml"

run_test "Missing input_format" "$TEST_DIR/missing_input_format.yaml"

run_test "Missing high_value_threshold" "$TEST_DIR/missing_threshold.yaml"

run_test "Missing output_path" "$TEST_DIR/missing_output_path.yaml"

run_test "Multiple missing parameters" "$TEST_DIR/multiple_missing.yaml"

run_test "Empty YAML" "$TEST_DIR/empty.yaml"

run_test "CSV file declared as JSON" "$TEST_DIR/csv_as_json.yaml"


echo
echo "=========================================="
echo " All tests completed"
echo "=========================================="