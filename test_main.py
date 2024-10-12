import pytest
from httpx import AsyncClient, ASGITransport
from fastapi import status
from main import app
from app.models import Item
from datetime import datetime, timezone

@pytest.mark.asyncio
async def test_create_item():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        item_data = {
            "name": "Test Item",
            "quantity": 5,
            "email": "test@example.com",
            "item_name": "Test Item",
            "expiry_date": datetime.now(timezone.utc).isoformat()  # Use timezone-aware datetime
        }
        response = await ac.post("/items", json=item_data)
        assert response.status_code == status.HTTP_200_OK
        assert "inserted_data" in response.json()
        assert "_id" in response.json()

@pytest.mark.asyncio
async def test_filter_items():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/items/filter", params={"email": "test@example.com"})
        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_get_item_count_by_email():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/items/aggregation")
        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_read_item():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # First, create an item to ensure there is an item to read
        item_data = {
            "name": "Test Item",
            "quantity": 5,
            "email": "test@example.com",
            "item_name": "Test Item",
            "expiry_date": datetime.now(timezone.utc).isoformat()  # Use timezone-aware datetime
}
        create_response = await ac.post("/items", json=item_data)
        item_id = create_response.json()["_id"]

        response = await ac.get(f"/items/{item_id}")
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["_id"] == item_id

@pytest.mark.asyncio
async def test_delete_item():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # First, create an item to ensure there is an item to delete
        item_data = {
            "name": "Test Item",
            "quantity": 5,
            "email": "test@example.com",
            "item_name": "Test Item",
            "expiry_date": datetime.now(timezone.utc).isoformat()  # Use timezone-aware datetime
}
        create_response = await ac.post("/items", json=item_data)
        item_id = create_response.json()["_id"]

        response = await ac.delete(f"/items/{item_id}")
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["message"] == "Item deleted successfully"

@pytest.mark.asyncio
async def test_update_item():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # First, create an item to ensure there is an item to update
        item_data = {
            "name": "Test Item",
            "quantity": 5,
            "email": "test@example.com",
            "item_name": "Test Item",
            "expiry_date": datetime.now(timezone.utc).isoformat()  # Use timezone-aware datetime
}
        create_response = await ac.post("/items", json=item_data)
        item_id = create_response.json()["_id"]

        updated_item_data = {
            "name": "Test Item",
            "quantity": 5,
            "email": "test@example.com",
            "item_name": "Test Item",
            "expiry_date": datetime.now(timezone.utc).isoformat()  # Use timezone-aware datetime
}
        response = await ac.put(f"/items/{item_id}", json=updated_item_data)
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["message"] == "Item updated successfully"

@pytest.mark.asyncio
async def test_create_clock_in():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        clock_in_data = {
            "email": "test_user@example.com",
            "inserted_data": datetime.now(timezone.utc).isoformat(),  # Use timezone-aware datetime
            "location": "Office"
        }
        response = await ac.post("/clock_in", json=clock_in_data)
        assert response.status_code == status.HTTP_200_OK
        assert "clock_in_time" in response.json()
        assert "_id" in response.json()

@pytest.mark.asyncio
async def test_read_clock_in():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # First, create a clock-in record to ensure there is one to read
        clock_in_data = {
            "email": "test_user@example.com",
            "inserted_data": datetime.now(timezone.utc).isoformat(),  # Use timezone-aware datetime
            "location": "Office"
        }
        create_response = await ac.post("/clock_in", json=clock_in_data)
        clock_in_id = create_response.json()["_id"]

        response = await ac.get(f"/clock_in/{clock_in_id}")
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["_id"] == clock_in_id

@pytest.mark.asyncio
async def test_update_clock_in():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # First, create a clock-in record to ensure there is one to update
        clock_in_data = {
            "email": "test_user@example.com",
            "inserted_data": datetime.now(timezone.utc).isoformat(),  # Use timezone-aware datetime
            "location": "Office"
        }
        create_response = await ac.post("/clock_in", json=clock_in_data)
        clock_in_id = create_response.json()["_id"]

        updated_clock_in_data = {
            "email": "test_user@example.com",
            "inserted_data": datetime.now(timezone.utc).isoformat(),  # Use timezone-aware datetime
            "location": "Office"
        }
        response = await ac.put(f"/clock_in/{clock_in_id}", json=updated_clock_in_data)
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["message"] == "Clock-In updated successfully"

@pytest.mark.asyncio
async def test_delete_clock_in():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        # First, create a clock-in record to ensure there is one to delete
        clock_in_data = {
            "email": "test_user@example.com",
            "inserted_data": datetime.now(timezone.utc).isoformat(),  # Use timezone-aware datetime
            "location": "Office"
        }
        create_response = await ac.post("/clock_in", json=clock_in_data)
        clock_in_id = create_response.json()["_id"]

        response = await ac.delete(f"/clock_in/{clock_in_id}")
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["message"] == "Clock-In deleted successfully"

@pytest.mark.asyncio
async def test_get_all_clock_ins():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/clock_in")
        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.json(), list) 