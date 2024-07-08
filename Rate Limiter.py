import time
from collections import defaultdict


class RateLimiter:

    def __init__(self, max_capacity, max_rate):
        self.max_capacity = max_capacity
        self.max_rate = max_rate
        self.allowance = defaultdict(lambda: max_capacity)
        self.last_check = defaultdict(time.time)

    def is_allowed(self, id):
        current_time = time.time()
        elapsed = current_time - self.last_check[id]
        self.last_check[id] = current_time
        refill = elapsed * (self.max_capacity / self.max_rate)
        if refill > 0:
            self.allowance[id] += refill
            print(f"allowance={self.allowance[id]}, refill={refill}")

        if self.allowance[id] > self.max_capacity:
            self.allowance[id] = self.max_capacity  # enforce maximum max_capacity

        if self.allowance[id] < 1.0:
            return False

        self.allowance[id] -= 1.0
        return True


if __name__ == "__main__":
    # Usage
    rate_limiter = RateLimiter(5, 2)

    def api_call(id: str, cnt: int):
        if rate_limiter.is_allowed(id):
            print(f"Call allowed for ID: {id}. cnt={cnt}")
            # proceed with API call
        else:
            print(f"Rate limit exceeded for ID: {id}, cnt={cnt}")

    # Test with some IDs
    cnt = 0
    start = time.time()
    for i in range(10):
        cnt += 1
        api_call("user1", cnt)
        time.sleep(0.1)
    print(f'Ended. Time spent: {time.time()-start} seconds.')
