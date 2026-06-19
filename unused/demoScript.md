# 🎤 FCValidator Keynote Demo Script
**Style:** Google Developer Summit / Expo Keynote Showcase  
**Tone:** Systems Programmer, Peer-to-Peer, Technical, Methodical  
**Target Duration:** 5–6 minutes  

---

## 🎬 Act I: The Language Boundary Dilemma (Screencast & Face Cam)

### 📸 Visual Layout
- **Initial State:** Browser open to `http://127.0.0.1:5000/` showing the *HPC Structural FEM Dashboard*.
- **Presenter view:** Camera active in the bottom-left corner (small overlay, 15% screen space).

---

### 🚀 Step-by-Step Action
1. **Look at the camera** with a calm, collaborative smile.
2. **Start speaking** immediately, setting a peer-to-peer tone.

---

### 🗣️ Spoken Script
> "Hi everyone. Today I want to talk about a silent crisis in high-performance scientific computing: language boundary compatibility.
> 
> In modern systems, we frequently mix languages. We write high-level web dashboards or control loops in C, C++, or Python, and link them directly to legacy Fortran solvers performing numerical heavy-lifting, like FEM or fluid dynamics.
> 
> Historically, we’ve relied on our linkers and compilers to keep us safe. But at the language boundary, compilers are completely blind. Let me show you what happens when we trust them blindly."

---

## 🎬 Act II: The Invisible Collision (Screencast Full Screen)

### 📸 Visual Layout
- **Focus:** Full screen browser displaying the FEM Dashboard.

---

### 🚀 Step-by-Step Action
1. Set **Solver Interoperability Build** dropdown to: `Buggy legacy ABI (No BIND(C))`
2. Set **Material Selection** dropdown to: `Steel`
3. Enter **Mesh Grid nx**: `100`
4. Enter **Mesh Grid ny**: `100`
5. Enter **Boundary Load Vector (N)**: `5000`
6. Click **Execute FEM Analysis**.
7. Point your cursor to the **corrupted red output banner** and the value `9234872139823.15 m`.

---

### 🗣️ Spoken Script
> "Here, I’m running a structural FEM solver simulation. I submit standard mesh sizes and loads for a Steel element. Both the C bridge and the Fortran core compiled successfully, and the linker merged the symbols without a single warning.
> 
> But look at the output. Instead of a normal physical displacement of a few millimeters, we get a garbage calculation: **9.2 trillion meters**, and the console reports a silent stack register overflow.
> 
> If this were running inside a weeks-long simulation, it would silently invalidate our entire numerical dataset with no warning. The linker links fine, but the binary interfaces are fractured."

---

## 🎬 Act III: The Forensic Code Audit (Terminal Split Screen)

### 📸 Visual Layout
- **Focus:** Split terminal window showing the buggy source files side-by-side.
  - **Left side:** Fortran interface block (`demo/demo_pairs/buggy/fem_solver.f90`)
  - **Right side:** C header prototype (`demo/demo_pairs/buggy/fem_wrapper.h`)

---

### 🚀 Step-by-Step Action
1. Open the split terminal and run:
   ```bash
   cat demo_pairs/buggy/fem_solver.f90
   ```
2. In the right pane, run:
   ```bash
   cat demo_pairs/buggy/fem_wrapper.h
   ```
3. Highlight the `character(len=*) :: material` declaration in Fortran.
4. Highlight the `long *nx, long *ny` pointers in the C header.

---

### 🗣️ Spoken Script
> "To a developer reviewing this boundary, it looks perfectly reasonable. We have the same variable names, matching parameters, and equivalent types. But underneath, there are two catastrophic, invisible errors.
> 
> First, our Fortran interface block lacks the modern `BIND(C)` attribute. Because it's missing, the Fortran compiler falls back to the legacy calling convention, silently appending a hidden `size_t` argument representing the length of `material` to the end of the argument list. C has no idea this exists, and omits passing it—corrupting our stack frame.
> 
> Second, Fortran's `integer` is 4 bytes. But on our 64-bit LP64 Linux environment, the C side expects pointers to 8-byte `long` values. Fortran reads 8 bytes from a 4-byte address, shifting the stack pointer by 32 bits. The compilers are blind to this."

