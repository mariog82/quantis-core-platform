# SDK Usage

```python
from sdk import QuantisClient, SDKConfig

client = QuantisClient(SDKConfig(base_url="http://localhost:8000"))
response = client.health()
assert response.success
```
