from celery import shared_task


@shared_task
def query_youtube_data_api():
    print("The task just ran.")