import { Octokit } from "octokit";
import dotenv from 'dotenv';
import buffer from 'buffer';



dotenv.config()

const octokit = new Octokit({
  auth: process.env.ACCESS_TOKEN
});

try {
  const response = await octokit.request('GET /repos/{owner}/{repo}/contents/{path}', {
      owner: 'arnavvjainn',
      repo: 'SPshORTS',
      path: 'backend/app.py',
      headers: {
          'X-GitHub-Api-Version': '2022-11-28'
      }
  });
  const content = response.data.content;
  const decodedContent = Buffer.from(content, 'base64').toString('utf-8');
  console.log(decodedContent);
} catch (error) {
  console.error('Error fetching repository data:', error);
}