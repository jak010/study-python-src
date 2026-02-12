from typing import List, overload


class Entity: ...


class Service:

    @overload
    def find_by_id(self, pk: int):
        ...

    @overload
    def find_by_id(self, sequence: int):
        ...

    def find_by_id(self, *args, **kwargs) -> Entity:
        sequence = kwargs.get('sequence', None)
        pk = kwargs.get('pk', None)

        if sequence:
            return 1
        elif pk:
            return 2
        else:
            raise ValueError()
