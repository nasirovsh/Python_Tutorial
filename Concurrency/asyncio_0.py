"""
At the heart of async IO are coroutines. A coroutine is a specialized version of a Python generator function.
A coroutine is a function that can suspend its execution before reaching return, and it can indirectly pass control to another coroutine for some time.
"""
import asyncio

async def count():
	print("One")
	await asyncio.sleep(1)
	print("Two")

async def main():
	await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
	import time
	s = time.perf_counter()
	asyncio.run(main())
	elapsed = time.perf_counter() - s
	print(f"{__file__} executed in {elapsed:0.2f} seconds.")

"""
<<< output >>>
One
One
One
Two
Two
Two
asyncio_0.py executed in 1.00 seconds.
"""			