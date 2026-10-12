"""Plain student lab record, built from measured project results."""


def build_content(p, h, page, table, code, source_excerpt, function_excerpt, link, metrics, evidence, rule):
    p("Experiment 1: Agile and Scrum Demo", "Title")
    h("Aim")
    p("To understand Agile methodology and the Scrum framework by simulating a small MLOps project. The experiment covers Scrum roles, the Product Backlog, Sprint planning, daily updates, review, retrospective and the development of a simple machine learning model.")
    rule()
    h("Learning Objectives")
    p("After completing this experiment, students will be able to:")
    for text in ("Understand Agile principles and the Scrum framework.",
                 "Identify Scrum roles and their responsibilities.",
                 "Prepare a Product Backlog and a Sprint Backlog.",
                 "Simulate planning, daily updates, review and retrospective.",
                 "Train a Decision Tree model and check its accuracy.",
                 "Understand how Agile is used in an MLOps project.",
                 "Use Git, automated tests and GitHub Actions in the project."):
        p(text, "List Bullet")
    rule()
    h("Real-Time Scenario")
    p("Suppose a company wants to build an AI system that classifies Iris flowers.")
    p("Instead of building the entire system at once, the team follows Agile Scrum and develops it in small iterations called Sprints.")
    p("During each Sprint, the team:")
    for text in ("plans the work,", "develops a part of the project,", "tests it,", "reviews progress,", "improves the next Sprint."):
        p(text, "List Bullet")
    p("This experiment applies those steps to an Iris Decision Tree project.")
    rule()

    page("Project setup and roles")
    p("This is an individual experiment. All five roles are simulated by Divyaprasad Sahu; the meeting records are a simulation. The model results, Git history and Actions runs come from actual executions.")
    h("Agile and Scrum")
    p("Agile divides the work into small parts that can be checked and improved. Scrum gives this work a structure: the Product Owner decides what is needed, the Scrum Master helps the work move forward, and Developers build the product. A Sprint has a fixed duration and a clear goal.")
    h("Step 1 Create the project")
    p("The project is stored locally in MLOps_Agile_Demo. Code, data, tests and documentation are kept in separate folders so they are easy to find.")
    code("MLOps_Agile_Demo/\n  src/       Python code\n  data/      Iris dataset\n  models/    Saved model and results\n  tests/     Automated tests\n  docs/      Backlogs report and evidence\n  .vscode/   Local editor tasks\n  .github/   Actions workflow")
    h("Using VS Code")
    p("Open the local project with File > Open Folder in VS Code. Open src/iris_demo.py from Explorer, then use Terminal > New Terminal to run the commands below. The project also includes tasks under Terminal > Run Task for training, prediction, tests and Git history.")
    code(".\\.venv\\Scripts\\python.exe -m src.iris_demo train\n.\\.venv\\Scripts\\python.exe -m src.iris_demo predict 5.1 3.5 1.4 0.2\n.\\.venv\\Scripts\\python.exe -m pytest -q")
    p("The recorded local runs were made through a command-line terminal. VS Code uses the same files and Python environment. GitHub is used afterward to share the project and run CI/CD.")
    h("Step 2 Assign the roles")
    table(["Role", "Work in this experiment"], [
        ["Product Owner", "Set the requirement of at least 95% accuracy and order the backlog."],
        ["Scrum Master", "Plan the Sprint, organise updates and help resolve blockers."],
        ["Data Engineer", "Load, check and split the Iris dataset."],
        ["ML Engineer", "Train the Decision Tree and save the model."],
        ["Tester", "Check accuracy, predictions, saved files and automated tests."],
    ], [1.5, 5.35])
    p("All roles are assigned to Divyaprasad Sahu for this simulation. In Scrum, the ML, data and testing roles are specialisations within Developers.")

    page("Backlogs and Sprint planning")
    h("Step 3 Product Backlog")
    table(["ID", "Task", "Priority", "Completion check"], [
        ["US1", "Download Iris dataset", "High", "150 rows and four features are available."],
        ["US2", "Clean dataset", "High", "Measurements and labels pass validation."],
        ["US3", "Train Decision Tree", "High", "The model trains with a fixed seed."],
        ["US4", "Evaluate accuracy", "Medium", "Accuracy is at least 95% on the test split."],
        ["US5", "Save model", "Medium", "The saved model can be loaded and used."],
        ["US6", "Prepare documentation", "Low", "Setup, code, results and Scrum records are included."],
    ], [.45, 1.6, .75, 4.05])
    p("Data preparation and training come first because the later tasks depend on them. Documentation has lower priority in the handout, but it is still needed for the final submission.")
    h("Step 4 Sprint planning")
    p("Sprint duration: one week. Sprint Goal: build the first working Iris model and deliver its code and results. The week is represented by five simulated working days.")
    table(["Sprint task", "Role", "Estimate"], [
        ["Prepare workspace and libraries", "Scrum Master", "20 min"],
        ["Load and export data", "Data Engineer", "20 min"],
        ["Check data and prepare features", "Data Engineer", "30 min"],
        ["Train the model", "ML Engineer", "30 min"],
        ["Evaluate and add tests", "Tester", "45 min"],
        ["Save and reload the model", "ML Engineer", "20 min"],
        ["Set up Git and Actions", "Scrum Master", "45 min"],
        ["Write report and demo instructions", "Product Owner", "60 min"],
    ], [3.55, 2.3, 1])
    p("The total estimate is 270 minutes. These are planning estimates. A task is considered done when its output works, the relevant tests pass and its instructions are recorded.")

    page("Scrum meeting records")
    h("Step 5 Daily Scrum")
    p("The following updates show how the work would move through the simulated week. Each update answers what was done yesterday, what is planned today and what is blocking progress.")
    table(["Day", "Yesterday", "Today", "Blocker and response"], [
        ["1", "Identify goal and roles", "Create folders and backlog", "Check Python and Git access."],
        ["2", "Prepare the workspace", "Load data and train", "Install missing libraries."],
        ["3", "Prepare the first model", "Evaluate and save it", "Fix any failing tests."],
        ["4", "Check local results", "Set up Actions and a branch", "Check GitHub access and logs."],
        ["5", "Prepare the delivery", "Review results and improve the plan", "Do not accept unfinished checks."],
    ], [.4, 1.7, 2.1, 2.65])
    h("Role updates for simulated day 3")
    table(["Role", "Yesterday", "Today", "Blocker"], [
        ["Product Owner", "Set requirements", "Check progress", "None simulated"],
        ["Scrum Master", "Plan tasks", "Organise updates", "Environment access"],
        ["ML Engineer", "Choose Decision Tree", "Train and save", "Validated data needed"],
        ["Data Engineer", "Load Iris", "Check and split data", "Missing libraries"],
        ["Tester", "Prepare test cases", "Run accuracy checks", "Trained model needed"],
    ], [1.25, 1.7, 2.05, 1.85])
    h("Step 7 Sprint Review")
    p("The review checks the model output, saved files, sample prediction and test results against the backlog. The model reached 100% accuracy on the fixed test split, and all 19 tests passed. The pull request and the main delivery run also passed.")
    h("Step 8 Sprint Retrospective")
    p("Keeping the seed fixed made the results repeatable. Saving the model made it possible to check prediction without training again. The main delays were library installation, restricted network access and temporary-folder permissions. These were resolved during setup and testing.")
    p("For the next Sprint, the tools and libraries should be checked before coding starts. Tests should be added with each task, and the delivered files should be checked before the work is marked complete.")

    page("Model development and results")
    h("Step 6 Build the model")
    p("The project uses the Iris dataset included with scikit-learn. It has 150 rows, four measurements and three flower classes. There were no missing values. One duplicate row was kept so the dataset and split remain the same as the handout.")
    p("The data is split into 120 training rows and 30 test rows. The Decision Tree is fitted only on the training rows. Seed 42 is used for both the split and classifier.")
    source_excerpt("src/iris_demo.py", 34, 43)
    h("Check the input data")
    function_excerpt("src/iris_demo.py", "validate_dataset")
    h("Observed output")
    code("Accuracy: 1.0000 (100.00%)\nTrain/test rows: 120/30\nPrediction: setosa")
    p("All 30 test examples were classified correctly, so the 95% requirement was met. This result belongs to the small fixed test split; more testing would be needed before using the model on new real-world data.")
    table(["Actual class", "Setosa", "Versicolor", "Virginica"],
          [[name, *row] for name, row in zip(metrics["target_names"], metrics["confusion_matrix"])],
          [2.35, 1.5, 1.5, 1.5])
    p("Rows show actual classes and columns show predictions. The diagonal entries add up to 30, with no incorrect predictions in this run.")

    page("Prediction and saving the model")
    h("Prediction code")
    p("Prediction takes sepal length, sepal width, petal length and petal width in centimetres. The code checks that all four values are finite and positive.")
    function_excerpt("src/iris_demo.py", "prediction_details")
    p("The sample input 5.1, 3.5, 1.4, 0.2 gives setosa. The leaf probability is also printed. It describes the training examples in that leaf and should not be treated as a guarantee that a prediction is correct.")
    h("Save the model and reports")
    function_excerpt("src/iris_demo.py", "save_training_outputs")
    p("The saved files are iris_model.joblib, metrics.json, confusion_matrix.csv and iris.csv. A test loads the saved model again and confirms that its predictions match the original model.")
    p("These are excerpts from the project files. The filenames and line numbers can be used to find the same code in VS Code.")

    page("Git and automated testing")
    h("Git commands used")
    code("git init -b main\ngit status\ngit add .\ngit commit -m \"feat: add reproducible Iris classifier\"\ngit log --oneline --graph --all\ngit switch -c feat/prediction-confidence\ngit diff --stat\ngit push -u origin main\ngit push -u origin feat/prediction-confidence\ngit pull --ff-only")
    p("Git was used in the local project to save changes and view history. GitHub was used to share the repository. Setup, model code, tests, workflow and documentation were saved in separate commits. The actual command output is included in docs/evidence/Git_Command_Transcript.md.")
    h("Automated tests")
    p("The tests check the dataset, invalid inputs, accuracy, repeatable training, sample predictions and saved-model loading. They also check that importing the module does not train a model.")
    function_excerpt("tests/test_iris_demo.py", "test_training_is_reproducible_and_meets_acceptance")
    code("python -m pytest -q --junitxml=reports/junit.xml\n19 passed")
    p("The same suite passed in a second clean environment and in GitHub Actions. The downloaded model was also loaded and used successfully.")
    h("Code change used for the CI demonstration")
    p("A feature branch added leaf probability to the prediction output, along with a test and an explanation in the README. This change was checked through pull request 1 before being merged into main.")
    link("Repository", "https://github.com/Divyaprasad-Sahu/mlops-agile-demo")
    link("Pull request", evidence["pr_url"])

    page("CI and delivery workflow")
    p("A push or pull request starts the test job. Delivery runs only on main and only after the tests pass. This connects a code change to testing and a downloadable project package.")
    h("Test job")
    source_excerpt(".github/workflows/ci.yml", 11, 32)
    h("Delivery job")
    source_excerpt(".github/workflows/ci.yml", 34, 57)
    p("The needs field makes delivery depend on the test job. The package contains source, data, model, results and instructions. The JUnit report is available as a separate test-results artifact.")

    page("Final review and result")
    h("Step 9 Sprint Increment")
    p("The final increment contains the working Decision Tree model, Python source, Iris data, accuracy report, automated tests, Scrum records and setup instructions. The model and source are also delivered as a ZIP through GitHub Actions.")
    h("Recorded CI and CD results")
    link("PR checks", evidence["pr_run_url"])
    link("Delivery after merge", evidence["main_run_url"])
    p("Feature commit: " + evidence["feature_sha"][:12] + ". Merge commit: " + evidence["merge_sha"][:12] + ". The PR tests passed; its delivery job was skipped as intended. After merge, both main jobs passed. The delivery artifact was downloaded and its model was checked.")
    h("Rubric checklist")
    table(["Component", "Weight", "Work included"], [
        ["Git commands", "20%", "Repository, commits, history, branch and pushes"],
        ["GitHub management", "20%", "Organised files, useful commits and a passing PR"],
        ["Python organisation", "20%", "Separate source, data, models, tests and docs"],
        ["Automated testing", "20%", "19 passing tests and JUnit results"],
        ["CI/CD", "20%", "PR checks followed by successful model delivery"],
    ], [1.65, .6, 4.6])
    h("Result")
    p("The experiment covers the Scrum activities and produces a working Iris classifier. The model achieved 100% accuracy on the given test split, which is above the required 95%. Git recorded the changes, pytest checked the project, and GitHub Actions tested and delivered it after a code change.")
    h("Viva notes")
    p("The Product Backlog lists all required work; the Sprint Backlog lists the work selected for one Sprint. The review checks the product, while the retrospective looks at how the work can be improved. CI runs the checks, and CD delivers the accepted package.")
    h("References")
    p("Experiment 1 Agile and Scrum Demo course handout; Scrum Guide at scrumguides.org; scikit-learn Iris documentation; GitHub Actions documentation. Detailed records and run logs are included in the project folder.")
    h("Student details")
    p("Name  Divyaprasad Sahu       Roll number  __________________")
    p("Course  __________________       Institution  __________________")
    p("Faculty  __________________       Date  12 October 2026")
