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

### Screenshots
#### `MLflow Dashboard and Registered Model`
![Screenshot (140)](https://github.com/vjabhi000985/MLflow_Prefect_Orchestration/assets/46738718/857b714b-0ff0-4622-b947-3df24948ae61)
![Screenshot (139)](https://github.com/vjabhi000985/MLflow_Prefect_Orchestration/assets/46738718/d986dd3d-9023-4fc0-9f77-f27ce8e555fd)

#### `Prefect Dashboard and Workflow`
![Screenshot (143)](https://github.com/vjabhi000985/MLflow_Prefect_Orchestration/assets/46738718/7bb9b3b9-8bc6-4919-9a1a-773cea73e411)
![Screenshot (144)](https://github.com/vjabhi000985/MLflow_Prefect_Orchestration/assets/46738718/f1d88a6d-4478-4067-9276-9394aead4952)
