# CreateCICD
This should allow you to create CI/CD pipelines for your applciations automatically. You just enter the github repo information, we'll analyze what your applicaton does and hopefully you get a YAML file that would create the CICD pipeline. This is currently only for javascript applications and creating a CI pipeline using Github Actions

## Plan of Action
- The plan is to create a package that you could install using CLI. 
- On running the command:
- read your package.json file -> send it to the api -> use together api's chat completion and prompt engineering to create a github action workflow -> create the file in your repository -> use the github api to create a worflow with the configuration -> display the status of the pipeline in the command line ( a progress bar or an status indicator)

## Current Status
- I am currently using together api's to generate the YAML file using prompt engineering. I am copying the contents of package.json file and passing it in the prompt. This is not at all accurate, just trying to get a proof of concept.
- Then the plan is to either fine-tune a model using package.json to Workflow files, input-output pairs or use a lot better prompt engineering.
- I am very new to this whole LLM scene, so let it rip 

### If you have any suggestions please let me know, you can find my email in my profile

