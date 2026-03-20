import subprocess
import json

proc = subprocess.Popen(
    ["./calculator.exe"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

data = {"numbers": [1, 2, 3, 4, 5]}
json_input = json.dumps(data).encode()
stdout, stderr = proc.communicate(json_input)

result = json.loads(stdout)
print(result["sum"])   # 55