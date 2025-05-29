🧯 Troubleshooting Guide for High Availability App

1. CORS Errors (Access-Control-Allow-Origin)

Error: No 'Access-Control-Allow-Origin' header is present on the requested resource.

Solution:

Go to each method (GET /read, POST /write, and their OPTIONS) in both AWS regions.

Under Method Response and Integration Response, manually add headers:

Access-Control-Allow-Origin: *

Access-Control-Allow-Methods: GET,POST,OPTIONS

Access-Control-Allow-Headers: Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token

Save and deploy the API.

2. Domain Access Issues (403/404)

Error: Accessing https://myprojectapp.xyz gives 403 Forbidden or 404 Not Found.

Solution:

Ensure the API Gateway base path mapping is set to / for the custom domain.

Verify that the ACM SSL certificate is correctly issued and covers your domain.

In Route 53, check if A-record (alias) is pointing to the correct API Gateway.

3. Missing Authentication Token

Error: {"message":"Missing Authentication Token"}

Solution:

Ensure you are using valid API paths like /read or /write, not just the base URL.

Example: https://myprojectapp.xyz/read

4. Lambda Not Triggering or No Logs in CloudWatch

Symptoms: Nothing appears in logs when invoking API.

Solution:

Open CloudWatch Logs for the Lambda function.

Add print(event) at the start of the lambda_handler function.

Confirm Lambda has permissions via the resource-based policy to be invoked by API Gateway (apigateway.amazonaws.com).

5. Data Not Instantly Updating in Web UI

Symptoms: Data is saved but not displayed right away.

Solution:

Ensure readData() is called after writeData() completes successfully.

Clear the input fields after saving using JavaScript to improve UX.

6. UI Error: Failed to Write Data

Symptoms: Alert message Failed to write data. after pressing Save.

Solution:

Confirm API CORS headers are correctly configured.

Debug using browser Console logs and inspect network requests.

Use valid JSON body format and ensure DynamoDB table name and region are correctly set in Lambda.

7. Changes Not Showing Up

Symptoms: Even after changes, API doesn’t reflect updates.

Solution:

After every change in API Gateway, click Deploy API.

Do a hard refresh in browser (Ctrl+Shift+R or Cmd+Shift+R).
