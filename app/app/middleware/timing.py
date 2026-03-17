import time

async def timing_middleware(request, call_next):
    start = time.time()
    response = await call_next(request)
    print("Request time:", time.time() - start)
    return response
