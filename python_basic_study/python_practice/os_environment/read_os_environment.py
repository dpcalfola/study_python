import os

secret_django = os.environ.get("study_DRF_django_secret_key")

print(secret_django)

env_all = os.environ
# print(env_all)

env_user = os.environ.get("USER")
print(env_user)