---

## 🎬 Act IV: Static Boundary Validation (Terminal Full Screen)

### 📸 Visual Layout
- **Focus:** Full screen terminal.

---

### 🚀 Step-by-Step Action
1. Run the validator command on the buggy pair:
   ```bash
   fcv validate demo/demo_pairs/buggy/fem_solver.f90 demo/demo_pairs/buggy/fem_wrapper.h
   ```
2. Wait a beat for the colored table to appear, then highlight the three errors.

---

### 🗣️ Spoken Script
> "Instead of compiling, linking, and running into runtime crashes, we run **FCValidator** directly on the source files. 
> 
> In less than a second, the static validation engine walks both front-ends—using `libclang` to parse the actual C compiler AST and our high-fidelity preprocessor for the Fortran block. 
> 
> The tool immediately flags all three boundary errors at compile-time: the parameter count mismatch caused by the hidden string length, and the explicit 4-byte vs 8-byte pointer width shifts for `nx` and `ny`."

---

## 🎬 Act V: The Structural Fix (Terminal & Browser)

### 📸 Visual Layout
- **Focus:** Terminal showing the code diff, then the browser.

---

### 🚀 Step-by-Step Action
1. Display the fixed Fortran interface:
   ```bash
   cat demo/demo_pairs/fixed/fem_solver.f90
   ```
2. Highlight the BIND(C) addition, `character(kind=c_char)` array, and `integer(c_int), value` attributes.
3. Run the validator on the fixed pair:
   ```bash
   fcv validate demo/demo_pairs/fixed/fem_solver.f90 demo/demo_pairs/fixed/fem_wrapper.h
   ```
4. Point to the clean output: **`0 Errors`**.

---

### 🗣️ Spoken Script
> "To resolve this, we rewrite the interface using modern Fortran 2003 C-interoperability standards.
> 
> We add the `BIND(C)` attribute to bind the internal name explicitly. We declare `material` as an interoperable `character(kind=c_char)` array, eliminating the legacy hidden string length injection. And we map the mesh dimensions explicitly to `integer(c_int)` passed by `value` to match C's standard 4-byte variables.
> 
> Let's run the validator again on our fixed pair. 
> 
> Immediate feedback: 0 Errors, clean status. We have mathematically verified our binary layout before compilation."

---

## 🎬 Act VI: The Payoff (Browser Full Screen)

### 📸 Visual Layout
- **Focus:** Full screen browser.

---

### 🚀 Step-by-Step Action
1. Go back to the browser window.
2. Toggle the **Solver Interoperability Build** dropdown to: `Fixed BIND(C) ABI (Compliant)`.
3. Submit the FEM form again.
4. Highlight the **green success alert** and the clean output value: `0.0238 m`.

---

### 🗣️ Spoken Script
> "Now, we toggle our solver build to the compliant BIND(C) compiler interface. 
> 
> We submit the exact same engineering mesh and load vectors.
> 
> The stack aligns perfectly. The registers load clean. We immediately receive our correct double-precision displacement result: **0.0238 meters** (23.8 millimeters), with absolute system integrity."

---

## 🎬 Act VII: Closer (Screencast & Face Cam)

### 📸 Visual Layout
- **Focus:** Bring your face camera back to prominent view (40% screen space).

---

### 🚀 Step-by-Step Action
1. Look directly at the camera, ending with a calm, expert tone.

---

### 🗣️ Spoken Script
> "Compilers and linkers compile files in isolation, leaving mixed-language boundaries completely unprotected.
> 
> **FCValidator** acts as a unified compile-time gatekeeper. By translating both language structures into a normalized, byte-level Intermediate Representation, it guarantees that your multi-language interfaces align perfectly before you ever hit compile. 
> 
> Thank you."

---
