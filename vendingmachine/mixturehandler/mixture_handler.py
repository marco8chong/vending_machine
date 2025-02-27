"""
mixture_handler.py

This script implements an mixture handler for vending machine that
handling the mixture proportions of plain water and fizzy water.

Author: Marco Chong (marco@marcochong.com)
"""

class MixtureHandler:

    _mixture = {}

    def __init__(self):
        pass

    @property
    def supported_mixtures(self):
        return dict(self._mixture)

    def add_supported_mixture(self, mixture_id: int, mixture: dict):
        if isinstance(mixture, dict):
            self._mixture[mixture_id] = mixture

    def clear_supported_mixtures(self):
        self._mixture = {}

    def get_supported_mixtures(self, mixture_id: int):
        if mixture_id in self._mixture:
            return dict(self._mixture[mixture_id])
        else:
            return {}