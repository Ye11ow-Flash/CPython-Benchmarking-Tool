

run_pyperformance() {
    read -p "Enter path to the python : " path
    pyperformance run --python="$path" -o pyperformance_op.json
}