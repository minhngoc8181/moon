## 2.1 Overview of the research situation, both domestically and internationally

In the field of information technology education, particularly in programming courses, automatic assessment systems have become an essential component for enhancing the efficiency and fairness of grading. Internationally, numerous tools and platforms such as CodeRunner \[1\], AutoGrader \[2\], Gradescope \[3\], and edX CodeOcean \[4\] have been widely adopted. These systems focus on evaluating code correctness through test cases, providing instant feedback, and supporting scalable assessment for large classes and online learning environments.

Ongoing international projects have addressed challenges related to assessing code with complex input types (e.g., arrays, user-defined types), supporting class-based design assignments, and integrating debugging guidance to enhance learning outcomes \[5\]. These systems often allow instructors to design flexible test cases with various input formats and automatically instantiate custom objects during test execution.

Domestically, while a number of universities in Vietnam have developed or adopted basic auto-grading tools—often using Python, C/C++, or Java—the majority of them are limited to input-output comparison or functional tests. Tools lack support for design-oriented assignments involving class hierarchies, encapsulation, and data abstraction as commonly seen in Data Structures or Object-Oriented Programming (OOP) courses. Furthermore, setting up test cases often requires instructors to write unit test code manually, posing a barrier for large-scale or non-technical users.

This research will help narrow the technological gap between domestic and international practices, offering a practical and intelligent solution aligned with current trends in programming education. By doing so, it contributes to enhancing assessment transparency, improving student learning outcomes, and supporting digital transformation in higher education.

## 2.2 Scientific ideas, relevance, and innovation

Key limitations of current domestic systems include:

*   No support for simple test case definitions using plain text files with structured parameters;
*   Lack of automated type conversion or constructor-based object instantiation for user-defined types;
*   No ability for students to perform pre-submission self-assessment;
*   Minimal integration with debugging or real-time feedback features.

These issues hinder teaching effectiveness and reduce student engagement in learning programming concepts that require structural and design thinking.

The proposed research aims to overcome these challenges by developing a robust and extensible automatic grading system that:

*   Supports the assessment of assignments with design requirements (e.g., defining classes, implementing methods with specific signatures);
*   Allows instructors to define test cases in plain text, supporting basic types, arrays, and user-defined types;
*   Automates parameter conversion and object instantiation during method testing;
*   Enables students to test their code locally and receive immediate feedback for each test case;
*   Provides a unified interface for both teaching and evaluation purposes.

## 2.3 Preliminary research results

A prototype has been developed and piloted with hundreds of students in Introduction to Programming (CSE 102), Applied Math (CSE 107), Programing and Problem Solving I (CSE 103) classes, using Java programming language. The results conduct with 90% students feedback that this tool helps them a lot in studying algorithms and programming languages.

## 2.4 References

\[1\]. Bralić, V., Kavran, K., & Valić, B. (2020). Automatic programming task grading–A case study in CodeRunner use at the University of applied sciences Velika Gorica. In 4th Contemporary Issues In Economy & Technology (CIET 2020) (pp. 697-707).

\[2\]. Messer, M., Brown, N. C., Kölling, M., & Shi, M. (2024). Automated grading and feedback tools for programming education: A systematic review. ACM Transactions on Computing Education, 24(1), 1-43.

\[3\]. Singh, A., Karayev, S., Gutowski, K., & Abbeel, P. (2017, April). Gradescope: a fast, flexible, and fair system for scalable assessment of handwritten work. In Proceedings of the fourth (2017) acm conference on learning@ scale (pp. 81-88).

\[4\]. Serth, S., Staubitz, T., Teusner, R., & Meinel, C. (2021, March). CodeOcean and CodeHarbor: Auto-Grader and Code Repository. In SPLICE 2021 workshop CS Education Infrastructure for All III: From Ideas to Practice, Virtual Event (p. 5).

\[5\]. Hieke Keuning, Johan Jeuring, and Bastiaan Heeren. 2018. A systematic literature review of automated feedback generation for programming exercises. ACM Transactions on Computing Education 19, 1, Article 3 (09 2018), 43 pages. DOI:https://doi.org/10.1145/3231711.

