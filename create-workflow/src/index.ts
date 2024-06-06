import express, { Request, Response } from 'express';
import bodyParser from 'body-parser';

const app = express();
const port = 3000;

app.use(bodyParser.json());

interface PackageJsonRequest extends Request {
  body: {
    packageJson: string;
  };
}

app.post('/api/generate-workflow', (req: PackageJsonRequest, res: Response) => {
  const { packageJson } = req.body;

  // Your logic to generate workflow YAML from package.json
  const workflowYaml = `
name: CI

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Node.js
        uses: actions/setup-node@v2
        with:
          node-version: '14'
      - name: Install dependencies
        run: npm install
      - name: Run tests
        run: npm test
  `;

  res.json({ workflowYaml });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
