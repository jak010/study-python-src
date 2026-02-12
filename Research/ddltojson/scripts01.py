from __future__ import annotations

from sql_interchange import SqlInterChange

from sqlparse.sql import Identifier
from sqlparse.sql import Function
from sqlparse.sql import Statement


def get_text():
    with open("./temp.sql", "r") as f:
        content = f.read()
        return content


class SqlDataType:
    def __init__(self, c_name, c_type, is_null):
        self.c_name = self.name_clear(c_name)
        self.c_type = str(c_type)
        self.is_null = is_null

    def name_clear(self, c_name):
        if '`' in c_name:
            return c_name.replace('`', '')

    # def __repr__(self):
    #     return f"SqlDataType(\n" \
    #            f" Identity={self.c_name},\n" \
    #            f" Type={self.c_type},\n" \
    #            f" Default={self.is_null}\n" \
    #            f")"

    def __repr__(self):
        return f"SqlDataType=({self.c_name}, {self.c_type}, {self.is_null})"

    def to_dict(self):
        return f'"{self.c_name}":"{self.c_type}"'


class Convert:

    def __init__(self, sql_interchange: SqlInterChange):
        self.sql_interchange = sql_interchange

    def execute(self):
        parenthesis = self.sql_interchange.get_parenthesis()

        # clear parenthesis

        to_text = parenthesis.value

        for x in to_text.split("\n"):
            if x == '(':
                continue
            elif x == ')':
                continue
            else:
                z = [x for x in x.split(" ") if x]
                c_name = z[0]
                c_type = z[1]
                c_any = z[2]

                remain = z[3::][0::1]

                # print(z)
                if z[0] not in ('PRIMARY', 'UNIQUE'):
                    if 'int' in c_type:
                        print(c_name, c_type, c_any, remain)
                        print("=" * 10)
                    if 'char' in c_type:
                        print(c_name, c_type, self.null_group(c_any, remain))
                        print("=" * 10)

                    # if 'enum' in c_type:
                    #     self.null_group(c_any, o, remain)
                    #     print(c_name, c_type, o)
                    #
                    # if 'decimal' in c_type:
                    #     self.null_group(c_any, o, remain)
                    #     print(c_name, c_type, o)

    def null_group(self, c_any, remain):
        o = []
        if c_any == 'NOT':
            remain.insert(0, c_any)
            for i, g in enumerate(remain, start=1):
                if i % 2 == 0:
                    o.append(' '.join(remain[i - 2:i]))

        return o


if __name__ == '__main__':
    convert = Convert(sql_interchange=SqlInterChange(get_text()))
    convert.execute()
