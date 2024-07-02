import httpx
import asyncio


async def fetch():
    async with httpx.AsyncClient(http2=True) as client:
        response = await client.get("http://localhost:9988")
        print("Status Code:", response.status_code)
        print("Response Body:", response.json())


if __name__ == "__main__":
    asyncio.run(fetch())
