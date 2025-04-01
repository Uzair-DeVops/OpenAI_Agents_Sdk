# import time

# def task1():
#     print("Task 1: Starting")
#     time.sleep(5)  # This call blocks the entire program for 3 seconds.
#     print("Task 1: Finished")

# def task2():
#     print("Task 2: Starting")
#     print("Task 2: Finished quickly")

# def main():
#     task1()  # Blocking: the program waits here until task1 finishes.
#     task2()  # Only starts after task1 is complete.

# if __name__ == "__main__":
#     main()


import asyncio

async def task1():
    print("Task 1: Starting")
    await asyncio.sleep(5)  # Non-blocking sleep; the event loop can run other tasks.
    print("Task 1: Finished")

async def task2():
    print("Task 2: Starting")
    print("Task 2: Finished quickly")

async def main():
    # Schedule both tasks concurrently.
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    await asyncio.gather(t1, t2)

if __name__ == "__main__":
    asyncio.run(main())


# import asyncio

# async def bake_lasagna():
#     print("Cook: Putting lasagna in the oven...")
#     # Simulate a slow task (like baking) with asyncio.sleep
#     await asyncio.sleep(3)  
#     print("Cook: Lasagna is done baking!")
#     return "baked lasagna"

# async def chop_veggies():
#     print("Cook: Starting to chop vegetables for the salad...")
#     # Simulate chopping time with asyncio.sleep
#     await asyncio.sleep(2)  
#     print("Cook: Finished chopping vegetables!")
#     return "chopped veggies"

# async def prepare_meal():
#     # Start baking the lasagna (this begins the slow task)
#     baking_task = asyncio.create_task(bake_lasagna())
    
#     # While the lasagna is baking, start chopping veggies.
#     veggies = await chop_veggies()
    
#     # Now wait for the lasagna to finish baking.
#     lasagna = await baking_task
    
#     # Assemble the meal using both results.
#     print(f"Cook: Assembling the meal with {lasagna} and {veggies}.")

# if __name__ == "__main__":
#     asyncio.run(prepare_meal())
