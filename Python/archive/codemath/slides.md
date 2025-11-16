# Automated Assessment Tool for Data Structures & Object-Oriented Design

**Presenter:** (Your name)
**Affiliation:** EIU – School of Computing & IT
**Audience:** Faculty, curriculum board, potential partners
**Duration:** \~15–20 minutes

---

# Agenda

* Introduction
* Automated Assessment Tool
* Research & Development Methods
* Research Plan
* Q\&A / Thank you

---

# Introduction — Information

* **Context:** Large cohorts in DSA & OOP need fair, fast, consistent assessment.
* **Motivation:** Existing auto-graders in VN focus on I/O; struggle with design-level evaluation.
* **Target courses:** Intro to Programming, Programming & Problem Solving I–II, Data Structures & Algorithms, OOP.
* **Stakeholders:** Students, instructors, programme QA, accreditation (AUN, etc.).
* **Benefits:** Faster feedback, transparency, scalable grading, better learning outcomes.

---

# Introduction — Literature Review

* **Global tools:** CodeRunner, Gradescope, VPL, CodeOcean—strong at functional tests and scale.
* **Gaps documented:** Limited design-quality checks (encapsulation, class hierarchy, signatures).
* **Pedagogy:** Formative feedback—granular, immediate feedback improves learning.
* **Opportunity:** Bridge functional correctness **and** design-level assessment for DSA/OOP.

---

# Introduction — Problems & Challenges

* Hard to test **arrays & user-defined types (UDTs)** and class-based designs.
* Instructors often must write **unit-test code**; high barrier to adoption.
* Limited **pre‑submission self‑assessment** for students.
* Minimal integration with **debugging / real-time feedback**.

---

# Automated Assessment Tool — Description

* A lightweight, local tool to **compile, run, and assess** Java assignments against **plain‑text test cases**.
* Focuses on **method-level tests inside student classes**, not just I/O.
* Generates **clear per‑test feedback** (pass/fail, inputs, expected vs. actual, errors).

---

# Automated Assessment Tool — Objectives

* Fair, transparent, accurate grading at scale.
* Support design‑oriented tasks in **DSA & OOP**.
* Enable **student self‑assessment** before submission.
* Lower authoring overhead for instructors.

---

# Automated Assessment Tool — Key Features

* **Plain‑text test cases:** target class, method, parameters, expected output.
* **Type conversion & object instantiation:** primitives, arrays, UDTs via constructors.
* **Reflection-based execution:** dynamic compilation, class loading, method invocation.
* **Rich feedback:** pass/fail, runtime errors, expected vs. actual, test inputs.
* **Reusable libraries of cases**; supports edge cases and design validation.

---

# Automated Assessment Tool — Architecture (High Level)

* **Test Case Parser**
  Parses structured .txt tests → in‑memory spec (class, method, params, expected).
* **Dynamic Execution Engine**
  In‑memory compile → load classes via reflection → convert params → instantiate UDTs → invoke methods → capture results.
* **Feedback Module**
  Compare expected vs. actual; surface errors and traces for debugging.

---

# Automated Assessment Tool — User Workflow

**Instructor**

1. Write assignment & required signatures.
2. Author .txt test cases (incl. edge cases).
3. Distribute tool + tests to students.

**Student**

1. Implement classes/methods.
2. Run tool locally; review per‑test feedback.
3. Iterate until all tests pass; submit.

---

# Evidence & Early Results (Pilot)

* **Prototype:** Java, used across multiple courses.
* **Students:** Hundreds; **>90%** reported improved understanding/debugging.
* **Validation:** Black‑box & white‑box; strong coverage for logic & functional errors.
* **Illustrative metrics:** Detection accuracy \~**95%** on mixed corpora (synthetic + authentic).

---

# Research & Development Methods

* **Literature & gap analysis** → requirements.
* **Interface design:** wireframes, usability tests (students & instructors).
* **Technology selection:** reflection/runtime options; GUI/test frameworks.
* **Prototype iterations (agile):** parser, invoker, visualizer.
* **Test case engineering:** coverage across control flow, data structures, OOP.
* **Prototype testing:** black‑box/white‑box, batch simulation, error‑resilience.
* **Expert validation:** review of test libraries and pedagogy value.

---

# Research Plan — Roadmap & Milestones

**Phase 1 (M1–M2):** Literature Review & Requirements
• Gap analysis; stakeholder interviews; success metrics.

**Phase 2 (M2–M3):** Interface Design
• Wireframes → usability tests → refine.

**Phase 3 (M3–M4):** Tech Exploration
• Evaluate Java/.NET, reflection, sandboxing; decide stack.

**Phase 4 (M4–M5):** Prototype v1
• Parser + execution engine + feedback module; smoke tests.

**Phase 5 (M5–M6):** Test Case Library v1
• 50+ exercises; 200+ cases; edge‑case coverage.

**Phase 6 (M6–M7):** Prototype Testing
• Accuracy, execution time, robustness; batch scenarios.

**Phase 7 (M7–M8):** Advanced Features
• Nested UDTs, class‑structure validation, multi‑scenario suites.

**Phase 8 (M8–M9):** Expert Validation & Final Testing
• Reviewer audit; regression; deployment readiness report.

**Phase 9 (M9–M10):** Deployment & Dissemination
• Pilot in at least two courses; surveys/logs; technical report + conference paper.

---

# Evaluation — Metrics & Instruments

* **Technical:** test detection accuracy; compile/run success; throughput; stability.
* **Pedagogical:** student self‑efficacy; time‑to‑feedback; reduction in regrade requests; pass rates.
* **Operational:** instructor setup time; test authoring time; grading time reduction.

---

# Risks & Mitigations

* **Security/sandboxing** for untrusted code → process isolation, resource limits.
* **Language dependence (Java‑first)** → design abstractions for future Python/C++ backends.
* **Instructor adoption** → templates, wizards, starter libraries; brief training.
* **Over‑fitting to tests** → randomized cases; hidden tests; design checks (signatures/UDTs).

---

# Initial Ideas — Extensions & Partnerships

* **Static analysis add‑ons:** style/complexity metrics, smells, basic design‑pattern checks.
* **LMS integration:** Moodle/Canvas plug‑in, Gradescope bridge, exportable CSV.
* **Analytics:** cohort dashboards (common errors, time‑to‑pass trends).
* **Plagiarism signals:** structural similarity (AST/CFG) as a separate report.
* **Multi‑language support:** Python/C++ runners; polyglot test DSL.
* **Community library:** shared test-case repository across courses/universities.

---

# Research Plan — Deliverables

* v1 prototype + test suite library
* Usability study & validation report
* Pilot deployment results dashboard
* Technical report & 1× conference submission
* Instructor guide + student quick‑start

---

# Thank You

**Contact:** (email)
**Questions?**
