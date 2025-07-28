# API Documentation – Pandang Istana Demo

## 1. Register New Guest

**POST** `/register_guest`  
Creates a new guest record and returns guest ID and QR code.

### Request Body (JSON)

```json
{
  "name": "Susilo Yudi",
  "institution": "Ministry of Finance",
  "email": "Susilo.yudi@kemenkeu.go.id"
}
