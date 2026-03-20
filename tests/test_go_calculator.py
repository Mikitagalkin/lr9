import subprocess
import json
import pytest
import os

def test_go_calculator():
    # Проверяем, что бинарник существует (если нет, тест пропускается)
    if not os.path.exists("go/calculator.exe"):
        pytest.skip("calculator.exe not found, compile Go first")
    proc = subprocess.Popen(
        ["./go/calculator.exe"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    input_data = {"numbers": [1, 2, 3, 4, 5]}
    json_input = json.dumps(input_data).encode()
    stdout, stderr = proc.communicate(json_input)
    result = json.loads(stdout)
    assert result["sum"] == 55