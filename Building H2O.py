import threading
from typing import Callable


class H2O:

    def __init__(self):
        self._mu = threading.Lock()
        self._need_h = threading.Condition(self._mu)
        self._need_o = threading.Condition(self._mu)
        self._num_h = 0
        self._num_o = 0

    def hydrogen(self, releaseHydrogen: "Callable[[], None]") -> None:
        with self._mu:
            while self._num_h == 2:
                self._need_o.wait()
            self._num_h += 1
            releaseHydrogen()
            self._maybeNotifyLocked()

    def oxygen(self, releaseOxygen: "Callable[[], None]") -> None:
        with self._mu:
            while self._num_o == 1:
                self._need_h.wait()
            self._num_o += 1
            releaseOxygen()
            self._maybeNotifyLocked()

    def _maybeNotifyLocked(self):
        assert self._mu.locked()
        if self._num_h == 2 and self._num_o == 1:
            self._num_h = 0
            self._num_o = 0
            self._need_o.notify()
            self._need_h.notify(n=2)


if __name__ == '__main__':
    releaseHydrogen = lambda: print('H', end="")
    releaseOxygen = lambda: print("O", end="")
    h2o = H2O()

    ts = []
    for _ in range(20):
        ts.append(threading.Thread(h2o.oxygen(releaseOxygen)))
        ts.append(threading.Thread(h2o.hydrogen(releaseHydrogen)))
        ts.append(threading.Thread(h2o.hydrogen(releaseHydrogen)))

    for t in ts:
        t.start()

    for t in ts:
        t.join()
