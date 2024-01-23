#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import unittest
import os

from pyspark.sql import SparkSession


class PySparkJIRATests(unittest.TestCase):
    def test_basic_load(self):
        spark = SparkSession.builder.getOrCreate()
        jira_username = os.environ.get("JIRA_USERNAME")
        jira_api_token = os.environ.get("JIRA_API_TOKEN")
        jql_query = "project = 'ES'"
        df = (
            spark.read.format("jira")
                .option("JIRA_USERNAME", jira_username)
                .option("JIRA_API_TOKEN", jira_api_token)
                .load(jql_query)
        )
        self.assertTrue(df.count() > 0)


if __name__ == '__main__':
    unittest.main()
