# CreateCICD
This should allow you to create CI/CD pipelines for your applciations automatically. You just enter the github repo information, we'll analyze what your applicaton does and hopefully you get a YAML file that would create the CICD pipeline

# Plan of Action
The plan is to create a package that you could install using CLI. 
On running the command:
it will read your package.json file -> send it to the api -> using together api's chat completion and prompt engineering create a github action workflow -> create the file in your repository -> use the github api to create a worflow with the configuration -> display the status of the pipeline in the command line ( a progress bar or an status indicator)


