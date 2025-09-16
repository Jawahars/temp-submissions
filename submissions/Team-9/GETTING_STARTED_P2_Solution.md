# GETTING_STARTED.md

Welcome! This guide will help you integrate with our API. Follow the steps below to authenticate, interact with endpoints, and format your requests and responses.

---

## Authentication

All requests require header-based authentication:

```
X-API-KEY: <your_api_key>
```

Include your API key in the `X-API-KEY` header for every request.

---

## Endpoints

### 1. Add Product

- **Method:** POST  
- **URL:** `/products`  
- **Request Body:**  
  ```json
  {
    "name": "Product Name",
    "sku": "SKU123",
    "price": 99.99
  }
  ```
- **Response:**  
  Returns the new product object with its ID.

---

### 2. Get Orders for Customer

- **Method:** GET  
- **URL:** `/customers/{id}/orders`  
- **Response:**  
  ```json
  [
    {
      "orderId": "ORD001",
      "amount": 150.00,
      "status": "processing"
    }
  ]
  ```

---

### 3. Update Order Status

- **Method:** PUT  
- **URL:** `/orders/{id}/status`  
- **Request Body:**  
  ```json
  {
    "status": "shipped"
  }
  ```
- **Response:**  
  Returns the updated order object.

> **Note:** The possible order statuses are `pending`, `processing`, and `shipped`.  
> The update order status endpoint is a priority (per Sarah).

---

## JSON Guidelines

### example_1: Product Object (Required)
```json
{
  "name": "Product Name",
  "sku": "SKU123",
  "price": 99.99
}
```

### example_2: Array of Order Objects (Required)
```json
[
  {
    "orderId": "ORD001",
    "amount": 150.00,
    "status": "processing"
  }
]
```

### example_3: Order Status Object (Optional)
```json
{
  "status": "shipped"
}
```

### user_profile_response: User Profile Object (Required)
```json
{
  "userId": "USR001",
  "name": "Jane Doe",
  "join_date": "2025-09-09"
}
```

---

## General Guidelines

- All strings must be UTF-8 encoded.
- Numbers must be JSON numbers (no quotes).
- Dates must use ISO 8601 format (`YYYY-MM-DD`).
- Use arrays for collections of objects.

---

For further questions, please contact our API support team.