## 2.5 Research objectives and content

### 2.5.1 Objectives

This project aims to design and implement an automatic grading system that enhances the fairness, transparency, and accuracy of student assessments in programming-related courses. From a scientific perspective, the system addresses the growing demand for scalable and objective evaluation methods in computer science education by leveraging automation techniques for code assessment and error detection. Practically, the software enables students to debug their programs effectively and can be deployed on personal computing environments, ensuring ease of use and accessibility. The solution is intended to support a wide range of courses, such as Introduction to Programming and Problem-solving I, II, etc., thereby aligning with the operational needs of educational institutions and contributing to the overall improvement of teaching quality and learning outcomes.

### 2.5.2 Research Content and Methods


**a) Content 1: Literature Review, Problem Analysis, and Idea Formation**

**Task:**

*   Expected scientific outcomes and evaluation criteria:

A clear understanding of existing grading systems for programming assignments, identification of their limitations, and formulation of a new idea addressing both functional and design-based evaluation. Evaluation based on comprehensiveness of literature review and originality of the proposed idea.

*   Methods:

Conduct a systematic review of international and domestic research papers, tools (e.g., CodeRunner, Gradescope), and software systems related to automated code grading. Discuss programming instructors to understand common grading challenges in design-focused courses (e.g., OOP, Data Structures).

*   Analysis and interpretation of the data collected:

Synthesize reviewed materials into a gap analysis table. Analyze instructor discussions to extract thematic issues (e.g., lack of support for class structures, difficulty creating test cases). Use the results to justify the need for the proposed tool.

**b) Content 2: Interface Design**

**Task:**

*   Expected scientific outcomes and evaluation criteria:

A functional and user-friendly interface prototype for both instructors and students. Evaluation criteria include usability (measured via user testing) and compatibility across platforms (Windows 10/11).

*   Methods:

Use Figma or similar design tools to create wireframes. Conduct usability testing sessions with representative users from both student and instructor groups.

*   Analysis and interpretation of the data collected:

Analyze test session and user feedback. Refine the interface based on commonly reported issues.

**c) Content 3: Technology Exploration and Selection**

**Task:**

*   Expected scientific outcomes and evaluation criteria:

A documented set of tools, frameworks, and programming languages selected for implementation. Evaluation based on their scalability, integration capability, and maintainability.

*   Methods:

Evaluate candidate technologies (e.g., Java/.NET for runtime reflection, GUI libraries, test frameworks). Run performance and compatibility tests to ensure they meet functional and system requirements.

*   Analysis and interpretation of the data collected:

Compare resultss, document advantages and trade-offs of each solution to justify final selection.

**d) Content 4: Prototype Implementation**

**Task:**

*   Expected scientific outcomes and evaluation criteria:

A functional prototype capable of parsing test case files, dynamically invoking student code, and displaying test results. Evaluation based on correct handling of method calls with complex parameters (arrays, UDTs).

*   Methods:

Implement using agile methodology in iterations. Develop core modules: parser, method invoker, and result visualizer. Use synthetic student code as input for testing.

*   Analysis and interpretation of the data collected:

Measure success rate of test execution and correctness of output. Identify limitations in prototype behavior and performance.

**e) Content 5: Test Case Definition**

**Task:**

*   Expected scientific outcomes and evaluation criteria:

A library of reusable test cases in plain-text format for design-based assignments. Evaluation based on coverage (types, complexity) and usability for instructors.

*   Methods:

Create test cases across various programming topics (e.g., condition statement, loop, etc.). Validate syntactic and semantic correctness manually and through automated tools.

*   Analysis and interpretation of the data collected:

Test on sample student submissions. Record which types of test cases detect common errors effectively. Refine structure accordingly.

**f) Content 6: Prototype Testing**

**Task:**

*   Expected scientific outcomes and evaluation criteria:

A validated prototype with performance and stability data. Evaluation includes system accuracy, execution time, and error resilience.

*   Methods:

Conduct black-box and white-box testing. Use a mix of synthetic and real student code. Simulate batch grading scenarios.

