import time
from collections import defaultdict


class RateLimiter:

    def __init__(self, rate, per):
        self.rate = rate
        self.per = per
        self.allowance = defaultdict(lambda: rate)
        self.last_check = defaultdict(time.time)

    def is_allowed(self, id):
        current_time = time.time()
        elapsed = current_time - self.last_check[id]
        self.last_check[id] = current_time
        refill = elapsed * (self.rate / self.per)
        if refill > 0:
            self.allowance[id] += refill
            print(f"allowance={self.allowance[id]}, refill={refill}")

        if self.allowance[id] > self.rate:
            self.allowance[id] = self.rate  # enforce maximum rate

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
