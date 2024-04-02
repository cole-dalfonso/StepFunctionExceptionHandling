import json

def lambda_handler(event, context):
    try:
        # Perform processing tasks with the input data
        processed_data = process_data(event)
        
        # Return processed data
        return {
            'statusCode': 200,
            'body': json.dumps(processed_data),
            'initialEvent' : event # Only because this is the very first lambda after the start
        }
    except Exception as e:
        # If an error occurs, raise an exception with appropriate error message
        raise Exception({
            'statusCode': 500,
            'body': format(str(e)),
            'initialEvent' : event
        })

def process_data(data):
    # Implement your processing logic here
    # This is where you would perform the actual processing tasks
    # You can also include error handling logic within this function
    if(data["exception"] == "processing"):
         raise Exception("exception in the processing lambda")
    else:
        pass
