"""
Дискорд embed из json

Автор: Yarovich
"""

from json import loads
from typing import List, Optional, Union


class _Field:
    """Информация про филд"""

    __slots__ = (
        'name', 'value', 'inline'
    )

    def __init__(self, data: dict):
        self.name: Optional[str] = data.get('name')
        self.value: Optional[str] = data.get('value')
        self.inline: Optional[bool] = data.get('inline') or True


class _Embed:
    """Информация про эмбед"""

    __slots__ = (
        '_data', 'title', 'description', 'color', 'timestamp', 'url',
        'author_name', 'author_url', 'author_icon_url', 'thumbnail_url',
        'image_url', 'footer_text', 'footer_icon_url'
    )

    def __init__(self, data: dict):
        self._data: dict = data
        self.title: Optional[str] = data.get('title')
        self.description: Optional[str] = data.get('description')
        self.color: Optional[int] = data.get('color')
        self.timestamp: Optional[str] = data.get('timestamp')
        self.url: Optional[str] = data.get('url')

        if data.get('author'):
            self.author_name: Optional[str] = data['author'].get('name')
            self.author_url: Optional[str] = data['author'].get('url')
            self.author_icon_url: Optional[str] = data['author'].get('icon_url')
        else:
            self.author_name = ''
            self.author_url = None
            self.author_icon_url = None

        if data.get('thumbnail'):
            self.thumbnail_url: str = data['thumbnail']['url']
        else:
            self.thumbnail_url = None

        if data.get('image'):
            self.image_url: str = data['image']['url']
        else:
            self.image_url = None

        if data.get('footer'):
            self.footer_text: Optional[str] = data['footer'].get('text')
            self.footer_icon_url: Optional[str] = data['footer'].get('icon_url')
        else:
            self.footer_text = None
            self.footer_icon_url = None

    @property
    def fields(self) -> List[_Field]:
        """Список филдов"""
        if self._data.get('fields') is not None:
            return list(map(_Field, self._data['fields']))
        return []


class _Message:
    """Вся информация про сообщение"""

    def __init__(self, data: dict):
        self._data: dict = data
        self.content: Optional[str] = data.get('content')

    @property
    def embeds(self) -> List[_Embed]:
        """Список ембедов"""
        if self._data.get('embeds') is not None:
            return list(map(_Embed, self._data['embeds']))
        return []


def embed_from_json(data: str) -> _Message:
    """Преобразование str в json и далее удобное использование"""
    data = loads(data)
    return _Message(data)


def load_from_dict(data: dict) -> _Message:
    """Тоже самое что и embed_from_json но сразу работаем с данными"""
    return _Message(data)
