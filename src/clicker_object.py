import pyautogui

from time import sleep

from configs import TIME_TO_START
from configs import CLICKS
from configs import DURATION
from configs import MILLISECOND


class Clicker:
    def __init__(
            self,
            time_to_start: float = TIME_TO_START,
            clicks: int = CLICKS,
            duration: float = DURATION
    ) -> None:
        self._time_to_start = time_to_start
        self._clicks = clicks
        self._duration = duration

    @property
    def time_to_start(self) -> float:
        return self._time_to_start

    @time_to_start.getter
    def time_to_start(self) -> float:
        return self._time_to_start

    @property
    def clicks(self) -> float:
        return self._clicks

    @clicks.getter
    def time_to_end(self) -> float:
        return self._clicks

    @property
    def duration(self) -> float:
        return self._duration

    @duration.getter
    def duration(self) -> float:
        return self._duration

    def start(self) -> None:
        if self._time_to_start:
            time_to_start = self._time_to_start

            while time_to_start > 0:
                print(f"До старта кликера {time_to_start:.3f} секунд.\nУспейте разместить курсор!\n")
                sleep(MILLISECOND)

                time_to_start -= MILLISECOND

        print("Старт!")

        mouse_position = pyautogui.position()
        pyautogui.click(
            *mouse_position,
            self._clicks,
            self._duration
        )

        print("Конец")
