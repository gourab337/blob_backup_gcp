import subprocess
import datetime

def backup_to_gcs(source_file_path, bucket_name, destination_blob_name, service_account_key_path):
    project_id = "ayushpay-v1"
    project_command = f"gcloud config set project {project_id}"
    activate_service_account_command = f"gcloud auth activate-service-account --key-file={service_account_key_path}"
    copy_command = f"gcloud alpha storage cp {source_file_path} gs://{bucket_name}/{destination_blob_name}"

    subprocess.run(project_command, shell=True)
    subprocess.run(activate_service_account_command, shell=True)
    subprocess.run(copy_command, shell=True)

source_file = "file.txt"
bucket_name = "ayushpay-v1"
today = datetime.datetime.now().strftime("%Y-%m-%d")
destination_blob = f"metabase/{today}-{source_file}"
service_account_key_path = "service_account_key.json"

backup_to_gcs(source_file, bucket_name, destination_blob, service_account_key_path)
