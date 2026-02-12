from __future__ import annotations

from functools import cached_property
from typing import Tuple, TYPE_CHECKING, List, Union

import sqlparse
from sqlparse.sql import Identifier
from sqlparse.sql import Parenthesis
from sqlparse.tokens import Whitespace

if TYPE_CHECKING:
    from sqlparse.sql import Statement
    from sqlparse.sql import Token


class TokenValidation:
    def is_whitespace(self, token: Token):
        return token.ttype == Whitespace

    def token_is_create(self, token: Token):
        return token.value == 'create'


class SqlInterChange:

    def __init__(self, sql_text):
        self.sql_text = sql_text

    @cached_property
    def validator(self) -> TokenValidation:
        return TokenValidation()

    @property
    def _parse(self) -> Tuple[Statement]:
        return sqlparse.parse(self.sql_text)

    @property
    def get_token(self) -> Tuple[Token]:
        # TODO: parse 결과에서 무조건 첫 번쨰를 꺼내오는 것, SQL 파일에 DDL이 복수개라면 적절한 처리가 필요함
        return tuple(sqlparse.sql.TokenList(self._parse[0].tokens))

    def get_parenthesis(self) -> Parenthesis:
        """ DDL에서 '(' 로 시작하고 ')' 로 끝나는 문자 리턴 """
        for sql in self._extract():
            if isinstance(sql, Parenthesis):
                return sql

    def _extract(self) -> List[Union[Identifier, Token, Parenthesis]]:
        sqls = []
        for token in self.get_token:
            if not self.validator.is_whitespace(token):
                sqls.append(token)
        return sqls
