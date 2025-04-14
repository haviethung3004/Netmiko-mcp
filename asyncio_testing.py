import asyncio

async def fetch_data(name, delay):
    print(f"Starting {name}...")
    await asyncio.sleep(delay)  # Simulates an I/O operation (e.g., network request)
    print(f"Finished {name} after {delay} seconds")
    return f"Data from {name}"

async def main():
    # Run multiple coroutines concurrently
    results = await asyncio.gather(
        fetch_data("Task 1", 2),
        fetch_data("Task 2", 1),
        fetch_data("Task 3", 3)
    )
    print("Results:", results)

# Run the event loop
asyncio.run(main())