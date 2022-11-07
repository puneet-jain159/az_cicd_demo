# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC # Sample notebook

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Aux steps for auto reloading of dependent files

# COMMAND ----------

# MAGIC %load_ext autoreload
# MAGIC %autoreload 2

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Example usage of existing code

# COMMAND ----------

from az_cicd_demo.tasks.sample_ml_task import SampleMLTask

pipeline = SampleMLTask._get_pipeline()
print(pipeline)

# COMMAND ----------

print("this is a additional comment I make")
