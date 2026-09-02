"""TTY-aware terminal rendering with guaranteed cursor restoration."""

from __future__ import annotations

from collections.abc import Mapping
import os
import sys
from typing import TextIO

from .engine import AxisSpec, AxisStatus, EngineConfig, EngineTick, SimulationResult


class TerminalRenderer:
    """Render simulation progress without emitting ANSI escapes to non-TTYs.

    ``NO_COLOR`` always disables color. Cursor hiding is used only for a live
    TTY display and is undone by :meth:`__exit__`, including on exceptions.
    """

    RESET = "\033[0m"
    BOLD = "\033[1m"
    CYAN = "\033[36m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    HIDE_CURSOR = "\033[?25l"
    SHOW_CURSOR = "\033[?25h"

    def __init__(
        self,
        stream: TextIO | None = None,
        *,
        color: bool | None = None,
        live: bool = False,
        environ: Mapping[str, str] | None = None,
    ) -> None:
        self.stream = stream or sys.stdout
        environment = os.environ if environ is None else environ
        isatty = getattr(self.stream, "isatty", None)
        self.is_tty = bool(callable(isatty) and isatty())
        self.color_enabled = (
            self.is_tty and color is not False and "NO_COLOR" not in environment
        )
        self.live = bool(live and self.is_tty)
        self._cursor_hidden = False

    def __enter__(self) -> TerminalRenderer:
        if self.live and not self._cursor_hidden:
            self.stream.write(self.HIDE_CURSOR)
            self.stream.flush()
            self._cursor_hidden = True
        return self

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> bool:
        if self._cursor_hidden:
            self.stream.write(self.SHOW_CURSOR)
            self.stream.flush()
            self._cursor_hidden = False
        return False

    def render_start(
        self, specs: tuple[AxisSpec, ...], config: EngineConfig
    ) -> None:
        labels = ", ".join(spec.label for spec in specs)
        self._line(
            self._paint(
                f"Prime Axis simulation: {labels} "
                f"(bounds {config.lower_bound}..{config.upper_bound})",
                self.BOLD + self.CYAN,
            )
        )

    def render_tick(self, tick: EngineTick) -> None:
        parts: list[str] = []
        for axis in tick.axes:
            color = {
                AxisStatus.ACTIVE: self.CYAN,
                AxisStatus.ANCHORED: self.GREEN,
                AxisStatus.FAILED: self.RED,
            }[axis.status]
            marker = " rerouted" if axis.rerouted else ""
            parts.append(
                self._paint(
                    f"{axis.label}={axis.node} {axis.status.value}{marker}", color
                )
            )
        self._line(
            f"tick {tick.clock.opportunity_index:04d} "
            f"t={tick.clock.lattice_time_s:.3f}s | " + " | ".join(parts)
        )

    def render_complete(self, result: SimulationResult) -> None:
        if result.succeeded:
            text = f"Complete: all axes anchored in {result.opportunities} opportunities."
            self._line(self._paint(text, self.BOLD + self.GREEN))
            return
        failures = ", ".join(
            f"{axis.label}: {axis.error or axis.status.value}"
            for axis in result.axes
            if axis.status is AxisStatus.FAILED
        )
        self._line(self._paint(f"Simulation incomplete: {failures}", self.BOLD + self.RED))

    def _paint(self, text: str, code: str) -> str:
        if not self.color_enabled:
            return text
        return f"{code}{text}{self.RESET}"

    def _line(self, text: str) -> None:
        self.stream.write(text + "\n")
        self.stream.flush()


__all__ = ["TerminalRenderer"]
