from openai import OpenAI
client = OpenAI()
# upload training file using File API
client.files.create(
  file=open("mydata.jsonl", "rb"),
  purpose="fine-tune"
)
#Start a fine-tuning job using the OpenAI SDK
client.fine_tuning.jobs.create(
  training_file="file-abc123", # File id created while uploading
  model="gpt-4o-mini-2024-07-18"
)
# Retrieve the state of a fine-tune
client.fine_tuning.jobs.retrieve("ftjob-abc123")
# Use a fine tune job
completion = client.chat.completions.create(
  model="ft:gpt-4o-mini:my-org:custom_suffix:id",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)
print(completion.choices[0].message)