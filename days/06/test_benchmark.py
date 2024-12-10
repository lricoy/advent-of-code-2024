import subprocess

def run_script(file):
    """Run a Python script and return its output."""
    subprocess.run(["python", file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def test_06_02(benchmark):
    benchmark(run_script, "06_02.py")

def test_06_02_brute_conc(benchmark):
    benchmark(run_script, "06_02_brute_conc.py")

def test_06_02_opt(benchmark):
    benchmark(run_script, "06_02_opt.py")

def test_06_02_opt_conc(benchmark):
    benchmark(run_script, "06_02_opt_conc.py")
