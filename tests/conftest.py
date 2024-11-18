# -*- coding: utf-8 -*-

import pytest

from tf_registry import RegistryClient


@pytest.fixture
def client() -> RegistryClient:
    return RegistryClient()
