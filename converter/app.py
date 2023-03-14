import json
from aws_lambda_powertools.tracing import Tracer
from aws_lambda_powertools.logging.logger import Logger


logger = Logger()
tracer = Tracer()

@tracer.capture_method
def on_conversion_job_created(job: dict):
    """
    Process an ConversionJobCreated event
    """
    logger.info({
        "message": "Execute job with id"
    })


@logger.inject_lambda_context
@tracer.capture_lambda_handler
def lambda_handler(event, context):

    logger.info({
        "message":  f"Received event {event}"
    })

    if event["job-type"] == "FileConversion":
        on_conversion_job_created(event["detail"])
    else:
        logger.warning({
            "message": "Unkown job-type {}".format(event["job-type"]),

        })
