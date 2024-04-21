from typing import Any, Dict, Type, TypeVar, Tuple, Optional, BinaryIO, TextIO, TYPE_CHECKING

from typing import List


from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.source import Source
from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="DocumentMetadata")


@_attrs_define
class DocumentMetadata:
    """ 
        Attributes:
            source (Union[Unset, Source]): An enumeration.
            source_id (Union[Unset, str]):
            url (Union[Unset, str]):
            created_at (Union[Unset, str]):
            author (Union[Unset, str]):
     """

    source: Union[Unset, Source] = UNSET
    source_id: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    author: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)


    def to_dict(self) -> Dict[str, Any]:
        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value


        source_id = self.source_id

        url = self.url

        created_at = self.created_at

        author = self.author


        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if source is not UNSET:
            field_dict["source"] = source
        if source_id is not UNSET:
            field_dict["source_id"] = source_id
        if url is not UNSET:
            field_dict["url"] = url
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if author is not UNSET:
            field_dict["author"] = author

        return field_dict



    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _source = d.pop("source", UNSET)
        source: Union[Unset, Source]
        if isinstance(_source,  Unset):
            source = UNSET
        else:
            source = Source(_source)




        source_id = d.pop("source_id", UNSET)

        url = d.pop("url", UNSET)

        created_at = d.pop("created_at", UNSET)

        author = d.pop("author", UNSET)

        document_metadata = cls(
            source=source,
            source_id=source_id,
            url=url,
            created_at=created_at,
            author=author,
        )

        document_metadata.additional_properties = d
        return document_metadata

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
