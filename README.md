## Features

- Create and manage payment transactions
- Query transaction history and status
- RESTful API endpoints
- Transaction status tracking (pending, completed, failed, cancelled)
- Built with FastAPI for high performance

## Prerequisites

- Python 3.8+
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Cosmolost/payment-dai-api.git
cd payment-dai-api
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file from the example:
```bash
cp .env.example .env
```

5. Update `.env` with your configuration

## Running the API

Start the development server:
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload
```
## Endpoints

### Health Check
- `GET /health` - Check API health status

### Transactions

#### Create Transaction
- `POST /transactions`
- Request body:
```json
{
  "amount": 100.0,
  "currency": "EUR",
  "recipient_address": "0x1234567890abcdef...",
  "description": "Payment for services"
}
```

#### Get Transaction
- `GET /transactions/{transaction_id}`

#### List Transactions
- `GET /transactions?status=pending&limit=10`

#### Update Transaction Status
- `PATCH /transactions/{transaction_id}/status`
- Request body:
```json
{
  "status": "completed"
}
```

Valid statuses: `pending`, `completed`, `failed`, `cancelled`

## Project Structure

```
payment-dai-api/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
└── README.md           # This file
```

## Future Enhancements

- [ ] Database integration (PostgreSQL/MySQL)
- [ ] Web3 integration for actual DAI transactions
- [ ] User authentication and authorization
- [ ] Transaction webhooks
- [ ] Rate limiting
- [ ] Comprehensive logging
- [ ] Unit and integration tests
- [ ] Docker containerization

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - See LICENSE file for details

## Support

For issues and questions, please open an issue on the repository.
