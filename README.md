# FCValidator: Fortran-C Cross-Language Interface Validator

## 👥 Student Development Team & Credits
Developed as part of the Compiler Design Course Project (Evaluation by HPE Team):

* **Tanmay Dev D** (1RV23CS269) — Department of Computer Science and Engineering, RVCE  
  *Email:* [tanmaydevd.cs23@rvce.edu.in](mailto:tanmaydevd.cs23@rvce.edu.in)
* **Tarun.R** (1RV23CS271) — Department of Computer Science and Engineering, RVCE  
  *Email:* [tarunr.cs23@rvce.edu.in](mailto:tarunr.cs23@rvce.edu.in)
* **Tejasvi Vasant Hegde** (1RV23CS272) — Department of Computer Science and Engineering, RVCE  
  *Email:* [tejasvivhegde.cs23@rvce.edu.in](mailto:tejasvivhegde.cs23@rvce.edu.in)

---

## 🎬 Video Demonstration Showcase

We have provided a complete keynote-style video walkthrough demonstrating **FCValidator** in action against a real-world scientific HPC simulation:
* **Online Stream (OneDrive Link):** [Watch Video Demonstration](https://1drv.ms/v/c/838889d9a4b62e44/IQABIxRq4Hi8RqEuj9h2iVrmAd3XZ5onEaAMgfwAKfOVsRU?e=bBKwcr)
* **Local Video File:** [demo/Demo.mp4](file:///c:/Users/tarun/Desktop/USEFUL/Projects/Compiler_Design_Docs_Backup/Compiler%20Design%20EL/fcvalidator/demo/Demo.mp4)

> [!IMPORTANT]
> **Disclaimer & Evaluation Scope:**
> The video demonstrates how FCValidator is integrated into a professional developer workflow using a custom **HPC Structural FEM Solver Web Dashboard** (built in Flask, dynamically invoking Fortran shared libraries). 
> 
> Please note that the Finite Element Method (FEM) web application is a simulated dashboard. The physical plate stress calculations, boundary loads, and material displacement stubs are simplified simulations constructed to clearly showcase tool behavior. However, the command-line static validation (`fcv validate`), AST compiler-level parsing, type-width matching, and terminal reports are **100% authentic, accurate, and run in real-time**.

To learn more about the demo application and how to run it locally on your system, please refer to the specialized **[demo/README.md](file:///c:/Users/tarun/Desktop/USEFUL/Projects/Compiler_Design_Docs_Backup/Compiler%20Design%20EL/fcvalidator/demo/README.md)**.

---

## 🛑 The Problem: The "Silent Data Corruption" Crisis in HPC
When writing high-performance computing (HPC) software (like LAPACK, BLAS, or modern scientific simulations), developers frequently mix Fortran for numerical heavy-lifting with C/C++ for networking, memory management, and system-level operations. 

To bridge the gap between these languages, developers use Fortran's `BIND(C)` interoperability standard. However, **compilers do not verify cross-language interfaces**. If a Fortran subroutine expects an 8-byte `INTEGER` but the C header provides a 4-byte `int`, the compiler will happily link them. At runtime, this results in silent stack corruption, segmented faults, or subtle mathematical inaccuracies that can invalidate months of scientific computation without ever throwing an error.

Common catastrophic mismatches include:
* **The "Hidden String Length" Trap:** Fortran strings implicitly append length variables to the end of argument lists. C functions unaware of this will corrupt the stack when Fortran attempts to write to that length variable.
* **Array Memory Layout:** Fortran represents 2D arrays in Column-Major order, while C uses Row-Major order. Accessing `a[i][j]` in C directly maps to `a(i, j)` in Fortran, causing silent transposition errors.
* **Platform-Dependent Traps:** `long` is 4 bytes on Windows 64-bit, but 8 bytes on Linux/macOS. Hardcoding interfaces to `long` causes cross-platform crashes.
* **Harvard Architecture Pointer Traps:** Mixing up data pointers (`c_ptr`) and instruction pointers (`c_funptr`) will cause immediate hardware-level segfaults on modern architectures like Apple ARM64 (M-series chips).

---

## ✨ What Purpose It Serves
**FCValidator** solves this problem by acting as a strict, static analysis gatekeeper. It reads your Fortran interface and your C header file, translates them into a normalized Intermediate Representation (IR), and statically validates that every single parameter, return type, struct padding, and pointer aligns perfectly at the binary/ABI level.

It does this **without needing to compile the code**. It is designed to be fast, lightweight, and capable of catching the 36 hardest ABI edge-cases known to break mixed-language systems.

---

## 🛠️ Installation & Building

For convenience and platform compliance, a dedicated `build.sh` script is provided to automate environment setup inside a local Python virtual environment (`.venv`).

### Automated Setup (Recommended)
```bash
./build.sh
```
This script will:
1. Detect and install system-level dependencies (like `python3-venv` and `libclang-dev` on Debian/Ubuntu systems).
2. Create an isolated Python virtual environment (`.venv`) to keep your host environment clean.
3. Install `fcvalidator` in editable developer mode (`pip install -e ".[dev]"`).

### Manual Setup
If you prefer setting up the environment manually:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

---

## 🚀 How to Run

### Automated Demonstration Suite
To run the standard validator demonstrations and the comprehensive `pytest` check suite automatically:
```bash
./run.sh
```

### Manual CLI Validation
Activate the virtual environment and run the command-line validator on your interfaces:
```bash
source .venv/bin/activate
fcv validate src/interface.f90 include/header.h --platform lp64
```

### CLI Command Options:
* `--platform`: Specify the target integer model. `lp64` (Linux/macOS defaults where `long` is 8 bytes), `ilp64` (specialized 64-bit integer models), or `llp64` (Windows 64-bit model where `long` is 4 bytes).
* `--format`: Output format: `text` (default rich console table), `json` (for scripting pipelines), or `sarif` (for GitHub Security Code Scanning).
* `--severity`: Filter the output by `info`, `warning`, or `error`. Default is `warning`.

---

## 🖥️ Troubleshooting Clang System Headers
Because `libclang` parses C headers using actual compiler frontends, it requires access to standard system headers (e.g., `<stdint.h>`, `<stddef.h>`).
* **Ubuntu/Debian:** Ensure `libclang-dev` is installed (handled automatically by `./build.sh`).
* **Windows (PowerShell):** If Clang cannot resolve system headers, configure your shell include environment variable pointing to Visual Studio or compiler directories:
  ```powershell
  $env:C_INCLUDE_PATH="C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Tools\MSVC\<version>\include"
  ```

---

## 🤖 CI/CD Integration (GitHub Actions)
Integrate `fcvalidator` directly into your pull-request pipeline to block mismatched interfaces before they are merged:
```yaml
name: ABI Static Verification
on: [push, pull_request]

jobs:
  validate-abi:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install FCValidator
        run: |
          sudo apt-get install -y libclang-dev
          pip install .
      - name: Run Verification
        run: |
          fcv validate src/interface.f90 include/header.h --format sarif > fcv-results.sarif
      - name: Upload SARIF Results
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: fcv-results.sarif
```

---

## 📸 Visual Demo Catalogue (Screenshots)

Below are the actual terminal demonstrations capturing the step-by-step installation and diagnostic workflow of FCValidator:

### 1. Environment Build & Installation
Executing `./build.sh` provisions the local virtual environment and installs the package in editable mode.
![01_install](screenshots/01_install.png)

### 2. High-Severity Mismatch Detection (TC-A-001)
Validating a character flag interface that lacks `BIND(C)` highlights the legacy calling convention mismatch, showing high-severity `ERROR` markers and argument list mismatches directly on the console.
![02_error_detection](screenshots/02_error_detection.png)

### 3. Validated Clean Interface Success Banner (TC-A-003)
Validating a fully compliant Fortran-C interface pair yields a clean status confirmation, showcasing the glowing green `No mismatches found!` banner.
![03_clean_interface](screenshots/03_clean_interface.png)

### 4. Colorized Structured JSON Output (TC-B-001)
Invoking the validator with `--format json` outputs a perfectly indented and readable JSON array, ideal for scripting integrations.
![04_json_output](screenshots/04_json_output.png)

### 5. Automated Regression Test Suite Execution
Running the full diagnostic checks executes all 68 interface edge scenarios, displaying green checkmarks and test statistics.
![05_pytest_passing](screenshots/05_pytest_passing.png)

---

## 📂 Project Organization & Documentation
For a deep dive into the design and evaluation of the project, please refer to the following documents:
- **[DESIGN.md](DESIGN.md)**: Details the parser architecture, language-neutral IR, and alternative design decisions.
- **[IMPLEMENTATION.md](IMPLEMENTATION.md)**: Walks through the Clang AST compiler frontend integration and Fortran parsing algorithms.
- **[EVALUATION.md](EVALUATION.md)**: Tabulates the complete 68 test suite, platform metrics, and reference LAPACK evaluation reports.
