# High-Availability-and-Disaster-Recovery-with-AWS-Serverless-Architecture


# 🌍 AWS Serverless Cross-Region DR Project

This project demonstrates how to build a **highly available and disaster-resilient** serverless application using AWS.

## 📦 Components

- **Amazon DynamoDB Global Tables**: Multi-region data replication
- **AWS Lambda**: Stateless compute functions (Python)
- **Amazon API Gateway**: REST APIs for frontend/backend interaction
- **Amazon Route 53**: DNS-based failover with health checks
- **AWS Certificate Manager**: TLS/SSL for custom domains
- **S3 (optional)**: Static website hosting for frontend

## 🌐 Architecture

![Architecture Diagram](architecture/diagram.png)

## ⚙️ How It Works

1. A user interacts with a simple web frontend hosted via S3 or API Gateway.
2. The frontend makes API calls to the `/write` or `/read` endpoints.
3. These APIs invoke Lambda functions that write to or read from a DynamoDB Global Table.
4. Route 53 health checks enable failover between two regions in case of service disruption.

## 🔧 Setup Steps (from AWS Console)

Each service was configured via the AWS Console:
- ✅ Created DynamoDB with Global Tables (us-east-1, us-west-2)
- ✅ Created IAM Role for Lambda access
- ✅ Deployed Lambda read/write functions in both regions
- ✅ Set up REST APIs in API Gateway with CORS and proxy integration
- ✅ Requested SSL certs via ACM and mapped custom domains
- ✅ Configured Route 53 DNS failover using health checks
- ✅ Built and deployed a responsive frontend (`frontend/index.html`)

## 🖥️ Demo Frontend

HTML + Bootstrap + JavaScript  
Located at: [`frontend/index.html`](frontend/index.html)

## 📜 Lambda Code

- [`lambda/read_function.py`](lambda/read_function.py)
- [`lambda/write_function.py`](lambda/write_function.py)

## ✅ Testing Failover

To simulate a regional failure:
- Delete/disable the primary region's API Gateway
- Route 53 health checks will route traffic to the secondary region
- The frontend continues to work seamlessly

## 📌 Notes

- Health check intervals were set to 30 seconds for quicker response
- DNS propagation may take a few minutes

---

## 🔗 Resources
- [AWS DynamoDB Global Tables](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html)
- [Route 53 Failover Routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html#routing-policy-failover)
