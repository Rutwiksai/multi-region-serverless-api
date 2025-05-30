
# 🌐 High Availability Serverless App with AWS

This project demonstrates a fully serverless, regionally redundant web app using:

- **Amazon API Gateway**
- **AWS Lambda**
- **Amazon DynamoDB**
- **Amazon S3**
- **Route 53 with Failover Routing**
- **Custom Domain (https://myprojectapp.xyz)**

---

## ⚙️ Architecture

![AWS_Architecture](https://github.com/user-attachments/assets/d60070fb-a4df-4bb6-ad9a-59817b1138f5)


---

## 🚀 Features

- Add and read data (Item ID + Data).
- Read data loads automatically on page load.
- Serverless architecture with **regional redundancy**.
- Configured CORS, domain, and HTTPS.
- Publicly accessible via `https://myprojectapp.xyz/`.

---

## 🧪 Test Instructions

Open app in browser:

```
https://myprojectapp.xyz/
```

---

## 🛠️ Setup Checklist

### 1. Backend
- ✅ Create Lambda functions for `/read` and `/write`
- ✅ Attach to API Gateway in both regions
- ✅ Configure CORS
- ✅ Deploy stages

### 2. Domain & DNS
- ✅ Register domain via Route 53 / GoDaddy
- ✅ Create SSL cert in ACM for `api.myprojectapp.xyz`
- ✅ Add A records with failover for `api.myprojectapp.xyz`
- ✅ Base path mapping from API Gateway custom domain

### 3. Frontend
- ✅ Create HTML + JS
- ✅ Replace endpoint in `apiUrl` with `https://api.myprojectapp.xyz`
- ✅ Upload HTML to public S3 bucket
- ✅ Bucket policy: public-read
- ✅ Optional: Serve via CloudFront

---

## 🧩 Troubleshooting Tips

| Issue | Fix |
|------|------|
| ❌ CORS error | Ensure CORS is enabled on API Gateway Method & Integration Response |
| ❌ `Missing Authentication Token` | Check `/write` and `/read` are deployed to correct stage |
| ❌ App only accessible via S3 URL | Set up CloudFront or Route 53 record for root domain |
| ❌ Write works but Read doesn’t | Check DynamoDB IAM role & region-specific configs |
| ❌ `403 Forbidden` or `SSL error` | Certificate not validated, domain not mapped |
| ❌ HTML changes not reflected | Re-upload HTML to S3 with correct `apiUrl` |
| ❌ `Bad request` in Route 53 | Remove conflicting A records before creating failover |

---

## 💰 Cost Considerations

| Service | Pricing Info |
|---------|---------------|
| Lambda | Free tier covers 1M requests/month |
| DynamoDB | Free tier covers 25GB storage & reads/writes |
| API Gateway | Pay per call (~$3/million) |
| Route 53 | ~$0.50/month per hosted zone |
| S3 | Free for low storage & traffic |
| ACM | SSL certs are **FREE** via ACM |

---

Built by Rutwik Sai Kanderi — feel free to raise issues or suggestions!

