## Using MLflow for Experiment Tracking and Model Management
### Intoduction
This project takes sentiment analysis to the next level by seamlessly integrating MLflow for robust experiment tracking, model management, and improved reproducibility. Also, it uses the Prefect for that helps us build organized and efficient data pipelines, especially for machine learning. 
It allows us to:
- Break down complex tasks: Prefect lets you divide your data processing or machine learning workflow into smaller, reusable steps called tasks.
- Manage task order: It cleverly manages the order in which these tasks run, ensuring everything happens at the right time.
- Keep an eye on progress: Prefect monitors your workflows as they run, catching any errors and offering visualizations to help you troubleshoot.

### Completed Tasks are :
- [✅] Integrate MLflow into your existing machine learning projects.
- [✅] Train machine learning models while logging relevant information with MLflow.
- [✅] Demonstrate how to log parameters, metrics, and artifacts using MLflow tracking APIs.
- [✅] Customizing MLflow UI with run names.
- [✅] Demonstrate metric plots.
- [✅] Demonstrate hyperparameter plots.
- [✅] Demonstrate how to register models and manage by tagging them.
- [✅] `(BONUS)` Build a Prefect Workflow and Auto Schedule it. Show the Prefect Dashboard with relevant outputs.

### Tools Used:
- `MLflow` : Open-source platform for managing the Machine Learning (ML) lifecycle.
   - *Streamlines deployment*: Simplifies the process of deploying models to production.
   - *Automates workflows*: Integrates with tools for experiment scheduling and deployment pipelines.

- `Prefect` : Manages task dependencies and execution order with scheduling options.
- `DagsHub` : Collaborative platform for data science and ML projects.

#### Relationship among the used tools are as follows: 
- `MLflow` and `Prefect` are complementary tools. `MLflow` focuses on ML experiment tracking and model management, while `Prefect` excels at building and orchestrating workflows (including ML workflows). They can work together for comprehensive ML lifecycle management.

- `DagsHub` offers functionalities similar to both `MLflow` and `Prefect`, with an emphasis on collaboration and version control. It can integrate with MLflow for experiment tracking and leverage Prefect for workflow orchestration within its platform.
