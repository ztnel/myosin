# -*- coding: utf-8 -*-
"""
Base Model Abstract
===================
Modified: 2021-12

Dependencies:
-------------
```
```
"""

import logging
from typing import Any, Dict
from modelio.typing import _PKey
from abc import ABC, abstractmethod
from modelio.etc.formatter import pformat


class BaseModel(ABC):

    def __init__(self, _id: _PKey) -> None:
        self._logger = logging.getLogger(__name__)
        self.id = _id

    def __eq__(self, o: object) -> bool:
        if hasattr(o, 'id') and hasattr(self, 'id'):
            return o.id == self.id  # type: ignore
        return False

    def __repr__(self) -> str:
        return "{}".format(pformat(self.serialize()))

    @property
    def id(self) -> _PKey:
        """
        Get state model id

        :return: state model id
        :rtype: _PKey
        """
        return self.__id

    @id.setter
    def id(self, _id: _PKey) -> None:
        """
        Set state model id

        :param _id: state model id 
        :type _id: _PKey
        """
        self.__id = _id

    @abstractmethod
    def serialize(self) -> Dict[str, Any]: ...

    @abstractmethod
    def deserialize(self, **kwargs) -> None: ...