*   Analysis and interpretation of the data collected:

Collect system logs, success/error rates, and feedback messages. Use descriptive statistics and error trace analysis to refine code.

**g) Content 7: Enhancement of Complex Features**

**Task:**

*   Expected scientific outcomes and evaluation criteria:

Extension of the prototype to support nested UDTs, multiple test scenarios, and class structure validation. Evaluation based on functional testing and expert review.

*   Methods:

Extend parser and runtime components. Introduce validation logic for method signatures and object behavior. Conduct regression testing after enhancements.

*   Analysis and interpretation of the data collected:

Compare performance and accuracy pre- and post-enhancement. Document error types resolved by the new features.

**h) Content 8: Design of Advanced Test Cases and Expert Validation**

**Task 1: Develop comprehensive test cases**

*   Expected scientific outcomes and evaluation criteria:

A complete set of test cases for various programming assignments, supporting different parameter types (basic types, arrays, and user-defined types). Evaluation based on correctness, coverage, and reusability across different courses.

*   Methods:

Analyze course requirements to design test case templates that follow a standardized structure (e.g., method name, input parameters, expected output). Ensure compatibility with the tool’s parser and execution engine. Focus on both functional and design validation.

*   Analysis and interpretation of the data collected:

Execute the test cases on a set of real and simulated student submissions. Measure accuracy in detecting common errors and evaluate ease of use for instructors. Refine the syntax and format based on usage feedback.

**Task 2: Expert review and validation of test cases**

*   Expected scientific outcomes and evaluation criteria:

Expert feedback confirming the appropriateness, effectiveness, and pedagogical value of the designed test cases. Evaluation includes acceptance rate and constructive suggestions.

*   Methods:

Invite experienced programming instructors or software developers to audit the test case sets. Provide sample student submissions and ask reviewers to evaluate detection accuracy, test coverage, and clarity.

*   Analysis and interpretation of the data collected:

Collect reviewer comments and rating scales. Analyze feedback qualitatively to refine edge case detection, reduce ambiguity, and improve pedagogical alignment. Incorporate expert-suggested improvements before final deployment.

**i) Content 9: Final Testing and Preparation for Deployment**

**Task:**

*   Expected scientific outcomes and evaluation criteria:

A validated and stable version of the grading system, ready for deployment. Evaluation based on system stability, correctness, and performance under real-world usage scenarios.

*   Methods:

Conduct end-to-end testing using finalized test cases, real assignments, and diverse student submissions. Simulate actual usage by instructors and students across multiple courses.

*   Analysis and interpretation of the data collected:

Monitor system logs, error rates, performance metrics, and user interaction patterns. Analyze to ensure all known issues are resolved and that the system performs as expected under typical and extreme conditions. Generate a final test report documenting results and readiness for deployment..

**j) Content 10: Deployment, Application in Courses, and Research Dissemination**

**Task 1:** **Deploy the tool and evaluate in real educational settings**

*   Expected scientific outcomes and evaluation criteria:

A proven deployment of the tool in real educational settings. Evaluation based on student and instructor satisfaction, grading time reduction, and learning outcome support.

*   Methods:

Deploy the system in at least two courses (e.g., OOP, Data Structures and Algorithms, etc.) at Eastern International University. Train instructors and collect user feedback.

*   Analysis and interpretation of the data collected:

Use surveys, interviews, and system usage logs. Perform qualitative and quantitative analysis to assess tool impact and gather improvement suggestions.

**Task 2: Writing and Submitting Research Publications**

*   Expected scientific outcomes and evaluation criteria:

One internal technical report and one conference paper. Evaluation based on the quality of documentation, completeness of technical details, and acceptance by a peer-reviewed venue.

*   Methods:

The technical report will summarize the development process, system architecture, usage guide, and evaluation results.

The research paper will highlight the innovative aspects of the grading system, compare with related tools, and present experimental results.

*   Expected Scientific Outcomes and Evaluation Criteria:

Use system usage data, survey results, and testing logs as the core dataset for analysis in the paper. Peer reviews and feedback from submissions will be used to refine and improve the clarity and scientific value of the research outputs.
