# PySpark JIRA Data Source


```bash
pip install pyspark-jira
```

```python
jira_username = "Your full email address that you used for logging in"
jira_api_token = "See https://id.atlassian.com/manage-profile/security"
jql_query = "project = 'ES'"
df = (
    spark.read.format("jira")
        .option("JIRA_USERNAME", jira_username)
        .option("JIRA_API_TOKEN", jira_api_token)
        .load(jql_query)
)
df.show()
```
