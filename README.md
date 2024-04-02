# Step Function Exception Handling

All tests are done with a test exectuion of the processing step function.

## Test 1
### Exception is thrown in processing-lambda
### Execution 

{
  "exception": "processing"
}

### Print in exception-handling-lambda

`{'Error': 'Exception', 'Cause': '{"errorMessage":"{\'statusCode\': 500, \'body\': \'exception in the processing lambda\', \'initialEvent\': {\'exception\': \'processing\'}}","errorType":"Exception","requestId":"b6926d73-9bc2-4f5b-a198-c075c1039b3b","stackTrace":["  File \\"/var/task/lambda_function.py\\", line 16, in lambda_handler\\n    raise Exception({\\n"]}'}`


## Test 2
### Exception is thrown in inner-processing-lambda

{
  "exception": "inner_processing"
}

### Print in exception-handling-lambda

`{'Error': 'Exception', 'Cause': '{"errorMessage":"{\'statusCode\': 500, \'body\': \\"\'exception\'\\", \'initialEvent\': {\'exception\': \'inner_processing\'}}","errorType":"Exception","requestId":"0c89effd-6f4e-4c55-87ec-b79297ea332a","stackTrace":["  File \\"/var/task/lambda_function.py\\", line 16, in lambda_handler\\n    raise Exception({\\n"]}'}`


## Test 3
### Exception is not thrown anywhere

{
  "exception": "none"
}

#### Print in exception-handling-lambda

(N/A because there was no exception)
