

test_py_version() {
    if [[ -z "$1" ]]; then
        echo "Please provide a python version to test"
        return -1
    fi
    source venv/bin/activate
    pyperformance run -o $1
}