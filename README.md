# GitLabBulk

This is a simple python script to clone all the projects under a given group in GitLab. 

**Note:** Will not download nested groups recursviely.  

## Similar Tools
[GitLabber](https://github.com/ezbz/gitlabber)

## Prerequisites

- Python 3

## Usage

```
app.py -u <repository-url> -g <group-id> -t <personal-aceess-token>
```

This will replicate the repository folder structure in your local file system. Personal access token should have `read_api` and `read_repository permission`
